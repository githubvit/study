#1\ 计算密集型应该使用多进程
# from multiprocessing import Process
# from threading import Thread
#
# import time
# # import os
# # print(os.cpu_count())
#
# def task1():
#     res=0
#     for i in range(1,100000000):
#         res+=i
#
# def task2():
#     res=0
#     for i in range(1,100000000):
#         res+=i
#
# def task3():
#     res=0
#     for i in range(1,100000000):
#         res+=i
#
# def task4():
#     res=0
#     for i in range(1,100000000):
#         res+=i
#
# if __name__ == '__main__':
#     # p1=Process(target=task1)
#     # p2=Process(target=task2)
#     # p3=Process(target=task3)
#     # p4=Process(target=task4)
#
#     p1=Thread(target=task1)
#     p2=Thread(target=task2)
#     p3=Thread(target=task3)
#     p4=Thread(target=task4)
#     start_time=time.time()
#     p1.start()
#     p2.start()
#     p3.start()
#     p4.start()
#     p1.join()
#     p2.join()
#     p3.join()
#     p4.join()
#     stop_time=time.time()
#     print(stop_time - start_time)



#2\ IO密集型应该使用多线程
from multiprocessing import Process
from threading import Thread

import time


def task1():
    time.sleep(3)

def task2():
    time.sleep(3)

def task3():
    time.sleep(3)

def task4():
    time.sleep(3)

if __name__ == '__main__':
    # p1=Process(target=task1)
    # p2=Process(target=task2)
    # p3=Process(target=task3)
    # p4=Process(target=task4)

    # p1=Thread(target=task1)
    # p2=Thread(target=task2)
    # p3=Thread(target=task3)
    # p4=Thread(target=task4)
    # start_time=time.time()
    # p1.start()
    # p2.start()
    # p3.start()
    # p4.start()
    # p1.join()
    # p2.join()
    # p3.join()
    # p4.join()
    # stop_time=time.time()
    # print(stop_time - start_time) #3.138049364089966

    p_l=[]
    start_time=time.time()

    for i in range(500):
        p=Thread(target=task1)
        p_l.append(p)
        p.start()

    for p in p_l:
        p.join()

    print(time.time() - start_time)