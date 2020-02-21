'''
1 GIL:全局解释器锁
    GIL本质就是一把互斥锁，是夹在解释器身上的，
    同一个进程内的所有线程都需要先抢到GIL锁，才能执行解释器代码

2、GIL的优缺点：
    优点：
        保证Cpython解释器内存管理的线程安全

    缺点：
        同一进程内所有的线程同一时刻只能有一个执行，
        也就说Cpython解释器的多线程无法实现并行


'''


from threading import Thread,current_thread
import time

def task():
    print('%s is running' %current_thread().name)
    time.sleep(3)
    print('%s is done' %current_thread().name)


if __name__ == '__main__':
    t1=Thread(target=task)
    t2=Thread(target=task)
    t3=Thread(target=task)
    t1.start()
    t2.start()
    t3.start()
