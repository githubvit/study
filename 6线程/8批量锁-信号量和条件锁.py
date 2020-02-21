# 一 信号量 = 一批锁
#  实例：(同时只有5个线程可以获得semaphore,即可以限制最大连接数为5)

from threading import Thread,Semaphore,current_thread
import time,random

def func():
    with sm:
       print('%s get sm'%current_thread().getName()) 
       time.sleep(random.randint(1,3))
if __name__ == '__main__':
    sm=Semaphore(5)
    for i in range(23):
        t=Thread(target=func)
        t.start()

# 二 条件锁 Condition
# 使得线程等待，只有满足某条件时，才释放n个线程

# 1 活动信号量
# from threading import Thread,Condition
# # 设置条件锁
# con=Condition()
# def run(n):
#     con.acquire()
#     con.wait()#等notify通知放行线程的数量
#     print('run the thread:%s'%n)
#     con.release()

# if __name__ == "__main__":
#     for i in range(10):
#         t=Thread(target=run,args=(i,))
#         t.start()
#     while True:
#         inp=input('>>')
#         if not inp.isdigit():
#             if inp == 'q':
#                 break
#             else:
#                 print('请输入数字')
#                 continue
#         con.acquire()
#         con.notify(int(inp))#通知wait放行多少线程，有点像活动信号量。
#         con.release()    

# 2 条件状态函数 con.wait_for(条件状态函数名) True就通过 False就阻塞
#  没有什么 相当于在线程中串联 该函数，然后根据函数的结果阻塞或通过。
# from threading import Thread,Condition

# con = Condition()

# # 设置条件函数 返回True/False 
# # 用con.wait_for(condition_func) 加载该函数
# def condition_func():
#     ret = False
#     inp = input('>>>')
#     if inp == '1':
#         ret = True
#     return ret


# def run(n):
#     con.acquire()
#     # 状态为False 则 阻塞 
#     con.wait_for(condition_func) #阻塞 等待 状态为True 则 通过
#     print("run the thread: %s" %n)
#     con.release()

# if __name__ == '__main__':
    
#     for i in range(10):
#         t = Thread(target=run, args=(i,))
#         t.start()