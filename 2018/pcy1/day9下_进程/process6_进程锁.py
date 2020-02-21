#_*_coding:utf-8_*_
'''
进程锁
进程锁不同于线程锁，进程之间本身是对立的，不会像线程对同一块数据产生误操作，
进程锁的主要用途在于标准输出如屏幕，不会打架
'''
from multiprocessing import Process, Lock


def f(l, i):
    l.acquire()#获取锁
    print('hello world', i)
    l.release()#释放锁


if __name__ == '__main__':
    # 定义锁
    lock = Lock()

    for num in range(50):
        Process(target=f, args=(lock, num)).start()#传递锁