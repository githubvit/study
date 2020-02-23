# 生产消费者模型2 协程 实现 单线程 任务 消息传递 
# https://www.bilibili.com/video/av81742647?from=search&seid=13812321267434886846
# 时间：100:00
# 管道的关闭和异常处理

import time 
import heapq
from collections import deque

def one():
    # 可等待类
    class Awaitable:
        def __await__(self):
            yield

    # 切换
    def switch():
        return Awaitable()

    # 调度类
    class Scheduler:
        def __init__(self):
            self.ready=deque()  # 立即执行队列 切函数 生成器 协程
            self.current=None   # 当前 生成器或协程
            self.sleeping=[]    # 延时执行堆 用来排序 切函数 生成器 协程
            self.sequence=0     # 延时队列中的序列号 最终排序依据

        # 延时堆 收集迭代(coro.send(None))后的协程 
        async def sleep(self,delay):
            self.sequence +=1
            deadline=time.time()+delay  # 终结时间 排序依据
            heapq.heappush(self.sleeping,(deadline,self.sequence,self.current)) # 收集协程并排序
            await switch()                              # 3 暂停 交出执行权

        # 做线头：仅仅用来第一次收集coro，直接 放到立即执行队列。
        def new_task(self,coro):
            self.ready.append(coro)   

        # 扯线头
        def run(self):
            while self.ready or self.sleeping:
                if not self.ready:
                    deadline,_,coro = heapq.heappop(self.sleeping)  # 取出当前终结时间最小的协程
                    delat=deadline-time.time()
                    # 并发：相等就同一，不等就小帮大。
                    if delat>0:
                        time.sleep(delat)
                    self.ready.append(coro)
                self.current = self.ready.popleft()     # 1 取出 协程对象
                try:
                    self.current.send(None)             # 2 协程 执行 self.current更新为下一步协程对象
                except StopIteration:
                    pass    
                
    scher=Scheduler()   # 生成调度对象

    # 异步队列
    class AsyncQueue:
        def __init__(self):
            self.items=deque()      # 消息队列
            self.waitting=deque()   # 排队队列 收集来早了的get

        # 放消息
        def put(self,item):
            self.items.append(item)
            if self.waitting:       # 处理来早了的get 阻塞的consumer 让其继续执行
                scher.ready.append(self.waitting.popleft())

        # 收消息
        async def get(self):
            if not self.items:
                self.waitting.append(scher.current) # get来早了 就把父协程 consumer收集到waitting
                await switch()  # 暂停 交出执行权
            return self.items.popleft()

    # 生产者
    async def producer(q,count):
        for i in range(count):
            print('生产了',i)
            q.put(i)
            await scher.sleep(1)
        print('生产结束')
        q.put(None)

    # 消费者
    async def consumer(q):
        while True:
            item=await q.get()      # 协程嵌套 无结果就阻塞 有结果才返回
            if item is None: break
            print('消费了',item)
        print('消费结束')         

    start=time.time()
    q=AsyncQueue()
    scher.new_task(producer(q,10))
    scher.new_task(consumer(q,))
    scher.run()
    print('[one]time: {:.4f}s'.format(time.time()-start))

# one()    

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
    # [one]time: 10.0117s


# 二 添加 关闭队列的属性和方法
def two():
    # 可等待类
    class Awaitable:
        def __await__(self):
            yield

    # 切换
    def switch():
        return Awaitable()

    # 调度类
    class Scheduler:
        def __init__(self):
            self.ready=deque()  # 立即执行队列 切函数 生成器 协程
            self.current=None   # 当前 生成器或协程
            self.sleeping=[]    # 延时执行堆 用来排序 切函数 生成器 协程
            self.sequence=0     # 延时队列中的序列号 最终排序依据

        # 延时堆 收集迭代(coro.send(None))后的协程 
        async def sleep(self,delay):
            self.sequence +=1
            deadline=time.time()+delay  # 终结时间 排序依据
            heapq.heappush(self.sleeping,(deadline,self.sequence,self.current)) # 收集协程并排序
            await switch()                              # 3 暂停 交出执行权

        # 做线头：仅仅用来第一次收集coro，直接 放到立即执行队列。
        def new_task(self,coro):
            self.ready.append(coro)   

        # 扯线头
        def run(self):
            while self.ready or self.sleeping:
                if not self.ready:
                    deadline,_,coro = heapq.heappop(self.sleeping)  # 取出当前终结时间最小的协程
                    delat=deadline-time.time()
                    # 并发：相等就同一，不等就小帮大。
                    if delat>0:
                        time.sleep(delat)
                    self.ready.append(coro)
                self.current = self.ready.popleft()     # 1 取出 协程对象
                try:
                    self.current.send(None)             # 2 协程 执行 self.current更新为下一步协程对象
                except StopIteration:
                    pass    
                
    scher=Scheduler()   # 生成调度对象

    # 队列关闭异常
    class QueueClosed(Exception):
        pass

    # 异步队列
    class AsyncQueue:
        def __init__(self):
            self.items=deque()      # 消息队列
            self.waitting=deque()   # 排队队列 收集来早了的get
            self._closed=False      # 状态 默认是打开的 

        def close(self):
            self._closed=True
            # 处理put时的最后一个 get ，用这个get激发异常让consumer结束
            if self.waitting and not self.items:
                for coro in self.waitting:
                    scher.ready.append(coro)

        # 放消息
        def put(self,item):
            if self._closed:        # 状态判断
                raise QueueClosed()   # 激发异常
            self.items.append(item)
            if self.waitting:       # 处理来早了的get 阻塞的consumer 让其继续执行
                scher.ready.append(self.waitting.popleft())

        # 收消息
        async def get(self):
            while not self.items:
            # if not self.items:
                if self._closed:
                    raise QueueClosed()
                self.waitting.append(scher.current) # get来早了 就把父协程 consumer收集到waitting
                await switch()  # 暂停 交出执行权
            return self.items.popleft()

    # 生产者
    async def producer(q,count):
        for i in range(count):
            print('生产了',i)
            q.put(i)
            await scher.sleep(1)
        print('生产结束')
        # q.put(None)
        q.close()

    # 消费者
    async def consumer(q):
        try:
            while True:
                item=await q.get()      # 协程嵌套 无结果就阻塞 有结果才返回
                if item is None: break
                print('消费了',item)
        except QueueClosed:
            print('消费结束')         

    start=time.time()
    q=AsyncQueue()
    scher.new_task(producer(q,10))
    scher.new_task(consumer(q,))
    scher.run()
    print('[two]time: {:.4f}s'.format(time.time()-start))

two()