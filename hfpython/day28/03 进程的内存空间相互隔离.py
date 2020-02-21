from multiprocessing import Process
import time

x=1000

def task():
    time.sleep(3)
    global x
    x=0
    print('儿子死啦',x)


if __name__ == '__main__':
    print(x)
    p=Process(target=task)
    p.start()
    time.sleep(5)
    print(x)









