# 主线程的生命周期=进程内所有线程运行完毕。

from threading import Thread
import time

def foo():
    print('123')
    time.sleep(1)
    print('123end')
    

def bar():
    print('456')
    time.sleep(3)
    print('456end')

if __name__ == "__main__":
    t1=Thread(target=foo)
    t2=Thread(target=bar)
    
    # 守护线程 t1
    # t1.daemon=True

    # 结果
    # 123
    # 456
    # 主线程
    # 123end
    # 456end

    
    # 守护线程 t2
    t2.daemon=True

    # 结果
    # 123
    # 456
    # 主线程
    # 123end

    t1.start()
    t2.start()

    print('主线程')