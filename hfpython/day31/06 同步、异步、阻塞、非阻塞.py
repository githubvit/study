#1、阻塞与非阻塞指的是程序的两种运行状态
# 阻塞：遇到IO就发生阻塞，程序一旦遇到阻塞操作就会停在原地，并且立刻释放CPU资源
# 非阻塞（就绪态或运行态）：没有遇到IO操作，或者通过某种手段让程序即便是遇到IO操作也不会停在原地，执行其他操作，力求尽可能多的占有CPU


#2、同步与异步指的是提交任务的两种方式：
# 同步调用：提交完任务后，就在原地等待，直到任务运行完毕后，拿到任务的返回值，才继续执行下一行代码
# 异步调用：提交完任务后，不在原地等待，直接执行下一行代码，结果？

from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import time,os,random

def task(x):
    print('%s 接客' %x)
    time.sleep(random.randint(1,3))
    return x**2

if __name__ == '__main__':
    # 异步调用
    p=ThreadPoolExecutor(4) # 默认开启的线程数是cpu的核数*5

    # alex，武佩奇，杨里，吴晨芋，张三

    obj_l=[]
    for i in range(10):
        obj=p.submit(task,i)
        obj_l.append(obj)

    # p.close()
    # p.join()
    p.shutdown(wait=True)

    print(obj_l[3].result())
    print('主')
















    # 同步调用
    p=ThreadPoolExecutor(4) # 默认开启的线程数是cpu的核数*5

    # alex，武佩奇，杨里，吴晨芋，张三

    for i in range(10):
        res=p.submit(task,i).result()

    print('主')