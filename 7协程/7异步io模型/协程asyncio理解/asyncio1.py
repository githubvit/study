
# 一次性学会python asyncio 
# https://www.bilibili.com/video/av85024826
# up主：小鱼儿teacher

# 基于 原生async框架 用 协程 实现 并发
import asyncio,time

def one():

    #  协程不是函数
    #  每隔1秒输出 hell world！1
    async def h1(count):
        n=0
        while n<count:
            print('hello world! 1')
            n+=1
            await asyncio.sleep(1) # await 交出运行控制权


    #  每隔1秒输出 hell world！2
    async def h2(n):
        while n>0:
            print('hello world! 2')
            n-=1
            await asyncio.sleep(1)

    start=time.time()
    # 创建 事件循环
    loop=asyncio.get_event_loop()        
    # 利用协程创建任务 或任务列表
    tasks=asyncio.gather(h1(5),h2(5))
    # 将 可等待对象(任务或futuer、协程) 注册到 事件循环，并启动
    loop.run_until_complete(tasks)
    print('[one]time:{:.4f}s'.format(time.time()-start))

# one()

# 结果
    # hello world! 1
    # hello world! 2
    # hello world! 1
    # hello world! 2
    # hello world! 1
    # hello world! 2
    # hello world! 1
    # hello world! 2
    # hello world! 1
    # hello world! 2
    # [one]time:5.0114s


# 基于 自己构建的 async 的底层框架 用协程 实现 上例

import async_scher
scher=async_scher.scher

def two():
    
    async def h1(count):
        n=0
        while n<count:
            print('hello world! 1')
            n+=1
            await scher.sleep(1) 

    async def h2(n):
        while n>0:
            print('hello world! 2')
            n-=1
            await scher.sleep(1)

    start=time.time()

    scher.new_task(h1(5))
    scher.new_task(h2(5))
    scher.run()

    print('[two]time:{:.4f}s'.format(time.time()-start))

two()

# 结果
    # hello world! 1
    # hello world! 2
    # hello world! 1
    # hello world! 2
    # hello world! 1
    # hello world! 2
    # hello world! 1
    # hello world! 2
    # hello world! 1
    # hello world! 2
    # [two]time:5.0055s