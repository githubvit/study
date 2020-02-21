#_*_coding:utf-8_*_
'''
多进程
一个进程可以启动子进程，进程之间是独立的，内存独立、数据不共享 。

'''
# from multiprocessing import Process
# # import  multiprocessing#这样也行，就是引入太多，下面定义要加模块名前缀
# import os
#
#
# def info(title):
#     print(title)
#     print'module name:', __name__
#     # print'parent process:', os.getppid()#python2.7在windows环境中还不能支持getppid，因为os模块调用的是系统
#     #的功能，windows上没有，python3.2以上版本解决了该问题
#     print'process id:', os.getpid()
#     print"\n\n"
#
#
# def f(name):
#     info('\033[31;1mcalled from child process function f\033[0m')
#     print('hello', name)
#
# if __name__ == '__main__':
# #这句是测试代码时用的，当手动执行时，执行if后面的代码，在别的模块import该模块时，不执行if后的代码。
##因为被别的模块因入室，__name__=模块名，自然就不会执行后面的代码。
#     #在windows下上面一句不能少，否则报RuntimeError:
#     info('\033[32;1mmain process line\033[0m')
#     # 定义进程
#     p = Process(target=f, args=('bob',))
#     # 启动进程
#     p.start()
#     # 等待进程执行完毕
#     # p.join()
#     # print name #name是在子进程定义的，父进程无法获取，说明各自是独立的
'''
以下是该例正常运行的结果：
本程序的进程号是1748，子进程p的进程号是2772，pycharm的进程号是2708
说明：本程序的父进程是pycharm，子进程是p。
C:\Users\gq\Anaconda3\python.exe "C:/python_018/第10周-源码/源码/get 进程id.py"
main process line
module name: __main__
parent process: 2708
process id: 1748



called from child process function f
module name: __mp_main__
parent process: 1748
process id: 2772



hello bob

'''
# ---------------------进程启动子进程，子进程启动线程
from multiprocessing import Process, Lock
import time,threading
# 线程目标函数
def thread_run():
    print(threading._get_ident())#输出线程号
# 子进程目标函数
def run(name,l):
    # time.sleep(2)
    l.acquire()  # 获取锁
    print('hello', name)
    # 在子进程中定义线程
    t = threading.Thread(target=thread_run,)
    t.start()
    l.release()  # 释放锁

# print(__name__)
if __name__ == '__main__':
    # 定义锁
    lock = Lock()
    for i in range(10):
        #起10个子进程
        p = Process(target=run, args=('bob %s' %i,lock))
        p.start()
    #p.join()