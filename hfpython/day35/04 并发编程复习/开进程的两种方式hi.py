# from multiprocessing import Process
# import os,time
#
# def task():
#     print('%s is ruuning' %os.getpid())
#     time.sleep(3)
#
#
# if __name__ == '__main__':
#     p=Process(target=task,)
#     p.start()
#     print('主')


from multiprocessing import Process

import os,time

class Work(Process):

    def run(self):
        print('%s is ruuning' %self.pid)
        time.sleep(3)


if __name__ == '__main__':
    p=Work()
    p.start()
    print('主')