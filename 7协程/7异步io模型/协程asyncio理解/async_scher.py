# 这是 自定义 的 async 底层 框架 的 统一 调度类
# 可让 普通函数 协程 socket 实现 单线程 异步 并发 

from collections import deque
import heapq
import time
import select

# 可等待类
class Awaitable:
    def __await__(self):
        yield

# 切换
def switch():
    return Awaitable()

# 协程外包 : 
class Task:
    def __init__(self,coro):
        self.coro=coro
    def __call__(self): # 该方法 是加括号就 执行 即 Task(coro)() 就执行
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
        # 1 定义 收发 字典：
        self.read_wait={}    # 等待接收的sock
        self.write_wait={}   # 等待发送的sock

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
    
    # 2 封装 socket 的 accept recv send
    # SOCK accept
    async def accept(self,sock):
        print('scher.accept(server)') 
        # 将父协程 server 先放到 等待读字典
        self.read_wait[sock]=self.current
        # print('暂停，交出执行权') 
        # 暂停 交出执行权
        await switch()
        return sock.accept()
    
    # sock recv 封装 sock.recv(maxnum)
    async def recv(self,sock,maxnum):
        print('scher.recv(conn)')
        # 将 该sock对象 和 当前协程 交给 select 的 等待读字典
        self.read_wait[sock]=self.current
        # print('暂停，交出执行权') 
        # 暂停 交出执行权
        await switch()  
        # 当select监测到该sock 有了返回，就回到当前协程的暂停处。
        # 用 该sock去取结果。  
        return  sock.recv(maxnum)
   
    # sock send
    async def send(self,sock,msg):
        print('scher.send(conn,msg)') 
        self.write_wait[sock]=self.current
        # 暂停 交出执行权
        await switch() 
        return sock.send(msg)    
    
    def run(self):
        while self.ready or self.sleeping or self.read_wait or self.write_wait:
        
            if not self.ready:
                # 3 用 select 处理 socket
                if self.read_wait or self.write_wait:
                    # 3.1 轮询 sock列表 轮询的timeout等于1秒。
                    can_read,can_write,_=select.select(self.read_wait,
                                                    self.write_wait,[],1)
                    for sock in can_read:
                        # 3.2 在select的读字典中 删除 当前sock 项
                        # 3.3 回到当前 sock 的 协程 的 暂停处 继续执行
                        self.ready.append(self.read_wait.pop(sock))
                    for sock in can_write:
                        # 同上
                        self.ready.append(self.write_wait.pop(sock))
                # 延时
                if self.sleeping:
                    deadline,_,func=heapq.heappop(self.sleeping)    # 取出 终结时间 最小的
                    delat=deadline-time.time()
                    # 并发：等则同，否则帮。
                    if delat>0:
                        time.sleep(delat)
                    self.ready.append(func)
            # 只要立即执行队列里有，就一直执行
            while self.ready:                             
                func=self.ready.popleft()
                func()

# 生成调度对象
scher=Scheduler()



