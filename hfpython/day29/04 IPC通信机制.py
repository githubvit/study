#进程之间通信必须找到一种介质，该介质必须满足
#1、是所有进程共享的
#2、必须是内存空间
#附加：帮我们自动处理好锁的问题
# from multiprocessing import Process,Manager,Lock
# import time
#
# mutex=Lock()
#
# def task(dic,lock):
#     lock.acquire()
#     temp=dic['num']
#     time.sleep(0.1)
#     dic['num']=temp-1
#     lock.release()
#
# if __name__ == '__main__':
#     m=Manager()
#     dic=m.dict({'num':10})
#
#     l=[]
#     for i in range(10):
#         p=Process(target=task,args=(dic,mutex))
#         l.append(p)
#         p.start()
#
#     for p in l:
#         p.join()
#     print(dic)


from multiprocessing import Queue

# 对列：
#1、共享的空间
#2、是内存空间
#3、自动帮我们处理好锁定问题
# q=Queue(3)
# q.put('first')
# q.put({'second':None})
# q.put('三')
#
# # q.put(4) #阻塞
# print(q.get())
# print(q.get())
# print(q.get())


#强调：
#1、队列用来存成进程之间沟通的消息，数据量不应该过大
#2、maxsize的值超过的内存限制就变得毫无意义

# 了解：
q=Queue(3)
# q.put('first',block=False)
# q.put('second',block=False)
# q.put('third',block=False)
# q.put('fourth',block=False)

q.put('first',block=True)
q.put('second',block=True)
q.put('third',block=True)
# q.put('fourth',block=True,timeout=3)


# q.get(block=False)
# q.get(block=False)
# q.get(block=False)
# q.get(block=False)

# q.get(block=True)
# q.get(block=True)
# q.get(block=True)
# q.get(block=True,timeout=2)
#

