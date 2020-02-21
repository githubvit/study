# 线程：是进程的执行单位，多个线程共享一个进程的数据。
# 线程的开销比进程小的多，因为不用申请内存空间。
# 线程之间都是平等的，没有父子之分。
from threading import Thread
import time,os
# 方式一
n=100
def task():
    print('id[%s]进程开启了线程'%os.getpid())
    time.sleep(1)
    global n
    n=0

if __name__ == "__main__":
    t=Thread(target=task)
    t.start()
    t.join()
    print('主',os.getpid(),n) 

#id[3652]进程开启了线程
#主 3652 0

#  方式二
# class MyThead(Thread):
#     def run(self):
#         print('id[%s]进程开启了线程'%os.getpid())
#         time.sleep(1)

# if __name__ == "__main__":
#     t=MyThead()
#     t.start()
#     print("主",os.getpid())        