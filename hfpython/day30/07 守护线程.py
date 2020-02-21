# from threading import Thread,current_thread
# import time
#
# def task():
#     print('%s is running' %current_thread().name)
#     time.sleep(3)
#
# if __name__ == '__main__':
#     t1=Thread(target=task,name='第一个线程')
#     t1.daemon = True
#     t1.start()
#
#     print('主线程')


from threading import Thread
import time
def foo():
    print(123)
    time.sleep(5)
    print("end123")

def bar():
    print(456)
    time.sleep(3)
    print("end456")

if __name__ == '__main__':

    t1=Thread(target=foo)
    t2=Thread(target=bar)

    t1.daemon=True
    t1.start()
    t2.start()
    print("main-------")

    '''
    123
    456
    main-------
    end456
    '''
