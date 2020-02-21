from multiprocessing import Process
import time,os

def task(n):
    print('%s is running' %n)
    time.sleep(n)



if __name__ == '__main__':
    p1=Process(target=task,args=(1,))
    p2=Process(target=task,args=(2,))
    p3=Process(target=task,args=(3,))
    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print('======主',os.getpid())

    time.sleep(10000)














