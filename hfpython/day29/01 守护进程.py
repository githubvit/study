from multiprocessing import Process
import time


def task(name):
    print('%s is running' % name)
    time.sleep(3)

if __name__ == '__main__':
    obj = Process(target=task, args=('egon',))
    obj.daemon=True
    obj.start()  # 发送信号给操作系统
    print('主')
