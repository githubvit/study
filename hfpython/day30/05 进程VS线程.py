#1、瞅一瞅PID
# from threading import Thread
# import time,os
#
# def task():
#     print('%s is running' %os.getpid())
#     time.sleep(3)
#
# if __name__ == '__main__':
#     t=Thread(target=task,)
#     t.start()
#     print('主线程',os.getpid())

#2、线程创建开销小
#3、同一进程内的多个线程共享该进程内的资源
from threading import Thread
import time,os

x=1000
def task():
    global x
    x=0

if __name__ == '__main__':
    t=Thread(target=task,)
    t.start()
    t.join()
    print('主线程',x)


