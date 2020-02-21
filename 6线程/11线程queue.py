from threading import Thread
import queue,time

# 不像进程，线程都可以直接读取进程中的数据了，为什么线程要用线程队列queue？

# 因为cpython是线程不安全的，为了数据安全，操作数据要加锁。
# 因此用线程队列queue就不用考虑加锁的问题了。

# 现在用的进程和线程队列都是跑在一台机器上，安全性、效率、可用性都非常低。
# 以后软件要做成分布式的，就不会只在一台机器上了运行了，
# 为了协调各个机器上的模块，
# 要用的队列都是基于云上的，
# 比如RabbitMQ消息队列，来一台机器专门运行该消息队列，
# 所有的机器都通过该消息队列协调，单台机器挂掉不影响总的运行。
# 如果专门运行消息队列的机器坏了，确实就over了，为此，一般，队列的运行都使用集群。

# 队列：先进先出 与进程队列完全一样
# q=queue.Queue(3)

# 堆栈：后进先出 last in first out 
# q=queue.LifoQueue(3)

# q.put(1)
# q.put(2)
# q.put(3)
# # q.put_nowait(4)

# 优先级队列 数值越小 越优先
q=queue.PriorityQueue(3)
q.put((10,'a'))
q.put((-3,'b'))
q.put((100,'c'))

print(q.get())
print(q.get())
print(q.get())

# (-3, 'b')
# (10, 'a')
# (100, 'c')
