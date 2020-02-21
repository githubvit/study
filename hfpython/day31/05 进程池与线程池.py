#进程池vs线程池

#为什么要用“池”：
# 池子使用来限制并发的任务数目，限制我们的计算机在一个自己可承受的范围内去并发地执行任务

#池子内什么时候装进程：并发的任务属于计算密集型
#池子内什么时候装线程：并发的任务属于IO密集型

# from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
# import time,os,random
#
# def task(x):
#     print('%s 接客' %os.getpid())
#     time.sleep(random.randint(2,5))
#     return x**2
#
# if __name__ == '__main__':
#     p=ProcessPoolExecutor() # 默认开启的进程数是cpu的核数
#
#     # alex，武佩奇，杨里，吴晨芋，张三
#
#     for i in range(20):
#         p.submit(task,i)

from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import time,os,random

def task(x):
    print('%s 接客' %x)
    time.sleep(random.randint(2,5))
    return x**2

if __name__ == '__main__':
    p=ThreadPoolExecutor(4) # 默认开启的线程数是cpu的核数*5

    # alex，武佩奇，杨里，吴晨芋，张三

    for i in range(20):
        p.submit(task,i)

