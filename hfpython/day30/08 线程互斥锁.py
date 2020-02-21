from threading import Thread,Lock
import time

mutex=Lock()
x=100

def task():
    global x
    mutex.acquire()
    temp=x
    time.sleep(0.1)
    x=temp-1
    mutex.release()


if __name__ == '__main__':
    start=time.time()
    t_l=[]
    for i in range(100):
        t=Thread(target=task)
        t_l.append(t)
        t.start()
    for t in t_l:
        t.join()

    print('主',x)
    print(time.time()-start)