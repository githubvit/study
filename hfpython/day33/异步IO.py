from concurrent.futures import ThreadPoolExecutor
from threading import current_thread
import time
import os

def task(n):
    print('%s is running' %current_thread().name)
    time.sleep(2)
    return n**2

def parse(obj):
    res=obj.result()
    print(res)

if __name__ == '__main__':
    t=ThreadPoolExecutor(4)

    future1=t.submit(task,1)
    future1.add_done_callback(parse) #parse函数会在future1对应的任务执行完毕后自动执行，会把future1自动传给parse

    future2=t.submit(task,2)
    future2.add_done_callback(parse)

    future3=t.submit(task,3)
    future3.add_done_callback(parse)

    future4=t.submit(task,4)
    future4.add_done_callback(parse)