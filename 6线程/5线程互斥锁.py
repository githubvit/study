# cpython是线程不安全的，怎么讲？
# 看下面的例子

# from threading import Thread
# import time

# # 定义全局变量n
# n=100
# def task():
#     global n
#     # 拿到n
#     temp=n
#     time.sleep(0.1) #模拟中间操作花费的时间
#     # 修改n
#     n=temp-1

# if __name__ == "__main__":
#     start_time=time.time()
#     # 启动100个线程
#     t_l=[]
#     for i in range(100):
#         t=Thread(target=task)
#         t_l.append(t)
#         t.start()

#     # 保证所有的线程执行完
#     for t in t_l:
#         t.join()

#     stop_time=time.time()

#     print('主',n,stop_time-start_time)
        
    # 主 99 0.11620426177978516

# 上例显示了 线程的不安全：
# 数据n被所有线程同时拿到，同时修改，说明一个进程中的线程对数据来说是不安全的。
# 为了数据安全，必须加锁，加锁可以变并行为串行，保证同一时刻，只能有一个线程访问该数据。

from threading import Thread,Lock
import time

# 定义全局变量n
n=100
def task():
    global n
    # 加锁
    # n_mutex.acquire()
    # # 拿到n
    # temp=n
    # time.sleep(0.1) #模拟中间操作花费的时间
    # # 修改n
    # n=temp-1
    # # 释放锁
    # n_mutex.release()

    # 用with就可以自动上锁和解锁，与上面的代码是一样的。
    with n_mutex:
        # 拿到n
        temp=n
        time.sleep(0.01) #模拟中间操作花费的时间，降低10倍
        # 修改n
        n=temp-1

if __name__ == "__main__":
    start_time=time.time()
    # 定义锁
    n_mutex=Lock()
    # 启动100个线程
    t_l=[]
    for i in range(100):
        t=Thread(target=task)
        t_l.append(t)
        t.start()

    # 保证所有的线程执行完
    for t in t_l:
        t.join()

    stop_time=time.time()

    print('主',n,stop_time-start_time)

    # 主 0 10.077508449554443
    # 主 0 1.0985488891601562