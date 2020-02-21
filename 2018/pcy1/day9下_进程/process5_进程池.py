#_*_coding:utf-8_*_
'''
进程池
进程池中定义进程和别的不同
类似线程中的信号量
'''
from  multiprocessing import Process, Pool,Lock
import time
import os

def Foo(i):
    time.sleep(2)

    print("in process",os.getpid())

    return i + 100

def Bar(*arg):
    print('-->exec done:', arg,os.getpid())
#回调函数是父进程执行的
# 比如子进程每次干完一件事，父进程就在数据库添加一条记录，用这个就很好，节约资源
# 如果在子进程干这件事，就非常耗资源，因为，每个子进程都要去连数据库。
#而用父进程干这事，就非常节约资源，只连接一次就可以。

if __name__ == '__main__':


    #定义进程池
    pool = Pool(processes=5) #允许进程池同时放入5个进程

    print"主进程",os.getpid()
    for i in range(10):

        # 定义进程
        pool.apply_async(func=Foo, args=(i,), callback=Bar) #并行并带回调callback=回调

        # pool.apply(func=Foo, args=(i,)) #进程池各个进程串行
        # pool.apply_async(func=Foo, args=(i,lock)) #并行
    print('end')
    pool.close()
    pool.join() #进程池中进程执行完毕后再关闭，一定要注意。如果注释，那么程序直接关闭。.join()
    '''
    使用进程池的bug，就是先close再join
    '''