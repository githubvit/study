# from multiprocessing import Process
# from threading import Thread
# import time
#
# def task(name):
#     print('%s is running' %name)
#     time.sleep(3)
#
# if __name__ == '__main__':
#     t=Thread(target=task,args=('egon',))
#     # t=Process(target=task,args=('egon',))
#     t.start()
#     print('主线程')


from multiprocessing import Process
from threading import Thread
import time

class MyThread(Thread):

    def run(self):
        print('%s is running' %self.name)
        time.sleep(3)

if __name__ == '__main__':
    t=MyThread()
    t.start()
    print('主线程')