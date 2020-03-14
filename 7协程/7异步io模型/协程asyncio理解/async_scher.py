# 这是 自定义 的 async 底层 框架 的 统一 调度类
# 可让 普通函数 协程 socket 实现 单线程 异步 并发 

from collections import deque
import heapq
import time
import select

# 回----------------------------------------------------------------------------------------------调
# 增加 调度类 的 回调类
# 使得协程或普通函数 在做线头时，即最开始使用调度类对象把协程或普通函数的切函数放进立即队列时。
# 即 new_task(协程的立即调用) 或 call_soon及call_later(普通函数的立即及延时调用)
# 返回一个 回调类的对象SchedulerCallback(func)
# 这样就可以用该对象下的回调方法绑定回调函数了。
class SchedulerCallback:
    def __init__(self,func):
        self.key=func
        self.result_status=False
        self.result=None
        self.status='Pending'
        self.callback=None

    # 回调 生成函数体 
    def add_done_callback(self,*args,callback=None):
        self.callback=lambda : callback(args,self) # 传入 self 保证回调函数的最后一个参数是回调对象自身

    # 结果 改变状态
    def get_result(self):
        self.result_status=True
        
# 回----------------------------------------------------------------------------------------------调        
        
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
        except StopIteration as e:
            # print('1',e)
            # 取得 该协程 结果
            if scher.res[self].result_status:
                # print('2',e)
                scher.res[self].result=e
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

        # 回----------------------------------------------------------------------------------------------调
        # 回调功能
        self.res={}          # 回调结果
        # 回----------------------------------------------------------------------------------------------调


    # 普通函数 把切函数 放进 立即执行队列
    def call_soon(self,func):
        self.ready.append(func)
        # 回----------------------------------------------------------------------------------------------调
        self.res[func]=SchedulerCallback(func)
        return self.res[func]
        # 回----------------------------------------------------------------------------------------------调

    # 普通函数 延时调用
    def call_later(self,delay,func):
        self.sequence +=1
        deadline=time.time()+delay  # 终结时间
        heapq.heappush(self.sleeping,(deadline,self.sequence,func)) # 放进延时推 并 排序

        # 回----------------------------------------------------------------------------------------------调
        self.res[func]=SchedulerCallback(func)
        return self.res[func]
        # 回----------------------------------------------------------------------------------------------调
    
            
    
    # 协程 立即调用
    def new_task(self,coro):
    # 回----------------------------------------------------------------------------------------------调
        func=Task(coro)
        self.ready.append(func)  
        self.res[func]=SchedulerCallback(func)
        return self.res[func]
    # 回----------------------------------------------------------------------------------------------调
   
    # 协程 延时调用
    async def sleep(self,delay):
        self.sequence +=1
        deadline=time.time()+delay  # 终结时间
        heapq.heappush(self.sleeping,(deadline,self.sequence,self.current)) # 放进延时推 并 排序
        await switch()

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
    
    # 回----------------------------------------------------------------------------------------------调   
    # 回调信号
    def callback_able(self):
        if self.res[self.current]:
            self.res[self.current].status='Done'
    # 回----------------------------------------------------------------------------------------------调        
    
    def run(self):
        cnt=0
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

                # 回----------------------------------------------------------------------------------------------调

                # 每步函数 运行的状态 'pending' 和 'Done'
                if self.res[func].status=='Done':                
                    print('fo对象',func,self.res[func],len(self.res),self.current)
                    # 如果有回调,就执行回调
                    if self.res[func].callback: 
                        self.res[func].callback()
                        cnt +=1
                        print('cnt',cnt)
                        # print('self.current:',self.current)
                    # 执行完了，就删除
                    del self.res[func]  
                # 回----------------------------------------------------------------------------------------------调
      


# 生成调度对象
scher=Scheduler()



# 二 异步队列 AsyncQueue

 # 1. 定义一个队列关闭异常
class QueueClosed ( Exception ):
    pass
# 2. 普通函数 定义callback的参数对象 用的类  
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
   
    # 普通函数 get f_get()
    # 和协程不同，其余都是一样的。
    # [有消息 就 取消息 并 处理消息] 或 
    # [没消息(即来早了) 就 去排队 (put之后再get)] 
    def f_get(self,callback):
        # 取消息
        # 如果 items 有 一个 有效的 item ，就返回这个 item
        if self.items:
            # 6 用Result对象 作为 参数 取值
            callback(Result(val=self.items.popleft())) #用回调处理左取出的 item
        else:
            # 7 状态判断  
            if self._closed:
                # 8 用Result对象 作为 参数 传递异常
                callback(Result(exc=QueueClosed())) #
            # 排队 (来早了，就去排队，把get放到排队队列self.waiting 中)
            # 如果 items是空的，就把 这次的 get函数体 添加到 排队队列 self.waiting 
            # 下次 put 的时候，就会把  排队 里的get 添加 到 调度对象的 执行队列中 立即执行 
            # 这就保证 get 一定在 put 后执行
            self.waiting.append(lambda: self.get(callback))
   
    # 协程 get c_get()
    # 收消息 其实 就是 这里和普通函数处理不同，其余都一样。
    async def c_get(self):
        while not self.items:
        # if not self.items:   # 必须改成上面 不然 最后一次 不会激发异常 
        # 而是 会继续return 然后 报错 IndexError: pop from an empty deque
            if self._closed:
                raise QueueClosed()
            self.waitting.append(scher.current) # get来早了 就把父协程 consumer收集到waitting
            await switch()  # 暂停 交出执行权
        return self.items.popleft()


q=AsyncQueue()