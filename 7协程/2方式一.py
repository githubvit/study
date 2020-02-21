# 协程 yield 并发
import time
def consumer():
    '''任务1:接收数据,处理数据'''
    while True:
        x=yield
        # time.sleep(1) #yield 不能处理阻塞

def producer():
    '''任务2:生产数据'''
    g=consumer()
    next(g)
    for i in range(10000000):
        g.send(i)

start=time.time()

#基于yield保存状态,实现两个任务直接来回切换,即并发的效果
#PS:如果每个任务中都加上打印,那么明显地看到两个任务的打印是你一次我一次,即并发执行的.

producer() 

stop=time.time()
print(stop-start) #0.9687032699584961

# 串行 
# import time
# def consumer():
#     '''任务1:接收数据,处理数据'''
#     pass


# def producer():
#     '''任务2:生产数据'''
#     for i in range(10000000):
#         pass

# start=time.time()

# #串行
# producer() 
# consumer()

# stop=time.time()
# print(stop-start) #0.2078714370727539

# 串行 效率 高于 并发 效率