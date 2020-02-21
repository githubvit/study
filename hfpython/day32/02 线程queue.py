import queue

# q=queue.Queue(3) #队列：先进先出
# q.put(1)
# q.put(2)
# q.put(3)
# # q.put(4)
#
# print(q.get())
# print(q.get())
# print(q.get())


# q=queue.LifoQueue(3) #堆栈：后进先出
#
# q.put('a')
# q.put('b')
# q.put('c')
#
# print(q.get())
# print(q.get())
# print(q.get())


q=queue.PriorityQueue(3) #优先级队列:可以以小元组的形式往队列里存值，第一个元素代表优先级，数字越小优先级越高
q.put((10,'user1'))
q.put((-3,'user2'))
q.put((-2,'user3'))


print(q.get())
print(q.get())
print(q.get())


