# 用 协程 async/await 来 实现 单线程 并发 socket 1
# https://www.bilibili.com/video/av81742647?from=search&seid=13812321267434886846
# 时间：115:00

# read_wait  readable
# write_wait  writeable

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

        self.accept_wait=deque()    # 等待连接的sock
        self.read_wait=deque()      # 等待接收的sock
        self.write_wait=deque()     # 等待发送的sock

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

    # SOCK accept
    async def accept(self,sock):
        print('scher.accept(server)') 
        while True:
            try:
                return sock.accept()
            except BlockingIOError:
                # 将父协程 server 先放到 等待连接队列
                self.accept_wait.append(self.current)
                # print('暂停，交出执行权') 
                # 暂停 交出执行权
                await switch()

    # sock recv
    async def recv(self,sock,maxnum):
        print('scher.recv(conn)')
        while True:
            try:
                return  sock.recv(maxnum)
                # data=sock.recv(maxnum)
                # if not data:
                #     print('linux 对方关闭了连接')
                #     sock.close()
                #     break
                # return data
                
            except BlockingIOError:
                # 将父协程 communication 先放到 等待读队列
                self.read_wait.append(self.current)
                
                # print('暂停，交出执行权') 
                # 暂停 交出执行权
                await switch()    
            except ConnectionResetError:
                print(' 对方关闭了连接')
                sock.close()
                raise ConnectionResetError()
    
    # sock send
    async def send(self,sock,msg):
        print('scher.send(conn,msg)') 
        while True:
            try:
                return sock.send(msg)
            except BlockingIOError:
                # 将父协程 server 先放到 等待连接队列
                self.write_wait.append(self.current)
                # print('暂停，交出执行权') 
                # 暂停 交出执行权
                await switch()
            except ConnectionResetError:
                print(' 对方关闭了连接')
                sock.close()
                raise ConnectionResetError()

    def run(self):
        while self.ready or self.sleeping or self.accept_wait or self.read_wait or self.write_wait:
            if not self.ready:
                if self.accept_wait:
                    time.sleep(0.3)         # 无阻塞 socket cpu 占用 太高 人为停一停 降低占用率
                    # 0.5的速度 并发 cpu占用率 瞬间最高到20% 没有问题，
                    # 0.05的速度 就大了，cpu占用率 瞬间最高到50%，非常高，并发的客户端 有时 会崩溃。
                    self.ready.append(self.accept_wait.popleft())
                if self.read_wait:
                    self.ready.append(self.read_wait.popleft())    
                if self.write_wait:
                    self.ready.append(self.write_wait.popleft())    
                if self.sleeping:    
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

#-----------------

# 协程 socket

from socket import *

# 收发 通信循环
async def communication(conn,cli_addr):
    while True:
       
        try:
            data=await scher.recv(conn,1024)
            if not data:break
            await scher.send(conn,b'GOT:'+data.upper())
        except ConnectionResetError:
            break
    # print('关闭来自[%s]的连接'%(cli_addr))  # 报错，元组作为一个元素要加‘，’
    # ypeError: not all arguments converted during string formatting
    print('关闭来自[%s]的连接'%(cli_addr,))  # 加','，表示该元组作为一个元素，就解决了。 
    print('队列中的数量:{}'.format(len(scher.ready))) 
    conn.close()

# 链接 循环
async def server():
    server=socket(AF_INET,SOCK_STREAM)
    server.bind(('127.0.0.1',8081))
    server.listen(5)
    server.setblocking(False)
    print('开始。。。')
    while True:
        
        # conn,cli_addr=server.accept()
        conn,cli_addr=await scher.accept(server)
        print('sock：{}, from:{}'.format(conn,cli_addr))
        # 建立 新的收发 协程
        scher.new_task(communication(conn,cli_addr))
    server.close()    

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
scher.new_task(server())
scher.run()
print('[one]time:{:.4f}s'.format(time.time()-start))



