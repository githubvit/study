from multiprocessing import Process
import time,random,os

def task(n):
    print('%s is runing' %n)
    time.sleep(n)
#
if __name__ == '__main__':
    start_time=time.time()
#
    p1=Process(target=task,args=(1,),name='任务1')
    p1.start()
#
    print(p1.pid)#p1子进程的id
    print(p1.name)
    # p1.terminate() #直接终止子程序 很少用 下面的p1.is_alive()会报True,
    # 因为这里只是向操作系统发了个信号，操作系统还没来得及结束p1

    # p1.join() #父进程等待子进程执行完 下面的p1.is_alive()会报False，
    # 因为join会卡住父进程。等子进程p1执行完，再执行下面的代码。
    print(p1.is_alive()) #p1进程是否是存在
#
    print('主')








# def task():
#     print('self:%s parent:%s' %(os.getpid(),os.getppid()))#pid本进程id和ppid父进程id
#     time.sleep(3)

# if __name__ == '__main__':
#     p1=Process(target=task,)
#     p1.start()

#     print(p1.pid)
#     print('主',os.getpid())