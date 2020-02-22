
# 生产-消费者模式
# https://www.bilibili.com/video/av81742647?from=search&seid=13812321267434886846
# 时间：33:00

# 通过该模型，引出了 协程队列 AsyncQueue 

# 上一讲 定义了一个调度的类， 实现了 单线程下 任务的切换和并发
#  本讲，将定义一个 异步队列 的类， 实现 单线程下 任务之间的消息传递 


import time
import queue


# 1. 多线程

import threading

def one():
    # 生产
    def producer(q,count):
        for n in range(count):
            print('生产了',n)
            q.put(n) #放入队列
            time.sleep(1)
        print('生产结束')
        q.put(None)
    # 消费
    def consumer(q):
        while True:
            item=q.get()
            if item is None:
                break
            print('消费了',item)
        print('消费结束')

    start=time.time()    
    # 建立队列 
    q=queue.Queue()

    # 建立线程
    t1=threading.Thread(target=producer,args=(q,10))
    t2=threading.Thread(target=consumer,args=(q,))
    t1.start()
    t2.start()

    # 等 消费者任务结束后 输出时间
    t2.join()
    print('[one]time',time.time()-start)

one()
# 结果
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
    # [one]time 10.01630187034607


# 2. 单线程
# 构建 异步队列 AsyncQueue
from collections import deque
import heapq
import time
def two():
    # 写一个调度的类：
    class Scheduler:
        def __init__(self):
            self.ready=deque() # 构建双向队列对象 模拟事件循环loop 里面装 准备执行的函数
            self.sleeping=[]   # 定义 延时 执行函数 列表
            self.sequence=0    # 终止时间相等时 排序的值 延时函数 的序列号

        def call_soon(self,func): # 模拟 loop.call_soon 回调并立即执行
            self.ready.append(func) # 把 准备执行的函数 右放入 队列

        def call_later(self,delay,func): # 模拟 loop.call_later 延时调用
            self.sequence+=1 #延时函数 的序列号 用self.sequence就解决了时间相等时 sort报错的问题
            deadline=time.time()+delay # 终止时间
            heapq.heappush(self.sleeping,(deadline,self.sequence,func))
            # heapq.heappush方法：
            # 1. 把self.sleeping转换成了堆，堆就是有序可迭代的生成器
            # 2. 把 元组(deadline,func) 加入堆中 并排好序
            # 两步并一步 

        def run(self):
            while self.ready or self.sleeping:
                if not self.ready:
                    #弹出self.sleeping堆中最小值
                    deadline, _, func = heapq.heappop(self.sleeping)
                    # 计算延时 不一定 就是delay,
                    # 如果延时相同，只用一个等，其余的到这，就不会>0了，不再睡了，直接加入队列执行。
                    # 因为延时堆是按大小排序的，所以前面小的帮后面大的睡了一部分。
                    # 那么总计时长，就是最大的，也就是最后的延时时间。就实现了并发。
                    delta=deadline-time.time()
                    if delta>0: 
                        time.sleep(delta) # 阻塞
                    self.ready.append(func) # 右加入到 准备执行 双向队列中

                while self.ready:
                    func=self.ready.popleft() # 从 双向队列中 左取出 准备执行的函数
                    func() # 执行

    sched=Scheduler() # 实例化调度类

    # 写一个异步的队列 
    class AsyncQueue:
        def __init__(self):
            self.items=deque()    # 消息队列 装的 就是 消息
            self.waiting=deque()  # 排队队列 这里面装的是 来早了的get

        #放消息 并 如果排队队列有get,就把 get 添加 到 调度对象的 准备执行队列中 执行
        #这样 放进去 的 消息 就立即被 取出 并得到 执行 了
        def put(self,item):
            # 放消息
            self.items.append(item)
            if self.waiting: # 处理排队中来早了的get
                func=self.waiting.popleft() # 取出 get
                # 立即执行 即self.get(callback)
                # func()  # 可能会得到深度调用、递归等
                sched.call_soon(func) # 加入 调度对象的 准备执行队列中 用 调度对象的 run 执行

        # [有消息 就 取消息 并 处理消息] 或 
        # [没消息(即来早了) 就 去排队 (put之后再get)] 
        def get(self,callback):
            # 取消息
            # 如果 items 有 一个 有效的 item ，就返回这个 item
            if self.items:
                callback(self.items.popleft()) #用回调处理左取出的 item
            else:
                # 排队 (来早了，就去排队，把get放到排队队列self.waiting 中)
                # 如果 items是空的，就把 这次的 get函数体 添加到 排队队列 self.waiting 
                # 下次 put 的时候，就会把  排队 里的get 添加 到 调度对象的 执行队列中 立即执行 
                # 这就保证 get 一定在 put 后执行
                self.waiting.append(lambda: self.get(callback))
    # 切函数 定义
    def producer(q,count):
        def _run(n):
            if n<count:
                print('生产了',n)
                # 放消息 并 如果排队队列 有 get，就立即 处理 消息
                q.put(n)
                sched.call_later(1,lambda: _run(n+1))
            else:
                print('生产结束')   
                q.put(None) 
        _run(0)        
        # for n in range(count):
        #     print('生产了',n)
        #     q.put(n) #放入队列
        #     time.sleep(1)
        # print('生产结束')
        # q.put(None)

    def consumer(q):
        # 回调函数： 消息处理 和 切函数 循环
        def _consume(item):
            if item is None:
                print('消费结束') 
            else:
                print('消费了',item)
                # 切函数 循环 添加到 准备执行列表 立即执行 
                # 下一步函数中 继续收消息 不断get 因此还要 q.get(callback = _consume)  
                # 所以这里放cousumer(q)
                sched.call_soon(lambda: consumer(q))

        # 收消息 并用 回调方式 处理消息  
        # 如果没有消息 该q.get(callback = _run) 函数体 会 放入 排队队列 
        # 因为 q 的get 使用 回调的方式处理消息
        # 所以 在 get 前，一定要有 消息处理函数，以便回调     
        q.get(callback = _consume)        

        # while True:
        #     item=q.get()
        #     if item is None:
        #         break
        #     print('消费了',item)
        # print('消费结束')

    start=time.time()
    q=AsyncQueue()
    sched.call_soon(lambda: producer(q,10))
    sched.call_soon(lambda: consumer(q,) )
    sched.run()
    print('[two]time',time.time()-start)

# two()

# 结果
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
    # [two]time 10.008880138397217

