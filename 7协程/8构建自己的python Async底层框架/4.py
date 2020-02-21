# 生成器 和 async/await 关键字 实现 单线程异步 io
# https://www.bilibili.com/video/av81742647?from=search&seid=13812321267434886846
# 时间：68:00

from collections import deque
import time 

# 1. 生成器 实现 单线程 多任务 交替
def one():
    class Scheduler:
        def __init__(self):
            self.ready=deque()
            self.current=None

        def new_task(self,gen):
            self.ready.append(gen)

        def run(self):
            while self.ready:
                self.current=self.ready.popleft()
                try:
                    next(self.current)
                    if (self.current):
                        self.ready.append(self.current)
                except StopIteration:
                    pass 

    scher=Scheduler()
   
    def countdown(n):
        while n>0:
            print('Down',n)
            time.sleep(1)
            yield
            n -= 1

    def countup(stop):
        x=0
        while x<stop :
            print('Up',x)
            time.sleep(1) 
            yield
            x += 1

    start=time.time()
    scher.new_task(countdown(5))
    scher.new_task(countup(5))
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
                    # next(self.current)
                    self.current.send(None) # 协程切换 发送给另一个协程 
                    if (self.current):
                        self.ready.append(self.current)
                except StopIteration:
                    pass 

    scher=Scheduler()

    # 可等待对象
    class Awaitable:
        def __await__(self):
            yield

    # 切换开关
    def switch():
        return Awaitable()

    # async 关键字 表示协程
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

two()

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