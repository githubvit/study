#统一 普通函数 协程 实现 单线程 多任务 并发 的 调度类 class Scheduler
from collections import deque
import heapq
import time

# 可等待类
class Awaitable:
    def __await__(self):
        yield

# 切换
def switch():
    return Awaitable()

# 协程包装 : 
class Task:
    def __init__(self,coro):
        self.coro=coro

    def __call__(self): # 该方法 是加括号就 执行 即 Task(coro) 就执行
        scher.current=self
        try:
            self.coro.send(None) # 执行 协程 更新 协程对象
        except StopIteration:
            pass

# 统一的调度类
class Scheduler:
    def __init__(self):
        self.ready=deque()  # 立即执行 队列
        self.current=None   # 当前 协程对象
        self.sleeping=[]    # 延时堆
        self.sequence=0     # 延时 小函数 序号 排序的最终依据

    # 普通函数 把切函数 放进 立即执行队列
    def call_soon(self,func):
        self.ready.append(func)

    # 普通函数 延时调用
    def call_later(self,delay,func):
        self.sequence +=1
        deadline=time.time()+delay  # 终结时间
        heapq.heappush(self.sleeping,(deadline,self.sequence,func)) # 放进延时推 并 排序
    
    # 协程 延时调用
    async def sleep(self,delay):
        self.call_later(delay,self.current)
        await switch()

    # 协程 立即调用
    def new_task(self,coro):
        self.ready.append(Task(coro))     

    def run(self):
        while self.ready or self.sleeping:
            if not self.ready:
                deadline,_,func=heapq.heappop(self.sleeping)    # 取出 终结时间 最小的
                delat=deadline-time.time()
                # 并发：等则同，否则帮。
                if delat>0:
                    time.sleep(delat)
                self.ready.append(func)
            while self.ready:                                   # 只要立即执行队列里有，就一直执行
                func=self.ready.popleft()
                func()



# 生成调度对象
scher=Scheduler()

# 队列关闭异常
class Queueclosed(Exception):
    pass

# 异步队列：
class AsyncQueue:
    def __init__(self):
        self.items=deque()          # 消息队列
        self.waitting=deque()       # 排队队列 处理来早了的get
        self._closed=False          # 状态 默认打开

    def close(self):
        self._closed=True           # 改变状态
        # 处理 最后一次 put 时，来早了的get，让其退出 consumer
        if self.waitting and not self.items:
            for coro in self.waitting:
                scher.ready.append(coro)

    def put(self,item):
        if self._closed:            # 状态判断
            raise Queueclosed()
        self.items.append(item)     # 放消息
        if self.waitting:           # 用来早了的 get 处理消息：推动 父协程 consumer 从 暂停后 继续执行
            scher.ready.append(self.waitting.popleft())

    # 协程 收消息 可以暂停
    async def get(self):
        while not self.items:                       # 没结果就一直阻塞
            if self._closed:
                raise Queueclosed()
            self.waitting.append(scher.current)     # 把父协程 consumer 放入排队队列 self.waitting
            await switch()                          # 暂停 交出执行权
        return self.items.popleft()             

 

# 普通函数 数数
def countDown(n):
    def _run(n):
        if n>0:
        # while n>0:    
            print('Down',n)
            # time.sleep(1)
            scher.call_later(1,lambda: _run(n-1))
            # n -=1
        # print('Down done') 
        else:
            print('Down done')
    _run(n)

def countUp(stop):
    def _run(x):
        # while x<stop:
        if x<stop:
            print('Up',x)
            # time.sleep(1)
            scher.call_later(1,lambda:_run(x+1))
            # x += 1
        # print('Up done')  
        else:
            print('Up done') 
    _run(0)        


# 协程

async def producer(q,count):
    for i in range(count):
        print('生产了',i)
        q.put(i)
        await scher.sleep(1)
    print('生产结束')
    q.close()

async def consumer(q):
    try:
        while True:
            item=await q.get()
            print('消费了',item)
    except Queueclosed:
        print('消费结束')
        

start=time.time()
q=AsyncQueue()
scher.new_task(producer(q,10))
scher.new_task(consumer(q,))
scher.call_soon(lambda:countDown(5))
scher.call_soon(lambda:countUp(5))
scher.run()
print('[one]time:{:.4f}s'.format(time.time()-start))

# 结果
    # 生产了 0
    # 消费了 0
    # Down 5
    # Up 0
    # 生产了 1
    # 消费了 1
    # Down 4
    # Up 1
    # 生产了 2
    # 消费了 2
    # Down 3
    # Up 2
    # 生产了 3
    # 消费了 3
    # Down 2
    # Up 3
    # 生产了 4
    # 消费了 4
    # Down 1
    # Up 4
    # 生产了 5
    # 消费了 5
    # Down done
    # Up done
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
    # [one]time:10.0085s