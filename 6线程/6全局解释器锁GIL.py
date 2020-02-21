#Python GIL(Global Interpreter Lock)
# 全局解释器锁
# 上例也说明了cpython是线程不安全的，
# 在Cpython解释器中，同一个进程下开启的多线程，同一时刻只能有一个线程执行，

# GIL本质就是一把互斥锁，
# 既然是互斥锁，所有互斥锁的本质都一样，都是将并发运行变成串行，
# 以此来控制同一时间内共享数据只能被一个任务所修改，进而保证数据安全。

# 可以肯定的一点是：保护不同的数据的安全，就应该加不同的锁。
# GIL保护的是解释器级的数据，保护用户自己的数据则需要自己加锁处理。


# 1、什么是GIL
#     全局解释器锁，本质就是一把互斥锁，是加到解释器身上的，
#     每一个python进程内都有这么一把锁。

# 2、有了GIL会对单进程下的多个线程造成什么样的影响
#     多线程要想执行，首先需要争抢GIL，
#     对所有待执行的线程来说，GIL就相当于执行权限，
#     同一时刻只有一个线程争抢成功，
#     即单进程下的多个线程同一时刻只有一个在运行
#     意味着单进程下的多线程没有并行的效果，但是有并发的效果

#     ps:分散于不同进程内的线程不会去争抢同一把GIL，
#       只有同一个进程的多个线程才争抢同一把GIL

# 3、为什么要有GIL
#     Cpython解释器的内存管理机制不是线程安全

# 4、GIL与自定义互斥锁的异同，多个线程争抢GIL与自定义互斥锁的过程分析
#     相同：
#         都是互斥锁
#     不同点：
#         GIL是加到解释器上的，作用于全局
#         自定义互斥锁作用于局部
#         单进程内的所有线程都会去抢GIL
#         单进程内的只有一部分线程会去抢自定义的互斥

# 5、什么时候用python的多线程，什么时候用多进程，为什么？
#     单进程下的多个线程是无法并行，无法并行意味着不能利用多核优

#     cpu干的计算的活，多个cpu意味提升了计算性能，
#     cpu是无法做IO操作，多个cpu在IO操作面前毫无用

#     当我们的程序是IO密集型的情况下，多核对性能的提升微不足道，此时可以使用python的多线程
#     当我们的程序是计算密集型的情况下，一定要用上多核优势，此时可以使用python的多进程

# 对计算来说，cpu越多越好，但是对于I/O来说，再多的cpu也没用
    # 应用：
    #     多线程用于IO密集型，如socket，爬虫，web
    #     多进程用于计算密集型，如金融分析

# 计算密集型：多进程效率高
# from multiprocessing import Process
# from threading import Thread
# import os,time
# def work():
#     res=0
#     for i in range(100000000):
#         res*=i

# if __name__ == '__main__':
#     l=[]
#     print('本机[%d]个cpu'%os.cpu_count()) #本机为4核
#     start=time.time()
#     for i in range(4):
#         # 多进程
#         p=Process(target=work) #耗时5.8s多
#         # 多线程
#         # p=Thread(target=work) #耗时19.9s多
#         l.append(p)
#         p.start()
#     for p in l:
#         p.join()
#     stop=time.time()
#     print('run time is %s' %(stop-start))

# 计算密集型：多进程效率高
from multiprocessing import Process
from threading import Thread
import threading
import os,time
def work():
    time.sleep(2) #模拟IO
    print('===>')

if __name__ == '__main__':
    l=[]
    print(os.cpu_count()) #本机为4核
    start=time.time()
    for i in range(400):
        # 多进程
        p=Process(target=work) #耗时13.01s多,大部分时间耗费在创建进程上
        # 多线程
        # p=Thread(target=work) #耗时2.2s多
        l.append(p)
        p.start()
    for p in l:
        p.join()
    stop=time.time()
    print('run time is %s' %(stop-start))