
# 需求：有个协程调度器，每隔1秒,拉起1个job,job并发

import asyncio
import random
# import functools
import time

# 1 没有实现并发 实际串行
def one():
    # 定义调度器 入口
    async def coro_scheduler():
        page=1
        while True:
            await asyncio.sleep(1) # 每隔1秒
            # 调job
            url='{}/{}'.format('www.baidu.com',page)
            await job(url)
            page +=1

    # # 定义job 下载网页 www.baidu.com/1
    async def job(url):
        # 模拟下载时间
        await asyncio.sleep(random.randint(1,3))
        print('下载成功',url) 

    # 启动协程
    asyncio.run(coro_scheduler())

# one()

# 1.5 自定义async 框架 实现上例1 串行
import async_scher
scher=async_scher.scher
def one_five():
    # 定义调度器 入口
    async def coro_scheduler():
        page=1
        while page<11:
            await scher.sleep(1) # 每隔1秒
            # 调job
            url='{}/{}'.format('www.baidu.com',page)
            await job(url)
            page +=1

    # # 定义job 下载网页 www.baidu.com/1
    async def job(url):
        # 模拟下载时间
        await scher.sleep(random.randint(1,3))
        print('下载成功',url) 

    # 启动协程
    start=time.time()
    scher.new_task(coro_scheduler())
    scher.run()
    print('[one_five]time{:.4f}s'.format(time.time()-start))

# one_five()

# 结果
    # 下载成功 www.baidu.com/1
    # 下载成功 www.baidu.com/2
    # 下载成功 www.baidu.com/3
    # 下载成功 www.baidu.com/4
    # 下载成功 www.baidu.com/5
    # 下载成功 www.baidu.com/6
    # 下载成功 www.baidu.com/7
    # 下载成功 www.baidu.com/8
    # 下载成功 www.baidu.com/9
    # 下载成功 www.baidu.com/10
    # [one_five]time28.0096s

# 2 实现 并发 的关键： 
#   1). 不能在一个协程等另一个协程，而是要把 另一个协程 注册给 事件循环loop
#   2). 让渡执行权给 事件循环loop 的其他任务 await asyncio.sleep(0)

# 定义调度器 入口
def two():
    async def coro_scheduler():
        page=1
        while True:
            await asyncio.sleep(.1) # 每隔.1秒 如果下面没有让渡执行权，也可在这里让渡
            # await 是 让渡 执行权 给 asyncio.sleep(1) 执行
            # 而 asyncio.sleep(1) 要执行1秒，
            # 然后 执行权 让渡给 事件循环中 的其他任务，job
            # 这样 事件循环loop中的job 就得到了执行的机会。
            # 而 asyncio.sleep(1) 可以用来调节 while True 的速度。
            # 如果 速度 为0 ，则 while True 瞬间 可以达到 5 位数的循环
            # 也就可以 瞬间 在 事件循环 中注册并启动 5位数 的任务。
            # 达到并发的效果

            # 如果上下都没有让渡执行权，那么事件循环中的job永远得不到执行
            # 也就是，一定要有await 让出 执行权

            # 调job
            url='{}/{}'.format('www.baidu.com',page)

             # 把job注册到事件循环
            task=asyncio.create_task(job(url))

            # 并发：不能在一个协程中等待另一个协程，
            # 下面这样注册还是串行
            # await asyncio.create_task(job(url))

            # 主动让渡执行权给job 
            # await asyncio.sleep(0) 

            page +=1

    # 定义job 下载网页 www.baidu.com/1
    async def job(url):
        # 模拟下载时间
        await asyncio.sleep(random.randint(1,3))
        print('下载成功',url) 

    # 启动协程
    asyncio.run(coro_scheduler())

# two()   

# 2.5 自定义async 框架 实现上例2 并发
def two_five():
    async def coro_scheduler():
        page=1
        while page<11:
            
            await scher.sleep(1) # 每隔1秒
            # 调job
            url='{}/{}'.format('www.baidu.com',page)
            # 实现并发的关键 就是在这里 新起 一个独立任务
            # scher.new_task(job(url))

            # 如果采用上述调用方式，就是一个协程两次运行，就会产生两次回调的问题，
            # 因此，在自定义的async框架中 增加了下面这种调用方式：稍后调用，
            # 就统一了 scher.new_task(job(url)) 和 原来job协程里的 await scher.sleep(random.randint(1,3))
            # 使得该协程只在稍后运行一次。因此，只产生一次回调。
            scher.later_task(random.randint(1,3),job(url))
            print ('page',page)
            page +=1

    # 定义job 下载网页 www.baidu.com/1
    async def job(url):
        # 模拟下载时间
        # await scher.sleep(random.randint(1,3))
        print('下载成功',url) 

    # 启动协程
    start=time.time()
    scher.new_task(coro_scheduler())
    scher.run()
    print('[two_five]time{:.4f}s'.format(time.time()-start))

two_five()

# 结果
    # 下载成功 www.baidu.com/1
    # 下载成功 www.baidu.com/3
    # 下载成功 www.baidu.com/2
    # 下载成功 www.baidu.com/5
    # 下载成功 www.baidu.com/4
    # 下载成功 www.baidu.com/6
    # 下载成功 www.baidu.com/7
    # 下载成功 www.baidu.com/8
    # 下载成功 www.baidu.com/9
    # 下载成功 www.baidu.com/10
    # [two_five]time11.0030s

# 3 并发+实现回调
def three():

    # 定义调度器 入口
    async def coro_scheduler():
        page=1
        while True:
            # await asyncio.sleep(.001) # 每隔1秒 可以用来调节速度。如果该行注释，则瞬间可以达到5位数。
            
            # 调job
            url='{}/{}'.format('www.baidu.com',page)
            task=asyncio.create_task(job(url)) # 把job注册给事件循环 等待执行

            # 回调，利用偏函数 扩充回调 给传递参数
            task.add_done_callback(functools.partial(call_job_done,url))

            await asyncio.sleep(0) # 主动让渡执行权给事件循环中的job 这一步很关键没有的话 还是串行
            page +=1

            print(page)

    # 定义job 下载网页 www.baidu.com/1
    async def job(url):
        # 模拟下载时间
        await asyncio.sleep(random.randint(1,3))
        return '返回值'

    # 回调
    def call_job_done(url,task): #回调的最后一个参数必须式task,
        #yongtask可以取得协程的返回值，以及处理异常task.exceptionc()
        print('下载成功',url,task.result(),task.exception()) 


    # 启动协程
    # asyncio.run()用try except 无法捕捉到KeyboardInterrupt异常 
    # 一按ctrl+c 报 主线程 没有事件循环
    # RuntimeError: There is no current event loop in thread 'MainThread'.

    # 用低级 api 解决 
    # 创建 事件循环
    loop=asyncio.get_event_loop()
    try: # 程序运行过程中，快捷键 Ctrl + C 会触发 KeyboardInterrupt 异常 

        # asyncio.run(coro_scheduler()) # 无法捕捉到KeyboardInterrupt异常
    
        loop.run_until_complete(coro_scheduler())
    except KeyboardInterrupt:
        # 取消 ctrl+c 后事件循环中的任务
        # 获取任务列表
        tasks=asyncio.Task.all_tasks()
        for i in tasks:
            i.cancel()
    finally:        
        print('game over')
   
# three()
    
# 速度0.001的瞬间 按下ctrl+c 启动了近6000任务，执行完了近4000任务。
# 5946
# 5947
# 下载成功 www.baidu.com/503 返回值 None
# 下载成功 www.baidu.com/502 返回值 None
# 下载成功 www.baidu.com/501 返回值 None
# 下载成功 www.baidu.com/3902 返回值 None
# 下载成功 www.baidu.com/3906 返回值 None
# 下载成功 www.baidu.com/3904 返回值 None
# 下载成功 www.baidu.com/3905 返回值 None
# 下载成功 www.baidu.com/3903 返回值 None
# 下载成功 www.baidu.com/504 返回值 None
# 下载成功 www.baidu.com/3971 返回值 None
# 下载成功 www.baidu.com/3966 返回值 None
# 下载成功 www.baidu.com/3968 返回值 None
# 下载成功 www.baidu.com/3965 返回值 None
# 下载成功 www.baidu.com/3956 返回值 None
# 下载成功 www.baidu.com/3951 返回值 None
# 下载成功 www.baidu.com/3946 返回值 None
# 下载成功 www.baidu.com/3947 返回值 None
# 下载成功 www.baidu.com/3945 返回值 None
# 下载成功 www.baidu.com/3935 返回值 None
# game over

# 速度为0的瞬间 按下ctrl+c 启动了7000多任务，执行完了5000多任务。
# 下载成功 www.baidu.com/5311 返回值 None
# 下载成功 www.baidu.com/5305 返回值 None
# 下载成功 www.baidu.com/5307 返回值 None
# 下载成功 www.baidu.com/5308 返回值 None
# 下载成功 www.baidu.com/5303 返回值 None
# 下载成功 www.baidu.com/5300 返回值 None
# 下载成功 www.baidu.com/5296 返回值 None
# 下载成功 www.baidu.com/5325 返回值 None
# 下载成功 www.baidu.com/2019 返回值 None
# 下载成功 www.baidu.com/2018 返回值 None
# 7113
# 7114
# 7115
# 7116
# 7117
# 7118
# 7119
# game over


# 3.5 自定义async 实现 并发+回调  <协程 + 并发 普通函数 + 回调函数>
# 从自定义async 引入q
# q=async_scher.q

def three_five():
    # 协程
    async def coro_scheduler():
        page=1
        while page<11:
            await scher.sleep(1) # 每隔1秒
            # 调job
            url='{}/{}'.format('www.baidu.com',page)

            # 普通函数的并发
            # 实现并发的关键 就是在这里 新起 一个独立任务
            sf_obj=scher.call_later(random.randint(1,3),lambda:job(url))
            
            # 回调
            sf_obj.add_done_callback(url,callback=call_job_done)

            # 表示要取得结果，才能在callback中用对象的result取得结果
            sf_obj.get_result()
            
            page +=1

    # 并发 普通函数
    # 定义job 下载网页 www.baidu.com/1
    def job(url):
        # 模拟下载时间
        # scher.call_later(random.randint(1,3),lambda:job(url))
        # print('3')
        return '返回值'

    # 回调
    def call_job_done(url,task): #回调的最后一个参数是SchedulerResult object ,
        # 用 SchedulerResult object 的 result 可以取得 并发普通函数 的返回值
        print('下载成功',url,task.result) 
        
    # 启动协程
    start=time.time()
    scher.new_task(coro_scheduler())
    scher.run()
    print('[three_five]time{:.4f}s'.format(time.time()-start))

# three_five()