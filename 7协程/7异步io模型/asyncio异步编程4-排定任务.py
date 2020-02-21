# 排定任务
# 排定 task / future 在事件循环中的执行顺序，也就是对应的协程先执行哪个，
# 遇到 IO 阻塞时，CPU 转而运行哪个任务，这是我们在进行异步编程时的一个需求。
# 前文所示的多任务程序中，事件循环里的任务的执行顺序由 
# asyncio.ensure_future / loop.create_task 和 asyncio.gather / asyncio.wait 排定


import asyncio
import time

# 1. loop.call_soon
# 将普通函数作为任务加入事件循环并排定执行顺序。

def one():
    def hello(name):          # 普通函数
        print('[hello] Hello, {}'.format(name))

    async def work(t, name):  # 协程函数
        print('[work]  start', name)
        await asyncio.sleep(t)
        print('[work]  {} after {}s stop'.format(name, t))

    loop = asyncio.get_event_loop()         # 创建事件循环
    # asyncio.ensure_future(work(1, 'A'))   # 向事件循环中添加任务  （第 1 个执行
    loop.create_task(work(1, 'A'))          # 效果同上
    
    # call_soon 将普通函数当作 task 加入到事件循环并排定执行顺序
    # 该方法的第一个参数为普通函数名字，普通函数的参数写在后面          （第 2 个执行
    loop.call_soon(hello, 'Tom')
    loop.create_task(work(2, 'B'))          # 向事件循环中添加任务   （第 3 个执行
    # 阻塞启动事件循环，顺便再添加一个任务                             （第 4 个执行
    loop.run_until_complete(work(3, 'C'))

# one()

# [work]  start A
# [hello] Hello, Tom
# [work]  start B
# [work]  start C
# [work]  A after 1s stop
# [work]  B after 2s stop
# [work]  C after 3s stop


# 2. loop.stop
# 此方法停止事件循环之前，每个任务都会获得一次执行机会

def two():
    # 普通函数
    def hello(name):
        print('[hello] Hello,{}'.format(name))

    # stop 普通函数
    def stop(loop):
        # 事件循环的 stop 方法会停止全部任务后结束事件循环
        # 在停止前，每个任务都将运行一次，直到遇到 IO 阻塞
        # 可以尝试将下面这行代码放到任意普通函数和协程函数的任意位置执行来查看区别
        loop.stop()
        

    def call_cancel():
        tasks=asyncio.Task.all_tasks()
        for i in tasks:
            i.cancel()

    # 协程函数
    async def work(t,name):
        print('[work] start',name)
        await asyncio.sleep(t)
        print('{} after {}s stop'.format(name,t))

    # 创建循环
    loop=asyncio.get_event_loop()

    # 创建任务1
    loop.create_task(work(1,'A'))     # 第1个执行

    # 创建任务2    
    # 用call_soon给 普通函数 创建任务 
    #  参数：普通函数名，普通函数参数
    loop.call_soon(hello,'Tom')       # 第2个执行

    # 创建任务3
    # 用call_soon给 stop普通函数 创建任务
    # 这个任务虽然是第 3 个执行，但要等待每个任务执行一次之后才会 stop
    loop.call_soon(stop,loop)

    # 创建任务4
    loop.create_task(work(2,'B'))

    # 清理事件循环 从内存中删除pending的任务 wait_for=<Future cancelled>
    loop.call_soon(call_cancel)

    # 为了让 run.stop 方法起作用
    # 这里使用 run_forever 方法无限运行事件循环，直到 run.stop 执行
    loop.run_forever()

    loop.close() #关闭之前会给出报告

# two()

# [work] start A
# [hello] Hello,Tom
# [work] start B

# 如果没有loop.close(),就没有下面的报告
# Task was destroyed but it is pending!
# task: <Task pending coro=<two.<locals>.work() running at d:/pyj/st/7协程/7异步io模型/asyncio异步编程4-排定任务.py:68> 
# wait_for=<Future cancelled>>
# Task was destroyed but it is pending!
# task: <Task pending coro=<two.<locals>.work() running at d:/pyj/st/7协程/7异步io模型/asyncio异步编程4-排定任务.py:68> 
# wait_for=<Future cancelled>>


# 3. loop.call_later

def three():
    def hello(name):
        print('[hello] Hello,{}'.format(name))

    # 协程函数
    async def work(t,name):
        print('[work] start',name)
        await asyncio.sleep(t)
        print('{} after {}s stop'.format(name,t))
    
    loop=asyncio.get_event_loop()
    loop.create_task(work(1,'A'))               #  1 5
    loop.call_later(1.2, hello, 'Tom')          #  6
    loop.call_soon(hello, 'Kitty')              #  2
    task4=loop.create_task(work(2, 'B'))        #  3 7
    loop.call_later(1, hello, 'Jerry')          #  4
    # 这个方法的参数其实无所谓，有就行，但参数须为 future / task
    loop.run_until_complete(task4)

# three()

# [work] start A
# [hello] Hello,Kitty
# [work] start B
# [hello] Hello,Jerry
# A after 1s stop
# [hello] Hello,Tom
# B after 2s stop


# 4. loop.call_at & loop.time
# call_soon 立刻执行，call_later 延时执行，call_at 在某时刻执行
# loop.time 就是事件循环内部的一个计时方法，返回值是时刻，数据类型是 float

# 这三个 call_xxx 方法的作用都是将普通函数作为任务排定到事件循环中，
# 返回值都是 asyncio.events.TimerHandle 实例，
# 它们不是  future ，不能作为 loop.run_until_complete  的参数

def four():
    def hello(name):
        print('[hello] Hello,{}'.format(name))

    # 协程函数
    async def work(t,name):
        print('[work] start',name)
        await asyncio.sleep(t)
        print('{} after {}s stop'.format(name,t))
    
    loop=asyncio.get_event_loop()
    # 事件循环内部时刻
    start = loop.time()                         
    loop.create_task(work(1,'A'))                  #  1 5
    loop.call_at(start+1.2, hello, 'Tom')          #  6
    loop.call_soon(hello, 'Kitty')                 #  2
    task4=loop.create_task(work(2, 'B'))           #  3 7
    loop.call_at(start+1, hello, 'Jerry')          #  4
    # 这个方法的参数其实无所谓，有就行，但参数须为 future / task
    loop.run_until_complete(task4)

# four()

# 结果和 3 一样



# 5. asyncio.lock 协程锁

# 协程锁通常使用在子协程中，其作用是将协程内部的一段代码锁住，直到这段代码运行完毕解锁。
# 协程锁的固定用法是使用 async with 创建协程锁的上下文环境，将代码块写入其中

def five():
    l = []
    lock = asyncio.Lock()   # 协程锁

    async def work(name):
        print('lalalalalalalala')     # 打印此信息是为了测试协程锁的控制范围      1:p1     5:p3
        
        # with 取代开头的 上锁lock.acquire() 和 结尾的 释放锁lock.release()。
        async with lock:                                                              # 6:go3  11:go5
            print('{} start'.format(name))  # 头一次运行该协程时打印             2:p2            12:p7
            if 'x' in l:                    # 如果判断成功
                return name                 # 直接返回结束协程，不再向下执行                      13:go6  
            await asyncio.sleep(0);         # 阻塞 0 秒，切换协程               3:go1
            print('----------')                                                       # 7:p4
            l.append('x')
            print('{} end'.format(name))                                              # 8:p5
            return name

    async def one():
        name = await work('one')                                      # go              9：go4
        print('{} ok'.format(name))                                                   # 10:p6

    async def two():
        name = await work('two')                                            # 4:go2   
        print('{} ok'.format(name))                                                           # 14:p8

    loop = asyncio.get_event_loop()
    tasks = asyncio.wait([one(), two()])
    loop.run_until_complete(tasks)

five() 
# 执行的时序：
# go:切  p:print
# go → 1:p1 → 2:p2 → 3:go1 → 4:go2 → 5:p3 → 6:go3 → 7:p4 → 
#   8:p5 → 9：go4 → 10:p6 → 11:go5 → 12:p7 → 13:go6 → 14:p8

# lalalalalalalala     one 主协程 切 one 的 work 子协程
# one start            sleep(0)  切 two主协程 切 two 的 work 子协程
# lalalalalalalala     with lock 切 one 的 work 子协程
# ----------           one 的 work 子协程 继续
# one end              one 的 work 子协程 执行完毕 锁 释放  切 one 主协程
# one ok               one 的 主协程 执行完毕 切 two 的 work 子协程
# two start            因为 l 里面有‘x’ 马上结束 two 的子协程 work 切 two 主协程
# two ok               two 主协程 执行完毕  