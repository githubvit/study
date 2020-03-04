
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

    3.3 难点2：对于原函数中有 item=q.get() 语句,为避免无消息时错误的返回None。
        对于协程：使得有消息就返回消息，无消息就把父协程放到排队队列，然后暂停交出执行权。
            当生产者put消息时，再去处理排队队列里的父协程，这时，就返回到get的暂停处向后执行。
            这里就要注意写法，避免返回None。
            while not items:
                self.waitting.append(self.current)
                await switch()
            return self.items.popleft()    
        对于普通函数：消费者函数consumer的切函数定义要用 回调方式 处理，
            使得有消息，就用回调处理消息并定义下一步切函数；没有消息就把get[ self.get(call_back)]
            放到排队队列中。 

    3.4 难点3：队列的关闭，一定要在队列的关闭方法 close() 中处理 最后一次 put 时，来早了的get。
        用这个get才能关闭队列和激发队列异常，使得消费者consumer程序捕捉到队列异常退出程序。
        要定义队列异常类 class QueueClosed(Exception)。
        对于协程：
            当put或get检测到closed状态为True时，激发队列异常。consumer捕获异常使得退出消费者程序。
        对于普通函数：
            要再定义一个 class Result 类，其中 定义 result方法，把该类的对象作为回调的参数，
            让消费者调用 Result对象的 result方法，item=res.result()。
            使得当get正常返回时，返回值 callback(Result(val=self.items.popleft()))。
            当closed状态为True时，返回异常 callback(Result(exc=QueueClosed())) 。
            这样，当消费者调用 Result对象的 result方法 捕获到异常就退出了程序。

4. 异步队列 class AsyncQueue
    普通函数：
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

            # 普通函数的 get 和协程不同，其余都是一样的。
            # [有消息 就 取消息 并 处理消息] 或 
            # [没消息(即来早了) 就 去排队 (put之后再get)] 
            def get(self,callback):

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
           
            #普通函数的消费者切函数定义 用 回调 方式
            def consumer(q):
                # 回调函数： 消息处理 和 切函数 循环
                # 10 改造：用 Result类对象 作为参数,调用其result方法 实现 正常返回 和 激发异常
                # 11 捕捉异常 
                def _consume(res):
                    try:
                        item=res.result()
                        print('消费了',item,q.con)
                        # 切函数 循环 添加到 准备执行列表 立即执行 
                        # 下一步函数中 继续收消息 不断get 因此还要 q.get(callback = _consume)  
                        # 所以这里放cousumer(q)
                        sched.call_soon(lambda: consumer(q))
                    except QueueClosed:
                        print('消费结束') 

                # 收消息 并用 回调方式 处理消息  
                # 如果没有消息 该q.get(callback = _run) 函数体 会 放入 排队队列 
                # 因为 q 的get 使用 回调的方式处理消息
                # 所以 在 get 前，一定要有 消息处理函数，以便回调     
                q.get(callback = _consume)        

                # 原函数
                # while True:
                #     item=q.get()
                #     if item is None:
                #         break
                #     print('消费了',item)
                # print('消费结束')
    
    协程：
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

            # 收消息 其实 就是 这里和普通函数处理不同，其余都一样。
            async def get(self):
                while not self.items:
                # if not self.items:   # 必须改成上面 不然 最后一次 不会激发异常 
                # 而是 会继续return 然后 报错 IndexError: pop from an empty deque
                    if self._closed:
                        raise QueueClosed()
                    self.waitting.append(scher.current) # get来早了 就把父协程 consumer收集到waitting
                    await switch()  # 暂停 交出执行权
                return self.items.popleft()

        # 消费者 协程
        async def consumer(q):
            try:
                while True:
                    item=await q.get()      # 协程嵌套 无结果就阻塞 有结果才返回
                    # if item is None: break
                    print('消费了',item)
            except QueueClosed:
                print('消费结束')         