# from multiprocessing import Process
# import time,random
#
# x=1000
#
# def task(n):
#     print('%s is runing' %n)
#     time.sleep(n)
#
# if __name__ == '__main__':
#     start_time=time.time()
#
#     p1=Process(target=task,args=(1,),name='任务1')
#     p1.start()
#
#     print(p1.pid)
#     # print(p1.name)
#     # p1.terminate()
#     # p1.join()
#     # print(p1.is_alive())
#
#     print('主')





from multiprocessing import Process
import time,random,os

x=1000

def task():
    print('self:%s parent:%s' %(os.getpid(),os.getppid()))
    time.sleep(3)

if __name__ == '__main__':
    p1=Process(target=task,)
    p1.start()


    print(p1.pid)
    print('主',os.getpid())
