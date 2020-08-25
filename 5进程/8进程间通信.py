# 上节抢票案例中用文件实现了进程间通信，
#  由于要从硬盘读出，并且为了数据安全，还要考虑加锁、释放锁等。
#  这就即慢又繁琐,尽量避免使用。

#  标准的进程间通信(IPC)不是用文件，而是用队列.
#  队列=管道+锁，在内存空间，并且已经处理好了锁的问题。

from multiprocessing import Queue

q=Queue(3) #生成队列对象，设置成 最多为3个元素。

q.put('fist') 
q.put({'a':2})
q.put(3)
# q.put('fourth') # 程序卡住 被阻塞 因为block默认为True，无法结束程序。
# q.put('fourth',block=False) #=q.put_nowait() 不阻塞block=False，立即抛异常 queue.Full 结束。
# q.put('fourth',timeout=3)  # 最大超时3秒，3秒后抛异常，结束程序。


print(q.get())
print(q.get())
print(q.get())
# print(q.get()) # 程序卡住 被阻塞 因为block默认为True，无法结束程序。
# print(q.get(block=False)) #=q.get_nowait,不阻塞block=False，立即抛异常 _queue.Empty 结束。
print(q.get(timeout=3)) # 最大超时3秒，3秒后抛异常，结束程序。