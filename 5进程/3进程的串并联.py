#  join

from multiprocessing import Process
import time,random

x=1000

def task(n):
    print('%s is runing' %n)
    time.sleep(n)

if __name__ == '__main__':
    # start_time=time.time()

    # p1=Process(target=task,args=(1,))
    # p2=Process(target=task,args=(2,))
    # p3=Process(target=task,args=(3,))

    #并联 3.1423635482788086
    # p1.start()
    # p2.start()
    # p3.start()

    # p1.join()
    # p2.join()
    # p3.join() 

    # 串联 6.37688684463501
    # p1.start()
    # p1.join()
    # p2.start()
    # p2.join()
    # p3.start()
    # p3.join() 

    # print('主',(time.time() - start_time))

# 组建进程列表 
    start_time=time.time()
    p_l=[]
    for i in range(1,4):
        p=Process(target=task,args=(i,))
        p_l.append(p)
        p.start()
        # p.join()#串联
    
    for p in p_l:
        p.join()#并联
    
    print('主',(time.time() - start_time)) #3.1749277114868164 3.141684055328369