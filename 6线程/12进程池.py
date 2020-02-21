# 操作系统的设计，因此可以归结为三点：

# （1）以多进程形式，允许多个任务同时运行；
# 
# （2）以多线程形式，允许单个任务分成不同的部分运行；
# 
# （3）提供协调机制，一方面防止进程之间和线程之间产生冲突，
# 另一方面允许进程之间和线程之间共享资源。


# 进程池

# 当实际进程数大于机器能承受的进程数时，使用进程池限制进程的数量
# 对计算来说，cpu越多越好，但是对于I/O来说，再多的cpu也没用
    # 应用：
    #     多线程用于IO密集型，如socket，爬虫，web
    #     多进程用于计算密集型，如金融分析 

# 进程或线程提交任务的两种方式：

# 1 同步调用：现在几乎不用了
#   提交任务后，就在原地等待任务执行完毕，
#   拿到任务的返回值，才继续下一行代码。 
#   导致任务串行执行。

# 2 异步调用+回调机制：实际使用的都是这种调用方式
#   提交任务后，不在原地等待，
#   任务一旦执行完毕就会触发 回调函数 的执行。 
#   任务是并发执行的。

#  何谓阻塞、非阻塞
#  进/线程的有三种执行状态：阻塞、就绪、运行
#  阻塞：是碰到io（读写）了，cpu把执行权限拿走了，进/线程就在原地等着了。
#  非阻塞：就绪或运行状态


# # 一 同步调用示例 
# from concurrent.futures import ProcessPoolExecutor
# import time,random,os
# # 1 数据生产者
# def task(n):
#     print('%s is running...'%os.getpid())
#     time.sleep(random.randint(1,3))
#     return n**2

# # 2 数据消费者
# def handle(res):
#     print('handle res %s'%res)

# if __name__ == "__main__":
#     # 设置进程池 规定进程数量 --干活的人数
#     pool=ProcessPoolExecutor(2)

#     # 起进程 设置任务数量 --客人数量
#     for i in range(5):

#         # 用进程池起进程 (任务，参数) 

#         # 同步示例 提交任务 等待结果 导致任务串行
#         res=pool.submit(task,i).result()
#         # print(res)
#         handle(res)

#     # 进程池的shutdown方法有两个作用 ：
#     # 1 等待 等待在 shutdown 之前的任务都完成，再执行后面的代码。
#     # 2 关门  shutdown之后不能再往进程池放任务。
#     pool.shutdown(wait=True) 

#     # pool.submit(task,333)#已关门，再放任务会报错

#     print('主')
   

# 二 异步调用+回调机制 示例 
from concurrent.futures import ProcessPoolExecutor
import time,random,os
# 1 数据生产者
def task(n):
    print('%s is running...task-%s'%(os.getpid(),n))
    time.sleep(random.randint(1,3))
    return n**2

# 2 数据消费者
def handle(obj):
    # 这里是用进程池回调函数add_done_callback获取的执行机会
    # 进程池回调函数会获取到数据生产者进程任务的对象obj
    # 进程池对象obj有个result()方法可以获取对象的结果。
    res=obj.result()
    print('handle res %s'%res)

if __name__ == "__main__":
    # 设置进程池 规定进程数量 --干活的人数 不填默认=cpu的数量。
    pool=ProcessPoolExecutor(2)

    # 起进程 设置任务数量 --客人数量
    for i in range(5):

        # 用进程池起进程 pool.submit(任务，任务的参数) 

        # 异步+回调示例 提交数据生产者任务 用回调函数add_done_callback处理数据消费者，

        # 进程池回调函数会获取到提交任务数据生产者进程任务的对象obj，
        # obj会作为参数传给回调函数
        pool.submit(task,i).add_done_callback(handle)
        # 上面这种进程池的提交任务和回调函数方式,
        #  就解耦了数据生产者和数据消费者.
        #  在两者之间建立了管道,
        #  生产者生产了对象obj放到管道里,
        #  消费者从管道里取出对象obj，获得结果obj.result()，进行消费.

        # 实际上 上面就是下面的合成
        # obj=pool.submit(task,i) #拿到对象
        # obj.add_done_callback(handle) #对象回调
        

    # 进程池的shutdown方法有两个作用 ：
    # 1 等待 等待在 shutdown 之前的任务都完成，再执行后面的代码。
    # 2 关门  shutdown之后不能再往进程池放任务。
    pool.shutdown(wait=True) 

    # pool.submit(task,333)#已关门，再放任务会报错

    print('主')

# 结果
# 6632 is running...task-0
# 7892 is running...task-1
# handle res 0
# 6632 is running...task-2
# 7892 is running...task-3
# handle res 1
# 7892 is running...task-4
# handle res 9
# handle res 4
# handle res 16

# 分析 ：
# 1 解决了io的问题，在生产者sleep时，即IO时，cpu会调消费者处理。
# 2 即submit碰到io时，调用回调add_done_callback执行。
# 3 这样就提高了执行效率。