#_*_coding:utf-8_*_
'''
经典语句：程序就是算法加数据结构。
算法（Algorithm）：一个计算机的计算过程，用来解决问题的方法
'''
'''
现在有n个数（n>10000的表单），设计算法，按大小顺序得到前10大的数。
应用场景：榜单TOP 10

'''

#装饰器，用来比较执行的时间
import time,sys,random,copy
def call_time(func):
    def decorator(*args,**kwargs):
        t1=time.time()
        x=func(*args,**kwargs)
        t2=time.time()
        print 'time cost:',func.__name__,t2-t1 #func.__name__输出函数名
        return x
    return decorator
# 表
li=list(range(100))
random.shuffle(li)
li1=copy.deepcopy(li)
li2=copy.deepcopy(li)
li3=copy.deepcopy(li)
li4=copy.deepcopy(li)

# 方法一，直接用选择算法，复杂度为topn
@call_time
def select_top(li,top):
    for i in range(top):
        for j in range(i+1,len(li)):
            if li[i]<li[j]:
                li[i],li[j]=li[j],li[i]
    # for i in range(top):
    #     print li[i]

# 方法二，直接用冒泡算法，复杂度为topn
@call_time
def bubble_top(li,top):
    for i in range(top):
        for j in range(len(li)-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
    # for i in range(len(li)-1,len(li)-top-1,-1):
    #     print li[i]

#方法三，用插入排序
'''
先从列表中截取需要的top数量列表，
将截取的top列表排序，
取列表中截取后续的数，和top列表中的数倒序比较，如果后续的数比top列表中的数大，就把top列表的数右移，
为了保证右移空间，top列表要多一个位置。
最后的top列表就是整个列表中最大的数。
'''
@call_time
def insert_top(li,topn):
    #1, 先从列表中截取需要的top数量列表，
    top=li[:topn+1]#为了保证右移空间，top列表要多一个位置。
    #2,将截取的top列表排序，用python自带的排序
    top.sort(reverse=True)#倒序，sort默认是升序
    #3,取列表中截取后续的数，和top列表中的数倒序比较，如果后续的数比top列表中的数大，就把top列表的数右移，
    for i in range(topn+1,len(li)):
        tmp=li[i]
        k = topn  # 记录k的初值
        for j in range(topn-1, -1, -1):#必须从topn-1开始，topn为右移位，这样就不会出现列表越界错误
            if tmp>top[j]:
                top[j+1]=top[j]#右移
                k=j#记录空位
            else:
                break
        top[k]=tmp#把取出来的数放入空位
    li[:topn+1]=top#把top写回去

# 方法四，堆排
'''
解决思路：
取前10大的数
取列表前10个元素建立一个小根堆。堆顶就是前10中最小的数。
依次向后遍历原列表，对于列表中的元素，如果小于堆顶，则忽略该元素；如果大于堆顶，则将堆顶更换为该元素，并且对堆进行一次调整；
遍历列表所有元素后，倒序弹出堆顶。
就得到10个最大的数。
'''
# 堆调整函数
#
# 它有个假设，就是堆顶的两个子堆都是完全二叉树堆，但是堆顶不见得是符合完全二叉树要求的
# 这个函数就是用来调整堆顶的，将堆顶元素插到合适的位置，从而得到完全二叉树堆。
# 这个调整函数的应用是很有意思的，
# 比如，使用这个函数对乱序堆通过从最下层有叶子的子树开始，逐级向上调整，最后可以得到完全二叉树堆。
# 小根堆调整函数，比小，保证堆顶最小，不保证堆底最大。
def sift(data,low,high):#data是堆，low是堆顶（开始是0），high就是堆底（len(data)-1）
    tmp=data[low]#先把堆顶取出来
    i=low #记录父节点位置
    j=2*i+1#记录左子节点位置
    while j<=high:#用子节点循环，直到堆底

        #从子节点中挑一个小的
        if j+1<=high and data[j]>data[j+1]:#j+1<=high，表示存在右子节点
            j+=1
        # print 'j',data[j]
        #如果子节点中小的比堆顶小，就上位
        if data[j]<tmp:
            data[i]=data[j]#第一轮的i是堆顶，子节点上位，j空出来
            i=j#把空出来的子节点变成新的父节点
            j=2*i+1#记录新的子节点
        else:
            break
    data[i]=tmp#把原来的堆顶放入空着的节点
    # print 'sf:',data[low]#看每次的堆顶
@call_time
def heap_top(li,topn):
    #1，截取原列表topn，建立初始top
    top = li[:topn]

    #2，建立top完全二叉树堆--小根堆
    low=topn//2-1#从最下层有叶子的子树开始
    high=topn-1
    for i in range(low,-1,-1):#从low开始，每次减一，到达堆顶0.
        sift(top,i,high)#通过i的变化实现逐级向上调整，最终到0.
    # print top#看建好的堆

    # 3，依次向后遍历原列表，对于列表中的元素，如果小于堆顶，则忽略该元素；
    # 如果大于堆顶，则将堆顶更换为该元素，并且对堆进行一次调整；
    for i in range(topn,len(li)):
        if li[i]>top[0]:
            top[0]=li[i]
            sift(top,0,topn-1)

    # 4,倒序弹出堆顶,就得到10个最大的数。
    for i in range(topn-1,0,-1):
        top[i],top[0]=top[0],top[i]#顶底互换，完成倒序
        sift(top,0,i-1)#开始把i即n-1堆底放到堆顶，现在的i是原来的堆顶，因此该堆底为i-1
        #这里的调整和上面不同，建立完全二叉树堆是从最小的子树往上调整，
        #这里是从上往下逐级调整，即从堆顶0开始，堆底在不断减小，堆的规模不断减小.

    return top


'''
用堆排取top：
如果是取大，就要建立top小根堆，然后原表和堆顶比大。
如果是取小，就要建立top大根堆，然后原表和堆顶比小。

'''

# ---------------------------------------------------------------

# select_top(li,10)
# bubble_top(li1,10)
# insert_top(li2,10)
# heap_top(li3,10)

# print li[0:10]
# print li1[len(li1)-10:len(li1)]
# print li2[0:10]
# print heap_top(li,10)

'''
1，100000数据量
选择time cost: select_top 0.138000011444
冒泡time cost: bubble_top 0.301999807358
插入time cost: insert_top 0.0670001506805
堆排time cost: heap_top   0.0139999389648

2，1000000数据量
选择time cost: select_top 1.70299983025 
冒泡time cost: bubble_top 3.3029999733 
插入time cost: insert_top 0.710000038147 
堆排time cost: heap_top   0.179000139236 

复杂度都是O(n):
细分析，堆排是nlogtopn。其他是ntopn。
因此，堆排top最快。
'''
# -----------------------------------------------------------------------
'''
优先队列：一些元素的集合，POP操作每次执行都会从优先队列中弹出最大（或最小）的元素。
堆——优先队列

Python内置模块——heapq
利用heapq模块实现堆排序
heappush()入堆
heappop（）出堆
def heapsort(li):
    h = []
    for value in li:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]

利用heapq模块实现取top-k
    heapq.nlargest(100, li)
    heapq.nsmallest(100,li)

'''
# 堆排序
import heapq
# 1，建堆
heap=[]
for i in li:
    heapq.heappush(heap,i)
# 2，出数
for i in range(len(heap)):
    print heapq.heappop(heap())





# @call_time
# def heapq_top(topn,li):
#     return heapq.nlargest(topn,li)
# heapq_top(10,li4)

'''
1000000数据量的比较:
time cost: heap_top   0.181999921799
time cost: heapq_top  0.270999908447
我们自己设计的堆排top比py的优先队列top快，这是因为py模块heapq一定还是有满足其他需求的代码。
总结，找top的算法应该用堆排。
'''