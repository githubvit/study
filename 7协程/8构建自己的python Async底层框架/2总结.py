
# 第2讲，通过生产-消费者模型 如何在单线程 实现 
# -> 定义一个 异步队列 的类  AsyncQueue ， 实现 单线程下 任务之间的消息传递

# 消息队列
# 放消息 
# 取消息
# 处理消息

# 生产 和 消费 的 速度 不一样的问题？
    # 1. 生产 快 消费慢 ，即时间上 put < get ， 保证了每次get都可以拿到消息。
    # 2. 生产 = 消费,也同样保证了get都可以拿到消息。
    # 3. 生产 慢 消费快，这就无法保证每次get都可以拿到消息。

# 上面的问题实际上就是解决，get时没有消息可以拿的问题。
# 如果消息确实发完了，那get可以终止，不是问题。
# 真正的问题在于，消息还没发完，消息队列里又没有消息 ，get时没有消息拿，怎么办？
    # 现象上就好像get来早了，来早了，怎么办，就等等，就定义一个排队队列，专门收集来早了的get。
    # 1 定义一个排队队列，
    # 2 把这种没有消息拿的 get函数体 存起来。
    # 3 每次put时，就先放消息，再处理排队队列的get，取出函数体，执行，这就保证了get可以拿到消息。
    # 4 这时get会进入下一轮get，如果没有消息，就按2说的，又被存到了排队队列里，接着按3、4、2...循环。
# 这样不管 put 和 get的速度怎么样，都可以保证让get有消息拿。


# 对于本例：就是put 慢  和 get 快
    # 由于put 慢  和 get 快 ，就会导致 每次都有来早了的get 
    # 因此 每次 都有 get 在排队队列里等 put 消息,
    # 所以 put 时 就从排队队列里 取出get 来处理 刚刚取出的 消息 ，消息立即被处理。
    # 由于get 在处理消息的同时，就会进入下一轮get，而这时消息队列的消息空了，所以，get每次都会来早了。


from collections import deque
import heapq
import time

# 写一个调度的类：
class Scheduler:
    def __init__(self):
        self.ready=deque() # 构建双向队列对象 模拟事件循环loop 里面装 准备执行的函数
        self.sleeping=[]   # 定义 延时 执行函数 列表
        self.sequence=0    # 终止时间相等时 排序的值 延时函数 的序列号

    def call_soon(self,func): # 模拟 loop.call_soon 回调并立即执行
        self.ready.append(func) # 把 准备执行的函数 右放入 队列

    def call_later(self,delay,func): # 模拟 loop.call_later 延时调用
        self.sequence+=1 #延时函数 的序列号 用self.sequence就解决了时间相等时 sort报错的问题
        deadline=time.time()+delay # 终止时间
        heapq.heappush(self.sleeping,(deadline,self.sequence,func))
        # heapq.heappush方法：
        # 1. 把self.sleeping转换成了堆，堆就是有序可迭代的生成器
        # 2. 把 元组(deadline,func) 加入堆中 并排好序
        # 两步并一步 

    def run(self):
        while self.ready or self.sleeping:
            if not self.ready:
                #弹出self.sleeping堆中最小值
                deadline, _, func = heapq.heappop(self.sleeping)
                # 计算延时 不一定 就是delay,
                # 如果延时相同，只用一个等，其余的到这，就不会>0了，不再睡了，直接加入队列执行。
                # 因为延时堆是按大小排序的，所以前面小的帮后面大的睡了一部分。
                # 那么总计时长，就是最大的，也就是最后的延时时间。就实现了并发。
                delta=deadline-time.time()
                if delta>0: 
                    time.sleep(delta) # 阻塞
                self.ready.append(func) # 右加入到 准备执行 双向队列中

            while self.ready:
                func=self.ready.popleft() # 从 双向队列中 左取出 准备执行的函数
                func() # 执行

sched=Scheduler() # 实例化调度类

# 写一个异步的队列 
class AsyncQueue:
    def __init__(self):
        self.items=deque()    # 消息队列 装的 就是 消息
        
        
        self.waiting=deque()  # 排队队列 这里面装的是 来早了 的 get

    #放消息 并 如果排队队列有get,就用get 立即处理 刚刚 put进去的消息
    # 这样 放进去 的 消息 就立即被 取出 并立即得到 处理了
    def put(self,item):
        # 放消息
        self.items.append(item)
        if self.waiting: # 处理 来早了 的get
            func=self.waiting.popleft() # 取出 get
            sched.call_soon(func) # 加入 调度对象的 执行队列中 立即执行

    # [有消息 就 取消息 并 处理消息] 或 
    # [没消息(即来早了) 就 去排队 (put之后再get)] 
    def get(self,callback):
        # 取消息
        # 如果 items 有 一个 有效的 item ，就返回这个 item
        if self.items:
            callback(self.items.popleft()) #用回调处理左取出的 item
        else: 
            # 如果 items是空的，就把 这次的 get函数体 放到 排队队列里 self.waiting 
            # 下次 put 的时候，就会把 排队队列self.waiting里的 get 拿出来 立即执行
            # 保证了get即使在put前先到，也要在put后执行 
            self.waiting.append(lambda: self.get(callback))

# 切函数 定义
def producer(q,count):
    def _run(n):
        if n<count:
            print('生产了',n,'排队队列q.waiting中数量',len(q.waiting))
            # 放消息 并 如果排队队列 有 get，就立即 处理 消息
            q.put(n)
            sched.call_later(1,lambda: _run(n+1))
        else:
            print('生产结束')   
            q.put(None) 
    _run(0)        
    # for n in range(count):
    #     print('生产了',n)
    #     q.put(n) #放入队列
    #     time.sleep(1)
    # print('生产结束')
    # q.put(None)

def consumer(q):
    # 回调函数： 消息处理 和 切函数 循环
    def _consume(item):
        if item is None:
            print('消费结束') 
        else:
            print('消费了',item)
            # 切函数 循环 添加到 准备执行列表 立即执行 
            # 下一步函数中 继续收消息 不断get 因此还要 q.get(callback = _consume)  
            # 所以这里放cousumer(q)
            sched.call_soon(lambda: consumer(q))
    # 收消息 并用 回调方式 处理消息  
    # 如果没有消息 该q.get(callback = _run) 函数体 会 放入 排队队列 
    # 因为 q 的get 使用 回调的方式处理消息
    # 所以 在 get 前，一定要有 消息处理函数，以便回调     
    q.get(callback = _consume)        
    # while True:
    #     item=q.get()
    #     if item is None:
    #         break
    #     print('消费了',item)
    # print('消费结束')
start=time.time()
q=AsyncQueue()
sched.call_soon(lambda: producer(q,10))
sched.call_soon(lambda: consumer(q,) )
sched.run()
print('[two]time',time.time()-start)

# 结果
# 生产了 0 排队队列q.waiting中数量 0
# 消费了 0
# 生产了 1 排队队列q.waiting中数量 1
# 消费了 1
# 生产了 2 排队队列q.waiting中数量 1
# 消费了 2
# 生产了 3 排队队列q.waiting中数量 1
# 消费了 3
# 生产了 4 排队队列q.waiting中数量 1
# 消费了 4
# 生产了 5 排队队列q.waiting中数量 1
# 消费了 5
# 生产了 6 排队队列q.waiting中数量 1
# 消费了 6
# 生产了 7 排队队列q.waiting中数量 1
# 消费了 7
# 生产了 8 排队队列q.waiting中数量 1
# 消费了 8
# 生产了 9 排队队列q.waiting中数量 1
# 消费了 9
# 生产结束
# 消费结束
# [two]time 10.010579347610474