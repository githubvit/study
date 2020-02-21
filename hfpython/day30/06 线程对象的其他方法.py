from threading import Thread,current_thread,active_count,enumerate
import time,os

def task():
    print('%s is running' %current_thread().name)
    time.sleep(3)

if __name__ == '__main__':
    t1=Thread(target=task,name='第一个线程')
    t2=Thread(target=task,)
    t3=Thread(target=task,)
    t1.start()
    t2.start()
    t3.start()

    # print(t1.is_alive())
    print(active_count())
    print(enumerate())
    print('主线程',current_thread().name)


