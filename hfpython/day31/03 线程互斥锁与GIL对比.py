from threading import Thread,Lock
import time

mutex=Lock()
count=0

def task():
    global count
    mutex.acquire()
    temp=count
    time.sleep(0.1)
    count=temp+1
    mutex.release()



if __name__ == '__main__':
    t_l=[]
    for i in range(2):
        t=Thread(target=task)
        t_l.append(t)
        t.start()
    for t in t_l:
        t.join()

    print('主',count)
