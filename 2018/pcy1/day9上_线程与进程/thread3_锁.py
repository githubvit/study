#_*_coding:utf-8_*_
'''
全局解释器锁GIL：保证同一时刻只有一个线程在执行，python自带。
互斥锁（线程锁）:多个线程同时修改同一个数据时，必须加锁mutex互斥锁。
    用户自己程序上的锁，保证数据只能被某线程修改。定义锁，获取锁，释放锁。3.x不用了。
    线程锁把线程变成串行，因此使用该锁要注意：1，马上释放2，运算量不要太大。
递归锁
信号量
'''
import threading,time
# 一，互斥锁，把线程变成串行
# 1，定义一把锁
# lock=threading.Lock()
#
# thread_list=[]#做一个线程列表,保证所有线程执行完毕
#
# def run(name):
#     # 2,获取该锁
#     lock.acquire()
#     print 'thread [%s] is runing'%name
#     time.sleep(0.25)
#     print '--thread [%s] is stop'%name
#     #3,释放该锁
#     lock.release()
#
# for i in range(10):#启动多个线程
#     t=threading.Thread(target=run,args=(('t-%s'%i,)))
#     t.start()
#     thread_list.append(t)#每启动一个线程，就加入线程列表
# for j in thread_list:#从线程列表中取出每个线程，让每个线程等待结束，这样就保证了print在最后
#     j.join()
# print '线程都已完成了',

# 二，递归锁：应对锁套锁的场景
def run1():
    print("grab the run1")
    lock.acquire()#第2把锁
    global num
    num += 1
    lock.release()#释放第2把锁
    return num


def run2():
    print("grab the run2")
    lock.acquire()#第3把锁
    global num2
    num2 += 1
    lock.release()#释放第3把锁
    return num2


def run3():
    lock.acquire()#这是第1把锁，是第一级
    res = run1()#进到这里，还会有第2把锁，是第二级，这时第1把锁还没释放
    print('--------between run1 and run2-----')
    res2 = run2()#进到这里，还会有第3把锁，和第2把锁平级，是第二级，这时第1把锁还没释放
    lock.release()#释放第1把锁
    print res, res2,'\n'


num, num2 = 0, 0
lock = threading.RLock()#递归锁是RLock，注意是R
for i in range(5):
    t = threading.Thread(target=run3)
    t.start()

while threading.active_count() != 1:
    # print(threading.active_count())
    pass
else:
    print('----all threads done---')
    print(num, num2)