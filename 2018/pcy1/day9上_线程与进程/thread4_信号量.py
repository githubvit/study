#_*_coding:utf-8_*_
'''
信号量：每次可以放行多个线程，不像互斥锁，每次只放行1个。
比如socketserver设定的每次同时连接数
'''
import threading,time

def run(n):
    semaphore.acquire()#信号量获取
    time.sleep(1)
    print("run the thread: %s\n" % n)
    semaphore.release()#信号量释放

if __name__ == '__main__':
    # 信号量设定BoundedSemaphore
    semaphore = threading.BoundedSemaphore(5)  # 最多允许5个线程同时运行
    for i in range(22):
        t = threading.Thread(target=run, args=(i,))
        t.start()
while threading.active_count() != 1:
    pass  # print threading.active_count()
else:
    print('----all threads done---')
    #print(num)