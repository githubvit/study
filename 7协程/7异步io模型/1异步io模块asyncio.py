# 单线程异步io 
# 异步调用+回调机制：
# 把任务往系统一提交，就继续执行下面的代码，系统干完了任务就把结果放到该任务的内存中。
# 全程不管，任务的结果自动拿到。
# 因此是效率最高的io模型。

# asyncio模块是用c语言开发的，python可以直接导入使用即可


# 1. 定义协程 关键字 async
# 协程函数: 定义形式为 async def 的函数;
# 协程对象: 调用 协程函数 所返回的对象。

# 1.1 可等待对象：
# 可等待对象：可以拿走执行权限+保存状态，也可以加入执行权限+恢复状态。
# 可等待对象对象可以在 await 语句中使用。
# 可等待 对象有三种主要类型: 协程, 任务 和 Future.

# 1.1.1  协程
# Python 协程属于 可等待 对象，因此可以在其他协程中被等待

import asyncio

# 定义协程函数
# async def nested():
    # return 42

# async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    # nested()
    # nested是一个协程函数 不是普通函数，不能用普通函数的执行方法执行
    # 会得到警告 RuntimeWarning:

    # Let's do it differently now and await it:
    # print(await nested())  # will print "42".
    # 协程属于 可等待 对象，因此可以在其他协程中被等待await
    # main协程中等待nested协程执行完成

# 执行协程 asyncio.run()
# asyncio.run(main())

# 结果
# d:/pyj/st/7协程/7异步io模型/1异步io模块asyncio.py:31: RuntimeWarning: coroutine 'nested' was never awaited
#   nested()
# RuntimeWarning: Enable tracemalloc to get the object allocation traceback
# 42

# 1.1.2  任务
# 任务 被用来设置日程以便 并发 执行协程。
# 当一个协程通过 asyncio.create_task() 等函数被打包为一个 任务，
# 该协程将自动排入日程准备立即运行:

# import asyncio

# async def nested():
#     return 42

# async def main():
#     # Schedule nested() to run soon concurrently
#     # with "main()".
#     task = asyncio.create_task(nested())

#     # "task" can now be used to cancel "nested()", or
#     # can simply be awaited to wait until it is complete:
#     await task

# asyncio.run(main())

#  1.1.3 Future 对象
# Future 是一种特殊的 低层级 可等待对象，表示一个异步操作的 最终结果。
# 当一个 Future 对象 被等待，这意味着协程将保持等待直到该 Future 对象在其他地方操作完毕。

async def main():
    await function_that_returns_a_future_object()

    # this is also valid:
    await asyncio.gather(
        function_that_returns_a_future_object(),
        some_python_coroutine()
    )



# 2. 模拟阻塞 await asyncio.sleep()
#  我们说的协程任务都是在单线程内的多协程，
#  所以，模拟任务的阻塞用time.sleep()，是不行的，因为那样会阻断该线程。
#  等于卡住了该线程内的所有协程任务。
#  asyncio模块提供了sleep来模拟协程的阻塞。asyncio.sleep()
#  另外 按照协程异步的规定，要在所有阻塞前，加入关键字await标记。
#  因此，要让阻塞模拟成功 就是 await asyncio.sleep()

# async def main():
#     print('Hello ...')
#     # 模拟阻塞
#     await asyncio.sleep(1)
#     print('... World!')

# # 协程的运行
# # Python 3.7+
# asyncio.run(main())

# 结果
# Hello ...
# ... World!

# 特殊的阻塞: 不阻塞 协程切换 await asyncio.sleep(0)




