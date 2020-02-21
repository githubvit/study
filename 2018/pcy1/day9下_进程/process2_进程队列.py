#_*_coding:utf-8_*_
'''
多进程之间数据传递方式1-采用进程队列
一个进程可以启动子进程，进程之间是独立的，内存独立、数据不共享 。
进程也有队列，进程队列外表看起来和线程队列很像，但实际不同，线程队列数据可以共享，进程之间的队列，采用pickle序列化，数据是克隆的。
应用于父子进程，或者同属于同一父进程的子进程进行交互。不相干的进程之间无法应用该队列进行通信。
'''
from multiprocessing import Process, Queue #进程中的队列在这里
import threading
# import Queue#这是线程的队列



def f(qq):
    print("in child:",qq.qsize())
    qq.put([42, None, 'hello'])#在子进程中put

if __name__ == '__main__':
    q = Queue()#进程队列定义写法
    # q=Queue.Queue()#线程队列的写法
    q.put("test123")
    # p = threading.Thread(target=f,)
    # 定义一个子进程p，在该进程中put
    p = Process(target=f, args=(q,))
    #如果采用线程队列的写法和模块，
    # 会产生TypeError: can't pickle thread.lock objects
    # 是因为进程之间彼此是独立的
    # 而进程队列使用了pickle序列化，克隆了进程传过来的数据。
    p.start()
    p.join()
    # 在父进程中get，看起来和线程一致，使用方法也一致，但实际上是克隆了子进程的数据。
    print("444",q.get_nowait())
    print("444",q.get_nowait())
     # prints "[42, None, 'hello']"
    #print(q.get())  # prints "[42, None, 'hello']"