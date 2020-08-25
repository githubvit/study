# 方式一
# from multiprocessing import Process
# import time
# # 子进程要执行的任务
# def task(name):
#     print('%s is running' %name)
#     time.sleep(3)
#     print('%s is done' %name)

# if __name__ == "__main__":
#     start_time=time.time()
#     # 在windows系统之上，开启子进程的操作一定要放到__main__这下面
#     # Process(target=task,kwargs={'name':'egon'}) # 任务，用字典传递参数
#     p=Process(target=task,args=('egon',))#传递参数用元组
#     p.start() # 向操作系统发送请求，操作系统会申请内存空间，然后把父进程的数据拷贝给子进程，作为子进程的初始状态
#     # p.join() # 父进程等待子进程执行完。
#     stop_time=time.time()
#     print('======主',stop_time-start_time)#从时间看出，操作系统申请内存空间很耗时间。
        
# 方式二
from multiprocessing import Process
import time

class MyProcess(Process):#继承Process类
    def __init__(self,name):
        super(MyProcess,self).__init__()#继承父类init
        self.name=name #子进程名称

    def run(self): #固定写法 必须定义run  子进程执行的任务
        # 就是把方式一的target函数写在这里，以便调p.start() 就是调run方法   
        print('%s is running' %self.name)
        time.sleep(3)
        print('%s is done' %self.name)


if __name__ == '__main__':
    p=MyProcess('egon')
    p.start()
    # p.join()
    print('主')

# 方式一常用    