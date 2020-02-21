import json
import time
import random
import os
from multiprocessing import Process,Lock

mutex=Lock()
# 互斥锁vs join的区别一：
# 互斥锁可以让一部分代码（修改共享数据的代码）串行，而join只能将代码整体串行


def search():
    time.sleep(random.randint(1,3))
    with open('db.json','r',encoding='utf-8') as f:
        dic=json.load(f)
        print('%s 剩余票数:%s' %(os.getpid(),dic['count']))

def get():
    with open('db.json','r',encoding='utf-8') as f:
        dic=json.load(f)
    if dic['count'] > 0:
        dic['count']-=1
        time.sleep(random.randint(1,3))
        with open('db.json','w',encoding='utf-8') as f:
            json.dump(dic,f)
        print('%s 购票成功' %os.getpid())

def task(lock):
    search()
    lock.acquire()
    get()
    lock.release()

if __name__ == '__main__':
    for i in range(10):
        p=Process(target=task,args=(mutex,))
        p.start()
        # p.join()


