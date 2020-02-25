# io_scheduler.py
#
# An example of implementing I/O operations in the scheduler

import time
from collections import deque
import heapq
from select import select

# Callback based scheduler (from earlier)
class Scheduler:
    def __init__(self):
        self.ready = deque()     # Functions ready to execute
        self.sleeping = []       # Sleeping functions
        self.sequence = 0 
        self._read_waiting = { }
        self._write_waiting = { }

    def call_soon(self, func):
        self.ready.append(func)

    def call_later(self, delay, func):
        self.sequence += 1
        deadline = time.time() + delay     # Expiration time
        # Priority queue
        heapq.heappush(self.sleeping, (deadline, self.sequence, func))

    def read_wait(self, fileno, func):
        # Trigger func() when fileno is readable
        self._read_waiting[fileno] = func
        
    def write_wait(self, fileno, func):
        # Trigger func() when fileno is writeable
        self._write_waiting[fileno] = func

    def run(self):
        while (self.ready or self.sleeping or self._read_waiting or self._write_waiting):
            if not self.ready:
                # Find the nearest deadline
                if self.sleeping:
                    deadline, _, func = self.sleeping[0]
                    timeout = deadline - time.time()
                    if timeout < 0:
                        timeout = 0
                else:
                    timeout = None     # Wait forever

                # Wait for I/O (and sleep)
                can_read, can_write, _ = select(self._read_waiting,
                                                self._write_waiting, [], timeout)
                
                for fd in can_read:
                    self.ready.append(self._read_waiting.pop(fd))
                for fd in can_write:
                    self.ready.append(self._write_waiting.pop(fd))

                # Check for sleeping tasks
                now = time.time()
                while self.sleeping:
                    if now > self.sleeping[0][0]:
                        self.ready.append(heapq.heappop(self.sleeping)[2])
                    else:
                        break

            while self.ready:
                func = self.ready.popleft()
                func()

    def new_task(self, coro):
        self.ready.append(Task(coro))   # Wrapped coroutine

    async def sleep(self, delay):
        self.call_later(delay, self.current)  
        self.current = None
        await switch()   # Switch to a new task

    async def recv(self, sock, maxbytes):
        self.read_wait(sock, self.current)
        self.current = None
        await switch()
        return sock.recv(maxbytes)

    async def send(self, sock, data):
        self.write_wait(sock, self.current)
        self.current = None
        await switch()
        return sock.send(data)

    async def accept(self, sock):
        self.read_wait(sock, self.current)
        self.current = None
        await switch()
        return sock.accept()

class Task:
    def __init__(self, coro):
        self.coro = coro        # "Wrapped coroutine"

    # Make it look like a callback
    def __call__(self):
        try:
            # Driving the coroutine as before
            sched.current = self
            self.coro.send(None)
            if sched.current:
                sched.ready.append(self)
        except StopIteration:
            pass


class Awaitable:
    def __await__(self):
        yield

def switch():
    return Awaitable()

sched = Scheduler()    # Background scheduler object

# ----------------

from socket import *
# async def tcp_server(addr):
#     sock = socket(AF_INET, SOCK_STREAM)
#     sock.bind(addr)
#     sock.listen(5)
#     while True:
#         client, addr = await sched.accept(sock)
#         print('Connection from', addr)
#         sched.new_task(echo_handler(client))

# async def echo_handler(sock):
#     while True:
#         data = await sched.recv(sock, 10000)
#         if not data:
#             break
#         await sched.send(sock, b'Got:' + data)
#     print('Connection closed')
#     sock.close()

# sched.new_task(tcp_server(('', 30000)))
# sched.run()


# 收发 通信循环
async def communication(conn,cli_addr):
    
    while True:
        await sched.sleep(1) # 放到 这里就是 传 timeout
        try:
            data=await sched.recv(conn,1024)
            if not data:break
            await sched.send(conn,b'GOT:'+data.upper())
        except ConnectionResetError:
            break
    # print('关闭来自[%s]的连接'%(cli_addr))  # 报错，元组作为一个元素要加‘，’
    # ypeError: not all arguments converted during string formatting
    print('关闭来自[%s]的连接'%(cli_addr,))  # 加','，表示该元组作为一个元素，就解决了。  
    print('队列中的数量:{}'.format(len(sched.ready))) 
    conn.close()

async def server():
    server=socket(AF_INET,SOCK_STREAM)
    server.bind(('127.0.0.1',8081))
    server.listen(5)
    # server.setblocking(False)
    print('开始。。。')
    while True:
        # conn,cli_addr=server.accept()
        conn,cli_addr=await sched.accept(server)
        print('sock：{}, from:{}'.format(conn,cli_addr))
        # await sched.sleep(1) # 报错 第 50 行 self._write_waiting, [], timeout) 提供了无效参数，这时还没有
        # 建立 新的收发 协程
        sched.new_task(communication(conn,cli_addr))
    server.close()    

sched.new_task(server())
sched.run()