
多任务 单线程 异步 并发 和 任务间 消息传递 的 总结：

任务种类：普通函数、生成器、协程、socket

1. 通过 down-up数数案例 说明 单线程 异步 并发 的实现

    1.1 第一步：实现 多任务交替
        1.1.1 切函数 —— 把函数 切成 一段一段的 小函数。
            普通函数： 
                在定义函数时，要用 递归 + [ lambda：每步函数 ] 的方法得到每步函数体，
                实现把函数切片。

            生成器、协程：天生就是切函数。因此不需要像普通函数那样刻意去定义，才能实现切函数。
                生成器通过 yield 关键字 实现 把函数切片。
                协程通过 async / await 关键字 实现 切片。

        1.1.2 装小函数 —— 用 双向队列deque 来装  切出来的小函数体。
            因为，双向队列deque 可以 右放入append，左取出popleft。保持流向。

        1.1.3 取小函数+执行+生成下一步小函数+装小函数 + 取小函数+...+装小函数 + 取... 
            这种循环实现了 多任务的 交替 执行。
    
        1.1.4 定义 调度类 class Scheduler。
            内有执行队列self.ready、用来装小函数、生成器对象、协程对象等；

            有self.current，用来装当前生成器或协程对象，便于操作当前对象；

            把函数装入队列的方法call_soon；

            把生成器对象、协程对象装入队列的方法news_task；

            从队列取出小函数（生成器对象、协程对象）执行的方法run。

            普通函数run：
                通过取出func函数体 然后 加括号func()，执行小函数，在执行的过程中，根据切函数的定义
                生成下一步小函数体，放入队列。

            生成器、协程run：
                生成器即可用 next(生成器对象) 又可用 生成器对象.send(None) 方法实现执行，执行同时就会自动更新
                生成器对象(即下一步小函数)，这是生成器本身的特性。

                协程 可用 协程对象.send(None) 方法 实现执行，并自动更新协程对象，这是协程本身的特性。


    1.2 第二步：实现 多任务并发 时分复用的实现
        1.2.1 先实现 小函数在队列里排序
            完善调度类，定义延时队列self.sleeping,用来装 不是立即执行的小函数，
            普通函数延时调用方法 call_later(delay,func) 用 堆排序heapq 实现把延时执行的小函数 有序 放入延时队列。
           
            协程延时调用方法 也是协程 async def sleep(delay)，实现的功能和使用的方法与普通函数的延时调用相同，不同在于最后要
            交出执行权 await switch()。

            为了协程切换（交出执行权） await switch() 实现，
            定义了可等待类 class Awaitable，及切换方法 switch。
        
        1.2.2 再按照 < 等则同 否则帮 > 的算法实现并行
            完善调度类，在run方法中，对于延时队列的小函数，实现 休息时间相同，就同一休息；
            休息时间不同，就少帮多休息，简言之 等则同 否则帮 。 

    1.3 实现 普通函数 的 调度类  和 协程 的 调度类  统一
        协程 和 普通函数的立即调用 和 延时调用 是不同的。
       
        run方法是相同的，统一为普通函数的run。
        为此，定义了协程外包类 class Task，在内部定义__call__方法，
        使得协程对象加括号+()就可以实现send(None)，实现执行并更新了自身。
        从形式上与普通函数 +() 就执行，统一了。

2. 统一 调度类

    最终 通过 引入 select ，及封装socket的accept、recv、send为协程的方法，实现了
    socket、协程、普通函数多任务异步并发。

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



3. 通过 produce-consumer生产-消费案例 说明 单线程 异步 并发时 任务间 的 消息传递

    3.1 定义 异步队列类 class AsyncQueue。实现存消息、放消息、取消息。
        用双向队列deque 实现了 消息队列、实现了 放消息put、取消息get。

    3.2 难点1：在于 处理来早了的get，即get时 队列里 没有消息，来早了，怎么办？等等呗，在哪等？
        因此，在  AsyncQueue 中定义了 排队队列 waitting，收集来早了的get。

    3.3 难点2：对于普通函数的消费者函数consumer的切函数定义，

    



