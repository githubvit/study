'''
1、单线程下实现并发:协程
    并发指的多个任务看起来是同时运行的

    并发实现的本质：切换+保存状态


    并发、并行、串行：
    并发：看起来是同时运行，切换+保存状态
    并行：真正意义上的同时运行，只有在多cpu的情况下才能
        实现并行，4个cpu能够并行4个任务

    串行：一个人完完整整地执行完毕才运行下一个任务



'''
# import time
# def consumer():
#     '''任务1:接收数据,处理数据'''
#     while True:
#         x=yield
#
#
# def producer():
#     '''任务2:生产数据'''
#     g=consumer()
#     next(g)
#     for i in range(10000000):
#         g.send(i)
#
# start=time.time()
# #基于yield保存状态,实现两个任务直接来回切换,即并发的效果
# #PS:如果每个任务中都加上打印,那么明显地看到两个任务的打印是你一次我一次,即并发执行的.
# producer() #1.0202116966247559
#
#
# stop=time.time()
# print(stop-start)











#
# import time
# def consumer(res):
#     '''任务1:接收数据,处理数据'''
#     pass
#
# def producer():
#     '''任务2:生产数据'''
#     res=[]
#     for i in range(10000000):
#         res.append(i)
#
#     consumer(res)
#     # return res
#
# start=time.time()
# #串行执行
# res=producer()
# stop=time.time()
# print(stop-start)
















# 纯计算的任务串行执行
import time
def task1():
    res=1
    for i in range(1000000):
        res+=i

def task2():
    res=1
    for i in range(1000000):
        res*=i

start=time.time()
#基于yield保存状态,实现两个任务直接来回切换,即并发的效果
#PS:如果每个任务中都加上打印,那么明显地看到两个任务的打印是你一次我一次,即并发执行的.
task1()
task2()
stop=time.time()
print(stop-start)



# 纯计算的任务并发执行
import time
def task1():
    res=1
    for i in range(1000000):
        res+=i
        yield
        time.sleep(10000)
        print('task1')

def task2():
    g=task1()
    res=1
    for i in range(1000000):
        res*=i
        next(g)
        print('task2')

start=time.time()
#基于yield保存状态,实现两个任务直接来回切换,即并发的效果
#PS:如果每个任务中都加上打印,那么明显地看到两个任务的打印是你一次我一次,即并发执行的.
task2()
stop=time.time()
print(stop-start)












