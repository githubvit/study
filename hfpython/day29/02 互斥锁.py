from multiprocessing import Process,Lock
import time,random

mutex=Lock()
# 互斥锁：
#强调：必须是lock.acquire()一次，然后 lock.release()释放一次，才能继续lock.acquire()，不能连续的lock.acquire()

# 互斥锁vs join的区别一：
# 大前提：二者的原理都是一样，都是将并发变成串行，从而保证有序
# 区别：join是按照人为指定的顺序执行，而互斥锁是所以进程平等地竞争，谁先抢到谁执行


def task1(lock):
    lock.acquire() #
    print('task1:名字是egon')
    time.sleep(random.randint(1,3))
    print('task1:性别是male')
    time.sleep(random.randint(1,3))
    print('task1:年龄是18')
    lock.release()

def task2(lock):
    lock.acquire()
    print('task2:名字是alex')
    time.sleep(random.randint(1,3))
    print('task2:性别是male')
    time.sleep(random.randint(1,3))
    print('task2:年龄是78')
    lock.release()


def task3(lock):
    lock.acquire()
    print('task3:名字是lxx')
    time.sleep(random.randint(1,3))
    print('task3:性别是female')
    time.sleep(random.randint(1,3))
    print('task3:年龄是30')
    lock.release()


if __name__ == '__main__':
    p1=Process(target=task1,args=(mutex,))
    p2=Process(target=task2,args=(mutex,))
    p3=Process(target=task3,args=(mutex,))

    # p1.start()
    # p1.join()
    # p2.start()
    # p2.join()
    # p3.start()
    # p3.join()

    p1.start()
    p2.start()
    p3.start()

