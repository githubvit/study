# from threading import Event,current_thread,Thread
# import time
#
# event=Event()
#
# def check():
#     print('%s 正在检测服务是否正常....' %current_thread().name)
#     time.sleep(3)
#     event.set()
#
#
# def connect():
#     print('%s 等待连接...' %current_thread().name)
#     event.wait()
#     print('%s 开始连接...' % current_thread().name)
#
# if __name__ == '__main__':
#     t1=Thread(target=connect)
#     t2=Thread(target=connect)
#     t3=Thread(target=connect)
#
#     c1=Thread(target=check)
#
#     t1.start()
#     t2.start()
#     t3.start()
#     c1.start()




from threading import Event,current_thread,Thread
import time

event=Event()

def check():
    print('%s 正在检测服务是否正常....' %current_thread().name)
    time.sleep(5)
    event.set()


def connect():
    count=1
    while not event.is_set():
        if count ==  4:
            print('尝试的次数过多，请稍后重试')
            return
        print('%s 尝试第%s次连接...' %(current_thread().name,count))
        event.wait(1)
        count+=1
    print('%s 开始连接...' % current_thread().name)

if __name__ == '__main__':
    t1=Thread(target=connect)
    t2=Thread(target=connect)
    t3=Thread(target=connect)

    c1=Thread(target=check)

    t1.start()
    t2.start()
    t3.start()
    c1.start()