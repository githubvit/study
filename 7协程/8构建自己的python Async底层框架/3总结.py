# 生产-消费者模式
# https://www.bilibili.com/video/av81742647?from=search&seid=13812321267434886846
# 时间：50:00

# 上一讲 通过 异步队列 class AsyncQueue 实现了消息传递和及时进行消息处里
# 这一讲 进一步完善 异步队列 class AsyncQueue 实现 队列的关闭 和 异常的处理


# 原来：
    # 通过 发送方 q.put(None)来 表示 发送结束
    # 接收方 判读 收到的是 None 就 退出接收
# 问题：队列 q 并没 真正关闭，还可以继续 发 和 收。

# 解决 队列的关闭

# 1. 定义 关闭状态 self._closed=True / False
# 2. 定义 队列关闭异常类 class QueueClosed(Exception): pass
    # 使得 队列关闭后 的 put 和 get 激发异常 
# 3. 定义 close 方法 def close(self): ...
    # 使得 q 不能再 put 
        # 置 self.close=True
        # 如果 close 为 True，再put时 就会 激发 队列关闭异常 QueueClosed。
    # q中消息队列中已有的消息可以继续被处理
    # 由于不能再put，所以要在clos时，处理最后一个put时，get放在排队队列里waitting的get函数体。
        # 否则，不能执行get的退出动作。
       
       
# 4. 定义 消息处理循环时 即 get时 ，正常处理消息和激发异常的类 

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
 
# 2. 定义callback的参数 用的类 
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
        self.items=deque()   
        self.waiting=deque() 
        # 3 设定状态
        self._closed=False     # 默认是打开的
    
    # 4 定义关闭的方法
    def close(self):
        self._closed=True      # 关闭队列

        #处理 最后一个put时， 排队队列 里的get,
        # 否则，无法执行get的退出动作： 打印 '消费结束'
        if self.waiting and not self.items: 
            for func in self.waiting:
                sched.call_soon(func)  # 执行该 get  实现 get 捕捉 QueueClosed 异常 退出。 
   
    def put(self,item):
        # 5 状态判断
        if self._closed:
            raise QueueClosed() # 激发 QueueClosed异常
        
        self.items.append(item)
        if self.waiting: 
            func=self.waiting.popleft() 
            sched.call_soon(func) 
    
    def get(self,callback):
        if self.items:
            # 6 用Result对象 作为 参数 取值
            callback(Result(val=self.items.popleft())) #用回调处理左取出的 item
        else:
            # 7 状态判断  
            if self._closed:
                # 8 用Result对象 作为 参数 传递异常
                callback(Result(exc=QueueClosed())) 
            
            self.waiting.append(lambda: self.get(callback))

def producer(q,count):
    def _run(n):
        if n<count:
            print('生产了',n)
            # 放消息 并 如果排队队列 有 get，就立即 处理 消息
            q.put(n)
            sched.call_later(1,lambda: _run(n+1))
        else:
            print('生产结束')   
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
            print('消费了',item)
            sched.call_soon(lambda: consumer(q))
        except QueueClosed:
            print('消费结束') 
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
# [two]time 10.01119589805603