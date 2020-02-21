from threading import Thread
import os,time

def task():
    print('%s is ruuning' %os.getpid())
    time.sleep(3)


if __name__ == '__main__':
    p=Thread(target=task,)
    p.start()
    print('主')


