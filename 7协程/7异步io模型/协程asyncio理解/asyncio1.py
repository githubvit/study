
# 一次性学会python asyncio 
# https://www.bilibili.com/video/av85024826
# up主：小鱼儿teacher

import asyncio

#  协程不是函数
#  每隔1秒输出 hell world
async def h1():
    while True:
        print('hello world! 1s')
        await asyncio.sleep(1) # await 交出运行控制权


#  每隔2秒输出 hell world
async def h2():
    while True:
        print('hello world! 2s')
        await asyncio.sleep(2)

# 创建 事件循环
loop=asyncio.get_event_loop()        
# 利用协程创建任务 或任务列表
tasks=asyncio.gather(h1(),h2())
# 将 可等待对象(任务或futuer、协程) 注册到 事件循环，并启动
loop.run_until_complete(tasks)
