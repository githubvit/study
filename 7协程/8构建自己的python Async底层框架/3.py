# 生产-消费者模式
# https://www.bilibili.com/video/av81742647?from=search&seid=13812321267434886846
# 时间：50:00

# 上一讲 通过 异步队列 class AsyncQueue 实现了消息传递和及时进行消息处里
# 这一讲 进一步完善 异步队列 class AsyncQueue 实现 队列的关闭 和 异常的处理

# 1 队列的关闭
# 原来：
    # 通过 发送方 q.put(None)来 表示 发送结束
    # 接收方 判读 收到的是 None 就 退出接收
# 问题：队列 q 并没 真正关闭，还可以继续 发 和 收。

# 定义 关闭状态 self.closed=True / False
# 定义 close 方法 def close(self): ...
    # 使得 q 不能再 put 
        # 置 self.close=True
        # 如果 close 为 True，再put时 就会 激发 队列关闭异常 QueueClosed。
    # q中消息队列中已有的消息可以继续被处理完。
    # 由于不能再put了，所以要在clos时，处理最后一个put时，get放在排队队列里waitting的get。
        #怎么保证最后一个put？
            # 由于此时closed已经是True了，
            # 所以，以下代码就可以保证，取出这个get 执行 就可以退出get了。
                # if self.waiting and not self.items:
                #  for func in self.waiting:
                #     sched.call_soon(func)  
        # 符合self.get(callback)满足了关闭条件（消息队列为空 且 close 为 True），get就会执行退出动作。
             # 7 状态判断  
                # if self._closed:
                #     # 8 用Result对象 作为 参数 传递异常
                #     callback(Result(exc=QueueClosed())) 
                
# 定义 队列关闭异常类 class QueueClosed(Exception): pass

# 关于get 的关闭
    # 前提： 如果 消息队列为空 且 close 为 True，就应关闭get.
    # 由于get 一直 在用 callback 不停处理 消息，我们就让 callback时 激发 队列关闭异常 QueueClosed。
    # 在callback时捕捉该异常，从而结束get.

    # callback怎么实现正常处理消息和激发异常？

        # 定义一个类 class Result，
            #  类中定义一个result方法：接收两个参数（正常值，异常）
                # 来正常值，返回正常值；
                # 来异常，激发异常
        # 把该类的对象作为callback的参数。callback(Result(val,exc))
        # 在callback定义中，执行该参数的result方法，即可实现正常处理消息和激发异常。

from collections import deque
import heapq
import time
def three():
    # 调度类：
    class Scheduler:
        def __init__(self):
            self.ready=deque() 
            self.sleeping=[]   
            self.sequence=0    

        def call_soon(self,func): 
            self.ready.append(func) 

        def call_later(self,delay,func): 
            self.sequence+=1 
            deadline=time.time()+delay 
            heapq.heappush(self.sleeping,(deadline,self.sequence,func))
           
        def run(self):
            while self.ready or self.sleeping:
                if not self.ready:
                    deadline, _, func = heapq.heappop(self.sleeping)
                    delta=deadline-time.time()
                    if delta>0: 
                        time.sleep(delta) 
                    self.ready.append(func) 
                while self.ready:
                    func=self.ready.popleft() 
                    func() 

    sched=Scheduler() # 实例化调度类

    # 1. 定义一个队列关闭异常
    class QueueClosed ( Exception ):
        pass

    # 2. 定义callback的参数对象 用的类  
    class Result:
        def __init__(self,val=None,exc=None):
            self.value=val
            self.exc=exc

        # 定义 正常返回 和 激发异常 的方法
        def result(self):
            # if self.value:
            #     return self.value
            # if self.exc:
            #     raise self.exc    
            # 上面的写法 当 self.value=0时 怎么办？
            # 所以改成：
            if self.exc:
                raise self.exc
            else:
                return self.value

    # 写一个异步的队列 
    class AsyncQueue:
        def __init__(self):
            self.items=deque()    # 消息队列 装的 就是 消息
            self.waiting=deque()  # 排队队列 这里面装的是 来早了的get
            # 3 设定状态
            self._closed=False     # 默认是打开的
            self.con=0

        # 4 定义关闭的方法
        def close(self):
            self._closed=True      # 关闭队列
            if self.waiting and not self.items: #处理 无消息时 排队队列 里的get
                for func in self.waiting:
                    sched.call_soon(func)   

        #放消息 并 如果排队队列有get,就把 get 添加 到 调度对象的 准备执行队列中 执行
        #这样 放进去 的 消息 就立即被 取出 并得到 执行 了
        def put(self,item):

            # 5 状态判断
            if self._closed:
                raise QueueClosed() # 激发 QueueClosed异常

            # 放消息
            self.items.append(item)
            if self.waiting: # 处理排队中来早了的get
                func=self.waiting.popleft() # 取出 get
                # 立即执行 即self.get(callback)
                # func()  # 可能会得到深度调用、递归等
                sched.call_soon(func) # 加入 调度对象的 准备执行队列中 用 调度对象的 run 执行

        # [有消息 就 取消息 并 处理消息] 或 
        # [没消息(即来早了) 就 去排队 (put之后再get)] 
        def get(self,callback):

            # 取消息
            # 如果 items 有 一个 有效的 item ，就返回这个 item
            if self.items:
                # 6 用Result对象 作为 参数 取值
                callback(Result(val=self.items.popleft())) #用回调处理左取出的 item
            else:
                self.con +=1
                # 7 状态判断  
                if self._closed:
                    # 8 用Result对象 作为 参数 传递异常
                    callback(Result(exc=QueueClosed())) #
                # 排队 (来早了，就去排队，把get放到排队队列self.waiting 中)
                # 如果 items是空的，就把 这次的 get函数体 添加到 排队队列 self.waiting 
                # 下次 put 的时候，就会把  排队 里的get 添加 到 调度对象的 执行队列中 立即执行 
                # 这就保证 get 一定在 put 后执行
                self.waiting.append(lambda: self.get(callback))
    # 切函数 定义
    def producer(q,count):
        def _run(n):
            if n<count:
                print('生产了',n,len(q.waiting))
                # 放消息 并 如果排队队列 有 get，就立即 处理 消息
                q.put(n)
                sched.call_later(1,lambda: _run(n+1))
            else:
                print('生产结束',len(q.waiting))   
                # 9 用新定义的 q 的close方法 关闭
                q.close()
        _run(0)        
        # for n in range(count):
        #     print('生产了',n)
        #     q.put(n) #放入队列
        #     time.sleep(1)
        # print('生产结束')
        # q.put(None)

    def consumer(q):
        # 回调函数： 消息处理 和 切函数 循环
        # 10 改造：用 Result类对象 作为参数,调用其result方法 实现 正常返回 和 激发异常
        # 11 捕捉异常 
        def _consume(res):
            try:
                item=res.result()
                print('消费了',item,q.con)
                # 切函数 循环 添加到 准备执行列表 立即执行 
                # 下一步函数中 继续收消息 不断get 因此还要 q.get(callback = _consume)  
                # 所以这里放cousumer(q)
                sched.call_soon(lambda: consumer(q))
            except QueueClosed:
                print('消费结束') 

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

three()        

# 结果
    # 生产了 0
    # 消费了 0
    # 生产了 1
    # 消费了 1
    # 生产了 2
    # 消费了 2
    # 生产了 3
    # 消费了 3
    # 生产了 4
    # 消费了 4
    # 生产了 5
    # 消费了 5
    # 生产了 6
    # 消费了 6
    # 生产了 7
    # 消费了 7
    # 生产了 8
    # 消费了 8
    # 生产了 9
    # 消费了 9
    # 生产结束
    # 消费结束
    # [two]time 10.008708477020264