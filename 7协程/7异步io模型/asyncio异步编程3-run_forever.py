# loop.run_forever
# loop.run_until_complete 方法运行事件循环，当其中的全部任务完成后，自动停止事件循环；
# loop.run_ferever 方法为无限运行事件循环，需要自定义 loop.stop 方法并执行之，举例说明：

import asyncio
import functools 
# 1.将 loop.stop 方法写入 协程函数 中，终止事件循环。
def run_forever1():
    async def work(loop, t):                    # 协程函数 传递loop事件循环对象
        print('start')
        await asyncio.sleep(t)                  # 子协程，模拟 IO 操作
        print('after {}s stop'.format(t))
        loop.stop()     # 停止事件循环，stop 后仍可重新运行，close 后不可   

    loop = asyncio.get_event_loop()             # 创建事件循环
    task = asyncio.ensure_future(work(loop, 1)) # 创建任务，该任务会自动加入事件循环
    loop.run_forever()  # 无限运行事件循环，直至 loop.stop 停止
    loop.close()        # 关闭事件循环，只有 loop 处于停止状态才会执行

# run_forever1()



# 2. 使用回调函数 终止 事件循环

def call_back_loop_stop(loop,task):  # 函数的最后一个参数须为 task或future
    loop.stop()                      # 停止事件循环，stop 后仍可重新运行，close 后不可

async def work(t):
    print('start')
    await asyncio.sleep(t)      # 子协程，模拟 IO 操作
    print('after {}s stop'.format(t))

def run_forever2():
    # 创建多协程
    coros=[work(i) for i in range(1,11)]
    
    # 创建多任务
    # tasks=asyncio.ensure_future(*coros) #报错TypeError: ensure_future() takes 1 positional argument but 10 were given
    tasks=asyncio.gather(*coros)
    # 创建事件循环
    loop=asyncio.get_event_loop()

    # tasks=[asyncio.ensure_future(work(i)).add_done_callback(functools.partial(call_back_loop_stop,loop)) for i in range(1,11)] 
    # 只有1个任务运行完成。

    # 因为要所有任务都完成，再终止事件循环，
    # 所以给任务收集器绑定回调，用偏函数传递loop参数
    tasks.add_done_callback(functools.partial(call_back_loop_stop,loop))

    loop.run_forever() # 无限运行事件循环，直至 loop.stop 停止
    loop.close()        # 关闭事件循环，只有 loop 处于停止状态才会执行

run_forever2()