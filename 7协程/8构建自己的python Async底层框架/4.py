# 生成器 和 async/await 关键字 实现 单线程异步 io
# https://www.bilibili.com/video/av81742647?from=search&seid=13812321267434886846
# 时间：68:00

from collections import deque
import time 

# 一 交替
# 三件事：
    # 切函数、
    # 把每段切出的函数放进队列、
    # 从队列挨个取出执行。

# 1. 生成器 实现 单线程 多任务 交替
def one():
    # 调度类
    class Scheduler:
        def __init__(self):
            self.ready=deque()      # 队列
            self.current=None       # 当前generator 生成器对象

        def new_task(self,gen):
            self.ready.append(gen) # 放入 generator 生成器对象

        def run(self):
            while self.ready:
                self.current=self.ready.popleft()               # 1 取出    
                try:
                    next(self.current)                          # 2 执行

                    #和上面的效果是一样的 都是 唤醒 generator 执行
                    # self.current.send(None) 

                    if (self.current):
                        self.ready.append(self.current) # 又放入

                except StopIteration: # 捕捉 next（）为空时抛的异常StopIteration
                    pass 

    scher=Scheduler() # 调度对象
   
    def countdown(n):
        while n>0:
            print('Down',n)
            time.sleep(1)

            # 切函数
            #用yield让循环暂停和返回 相当于把函数切片 分段 运行
            yield                                             # 3 暂停 并 交出执行权
            n -= 1

    def countup(stop):
        x=0
        while x<stop :
            print('Up',x)
            time.sleep(1) 
            yield
            x += 1

    start=time.time()
    # 做线头
    scher.new_task(countdown(5))
    scher.new_task(countup(5))
    # 扯线头
    scher.run()
    print('[yield]time{:.4}s'.format(time.time()-start))

# one()

# 结果
    # Down 5
    # Up 0
    # Down 4
    # Up 1
    # Down 3
    # Up 2
    # Down 2
    # Up 3
    # Down 1
    # Up 4
    # [yield]time10.01s  

# 2. async/await 关键字 实现 单线程 多任务 交替
# 1和2两套 不能 混用
def two():
    class Scheduler:
        def __init__(self):
            self.ready=deque()
            self.current=None

        # def new_task(self,gen):
        #     self.ready.append(gen)
        def new_task(self,coro):    
            self.ready.append(coro)

        def run(self):
            while self.ready:
                self.current=self.ready.popleft()
                try:
                    # next(self.current) # 报错：TypeError: 'coroutine' object is not an iterator
                    self.current.send(None) # 用了协程后，只能用send(None) 唤醒 就是 交出执行权
                    if (self.current):
                        self.ready.append(self.current)
                except StopIteration:
                    pass 

    scher=Scheduler()

    # 可等待对象
    # 提供生成器的功能：存储和暂停
    class Awaitable:
        def __await__(self):
            yield

    # 切换开关：
    def switch():
        return Awaitable()

    # async 关键字 表示协程（切函数） await 替代 yield 暂停和交出执行权
    async def countdown(n):
        while n>0:
            print('Down',n)
            time.sleep(1)
            # yield
            await switch()
            n -= 1

    async def countup(stop):
        x=0
        while x<stop :
            print('Up',x)
            time.sleep(1) 
            # yield
            await switch()
            x += 1

    start=time.time()
    scher.new_task(countdown(5))
    scher.new_task(countup(5))
    scher.run()
    print('[async/await]time{:.4}s'.format(time.time()-start))

# two()

# 结果
    # Down 5
    # Up 0
    # Down 4
    # Up 1
    # Down 3
    # Up 2
    # Down 2
    # Up 3
    # Down 1
    # Up 4
    # [async/await]time10.01s



# 二 并发
# 按照1.py的处理方式 
    # 增加延时执行 小函数列表sleeping
    # 把延时 小函数放进延时堆。
    # 用堆排序heapq把延时 小函数放进延时推，并按 终结时间（ 小函数的执行时间）排序
    # 在执行中的并发实现：
        # 延时堆 小函数按时序休息，
        # 休息时间相等的同一休息，小的帮大的休息。
        # 把延时堆中休息完的 小函数及时加入到准备执行队列，并执行，实现并发。


# 3. yield 实现 单线程 多任务 并发

import heapq

def three():
    class Scheduler:
        def __init__(self):
            self.ready=deque()
            self.current=None
            self.sleeping=[]   # 增加 定义 延时 执行函数 列表
            self.sequence=0    # 终止时间相等时 排序的值
        
        def sleep(self,delay):
            self.sequence+=1 # 用self.sequence就解决了时间相等时 sort报错的问题
            # print('self.sequence',self.sequence)
            deadline=time.time()+delay # 终止时间

            # 除第一次（即做线头时）的gen是直接放入self.ready的，
            # 后面每次next(g)完，都先放到sleeping，按 终止时间 排序，这是并发的前提。
            # 用堆排序把 新得的self.current 生成器 放进延时推，并按 终结时间（小函数的执行时间） 排序
            heapq.heappush(self.sleeping,(deadline,self.sequence,self.current))
        
        # 第一次 放入 做线头
        def new_task(self,gen):    
            self.ready.append(gen) 

        def run(self):
            while self.ready or self.sleeping:
                # print('1')
                if not self.ready:
                    # print('2')
                    #弹出self.sleeping堆中最小值
                    deadline, _, gen = heapq.heappop(self.sleeping)
                    delta=deadline-time.time()
                    # 并发 休息时间相等，同一休息；不等，少帮多。
                    if delta>0:
                        time.sleep(delta) # 阻塞
                    self.ready.append(gen)    
                self.current=self.ready.popleft()
                # print('1')
                try:
                    next(self.current) # 执行 一轮 碰到yield交出执行权
                                       
                    # self.current.send(None) 
                    # print('喂')


                    # 新的生成器不放self.ready，否则就是串行，
                    # 改成放到self.sleeping延时队列 去实现并发执行
                    # if (self.current): 
                    #     self.ready.append(self.current) 
                except StopIteration:
                    pass 

    scher=Scheduler()

    def countdown(n):
        while n>0:
            print('Down',n)
            # time.sleep(1)
            scher.sleep(1) # 延时时长
            yield          # 暂停 交出执行权
            n -= 1

    def countup(stop,):
        x=0
        while x<stop :
            print('Up',x)
            # time.sleep(1)
            scher.sleep(1) 
            yield
            x += 1

    start=time.time()
    scher.new_task(countdown(5))
    scher.new_task(countup(5))
    scher.run()
    print('[ yield ]time{:.4}s'.format(time.time()-start))

# three()

    # Down 5
    # Up 0
    # Down 4
    # Up 1
    # Down 3
    # Up 2
    # Down 2
    # Up 3
    # Down 1
    # Up 4
    # [ yield ]time5.016s


# 4. async/await 实现 单线程 多任务 并发

def four():
    class Scheduler:
        def __init__(self):
            self.ready=deque()
            self.current=None
            self.sleeping=[]   # 增加 定义 延时 执行函数 列表
            self.sequence=0    # 终止时间相等时 排序的值
        
        def sleep(self,delay):
            self.sequence+=1 # 用self.sequence就解决了时间相等时 sort报错的问题
            # print('self.sequence',self.sequence)
            deadline=time.time()+delay # 终止时间

            # 除第一次（即做线头时）的coro是直接放入self.ready的，
            # 后面每次coro.send(None)完，都先放到sleeping，按 终止时间 排序，这是并发的前提。

            # 用堆排序把 新得的self.current 协程 放进延时推，并按 终结时间（小函数的执行时间） 排序
            heapq.heappush(self.sleeping,(deadline,self.sequence,self.current))

        def new_task(self,coro):    
            self.ready.append(coro)

        def run(self):
            while self.ready or self.sleeping:
                # print('1')
                if not self.ready:
                    # print('2')
                    #弹出self.sleeping堆中最小值
                    deadline, _, coro = heapq.heappop(self.sleeping)
                    delta=deadline-time.time()
                    # 并发 休息时间相等，同一休息；不等，少帮多
                    if delta>0:
                        time.sleep(delta) # 阻塞
                    self.ready.append(coro)    
                self.current=self.ready.popleft()
                # print('1')
                try:
                    # next(self.current) 
                    # 报错：TypeError: 'coroutine' object is not an iterator

                    # 用了协程后，只能用send(None) 唤醒执行
                    self.current.send(None) 
                    # print('喂')

                    # 执行完每一轮的协程self.current不能直接放self.ready,否则只能串行
                    # 改成先放到self.sleeping延时队列排序，去实现并发。
                    # if (self.current):
                    #     self.ready.append(self.current)
                except StopIteration:
                    pass 

    scher=Scheduler()

    # 可等待对象
    # 提供生成器的功能：存储和暂停
    class Awaitable:
        def __await__(self):
            yield

    # 切换开关：
    def switch():
        return Awaitable()

    # async 关键字 表示协程（切函数） await 替代 yield 暂停和交出执行权
    async def countdown(n):
        while n>0:
            print('Down',n)
            # time.sleep(1)
            scher.sleep(1) #延时时长
            # yield
            await switch() #暂停 交出执行权 await 后面 必须是一个可等待对象
            n -= 1

    async def countup(stop,):
        x=0
        while x<stop :
            print('Up',x)
            # time.sleep(1)
            scher.sleep(1) 
            # yield
            await switch()
            x += 1

    start=time.time()
    scher.new_task(countdown(5))
    scher.new_task(countup(5))
    scher.run()
    print('[async/await]time{:.4}s'.format(time.time()-start))

# four()

    # Down 5
    # Up 0
    # Down 4
    # Up 1
    # Down 3
    # Up 2
    # Down 2
    # Up 3
    # Down 1
    # Up 4
    # [async/await]time5.012s


# 三 优化
# 5. async/await 优化方案
# 把 class Scheduler 中的sleep 改成 协程 进一步优化了代码，
# 这样就可以把 原来down和up中的await switch() 放到 sleep 中了。
def five():
    class Scheduler:
        def __init__(self):
            self.ready=deque()
            self.current=None
            self.sleeping=[]   # 增加 定义 延时 执行函数 列表
            self.sequence=0    # 终止时间相等时 排序的值
        
        # 改成协程 可以放 await switch() 优化 down和up
        async def sleep(self,delay):
            self.sequence+=1 # 用self.sequence就解决了时间相等时 sort报错的问题
            # print('self.sequence',self.sequence)
            deadline=time.time()+delay # 终止时间
            # 每次执行完一轮的协程先放入延时队列，按终结时间排序，这是并发的关键。
            heapq.heappush(self.sleeping,(deadline,self.sequence,self.current))
            # sleep改成 协程 函数，就可以放进来了，不然await 不能放到普通函数中。
            await switch()                                              # 3 暂停 

        # 除第一次的协程(即做线头时)用 scher.new_task(coro) 直接放入self.ready外，
        # 其余每一轮的协程对象都要用 await scher.sleep() 先放入延时队列self.sleeping,实现并发
        def new_task(self,coro):    
            self.ready.append(coro)

        def run(self):
            while self.ready or self.sleeping:
                # print('1')
                if not self.ready:
                    # print('2')
                    #弹出self.sleeping堆中最小值
                    deadline, _, coro = heapq.heappop(self.sleeping)
                    delta=deadline-time.time()
                    if delta>0:
                        time.sleep(delta) # 阻塞
                    self.ready.append(coro)    
                self.current=self.ready.popleft()                       # 1 取出
                # print('1')
                try:
                    # next(self.current) 
                    # 报错：TypeError: 'coroutine' object is not an iterator

                    # 用了协程后，只能用g.send(None) 取代 next(g)唤醒执行
                    self.current.send(None)                             # 2 执行
                    # print('喂')
                    
                except StopIteration:
                    pass 

    scher=Scheduler()

    # 可等待对象
    # 提供生成器的功能：存储和暂停
    class Awaitable:
        def __await__(self):
            yield

    # 切换开关：
    def switch():
        return Awaitable()

    # async 关键字 表示协程（切函数） await 替代 yield 暂停和交出执行权
    async def countdown(n):
        while n>0:
            print('Down',n)
            await scher.sleep(1) #延时时长 time.sleep() + yield 暂停 交出执行权
            n -= 1

    async def countup(stop,):
        x=0
        while x<stop :
            print('Up',x)
            await scher.sleep(1) 
            x += 1

    start=time.time()
    # 做线头
    scher.new_task(countdown(5))
    scher.new_task(countup(5))
    # 扯线头
    scher.run()
    print('[async/await]time{:.4}s'.format(time.time()-start))

five()

    # Down 5
    # Up 0
    # Down 4
    # Up 1
    # Down 3
    # Up 2
    # Down 2
    # Up 3
    # Down 1
    # Up 4
    # [async/await]time5.007s