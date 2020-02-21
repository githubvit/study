# 生产者和消费者都是独立的进程
# 两者不直接接触，通过队列联系，就是通过队列解耦：
#   生产者将生产的结果放入队列，继续生产
#   消费者从队列中取出生产者的结果，进行消费


# 方式一
# from multiprocessing import Process,Queue
# import time,random

# def producer(name,food,q):
#     for i in range(10):
#         res='%s%s'%(food,i)
#         time.sleep(random.randint(1,3))#模拟生产时间
#         q.put(res)
#         print('[%s]生产了<%s>'%(name,res))

# def consumer(name,q):
#     while True:
#         res=q.get()
#         if res is None:break
#         time.sleep(random.randint(1,3))
#         print('[%s]吃了<%s>'%(name,res))

# if __name__ == "__main__":
#     # 队列
#     q=Queue()

#     # 生产者们
#     p1=Process(target=producer,args=('oldboy','包子',q))
#     p2=Process(target=producer,args=('oldgirl','骨头',q))

#     # 消费者们
#     c1=Process(target=consumer,args=('alex',q))
#     c2=Process(target=consumer,args=('wpq',q))
#     c3=Process(target=consumer,args=('egon',q))

#     p1.start()
#     p2.start()

#     c1.start()
#     c2.start()
#     c3.start()
    
#     # 如何保证生产者进程结束后，不让消费者进程卡住？
#     # 在生产者们结束后，往队列里发结束信号None。

#     p1.join()
#     p2.join()
#     q.put(None)
#     q.put(None)
#     q.put(None)

#     print('主')

# 方式二 
# 上例中为了不让消费者进程卡住，要往队列里发结束信号，
# 有几个消费者就要发几个结束信号，不方便。
# 为此，python提供了JoinableQueue队列模型

# 该模型有 task_done()方法和join方法。
# 在从队列每次get后，就task_done()一次。
# 当队列里的内容取完后，就可以激发join()方法。
# 否则就会卡在join()。这样就可以保证队列中的元素可以取完。
# 再把消费者设置为守护进程，就可以在程序执行到最后一行时结束。

from multiprocessing import Process,JoinableQueue
import time,random

def producer(name,food,q):
    for i in range(3):
        res='%s%s'%(food,i)
        time.sleep(random.randint(1,3))#模拟生产时间
        q.put(res)
        print('[%s]生产了<%s>'%(name,res))

def consumer(name,q):
    while True:
        res=q.get()
        time.sleep(random.randint(1,3))
        print('[%s]吃了<%s>'%(name,res))
        # 从队列每次get后，就task_done()一次
        q.task_done()

if __name__ == "__main__":
    # 队列
    q=JoinableQueue()

    # 生产者们
    p1=Process(target=producer,args=('oldboy','包子',q))
    p2=Process(target=producer,args=('oldgirl','骨头',q))

    # 消费者们
    c1=Process(target=consumer,args=('alex',q))
    c2=Process(target=consumer,args=('wpq',q))
    c3=Process(target=consumer,args=('egon',q))

    # 设置消费者们为守护进程：
    # 这样当主程序运行完最后一行时，消费者们就会关闭。
    c1.daemon=True
    c2.daemon=True
    c3.daemon=True

    p1.start()
    p2.start()

    c1.start()
    c2.start()
    c3.start()
    
    # 如何保证生产者进程结束后，不让消费者进程卡住？
    p1.join()
    p2.join()
    # 一定要在生产者join后才能用队列join
    # 当队列里的内容取完后，就可以激发join()方法。
    # 否则就会卡在join()，不执行下面的代码。这样就可以保证队列中的元素可以取完。
    q.join()

    print('主')
