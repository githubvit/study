#   https://gist.github.com/dabeaz/f86ded...
# 第1讲，通过Down和up两个数数 的任务 如何在一个线程 实现 -> 交替执行 -> 并发执行？
# 1. 交替
    # 1.1 把函数Down（或up） 切割 成 1个个小的函数。
    # 1.2 把Down和up的小函数交替放进一个队列里。
    # 1.3 从队列里逐个取出执行，就完成了交替。

    # 1.4 交替的实现
        #  1.4.1 这就需要定义一个调度的类来帮助实现，
            #   这个类里有队列，
            #   能把函数放进队列，
            #   能从队列取出执行

            # 写一个调度的类：
            class Scheduler:
                # 这个类里有队列，
                def __init__(self):
                    self.ready=deque() # 构建双向队列对象 模拟事件循环loop 里面装 准备执行的函数

                # 能把函数放进队列，    
                def call_soon(self,func): # 模拟 loop.call_soon 回调并立即执行
                    self.ready.append(func) # 把 准备执行的函数 右放入 队列

                # 能从队列取出执行
                def run(self):
                    while self.ready:
                        func=self.ready.popleft() # 从 双向队列中 左取出 准备执行的函数
                        func() # 执行

            sched=Scheduler() # 实例化调度类

        #  1.4.2 函数定义阶段 切函数
            #   对于（while和for 等）循环类的函数，都可以把每步切成一个小函数。
            #   通过改变循环类函数的定义方式，即可实现：
            #   比如：原循环函数 如下
            def countdown(n):
                while n>0:
                    print('Down',n)
                    time.sleep(1)
                    n-=1
            #   改成一步一个小函数，放进调度对象的队列里
            def countdown(n):
                if n>0:
                    print('Down',n)
                    time.sleep(1)
                    sched.call_soon(lambda:countdown(n-1)) # 把 函数的代码 加入 队列  所以一定要用 lambda

        #  1.4.3 执行 做线头 -> 扯线头
            # 用调度对象 在队列里先放进去 两个函数体（起始任务的内容）->做线头
            sched.call_soon(lambda : countdown(5))
            sched.call_soon(lambda :countup(5)) 

            # 当run起来 的时候，-> 扯线头
                # 调度对象 递归的 调用下一步任务 → 即 在队列里 再放进去 两个函数体（下一步任务的内容）→ 执行
                # 如此 不断 的递归调用、执行，当满足递归截止条件就结束，该函数循环结束
                # 这个run就很像 扯线头
            sched.run()

# 2. 并发
    # 2.1 进一步完善 调度类
        # 增加延时执行小函数列表
        # 把延时小函数放进延时堆。
        # 用堆排序把延时小函数放进延时推，并按 终结时间（小函数的执行时间）排序
        # 在执行中的并发实现：
            # 延时堆小函数按时序休息，
            # 休息时间相等的同一休息，小的帮大的休息。
            # 把延时堆中休息完的小函数及时加入到准备执行队列，并执行，实现并发。

    # 2.2 进一步完善 切函数
        # 循环中的每一步更像一个小函数
        # 使用改进的调度对象 的 延时调用

    # 2.3 并发的实现

        # 调度类的改进：
        class Scheduler:
            # 1 增加延时执行小函数列表
            def __init__(self):
                self.ready=deque() # 构建双向队列对象 模拟事件循环loop 里面装 准备执行的函数
                self.sleeping=[]   # 增加 定义 延时 执行函数 列表
                self.sequence=0    # 终止时间相等时 排序的值

            def call_soon(self,func): # 模拟 loop.call_soon 回调并立即执行
                self.ready.append(func) # 把 准备执行的函数 右放入 队列

             # 2 把延时小函数放进延时堆。
            def call_later(self,delay,func): # 模拟 loop.call_later 延时调用
                self.sequence+=1 # 用self.sequence就解决了时间相等时 sort报错的问题
                deadline=time.time()+delay # 终止时间
                 # 3 用堆排序把延时小函数放进延时推，并按 终结时间（小函数的执行时间）排序
                heapq.heappush(self.sleeping,(deadline,self.sequence,func))
                 
            # 只要run起来，准备执行队列的任务 会被立即执行 延时队列的任务 一定到时执行
            def run(self):
                # 不间断的执行 准备执行队列 和 延时执行 队列
                while self.ready or self.sleeping:
                    if not self.ready:
                        #弹出self.sleeping堆中最小值
                        deadline, _, func = heapq.heappop(self.sleeping)

                        # 4 并发的实现
                        # 延时堆小函数按时序休息，
                        # 休息时间相等的同一休息，小的帮大的休息。
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

        # 完善 切函数
            # 原函数
            def countup(stop):
                x=0
                while x<stop:
                    print('up',x)
                    time.sleep(1)
                    x+=1

            # 改进 切函数：把循环的每一步切成小函数。放进 执行队列。
            def countup(stop,x=0):
                if x<stop:
                    print('up',x)
                    time.sleep(1)
                    # 用调度对象 递归调用 把每一步函数 加入 准备执行队列
                    sched.call_soon(lambda : countup(stop,x+1))

            # 完善 切函数
            def countup(stop):
                # 循环中的每一步更像一个小函数
                def _run(x):
                    if x<stop:
                        print('up',x)
                        #  使用改进的调度对象 的 延时调用
                        sched.call_later(1,lambda : _run(x+1))
                _run(0)

# 如何在单线程实现并发总结：
    #  1. 定义 函数 按 切函数 定义，用调度对象的 call_soon 或 call_later 把小函数放到 队列 中。
    #  2. 用调度对象的call_soon调用函数 做线头
    #  3. 用调度对象的run方法执行 扯线头              