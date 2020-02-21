# 一些概念：
# • event_loop 事件循环：
#       程序开启一个无限的循环，并把一些函数注册到事件循环上。
#       当满足事件发生的时候，调用相应的协程

# • coroutine 协程：
#       协程对象，使用 async 关键字定义的函数，它的调用不会立即执行函数，
#       而是会返回一个协程对象。协程对象需要注册到事件循环，由事件循环调用

# • task 任务：
#       一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，
#       其中包含任务的各种状态
#       Task 对象被用来在事件循环中运行协程。
#       如果一个协程在等待一个 Future 对象，Task 对象会挂起该协程的执行并等待该 Future 对象完成。
#       当该 Future 对象 完成，被打包的协程将恢复执行。

# • future ：
#       代表将来执行或没有执行的任务的结果。它和 task 没有本质的区别

# async / await 关键字：
#       Python3.5 用于定义协程的关键字，async 定义一个协程，
#       await 用于挂起阻塞的异步调用接口

import time
import asyncio
import functools
# 1. 基本协程
def one():
    start = time.time()
    
    # async 关键字可定义一个协程函数
    # @asyncio.coroutine 这个装饰器也可以定义协程
    # 注意，函数的返回值才是协程，也叫事件
	
    # 协程不能单独运行，需要作为事件注入到事件循环 loop 里

    async def do_some_work(x):
        # time.sleep(.01) # 因为time.sleep会阻断整个线程，当单线程多任务时，就会卡住所有任务，这与协程的初衷不符。
        await asyncio.sleep(.01)
        print('[do_some_work]  这是个协程任务')
        print('[do_some_work]  Coroutine {}'.format(x))

    coroutine = do_some_work('one')     # 创建协程

    loop = asyncio.get_event_loop()     # 创建事件循环

    loop.run_until_complete(coroutine)  # 将协程注入事件循环生成任务对象并启动

    print('----- 运行耗时：{:.4f}s -----'.format(time.time()-start)) # :.4f 保留4位小数

# one()

# [do_some_work]  这是个协程任务
# [do_some_work]  Coroutine one
# ----- 运行耗时：0.0120s -----

# 2. task 任务
def two():
    start = time.time()
    async def do_some_work(x):
        await asyncio.sleep(.01)
        print('[do_some_work]  这是个协程任务')
        print('[do_some_work]  Coroutine {}'.format(x))

    coroutine = do_some_work('two')         # 创建协程
    loop = asyncio.get_event_loop()         # 创建事件循环

    task = loop.create_task(coroutine)      # 将协程作为参数创建任务
    # task = asyncio.ensure_future(coroutine) 作用同上
    # task 是 asyncio.Task 类的实例，asyncio.Task 是 asyncio.Future 的子类
    # 为什么要用协程创建 task ？这个过程中 asyncio.Task 类中做了一些工作
    # 其中包括预激协程，以及协程运行过程中遇到某些异常时的处理

    print(isinstance(task, asyncio.Task))   
    print(isinstance(task, asyncio.Future))
    print('[task] ', task._state)           # 打印任务状态

    loop.run_until_complete(task)           # 将任务注入事件循环并启动

    print('[task] ', task._state)           # 打印任务状态
    print('----- 运行耗时：{:.4f}s -----'.format(time.time()-start))

# two()

# True
# True
# [task]  PENDING
# [do_some_work]  这是个协程任务
# [do_some_work]  Coroutine two
# [task]  FINISHED
# ----- 运行耗时：0.0240s -----


# 3.  绑定回调
#   假如协程是一个 IO 操作，等它处理完数据后，我们希望得到通知，以便下一步数据的处理。
#   这一需求可以通过往 future 对象中添加回调来实现。
#   回调函数的最后一个参数是 future 对象，通过该对象可以获取协程返回值。
#   如果回调需要多个参数，可以通过偏函数导入

def three():
    start=time.time()

    async def do_some_work(x):
        await asyncio.sleep(.01)
        print('[do_some_work]  这是个协程任务')
        print('[do_some_work]  Coroutine {}'.format(x))

    def call_back(name,task): #回调函数   注意回调函数的最后一个参数必须为 future或task

        print('[call_back]回调函数，接到通知')   
        print('[call_back] {} 状态：{}'.format(name,task._state))    

    coroutine=do_some_work('three') # 创建协程
    loop=asyncio.get_event_loop()   # 创建事件循环

    task=loop.create_task(coroutine) #用协程创建任务
    # task=asyncio.ensure_future(coroutine) #效果同上 不同之处 在于可以在没有loop时，就可以。
    # task=asyncio.create_task(coroutine) #报错 RuntimeError: no running event loop

    task.add_done_callback(functools.partial(call_back,'coro的回调'))#用偏函数扩充回调函数，传递参数
   
    print('[task] ', task._state)           # 打印任务状态
    loop.run_until_complete(task) #将任务注入事件循环并启动任务
    print('[task] ', task._state)           # 打印任务状态
    print('----- 运行耗时：{:.4f}s -----'.format(time.time()-start))

# three()
    
# [task]  PENDING
# [do_some_work]  这是个协程任务
# [do_some_work]  Coroutine three
# [call_back]回调函数，接到通知
# [call_back] coro的回调 状态：FINISHED
# [task]  FINISHED
# ----- 运行耗时：0.0200s -----


	
# 4. 多个协程任务 
#   asyncio.gather 协程或任务收集器
#   实际项目中，往往有多个协程，同时在一个 loop 里运行。
#   为了把多个协程交给 loop，需要借助 asyncio.gather 方法。
#   任务的 result 方法可以获得对应的协程函数的 return 值

def four():
    start=time.time()

    async def do_some_work(t):
        print('[do_some_work] coroutine start sleep <{}> s'.format(t))
        await asyncio.sleep(t)
        return '[do_some_work] coroutine done sleep [{}] s'.format(t)

    def call_back(task):#用回调打印协程的结果
        res=task.result()
        print(res)

    coroutine1=do_some_work(5) #创建睡5秒的协程
    coroutine2=do_some_work(2) #创建睡2秒的协程
    
    # task1=asyncio.ensure_future(coroutine1) #用协程1创建任务1
    # task2=asyncio.ensure_future(coroutine2)

    # task1.add_done_callback(call_back) #启用回调函数来处理任务的结果
    # task2.add_done_callback(call_back)


    # gather的使用

    # gather的作用和wait不同的是。
    # 1.采用wait收集输出的结果不是futuer，
    #   没有add_done_callback回调，
    #   而gather做收集器，输出futuer，有回调功能。
    # 2.可以按照传入参数的顺序，顺序输出。

    # gather=asyncio.gather(task1,task2)  #用任务收集器gather收集任务
    # gather.add_done_callback(call_back) 
    #启用收集器的回调函数来处理任务的结果，在5秒后才输出个列表，
    # 即gather的回调是在收集器里的任务都完成后，再执行回调。 
    # ['[do_some_work] coroutine done sleep [5] s', '[do_some_work] coroutine done sleep [2] s']

    # 将上面的任务建立和收集两步并作一步
    tasks=asyncio.gather(coroutine1,coroutine2)
    
    # tasks=asyncio.wait(coroutine1,coroutine2) # 报错 wait() takes 1 positional argument but 2 were given
    # tasks=asyncio.wait([coroutine1,coroutine2])
    # 采用wait收集输出的结果不是futuer，没有add_done_callback回调，而gather做收集器，输出式futuer，有回调功能。
    # 回调
    tasks.add_done_callback(call_back) # 采用wait收集 AttributeError: 'coroutine' object has no attribute 'add_done_callback'

    loop=asyncio.get_event_loop() #创建事件循环
    
    # loop.run_until_complete(gather).add_done_callback(call_back) 
    # 将收集器注入事件循环并启动，并启用回调函数来处理收集器中完成任务的结果
    # 报错：AttributeError: 'list' object has no attribute 'add_done_callback'
    # 列表对象没有'add_done_callback'
    loop.run_until_complete(tasks)
   
    print('----- 运行耗时：{:.4f}s -----'.format(time.time()-start))

four()

# [do_some_work] coroutine start sleep <5> s
# [do_some_work] coroutine start sleep <2> s
# ['[do_some_work] coroutine done sleep [5] s', '[do_some_work] coroutine done sleep [2] s']
# ----- 运行耗时：5.0039s -----


# 5. 即时取得协程结果 asyncio.as_completed(aws, *, loop=None, timeout=None)
# 并发地运行 aws 集合中的 可等待对象。
# 返回一个 Future 对象的迭代器。
# 返回的每个 Future 对象代表来自剩余可等待对象集合的最早结果
# 示例：
# for f in as_completed(aws):
#     earliest_result = await f
#     。。。  


def five():
    start=time.time()

    async def do_some_work(t):
        print('[do_some_work] coroutine start sleep <{}> s'.format(t))
        await asyncio.sleep(t)
        return '[do_some_work] coroutine done sleep [{}] s'.format(t)

    def call_back(res):#这个回调直接取得了协程的结果
        # res=task.result()
        print(res)

    async def main():
        tasks=[]
        for i in range(1,6):
            tasks.append(asyncio.ensure_future(do_some_work(i)))
            # tasks.append(do_some_work(i))

        for task in asyncio.as_completed(tasks):
            call_back(await task) #回调直接取得了协程的结果   

    loop=asyncio.get_event_loop() #创建事件循环
    loop.run_until_complete(main())

    print('----- 运行耗时：{:.4f}s -----'.format(time.time()-start))

# five()

# [do_some_work] coroutine start sleep <1> s
# [do_some_work] coroutine start sleep <2> s
# [do_some_work] coroutine start sleep <3> s
# [do_some_work] coroutine start sleep <4> s
# [do_some_work] coroutine start sleep <5> s
# [do_some_work] coroutine done sleep [1] s
# [do_some_work] coroutine done sleep [2] s
# [do_some_work] coroutine done sleep [3] s
# [do_some_work] coroutine done sleep [4] s
# [do_some_work] coroutine done sleep [5] s
# ----- 运行耗时：4.9923s -----

# 直接用协程，没有转task
# [do_some_work] coroutine start sleep <2> s
# [do_some_work] coroutine start sleep <3> s
# [do_some_work] coroutine start sleep <1> s
# [do_some_work] coroutine start sleep <5> s
# [do_some_work] coroutine start sleep <4> s
# [do_some_work] coroutine done sleep [1] s
# [do_some_work] coroutine done sleep [2] s
# [do_some_work] coroutine done sleep [3] s
# [do_some_work] coroutine done sleep [4] s
# [do_some_work] coroutine done sleep [5] s
# ----- 运行耗时：4.9944s -----