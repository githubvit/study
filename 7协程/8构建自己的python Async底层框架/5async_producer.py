# 生产消费者模型1 协程 实现 单线程 任务 消息传递 
# https://www.bilibili.com/video/av81742647?from=search&seid=13812321267434886846
# 时间：91：00

# 多线程 实现 消息传递
import queue
import time
from threading import Thread

def one():
    # 生产者
    def prducer(q,count):
        for i in range(count):
            print('生产了',i)
            q.put(i)
            time.sleep(1)

        print('生产结束')
        q.put(None)

    # 消费者
    def consumer(q):
        while True:
            item=q.get()
            if item is None:
                break
            print('消费了',item)
        print('消费结束')    

    start=time.time()
    q=queue.Queue()
    t1=Thread(target=prducer,args=(q,10))
    t2=Thread(target=consumer,args=(q,))
    t1.start()
    t2.start()
    t2.join()
    print('[one Threa]time:{:.4}s'.format(time.time()-start))

# one()

    # 生产了 0
    # 消费了 0
    # 生产了 1
    # 消费了 1
    # 生产了 2
    # 消费了 2
    # 生产了 3
    # 消费了 3
    # 生产了 4
    # 消费了 4
    # 生产了 5
    # 消费了 5
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
    # [one Threa]time:10.01s

# 2. 单线程 实现 消息传递

from collections import deque
import heapq

def two():

    # 可等待类
    class Awaitable():
        def __await__(self):
            yield
    # 切换
    def switch():
        return Awaitable()

    # 调度类
    class Scheduler:
        def __init__(self):
            self.ready=deque()
            self.current=None
            self.sleeping=[]
            self.sequence=0

        def new_task(self,coro):
            self.ready.append(coro)

        async def sleep(self,delay):
            self.sequence += 1
            deadline=time.time()+delay
            heapq.heappush(self.sleeping,(deadline,self.sequence,self.current))
            # self.current=None
            await switch()

        def run(self):
            while self.ready or self.sleeping:
                if not self.ready:
                    deadline,_,coro=heapq.heappop(self.sleeping)
                    delat=deadline-time.time()
                    if delat>0:
                        time.sleep(delat)
                    self.ready.append(coro)    
                self.current=self.ready.popleft()
                try:
                    self.current.send(None)
                except StopIteration:
                    pass    

    scher=Scheduler()

    # 异步队列类 AsyncQueue
    class AsyncQueue():
        def __init__(self):
            self.items=deque()
            self.waitting=deque()

        def put(self,item):
            self.items.append(item)
            if self.waitting:
                scher.ready.append(self.waitting.popleft())

        # 优化的get写法
        async def get(self):
            # 先判断没有消息
            if not self.items:
                # 没有消息 就把引用get的父协程 scher.current (就是 consumer) 放到 waitting 队列。
                # 等到 生产者 put 的时候，会从 waitting里取出 该父协程 继续执行
                self.waitting.append(scher.current)
                # 暂停，交出执行权。
                await switch()
                print('s')
            # 这样就在 暂停 后面 有了 正确的返回
            # put时，从waitting取出 scher.current (就是 consumer) 继续执行
            # 先打印 s，接着就到了这里，因在put完消息后，所以一定有消息
            # 这时得到的 None 就是 put 进来 的  None。 
            return self.items.popleft()


        # 用while，没有结果就继续在get里循环，直到有结果就返回到consumer协程的循环里。        
        async def get2(self):
            while True:
                if self.items:
                    return self.items.popleft()
                else:
                    # 没有消息 就把引用get的父协程 scher.current (就是 consumer) 放到 waitting 队列。
                    # 等到 生产者 put 的时候，会从 waitting里取出 该父协程 继续执行
                    self.waitting.append(scher.current)
                    # 暂停，交出执行权。
                    await switch()
                    print('s')

        # 错误的 get 协程写法 导致 consumer 协程中 item=await q.get()得到 Noneitem
        async def get1(self):
            if self.items:
                return self.items.popleft()
            else:
                # 没有消息 就把引用get的父协程 scher.current (就是 consumer) 放到 waitting 队列。
                # 等到 生产者 put 的时候，会从 waitting里取出 该父协程 继续执行
                # 由于 是 停留 在 get 协程 内部 的 await switch()，所以 从其后 继续执行
                # 会 先 打印 s，由于这行后面没有了代码，就返回None，让item=await q.get()得到 None。
                # 这个None是错误的，不是put进来的。
                self.waitting.append(scher.current)
                await switch()
                print('s')


    # 生产者
    async def prducer(q,count):
        for i in range(count):
            print('生产了',i)
            q.put(i)
            await scher.sleep(1)
        print('生产结束')
        q.put(None)
        # q.put('None')

    # 消费者
    async def consumer(q):
        n=0
        while True:
            n+=1
            print(n)
            item=await q.get()
# 协程嵌套子协程：
    # 就是为了在子协程内部 yield 或 await switch() 暂停 交出执行权 到外面弄点别的
        # 比如在这里，如果await q.get()没有返回结果，
            # 就先把父协程async def consumer(q)存到q的waitting的队列里。
                # 等生产者put的时候，就从waitting里拿出来继续执行。如还没结果，就继续上一步。
                # 直到有结果返回，就从子协程回到了父协程，继续父协程的执行。
                # 就是 没结果 就在 子协程 阻塞，有结果 父协程才继续执行。
                # 这一段代码就是子协程的代码，这里看不到的。
# 有结果返回的协程写法注意事项：
    # 看get协程的注释，错误的写法导致返回None，因为没有return时，结果就是None   
    # 导致一轮后，item就得到None,退出了consumer的循环，不再get，显示'消费结束'。 
    # 就把原来的 if item is None 改成了 if item == 'None'，才发现是get协程写法错误导致。 
#------------------------------------------------        
            if item is None:
            # if item == 'None':
                break
            print('消费了',item)
            
        print('消费结束')  

    start=time.time()
    q=AsyncQueue()
    scher.new_task(prducer(q,10))
    scher.new_task(consumer(q))
    scher.run()
    print('[two async]time:{:.4}'.format(time.time()-start))

two()

# 优化的get 的结果：
    # 生产了 0
    # 1
    # 消费了 0
    # 2
    # 生产了 1
    # s
    # 消费了 1
    # 3
    # 生产了 2
    # s
    # 消费了 2
    # 4
    # 生产了 3
    # s
    # 消费了 3
    # 5
    # 生产了 4
    # s
    # 消费了 4
    # 6
    # 生产了 5
    # s
    # 消费了 5
    # 7
    # 生产了 6
    # s
    # 消费了 6
    # 8
    # 生产了 7
    # s
    # 消费了 7
    # 9
    # 生产了 8
    # s
    # 消费了 8
    # 10
    # 生产了 9
    # s
    # 消费了 9
    # 11
    # 生产结束
    # s
    # 消费结束
    # [two async]time:10.03


# 正确的 get2 的结果：用 while 让没有结果 就 在get循环，直到有结果，就返回到consumer协程。
    # 生产了 0
    # 1
    # 消费了 0
    # 2
    # 生产了 1
    # s
    # 消费了 1
    # 3
    # 生产了 2
    # s
    # 消费了 2
    # 4
    # 生产了 3
    # s
    # 消费了 3
    # 5
    # 生产了 4
    # s
    # 消费了 4
    # 6
    # 生产了 5
    # s
    # 消费了 5
    # 7
    # 生产了 6
    # s
    # 消费了 6
    # 8
    # 生产了 7
    # s
    # 消费了 7
    # 9
    # 生产了 8
    # s
    # 消费了 8
    # 10
    # 生产了 9
    # s
    # 消费了 9
    # 11
    # 生产结束
    # s
    # 消费结束
    # [two async]time:10.02


# 错误的 get1 的 结果
    # 生产了 0
    # 1
    # 消费了 0
    # 2
    # 生产了 1   生产者put:取出consumer 协程,继续运行,从上次暂停的 get1协程 的 await switch() 后面一行'print('s')' 开始执行
    # s          print('s') 后面没了，就让 item=await q.get1() 得到 None。
    # 消费结束    退出循环，不再get，  
    # 生产了 2
    # 生产了 3
    # 生产了 4
    # 生产了 5
    # 生产了 6
    # 生产了 7
    # 生产了 8
    # 生产了 9
    # 生产结束
    # [two async]time:10.01