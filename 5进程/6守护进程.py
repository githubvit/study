# 守护进程：
#   当子进程执行的任务在父进程代码运行完毕后就没有存在的必要了，
#   那么该子进程就应设置为守护进程。

#  守护进程 在主进程代码最后一行运行完，即结束；
#  守护进程的结束不是主进程结束时而是主进程代码运行完时。

from multiprocessing import Process
import time

# def task(name):
#     print('%s is running'%name)
#     time.sleep(5)
#     print('%s is done'%name)

# if __name__ == "__main__":
#     p=Process(target=task,args=('egon',))
#     p.daemon=True #设为守护进程，就不会再等5秒了
#     p.start()
#     print('--->主') # 主程序执行到这里结束，守护进程也结束

def foo():
    print(123)
    time.sleep(1)
    print('end123')

def bar():
    print(456)
    time.sleep(3)
    print('end456')

if __name__ == "__main__":
    p1=Process(target=foo)
    p2=Process(target=bar)

    p1.daemon=True
    p1.start()
    p2.start()

    # time.sleep(1)
    print('main-----------')    