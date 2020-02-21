# 构建自己的Python Async底层框架
# https://www.bilibili.com/video/av81742647?from=search&seid=13812321267434886846
# up:渣理大大


# 一 用 自定义的调度类 构建协程 ：实现并发 


# 两个任务 
# 1.  每隔1秒1个数 从5数到1
# 2.  每隔1秒1个数 从0数到4

import time

# 1. 单线程串行

def one():
    
    def countdown(n):
        while n>0:
            print('Down',n)
            time.sleep(1)
            n-=1

    def countup(stop):
        x=0
        while x<stop:
            print('up',x)
            time.sleep(1)
            x+=1

    start=time.time()
    countdown(5)
    countup(5)
    print('[one] {:.4f}'.format(time.time()-start))

# one()    

# Down 5
# Down 4
# Down 3
# Down 2
# Down 1
# up 0
# up 1
# up 2
# up 3
# up 4
# [one] 10.0057

# 2. 多线程并发
from concurrent.futures import ThreadPoolExecutor
def two():

    def countdown(n):
        while n>0:
            print('Down',n)
            time.sleep(1)
            n-=1

    def countup(stop):
        x=0
        while x<stop:
            print('up',x)
            time.sleep(1)
            x+=1

    start=time.time()
    tp=ThreadPoolExecutor(2)

    tp.submit(countdown,5)
    tp.submit(countup,5)

    tp.shutdown()#关池
    print('[two]time: {:.4f}'.format(time.time()-start))

# two()
# Down 5
# up 0
# Down 4
# up 1
# Down 3
# up 2
# Down 2
# up 3
# up 4
# Down 1
# [two]time: 5.0073


# 3. How to achieve concurrency without threads?
# 单线程如何实现并发？

#  3.1 Issue:Figure out how to switch between tasks.
#  问题：找出如何在任务之间切换

# 引入双向队列 deque
from collections import deque

def three_one():
    # 写一个调度的类：
    class Scheduler:
        def __init__(self):
            self.ready=deque() # 构建双向队列对象 模拟事件循环loop 里面装 准备执行的函数

        def call_soon(self,func): # 模拟 loop.call_soon 回调并立即执行
            self.ready.append(func) # 把 准备执行的函数 右放入 队列

        def run(self):
            while self.ready:
                func=self.ready.popleft() # 从 双向队列中 左取出 准备执行的函数
                func() # 执行

    sched=Scheduler() # 实例化调度类

    # 改造countdown 和 countup
    # 不用 while 用 sched 的回调 call_soon(self,func)
    # callback function
    def countdown(n):
        if n>0:
            print('Down',n)
            time.sleep(1)
            sched.call_soon(lambda:countdown(n-1)) # 把 函数的代码 加入 队列  所以一定要用 lambda

    # 用调度对象的回调来 调用 即 将函数体 加入队列
    # sched.call_soon(lambda:countdown(5))
    # 用调度对象的执行来 执行 即 从队列中 取出函数 执行
    # sched.run()
    def countup(stop,x=0):
        if x<stop:
            print('up',x)
            time.sleep(1)
            sched.call_soon(lambda : countup(stop,x+1))

    start=time.time()
    # 在队列里先放进去 两个函数体（起始任务的内容）-线头
    sched.call_soon(lambda : countdown(5))
    sched.call_soon(lambda :countup(5)) 
    
    # 扯线头——当runz起来 的时候，
    # 就  递归的 调用下一级任务 → 即 在队列里 再放进去 两个函数体（下一级任务的内容）→ 执行
    # 如此 不断 的递归调用、执行，当满足递归截止条件就结束，运行后面的代码
    # 这个run就很像 扯线头
    sched.run()
    print('[three]time: {:.4f}'.format(time.time()-start))

# three_one()

# Down 5
# up 0
# Down 4
# up 1
# Down 3
# up 2 
# Down 2
# up 3
# Down 1
# up 4
# [three]time: 10.0051

# 3.2 延时回调 实现 并发
# 交替执行做到了，时间好像还是串行，进一步 改造 模拟 call_later 延时回调
def three_two():
    # 写一个调度的类：
    class Scheduler:
        def __init__(self):
            self.ready=deque() # 构建双向队列对象 模拟事件循环loop 里面装 准备执行的函数
            self.sleeping=[]   # 定义 延时 执行函数 列表
        
        def call_soon(self,func): # 模拟 loop.call_soon 回调并立即执行
            self.ready.append(func) # 把 准备执行的函数 右放入 队列

        def call_later(self,delay,func): # 模拟 loop.call_later 延时调用
            deadline=time.time()+delay # 终止时间
            self.sleeping.append((deadline,func)) # 给 延时列表 添加（终止时间，延时执行函数体）元组
            self.sleeping.sort() # 这会按照元组的第一个，即终止时间排序。
            # 如果 终止时间相同 则比第二项 
            # 因为比第二项时  是匿名函数lambda 函数名都一样 全是fuction
            # 则会报错 TypeError: '<' not supported between instances of 'function' and 'function'

        def run(self):
            while self.ready or self.sleeping:
                if not self.ready:
                    # 在sleeping列表里找到最近的终止时间，因为已经排序，0号元组就是
                    # deadline,func=self.sleeping[0]# 这是错误的用法，不能用来解压
                    deadline,func=self.sleeping.pop(0)
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


    def countdown(n):
        if n>0:
            print('Down',n)
            # time.sleep(1) # 阻塞（没有内容可以运行）
            # sched.call_soon(lambda:countdown(n-1)) 
            sched.call_later(1.001,lambda:countdown(n-1)) # 避免时间相等 报错

    
    def countup(stop):
        def _run(x):
            if x<stop:
                print('up',x)
                # time.sleep(1)
                # sched.call_soon(lambda : _run(x+1))
                sched.call_later(1,lambda : _run(x+1))
        _run(0)

    start=time.time()
    sched.call_soon(lambda : countdown(5))
    sched.call_soon(lambda :countup(5))    
    sched.run()
    print('[three]time: {:.4f}'.format(time.time()-start))

# three_two()

# Down 5
# up 0
# up 1
# Down 4
# up 2
# Down 3
# up 3
# Down 2
# up 4
# Down 1
# [three]time: 5.0211


# 3.3 使用堆 heapq 优化 调度类 简化代码 
# 上例中 时间上并发了，但是两个任务的时间不能相同 sort会报错
# 给每个函数添加 序列号 self.sequence 项，每加个函数，就+1
# 这样如果 时间相等 则 比较后面的 self.sequence，就没有问题了
import heapq

def three_three():
    # 写一个调度的类：
    class Scheduler:
        def __init__(self):
            self.ready=deque() # 构建双向队列对象 模拟事件循环loop 里面装 准备执行的函数
            self.sleeping=[]   # 定义 延时 执行函数 列表
            self.sequence=0    # 终止时间相等时 排序的值

        def call_soon(self,func): # 模拟 loop.call_soon 回调并立即执行
            self.ready.append(func) # 把 准备执行的函数 右放入 队列

        def call_later(self,delay,func): # 模拟 loop.call_later 延时调用
            self.sequence+=1 # 用self.sequence就解决了时间相等时 sort报错的问题
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

    def countdown(n):
        def _run(n):
            if n>0:
                print('Down',n) 
                sched.call_later(1,lambda:_run(n-1))
        _run(n)
    
    def countup(stop):
        def _run(x):
            if x<stop:
                print('up',x)
                sched.call_later(1,lambda : _run(x+1))
        _run(0)

    start=time.time()
    sched.call_soon(lambda : countdown(5))
    sched.call_soon(lambda :countup(5))    
    sched.run()
    print('[three]time: {:.4f}'.format(time.time()-start))

three_three()

# Down 4
# up 1
# Down 3
# up 2
# Down 2
# up 3
# Down 1
# up 4
# [three]time: 5.0038
