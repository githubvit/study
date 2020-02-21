#_*_coding:utf-8_*_
'''
线程thread，
线程包含在进程中，是进程的执行单位，每个线程就是一串指令流，
python的多线程运行和多进程运行都是按时分模式，由于CPU频率很快，因此单核计算机看起来也能并行。
'''

import threading,time
def run(name):
    print 'thread [%s] is runing'%name
    time.sleep(2)

# 1,建立线程对象
# 线程的并行写法，参数用元组形式
t1=threading.Thread(target=run,args=(('t1',)))
# t1=threading.Thread(target=run('t1'))#这样写就必须等t1执行完成才能执行下面的程序，一般不用
t2=threading.Thread(target=run,args=(('t2',)))
t3=threading.Thread(target=run,args=(('t3',)))

# 2,启动线程
t1.start()

# 3,线程等待
t1.join()#就是等待，意思是等t1结束，才运行下面的线程。把线程并行123改成了串行1,23
t2.start()
t3.start()
