#  用 协程 async/await 来 实现 单线程 并发 socket 2 select

# 用 select 做代理 收发
    # 应用程序 把要连接的 socket对象 都交给 select，  自己可以干点别的，不会阻塞。
    # select 会和 系统的io接口 打交道，当某个socket 有返回，就通知应用程序的该socket来取。
    # 这样 就可以 让 应用程序 起一堆socket，可以保证并发，不阻塞。

# select做了哪些事？
    # 1 设定 server 为 非阻塞  等于 # server.setblocking(False)
    # 2 与系统io接口打交道，轮询 三个(socket对象)列表： 读列表 写列表 异常列表，一般只用两个，第三个写空列表。
    # 3 输出 三个(socket对象)列表：能读、能写、异常。一般用前两个即可。
        #  把系统io接口有返回的socket 输出到 相应列表。如下：
            #  让select的超时时间timeout等于1秒。
            #  can_read,can_write,_ = select.select(self.read_wait,self.write_wait,[],1)
        #  循环能读、能写列表，取出socket对象连接系统io，此时的socket对象即可立即收发数据。

# 本例的实现：
    #  1 定义 收发 字典 ：
       # self.read_wait={}    # 等待接收的sock
       # self.write_wait={}   # 等待发送的sock

    #  2 封装 socket 的 accept recv send
        # 以 封装 recv 为例，步骤accept和send都一样。

        # async def recv(self,sock,maxnum):

              # 2.1 将 该sock对象 和 当前协程 交给 select 的 等待读字典
        #     self.read_wait[sock]=self.current

              # 2.2 暂停 交出执行权
        #     await switch()   
         
              # 2.3 当select监测到该sock 有了返回，就回到当前协程的暂停处。
              # 用 该sock去取结果。
        #     return  sock.recv(maxnum)

    # 3 用 select 处理 socket
        # if self.read_wait or self.write_wait:
        #     # 3.1 轮询 sock列表 轮询的timeout等于1秒。
        #     can_read,can_write,_=select.select(self.read_wait,
        #                                     self.write_wait,[],1
        #     for sock in can_read:
        #         # 3.2 在select的读字典中 删除 当前sock 项
        #         # 3.3 回到当前 sock 的 协程 的 暂停处 继续执行
        #         self.ready.append(self.read_wait.pop(sock))
        #     for sock in can_write:
        #         # 同上
        #         self.ready.append(self.write_wait.pop(sock)) 
    

# 本例的精妙之处，在于select的读列表、写列表参数用了字典。
    # 数据结构的妙用，定义字典：
        # self.read_wait[sock]=当前协程

    # 正是因为这样定义，才可以实现当 该sock 有返回，就 返回到 当前sock 的 协程。
        
    # 也正是因为这样定义，才可以 让 self.read_wait.pop(sock) 实现：
        #  在select的读字典中 删除 当前sock 项
        #  返回 以 当前 sock 为 key 的 值 ，即当前sock暂停的协程


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
        await scher.sleep(1) # 这就实现了延时1秒，而不是和原版中的这里是传timeout
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
    # server.setblocking(False)
    print('开始。。。')
    while True:
        # await scher.sleep(1)
        # conn,cli_addr=server.accept()
        conn,cli_addr=await scher.accept(server)
        print('sock：{}, from:{}'.format(conn,cli_addr))
        # 建立 新的收发 协程
        scher.new_task(communication(conn,cli_addr))
        # await switch()
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


# 协程 生产-消费

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

