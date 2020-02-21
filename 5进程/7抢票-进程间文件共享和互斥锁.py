# 一 互斥锁：为了数据安全，把并发变成串行，牺牲了一点效率。

# 例 共享打印

#  三个进程共享一个打印，希望每次打印完，才打印另一个进程的内容

# from multiprocessing import Process,Lock
# import os,time

# def printyf(pt_mutex):
#     pt_mutex.acquire() #上锁
#     print('%s is print start... '%os.getpid())
#     time.sleep(1)
#     print('%s is print done '%os.getpid())
#     pt_mutex.release() #释放锁

# if __name__ == "__main__":
#     pt_mutex=Lock()#生成打印锁对象，给每个进程加上这把锁(当参数传进去)
#     p1=Process(target=printyf,args=(pt_mutex,))
#     p2=Process(target=printyf,args=(pt_mutex,))
#     p3=Process(target=printyf,args=(pt_mutex,))
   

#     p1.start()
#     p2.start()
#     p3.start()

# 2700 is print start...
# 2700 is print done
# 1172 is print start...
# 1172 is print done
# 8620 is print start...
# 8620 is print done


#二  抢票：查票、购票。
# 利用不同进程可以读同一文件，来使数据在不同进程间传递。
# 文件json格式 7qp.json： {"count":1}

# 没加锁
# from multiprocessing import Process
# import os,json,time,random

# # 查票
# def search():
#     # time.sleep(random.randint(1,3)) #模拟网络延迟
#     dic=json.load(open(r'D:\pyj\st\进程\7qp.json','r',encoding='utf-8')) #购票信息
#     res=dic['count']
#     print('%s 查询到剩余 %s 张票'%(os.getpid(),res))
    

# # 购票
# def get():
#     # 先用load读，再用dump写。
#     dic=json.load(open(r'D:\pyj\st\进程\7qp.json','r',encoding='utf-8'))#购票信息
#     if dic['count']>0:#如果有余票
#         dic['count']-=1
#         # 将修改后的dic回写。
#         time.sleep(random.randint(1,3)) #模拟网络延迟
#         dic=json.dump(dic,open(r'D:\pyj\st\进程\7qp.json','w',encoding='utf-8'))
#         print('%s 购票成功'%(os.getpid()))

# def task():
#     search()
#     get()

# if __name__ == "__main__":
#     for i in range(10):
#         p=Process(target=task)
#         p.start()

# 3568 查询到剩余 1 张票
# 6652 查询到剩余 1 张票
# 9232 查询到剩余 1 张票
# 136 查询到剩余 1 张票
# 4840 查询到剩余 1 张票
# 6804 查询到剩余 1 张票
# 6684 查询到剩余 1 张票
# 1272 查询到剩余 1 张票
# 1088 查询到剩余 1 张票
# 8468 查询到剩余 1 张票
# 6652 购票成功
# 136 购票成功
# 1088 购票成功
# 8468 购票成功
# 3568 购票成功
# 4840 购票成功
# 6684 购票成功
# 9232 购票成功
# 6804 购票成功
# 1272 购票成功

# 枷锁
from multiprocessing import Process,Lock
import os,json,time,random

# 查票
def search():
    time.sleep(random.randint(1,3)) #模拟网络延迟
    dic=json.load(open(r'D:\pyj\st\study\5进程\7qp.json','r',encoding='utf-8')) #购票信息
    res=dic['count']
    print('%s 查询到剩余 %s 张票'%(os.getpid(),res))
    

# 购票
def get():
    # 先用load读，再用dump写。
    dic=json.load(open(r'D:\pyj\st\study\5进程\7qp.json','r',encoding='utf-8'))#购票信息
    if dic['count']>0:#如果有余票
        dic['count']-=1
        # 将修改后的dic回写。
        time.sleep(random.randint(1,3)) #模拟网络延迟
        dic=json.dump(dic,open(r'D:\pyj\st\study\5进程\7qp.json','w',encoding='utf-8'))
        print('%s 购票成功'%(os.getpid()))

def task(gp_mutex):
    search()
    # 在这里加锁，让上面查票还是并行，但购票变成串行。
    gp_mutex.acquire()#上锁 一定要释放，不然大家都抢不到。
    get()
    gp_mutex.release()#释放锁

if __name__ == "__main__":
    # 在主进程 造一把购票进程锁：给每个进程加上这把锁(当参数传进去)，
    # 这把锁就可以达到在同一时间只允许一个进程购票。即把并行改为串行。
    gp_mutex=Lock()
    for i in range(10):
        p=Process(target=task,args=(gp_mutex,))
        p.start()

# 都可以查，只有1个购买成功。
# 7156 查询到剩余 1 张票
# 9736 查询到剩余 1 张票
# 6116 查询到剩余 1 张票
# 2236 查询到剩余 1 张票
# 1368 查询到剩余 1 张票
# 5072 查询到剩余 1 张票
# 5696 查询到剩余 1 张票
# 6568 查询到剩余 1 张票
# 1708 查询到剩余 1 张票
# 6088 查询到剩余 1 张票
# 7156 购票成功

