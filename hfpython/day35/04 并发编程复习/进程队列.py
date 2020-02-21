from multiprocessing import Queue


q=Queue(3)

#队列：
#1、是内存空间
#2、自动处理锁的问题

#3、队列是先进先出，可以放任意的python数据类型
#4、队列中不应该存放很大的数据，而是一些消息级的数据

q.put('first')
q.put('sencod')
q.put('third')
# q.put('third')

print(q.get())
print(q.get())
print(q.get())

