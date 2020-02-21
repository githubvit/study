#_*_coding:utf-8_*_
'''
线程thread，
主线程就是程序
'''

import threading,time
#一， 用类的方法定义线程
# class MyThread(threading.Thread):
#     def __init__(self,name):
#         super(MyThread,self).__init__()
#         self.name=name
#     def run(self):#这个函数名必须是run
#         print 'thread [%s] is runing'%self.name
#         time.sleep(0.25)
# t1=MyThread('t1')
# t2=MyThread('t2')
# t1.start()
# # t1.join()
# t2.start()
#-------------------------
'''
二，保证《print'线程都已完成了'》在子线程都结束后，输出
'''
# 方式1 线程列表-join
# thread_list=[]#做一个线程列表
# def run(name):
#     print 'thread [%s] is runing'%name
#     time.sleep(0.25)
#     print '--thread [%s] is stop'%name
#
# for i in range(10):#启动多个线程
#     t=threading.Thread(target=run,args=(('t%s'%i,)))
#     t.start()
#     thread_list.append(t)#每启动一个线程，就加入线程列表
# for j in thread_list:#从线程列表中取出每个线程，让每个线程等待结束，这样就保证了print在最后
#     j.join()
# print '线程都已完成了',threading.current_thread()#通过current_thread()看出当前程序就是MainThread主线程


# 方式2 while-active_count()

# def run(name):
#     print 'thread [%s] is runing\n'%name
#     time.sleep(0.0000025)
#     print '--thread [%s] is stop\n'%name
#
# for i in range(10):#启动多个线程
#     t=threading.Thread(target=run,args=(('t%s'%i,)))
#     t.start()

# while threading.active_count()>1:#只要还有2个以上激活的线程就循环
#     print 'activ_count num:%s\n' %  threading.active_count()

# print '线程都已完成了',threading.current_thread()

# 三，守护线程
def run(name):
    print 'thread [%s] is runing\n'%name
    time.sleep(1)
    print '--thread [%s] is stop\n'%name

for i in range(10):#启动多个线程
    t=threading.Thread(target=run,args=(('t%s'%i,)))
    t.setDaemon(True)#设定子线程都为守护线程，一定要在statr之前设定
    t.start()


print '线程都已完成了',threading.current_thread()#主线程不会等守护线程结束，主线程运行完毕就退出了程序。
# 比如socketserver，server端就是主线程，连接的实例就是守护线程。server端一结束，就直接退出了程序。