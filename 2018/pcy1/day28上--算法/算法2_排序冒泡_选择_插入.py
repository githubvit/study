#_*_coding:utf-8_*_
'''
经典语句：程序就是算法加数据结构。
算法（Algorithm）：一个计算机的计算过程，用来解决问题的方法
'''
'''
列表排序
    将无序列表变成有序列表
应用场景
    各种榜单
    各种表格
    给二分查找用，因为二分查找是建立在有序的基础上的
    给其他算法用
输入：无序列表
输出：有序列表

各种排序算法：
    LB三人组
        # 冒泡排序
        # 选择排序
        # 插入排序
        
    快速排序
    
    排序NB二人组
        堆排序
        归并排序
        
    没什么人用的排序
        基数排序
        希尔排序
        桶排序
        
算法关键点：有序区，无序区
    通过把无序区的数据送人有序区，不断扩大有序区，减小无序区。
'''
import random,copy
#装饰器，用来比较执行的时间
import time
def call_time(func):
    def decorator(*args,**kwargs):
        t1=time.time()
        x=func(*args,**kwargs)
        t2=time.time()
        print 'time cost:',func.__name__,t2-t1 #func.__name__输出函数名
        return x
    return decorator
# 生成无序列表
li1=list(range(10000))
# 用随机洗牌打乱
random.shuffle(li1)
# 深度拷贝，保证每个算法用的列表都是一致的。
# li2=copy.deepcopy(li1)
# li3=copy.deepcopy(li1)
# li4=copy.deepcopy(li1)
li5=copy.deepcopy(li1)
li6=copy.deepcopy(li1)
# print li1
'''
一，冒泡排序:

以升序排序为例:大的就往后排

前后两个数比较，如果前大后下，就把前后交换。

开始：li=[546372891]
整个比完一轮叫一趟。

外层i
第0趟：无序区为全部，有序区为0
    内层j
       0    [5 46372891]54换
       1    [45 6372891]56不换
       2    [456 372891]63换
       3    [4536 72891]67不换
       4    [45367 2891]72换
       5    [453627 891]78不换
       6    [4536278 91]89不换
       7    [45362789 1]91换
       结果  [453627819 ] 9进入有序区
       无序区减1，有序区加1
       
          无序区循环比较     结果           有序区
第1趟：    [45362781]      [43526718]      [89]
第2趟：    [4352671]       [3425617]       [789]      
第3趟：    [342561]        [324516]        [6789]  
第4趟：    [32451]         [23415]         [56789]
第5趟：    [2341]          [2314]          [456789]
第6趟：    [231]           [213]           [3456789]
第7趟：    [21]            [12]            [23456789]

总结：9个数共计8趟（0-7）外层循环次数=len(li)-1，
    每趟无序区的数量为len(li)-i,内层循环次数=数量-1，很简单，3个数比较，2次出结果
    内层循环次数=len(li)-i-1
'''

@call_time
def bubble_sort(li):
    for i in range(len(li)-1):#外层趟数
        for j in range(len(li)-i-1):#内层无序区前后比较
            if li[j]>li[j+1]:#升序
                li[j],li[j+1]=li[j+1],li[j]#前后交换


# 用冒泡排序
# bubble_sort(li1)
# print li1

# 冒泡排序优化
'''
思路：在某趟中，如果发现已经排好了（即前后没有发生交换），就不必再循环了
用布尔变量定义交换标识。
比较一下和原来的时间花费
'''
@call_time
def bubble_sort_1(li):
    for i in range(len(li)-1):#外层趟数
        exchange=False
        for j in range(len(li)-i-1):#内层无序区前后比较
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]#前后交换
                exchange=True
        if not exchange:#如果没有交换，就得到了结果
            break
# 生成无序列表

# list(range(3000))
# # 用随机洗牌打乱
# random.shuffle(li2)

# 用优化冒泡排序
# bubble_sort_1(li2)
'''
冒泡排序和优化冒泡排序的时间复杂度比较：
首先，都是O(n2)，
然后，分为一般情况、最坏情况、最好情况
冒泡就都是O(n2)，优化后，一般和最坏都是O(n2)，最好是O(n)也就是列表本身就是有序的情况，只执行1趟。
'''
'''
二，选择排序
以升序排列为例：
一趟遍历记录列表中最小的数，放到第1个位置。

假设第一个位置是最小的，让后面的数来比，如果比它小，就换位置，
继续拿这个位置的数和后面的比，就会找出最小的

再一趟遍历记录剩余列表中最小的，放到第2个位置。
以此类推...
'''
@call_time
def select_sort(li):
    for i in range(len(li)-1):#假设当前的i最小
        for j in range(i+1,len(li)):#用后面的数逐个和当前的数比较
            if li[j]<li[i]:#每个数就是和当前的i比较
                li[j],li[i]=li[i],li[j]#就是和当前的i交换


# 用选择排序
# select_sort(li3)
# print li3
# 另一种选择排序，谈不上优化，是把有序区放在内层，开始比的规模小，后面比的规模大，
# 内层的有序区是相对有序，不到最后不出结果
@call_time
def select_sort_1(li):
    # print li
    for i in range(1,len(li)):#假设前面的是最小的，是有序的
        for j in range(0,i):#拿当前的i和前面的j逐个比较，开始比的规模小，后面比的规模大，不到最后不出结果
            if li[j]>li[i]:
                li[j],li[i]=li[i],li[j]

        # print li
# select_sort_1(li4)
# print  li4
'''
选择和冒泡比，就是有序区在前，而冒泡在后。时间复杂度一样都是O(n2),
从实验结果看选择要快一点
'''

'''
三，插入排序
类似打牌时，边抓牌边理牌的过程。
以升序为例：
1，
开始手上有1张0号牌，拿1号牌，如果1号比0号小，0号右移1位，否则不动；把1号放入空出来的位置。
2，
接着来了2号，2号先跟1号比，如果2号比1号小，1号右移1位；否则不动。
2号再跟0号比，同样，如果2号比0号小，0号右移1位；否则不动。
把2号放入空出来的位置。
...以此类推，
'''

@call_time
def insert_sort(li):
    # print li
    for i in range(1,len(li)):
        tmp=li[i]#把要比较的牌赋给一个变量tmp
        j=(i-1)
        while j>=0 and li[j]>tmp:#和前面的有序区倒序比较，
            # 把条件放在while高效，因为不必把循环做到底
            li[j+1]=li[j] #右移1位，倒过来是左移li[j]=li[j+1]
            j=j-1#倒序比较，从j->0
        li[j+1]=tmp#这一趟循环结束后，把要比较的牌插入腾出来的位置
        # 本来空出来的是位置j，li[j]=tmp，
        # 但在while循环末尾，j=j-1,j往前推了1位，这样就保证了截至条件。
        # 所以空出来的是j+1，li[j+1]=tmp才能把tmp放入空出来的位置。
        # print li
insert_sort(li5)

# 下面这个是用for循环做的插入排序。
@call_time
def insert_sort_1(li):
    # print li
    for i in range(1,len(li)):#手里有张0号牌，所以循环从1开始
        tmp=li[i]#抓牌赋给并tmp
        # ki=i#记录tmp的初始位置

        for j in range(i-1,-1,-1):#拿tmp和前面的j逐个倒序比较，开始是i-1，最后是0。
    #这种range有三个值的时候，i-1是开始，-1是结束（左闭右不闭，到不了-1，只能到0），最后的-1是步长。

            if li[j]>tmp:#倒序比较，开始j为i-1，因此是从i-1到0。

                li[j+1]=li[j]#右移把[j]加1右移到[j+1]

                # li[j] = tmp  # 把tmp放入空出来的位置，
                # 如果直接这样放，没有比先记录位置ki，本轮循环结束，再放入空位快。

                # ki=j#记录空出来的位置
            #     更优化的写法是连ki这个位置记录变量都不需要，直接把空位给tmp原来的下标i
            #     这样写并不比有ki快，姿势好看而已，别人也不太容易看懂，变量少了1个
                i=j

            else:#不满足if，就说明已经排好了，本轮不用再循环
                break

        # li[ki]=tmp#把tmp放入空出来的位置
        li[i]=tmp#把tmp放入空出来的位置

        # print li
insert_sort_1(li6)

'''
几个排序算法的比较结果:

1，10000个
冒泡排序        time cost: bubble_sort      7.03699994087
冒泡优化        time cost: bubble_sort_1    8.13300013542
选择排序        time cost: select_sort      6.06699991226
选择排序2       time cost: select_sort_1    6.10299992561
插入排序        time cost: insert_sort      4.13100004196
插入排序2       time cost: insert_sort_1    5.45799994469

2,5000个
冒泡排序        time cost: bubble_sort      1.78299999237
冒泡优化        time cost: bubble_sort_1    2.05899977684
选择排序        time cost: select_sort      1.52900004387
选择排序2       time cost: select_sort_1    1.51900005341
插入排序        time cost: insert_sort      1.04399991035
插入排序2       time cost: insert_sort_1    1.36500000954


3,1000个
冒泡排序        time cost: bubble_sort      0.074000120163
冒泡优化        time cost: bubble_sort_1    0.0859999656677
选择排序        time cost: select_sort      0.0620000362396
选择排序2       time cost: select_sort_1    0.0609998703003
插入排序        time cost: insert_sort      0.0390000343323
插入排序2       time cost: insert_sort_1    0.0550000667572


排名结果，从快到慢，插入>插入2>选择>选择2>冒泡>冒泡优化
数据越大越明显
---------------------
第二轮，
1，1000
冒泡排序  time cost: bubble_sort   0.0770001411438
冒泡优化  time cost: bubble_sort_1 0.0869998931885
选择排序  time cost: select_sort   0.0650000572205
选择排序2 time cost: select_sort_1 0.0620000362396
插入排序  time cost: insert_sort   0.0450000762939
插入排序2 time cost: insert_sort_1 0.0329999923706

2，5000
冒泡排序  time cost: bubble_sort   1.78299999237
冒泡优化  time cost: bubble_sort_1 2.06700015068
选择排序  time cost: select_sort   1.52699995041
选择排序2 time cost: select_sort_1 1.52499985695
插入排序  time cost: insert_sort   1.04200005531
插入排序2 time cost: insert_sort_1 0.80999994278

3,10000
冒泡排序  time cost: bubble_sort   7.10800004005
冒泡优化  time cost: bubble_sort_1 8.26799988747
选择排序  time cost: select_sort   6.14300012589
选择排序2 time cost: select_sort_1 6.16999983788
插入排序  time cost: insert_sort   3.72100019455
插入排序2 time cost: insert_sort_1 3.35199999809


排名结果，从快到慢，插入2>插入>选择>选择2>冒泡>冒泡优化
数据越大越明显

插排之所以快，
1，首先是从无序区取数和有序区比，而不是只在无序区比较。
2，其次是把有序区倒序和无序区的比，这样可以减少每趟比的次数。
'''