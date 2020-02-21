from multiprocessing import Process
import time

def task(name):
    print('%s is running' %name)
    time.sleep(3)
    print('%s is done' %name)


if __name__ == '__main__':
    # 在windows系统之上，开启子进程的操作一定要放到这下面
    # Process(target=task,kwargs={'name':'egon'})
    p=Process(target=task,args=('egon',))
    p.start() # 向操作系统发送请求，操作系统会申请内存空间，然后把父进程的数据拷贝给子进程，作为子进程的初始状态
    print('======主')




from multiprocessing import Process
import time

class MyProcess(Process):
    def __init__(self,name):
        super(MyProcess,self).__init__()
        self.name=name

    def run(self):
        print('%s is running' %self.name)
        time.sleep(3)
        print('%s is done' %self.name)


if __name__ == '__main__':
    p=MyProcess('egon')
    p.start()
    print('主')










