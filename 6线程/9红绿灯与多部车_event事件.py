# 1个进程下的多个线程协同工作，多个线程依赖某个线程的情况。
# 即 其他线程需要通过判断某个线程的状态来确定自己下一步的操作。
# 就把某个线程比作红绿灯，其他的多个线程比作车。

# event.isSet()：返回event的状态值 = True/False；
# event.wait()：如果 event.isSet()==False将阻塞线程；
# event.set()： 设置event的状态值为True，所有阻塞池的线程激活进入就绪状态， 等待操作系统调度；
# event.clear()：恢复event的状态值为False。



# 红绿灯案例

# from threading import Thread,Event,current_thread
# import time,random


# # 设置事件

# event=Event()

# # 红绿灯
# def trafficLights():
#     print('event的状态',event.is_set())#event的默认状态是False，即红灯
#     print('灯[%s] 红灯'%current_thread().getName())
#     time.sleep(3)
#     # 设置为绿灯 即True 和 车中的wait()方法搭配使用
#     event.set()
#     print('灯[%s] 绿灯'%current_thread().getName())
    
    

# # 车
# def car():
#     print('车[%s] 等红灯'%current_thread().getName())
#     event.wait()
#     print('车[%s] 通过该路口'%current_thread().getName())

# if __name__ == "__main__":
#     t1=Thread(target=trafficLights) # 灯

#     t2=Thread(target=car) # 车
#     t3=Thread(target=car) # 车
#     t4=Thread(target=car) # 车
    
#     t1.start()
#     t2.start()
#     t3.start()
#     t4.start()


# 链接MySQL案例

# 例如，有多个工作线程尝试链接MySQL，
# 用一个线程 检查 MySQL服务是否正常，
# 其余多个 链接 线程等检查线程 检查服务正常后， 才去链接。
# 那么我们就可以采用threading.Event 机制来协调各个工作线程的连接操作。

# from threading import Thread,Event,current_thread
# import time,random

# # 设置事件
# event=Event()

# def check():
#     print('%s checking MySQL...'%current_thread().getName())
#     time.sleep(5)
#     # 改变状态 为 True
#     print('%s is ok!'%current_thread().getName())
#     event.set()

# def connt():
#     # 如果事件的状态为False时，就去尝试连接。。。
#     count=0
#     while not event.is_set():
#         if count==3: # 如果3次没有连上 则 结束该线程（通过激发错误） 
#             raise TimeoutError('超时')#结束该线程 不是结束程序
#         print('%s try to connect MySQL...[%s]time'%(current_thread().getName(),count))
        
#         # 阻塞1-3秒 （如果wait中没有数字，就会一直等event.set()）
#         # 由于上面sleep是5秒，
#         # 如果某线程随机时间平均值>5/3大约1.67，则该线程可以连上
#         event.wait(random.randint(1,3))
#         count+=1
#     print('%s connected MySQL.'%current_thread().getName())

# if __name__ == "__main__":
#     t1=Thread(target=check)#检查

#     t2=Thread(target=connt)
#     t3=Thread(target=connt)
#     t4=Thread(target=connt)

#     t1.start()
#     t2.start()
#     t3.start()
#     t4.start()
