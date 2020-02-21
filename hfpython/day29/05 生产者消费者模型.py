#生产者消费者模型
# 该模型中包含两类重要的角色：
#1、生产者：将负责造数据的任务比喻为生产者
#2、消费者：接收生产者造出的数据来做进一步的处理，该类人物被比喻成消费者


# 实现生产者消费者模型三要素
#1、生产者
#2、消费者
#3、队列

# 什么时候用该模型：
#程序中出现明显的两类任何，一类任务是负责生产，另外一类任务是负责处理生产的数据的

# 该模型的好处：
# 1、实现了生产者与消费者解耦和
# 2、平衡了生产力与消费力，即生产者可以一直不停地生产，消费者可以不停地处理，因为二者
#不再直接沟通的，而是跟队列沟通

import time
import random
from multiprocessing import Process,Queue

def consumer(name,q):
    while True:
        res=q.get()
        time.sleep(random.randint(1,3))
        print('\033[46m消费者===》%s 吃了 %s\033[0m' %(name,res))


def producer(name,q,food):
    for i in range(5):
        time.sleep(random.randint(1,2))
        res='%s%s' %(food,i)
        q.put(res)
        print('\033[45m生产者者===》%s 生产了 %s\033[0m' %(name,res))


if __name__ == '__main__':
    #1、共享的盆
    q=Queue()

    #2、生产者们
    p1=Process(target=producer,args=('egon',q,'包子'))
    p2=Process(target=producer,args=('刘清政',q,'泔水'))
    p3=Process(target=producer,args=('杨军',q,'米饭'))

    #3、消费者们
    c1=Process(target=consumer,args=('alex',q))
    c2=Process(target=consumer,args=('梁书东',q))


    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()