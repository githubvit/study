from gevent import monkey,spawn;monkey.patch_all()
import time

def f1():
    print('from f1 1')
    time.sleep(3)
    print('from f1 2')

def f2():
    print('from f2 1')
    time.sleep(2)
    print('from f2 2')

def f3():
    print('from f3 1')
    time.sleep(5)
    print('from f3 2')


g1=spawn(f1)
g2=spawn(f2)
g3=spawn(f3)

# time.sleep(10)
g1.join()
g2.join()
g3.join()