# 协程按ctrl+c的终止 
# 1.捕捉 Ctrl + C 触发的 KeyboardInterrupt 异常
# 2.取得事件循环的全部任务 tasks = asyncio.Task.all_tasks()
# 3.循环任务列表。用任务的 task.cancel() 方法 从内存中删除 pending的任务 


import asyncio,time

async def work(id,t):
    print('working {} ...'.format(id))
    await asyncio.sleep(t)
    print('work {} done'.format(id))

def main():
    start=time.time()
    # 创建协程列表
    coros=[work(i,i) for i in range(1,5)] #列表生成式

    # 收集协程 列表参数要加*
    gather=asyncio.gather(*coros)

    # 创建事件循环
    loop=asyncio.get_event_loop()

    # 将收集到的协程注册到事件循环，并启动事件循环
    try: # 程序运行过程中，快捷键 Ctrl + C 会触发 KeyboardInterrupt 异常
        loop.run_until_complete(gather)
    except KeyboardInterrupt: 
        # pass
        # 每个线程里只能有一个事件循环
        # 此方法可以获得事件循环中的所有任务的集合
        # 任务的状态有 PENDING 和 FINISHED 两种
        tasks = asyncio.Task.all_tasks()
        # print(tasks)
        for i in tasks:
            # 可以看到pending的任务还在内存中，wait_for=<Future pending cb=[<TaskWakeupMethWrapper object at 0x0000022D87922768>()]>
            print('任务{}'.format(i))

            # 任务的 cancel 方法可以 取消 未完成 的任务，从内存中取消pending任务
            # 取消成功返回 True ，已完成的任务取消失败返回 False
            print('取消状态：{}'.format(i.cancel()))
        
    finally:
        tasks = asyncio.Task.all_tasks()
        for i in tasks:
            print('取消状态后的task:{}'.format(i))# pending的任务已取消 wait_for=<Future cancelled> 已无内存地址 
        # loop.close()
        
    print('main {:.4f} s'.format(time.time()-start)) 

if __name__ == "__main__":
    main()

# 任务<Task pending coro=<work() running at d:/pyj/st/7协程/7异步io模型/asyncio异步编程2-cancel.py:7> 
# wait_for=<Future pending cb=[<TaskWakeupMethWrapper object at 0x0000022D87922768>()]> 
# cb=[gather.<locals>._done_callback() at d:\Anaconda3\lib\asyncio\tasks.py:691]>
# 取消状态：True
# 任务<Task finished coro=<work() done, defined at d:/pyj/st/7协程/7异步io模型/asyncio异步编程2-cancel.py:5> 
# result=None>
# 取消状态：False
# 任务<Task finished coro=<work() done, defined at d:/pyj/st/7协程/7异步io模型/asyncio异步编程2-cancel.py:5>
# result=None>
# 取消状态：False
# 任务<Task pending coro=<work() running at d:/pyj/st/7协程/7异步io模型/asyncio异步编程2-cancel.py:7> 
# wait_for=<Future pending cb=[<TaskWakeupMethWrapper object at 0x0000022D87922828>()]> 
# cb=[gather.<locals>._done_callback() at d:\Anaconda3\lib\asyncio\tasks.py:691]>
# 取消状态：True
# 取消状态后的task:<Task pending coro=<work() running at d:/pyj/st/7协程/7异步io模型/asyncio异步编程2-cancel.py:7> 
# wait_for=<Future cancelled> 
# cb=[gather.<locals>._done_callback() at d:\Anaconda3\lib\asyncio\tasks.py:691]>
# 取消状态后的task:<Task finished coro=<work() done, defined at d:/pyj/st/7协程/7异步io模型/asyncio异步编程2-cancel.py:5> result=None>     
# 取消状态后的task:<Task finished coro=<work() done, defined at d:/pyj/st/7协程/7异步io模型/asyncio异步编程2-cancel.py:5> result=None>     
# 取消状态后的task:<Task pending coro=<work() running at d:/pyj/st/7协程/7异步io模型/asyncio异步编程2-cancel.py:7> 
# wait_for=<Future cancelled> 
# cb=[gather.<locals>._done_callback() at d:\Anaconda3\lib\asyncio\tasks.py:691]>
# main 3.0431 s




