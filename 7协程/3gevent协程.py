# 单线程下实现遇到IO切换

from gevent import monkey; monkey.patch_all() # 给所有IO加标记
from threading import current_thread
import gevent,time

def eat():
    print('%s eat 1'%current_thread().getName())
    time.sleep(2)
    print('%s eat 2'%current_thread().getName())

def play():
    print('%s play 1'%current_thread().getName())
    time.sleep(5)
    print('%s play 2'%current_thread().getName())

g1=gevent.spawn(eat)
g2=gevent.spawn(play)

# gevent.sleep(100)
# g1.join()
# g2.join()
print(current_thread().getName())
gevent.joinall([g1,g2])

# MainThread
# DummyThread-1 eat 1
# DummyThread-2 play 1
# DummyThread-1 eat 2
# DummyThread-2 play 2

# 线程名 Dummy：假的
# 所以 真正只有一个线程MainThread，
# 其他的线程名只是标记程序monkey.patch_all()为了区分不同的任务而起的，其实都是一个线程MainThread。