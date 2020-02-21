#_*_coding:utf-8_*_
'''
经典语句：程序就是算法加数据结构。
算法（Algorithm）：一个计算机的计算过程，用来解决问题的方法
'''
'''
高级排序算法：nlogn
'''
import random,copy
#装饰器，用来比较执行的时间
import time,sys
def call_time(func):
    def decorator(*args,**kwargs):
        t1=time.time()
        x=func(*args,**kwargs)
        t2=time.time()
        print 'time cost:',func.__name__,t2-t1 #func.__name__输出函数名
        return x
    return decorator
@call_time
def bubble_sort(li):
    for i in range(len(li)-1):#外层趟数
        for j in range(len(li)-i-1):#内层无序区前后比较
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
# 生成无序列表
li1=list(range(1000000,-1,-1))

'''
怎么生成倒序列表;
li1=list(range(10000,-1,-1))
'''
sys.setrecursionlimit(100000)#设定递归级别
# 用随机洗牌打乱
# random.shuffle(li1)
li2=copy.deepcopy(li1)
li3=copy.deepcopy(li1)
li4=copy.deepcopy(li1)

# print li1

'''

一，快排
快排思路
    取一个元素p（第1个元素），使元素p归位
    列表被p分成两部分，左边都比p小，右边都比p大
    递归完成排序
    
    排序前：[5 74631298]
    p归位： [2143 5 6798]
    用递归继续左边归位和右边归位，完成排序.
    
    时间复杂度O(nlogn)，比前面的算法O(n2)要低,因此要快。
    
算法关键点：1，整理 就是归位 2，递归

怎么归位：
1，先把第一个元素取出来，赋给一个变量，空出来第0个位置
    5[ 74631298]
    tmp=5
    右指针right=len(data)-1
    左指针left=1
2，从右边开始比较,比tmp大就不动，8不动、9不动，
    2比tmp小，就要放到空出来的0位置。
    然后2原来的位置空出来。
    5[274631 98]
3， 接着从左边开始比较，比tmp小就不动，7比tmp大，
    就要移到2原来空出来的位置上，
    7原来的位置空出来。
    5[2 4631798]
4，然后又从右边开始比较，比tmp大就不动，1比tmp小，
    就要移到7原来空出来的位置上，
    1原来的位置空出来。
    5[21463 798]
5，然后又从左边开始比较，比tmp小就不动，4比tmp小，
    不动，继续6比tmp大，就要移到1原来空出来的位置上，
    6原来的位置空出来。   
     5[214 36798]
6，然后又从右边开始比较，比tmp大就不动，3比tmp小，
    就要移到6原来空出来的位置上，
   3原来的位置空出来。
    5[2143 6798]
7，left指针和right指针重合，5放入3空出来的位置。
    [214356798]
    if data[len(data)-1]>tmp:
一趟：
    5[ 74631298]
    5[274631 98]
    5[2 4631798]
    5[21463 798]
    5[214 36798]
    5[2143 6798]
    [214356798]
'''

# ------------------------快排------------------------------------------
# 右手左手一个慢动作（归位），左手右手慢动作重播（递归）
# 框架函数，用归位元素分开左右，递归（每一次都是归位、分开左右，不断的缩小范围，最终使得所有元素归位）
def quick_sort(data,left,right):#刚开始：left=0，right=len(data)-1
    if left<right:#递归终止条件，left<right保证有两个元素，1个元素就不递归了
        mid=partition(data,left,right)#归位函数，mid已放好
        quick_sort(data,left,mid-1)#递归左边
        quick_sort(data,mid+1,right)#递归右边
    # return data
# 归位函数，找到自己的位置，升序：把大的放右边，小的放左边
def partition(data,left,right):#刚开始：left=0，right=len(data)-1

    # 1，先把第一个元素取出来，赋给一个变量，空出来left位置
    tmp=data[left]
    while left<right:#左右各放1次完成1个循环，左右碰到一起完成整改循环，列表遍历了一次。
    # 当左右指针碰到一起就结束循环left=right，归位

        # 2，先从右边开始比较, 比tmp大就不动，
        while left<right and data[right]>=tmp:#升序，等号不动，指针继续移动
            right-=1 #右指针左移

        # 3，比tmp小，就要放到原来空出来的left位置（第1个是0），并空出right自己的位置
        data[left]=data[right]

        # 4，接着从左边开始比较，比tmp小就不动
        while left<right and data[left]<=tmp:
            left+=1 #左指针右移

        # 5，比tmp大，就要移到right空出来的位置上，并空出left自己的位置
        data[right]=data[left]

    # 6，left指针和right指针重合，把tmp放入空出来的位置。归位，这时left=right，所以写data[right]=tmp是一样的
    data[left]=tmp#归位
    # print '左和右',left,right
    return left #把这时的left或right指针返回
#-----------------------------------------------------------


#  把递归函数包起来，避免装饰器的问题
@call_time
def quickly(data):
    right = len(data) - 1  # 初始化右指针
    left = 0  # 初始化左指针
    return quick_sort(data,left,right)

# li7=quickly(li1)


# print li7

'''
快排复杂度分析：

def quick_sort这个是递归函数，每次分开left和right递归，类似二分，复杂度算logn
def partition这个有两层while循环，乍看像n2，但细分析，这个函数只是把列表走了一遍，
因此复杂度为n
那么，总复杂度为O(nlogn)

速度比较，和前面最快的插排比
插入排序        time cost: insert_sort      4.13100004196
快速排序        time cost: quickly          0.0270001888275
'''
# -----------------python自带排序模块-----------------------------------
'''
二，python自带排序模块sort
# python自带的排序算法模块，时间复杂度和快排是一样的，但是比快排要快一个数量级，
# 因为该模块是用c写的，别的语言自带的排序都是快排。
'''

@call_time
def sys_sort(data):
    return data.sort()
li8=sys_sort(li2)
# print li2
'''
1百万数据量的比较：
快排 time cost: quickly 4.38199996948
自带 time cost: sys_sort 0.712000131607

'''
# -----------------------------------------------------------------------
'''
快排遇到极端情况，就是倒序，每次归位后，没有分开左右，复杂度为O(n2)和其他lb排序一样。
实验时，要把递归级别加大sys.setrecursionlimit(10000)#设定递归级别,要比列表多1个数量级
否则报递归深度超出最大数错误
RuntimeError: maximum recursion depth exceeded

对于1000个倒序的列表，快排结果和普通算法差不多
time cost: quickly  0.039999961853
time cost: sys_sort 0.0
'''

#--------------------------------------------------------------------
'''
三，堆排序
堆排序过程
     1. 把列表当成完全二叉树，建成堆
         通过从最下层有叶子的子树开始逐级调整，最后可以得到堆。
     2. 得到堆顶元素，为最大元素
     3. 去掉堆顶，将堆最后一个元素放到堆顶，此时可通过一次调整重新使堆有序。
     4. 堆顶元素为第二大元素。
     5. 重复步骤3，直到堆变空，得到有序列表。

父节点和左子节点的编号下标关系:i(父) – 2i+1（左子）
                          0
                     1        2
                  3     4   5    6
                7   8 9 
'''

# 堆调整函数
#
# 它有个假设，就是堆顶的两个子堆都是完全二叉树堆，但是堆顶不见得是符合完全二叉树要求的
# 这个函数就是用来调整堆顶的，将堆顶元素插到合适的位置，从而得到完全二叉树堆。
# 这个调整函数的应用是很有意思的，
# 比如，使用这个函数对乱序堆通过从最下层有叶子的子树开始，逐级向上调整，最后可以得到完全二叉树堆。
# 大根堆调整函数，比大，保证堆顶最大，不保证堆底最小。
def sift(data,low,high):#data是堆，low是堆顶（开始是0），high就是堆底（len(data)-1）
    tmp=data[low]#先把堆顶取出来
    i=low #记录父节点位置
    j=2*i+1#记录左子节点位置
    while j<=high:#用子节点循环，直到堆底

        #从子节点中挑一个大的
        if j+1<=high and data[j]<data[j+1]:#j+1<=high，表示存在右子节点
            j+=1
        # print 'j',data[j]
        #如果子节点中大的比堆顶大，就上位
        if data[j]>tmp:
            data[i]=data[j]#第一轮的i是堆顶，子节点上位，j空出来
            i=j#把空出来的子节点变成新的父节点
            j=2*i+1#记录新的子节点
        else:
            break
    data[i]=tmp#把原来的堆顶放入空着的节点
    # print 'sf:',data[low]#看每次的堆顶


@call_time
def heap_sort(data):
    #1，建立完全二叉树堆
    n=len(data)
    low=n//2-1#从最下层有叶子的子树开始
    high=len(data)-1
    for i in range(low,-1,-1):#从low开始，每次减一，到达堆顶0.
        # print 'hp:',data[i]
        sift(data,i,high)
    # print data#看建好的堆
    # 这是建好的堆[9, 8, 5, 7, 4, 2, 0, 3, 6, 1]

    #2，对建好的完全二叉树堆，每次把堆顶取下来，将堆最后一个元素放到堆顶，顶底互换，
    # 这样，该堆就不是完全二叉树堆了
    # 使用调整函数，将堆顶取下插入合适的位置，又变成了完全二叉树堆，
    # 又重复前面做的，每次重复，堆的规模不断变小，最后取完，变成有序列表。
    for i in range(n-1,0,-1):
        data[i],data[0]=data[0],data[i]
        sift(data,0,i-1)#开始把i即n-1堆底放到堆顶，现在的i是原来的堆顶，因此该堆底为i-1
        #这里的调整和上面不同，建立完全二叉树堆是从最小的子树往上调整，
        #这里是从上往下逐级调整，即从堆顶0开始，堆底在不断减小，堆的规模不断减小.
# hl=[6, 3, 0, 7, 4, 2, 5, 8, 9, 1]
heap_sort(li3)
# print li3
    # 这是原表的堆
    #         6
    #      3      0
    #    7   4  2   5
    #   8 9 1

 # 通过对原堆从最小子树开始逐级向上调整得到完全二叉树堆
 #            9
 #         8      5
 #       7   4  2   0
 #      3 6 1
 #对完全二叉树进行顶底互换、调整，最终得到有序列表

# -----------------------------------------------------------------------
'''
四，归并排序
1，归并
假设有一个列表为两段有序：
[135724689]
两个指针low和mid右移逐个取数，
开始low指向1和mid指向2，
比较，升序为例，小的放入新建的列表tmp，
1放入tmp，low右移指向3；
low和mid继续比，2放入tmp，mid右移指向4。
以此类推，如果一边的数有多，就逐个放入tmp，
tmp变成有序列表，这叫完成1次归并。
把tmp写回原列表完成排序

2，分解
分解：将列表越分越小，直至分成一个元素。
一个元素是有序的。
合并：将两个有序列表归并，列表越来越大。
    分解    94638257
           9463  8257
          94 63  82 57
   ------9 4 6 3 8 2 5 7-----
    归并   49 36  28 57
           4369  2578
            23456789

'''

# 先分解后归并
def merage_sort(data,low,high) :
    if low<high:#如果有两个以上数
        # 分解
        mid=(low+high)//2 #不能写成mid=(low+high)/2,这样mid就不会等于0，无法终止递归。
        # print mid
        merage_sort(data,low,mid)
        merage_sort(data,mid+1,high)
        '''
        注意
        merage_sort(data,low,mid)
        merage_sort(data,mid+1,high)
        为什么不能写成
        merage_sort(data,low,mid-1)
        merage_sort(data,mid,high)
        这样也刚好分成了两半。
        但是递归结束条件是if low<high:
        mid就是low，只有当mid>=high时，才会终止递归，
        而mid=(low+high)//2，mid在不断增加，
        但high和一个比自己小的数相加÷2，永远无法大于等于自己。
        因此，要给mid+1,在mid为high-1时，low会等于high，从而终止递归。
        '''
        # print 'low', low
        # print 'mid', mid
        # print 'high', high
        # print '------------'
        # 归并
        merage(data,low,mid,high)



#归并函数:对一个两段有序的列表，归并为一个有序列表
def merage(data,low,mid,high):
    tmp=[]#归并列表
    i=low#左指针记录初始值
    j=mid+1#右指针记录初始值
    while i<=mid and j<=high:#两段都有数，把小的放入tmp，指针右移
        if data[i]<data[j]:#升序
            tmp.append(data[i])#放入归并列表
            i+=1#左指针右移
        else:
            tmp.append(data[j])
            j+=1#右指针右移
    while i<=mid:#只有左边有数，逐个放入tmp，指针右移
        tmp.append(data[i])
        i += 1
    while j<=high:#只有右边有数，逐个放入tmp，指针右移
        tmp.append(data[j])
        j += 1
    data[low:high+1]=tmp#把归并列表写入，完成排序，切片在左边不影响速度,左闭右开，所以high+1。
@call_time#把递归包起来规避装饰器
def msort(data):
    low=0
    high=len(data)-1
    return merage_sort(data,low,high)

# hl=[2, 7, 8, 3, 1, 4, 5, 0, 9, 6]




msort(li4)
# print li4





'''
1,10000
快排time cost: quickly   0.0279998779297
自带time cost: sys_sort  0.00300002098083
堆排time cost: heap_sort 0.0529999732971
归排time cost: msort     0.0370001792908

2,100000
快排time cost: quickly   0.34500002861
自带time cost: sys_sort  0.0410001277924
堆排time cost: heap_sort 0.71599984169
归排time cost: msort     0.452000141144

3,1000000
快排time cost: quickly   4.40799999237
自带time cost: sys_sort  0.724999904633
堆排time cost: heap_sort 9.51800012589
归排time cost: msort     5.73699998856

4,倒序1000
快排time cost: quickly   0.039999961853
自带time cost: sys_sort  0.0
堆排time cost: heap_sort 0.00400018692017
归排time cost: msort     0.0019998550415

5,倒序10000
快排 出不来
自带time cost: sys_sort  0.0
堆排time cost: heap_sort 0.0539999008179
归排time cost: msort     0.0329999923706

6,倒序100000
自带time cost: sys_sort  0.00200009346008
堆排time cost: heap_sort 0.645999908447
归排time cost: msort     0.361000061035

7,倒序1000000
自带time cost: sys_sort  0.0209999084473
堆排time cost: heap_sort 7.56700015068
归排time cost: msort     4.17100000381
'''

'''
最牛的就是python自带的排序sort，其余的总结如下：

1，三种排序算法的时间复杂度都是O(nlogn)

2，一般情况下，就运行时间而言：
    快速排序 < 归并排序 < 堆排序

3，三种排序算法的缺点：
    快速排序：极端情况下排序效率低，倒序到10000出不来
    
    归并排序：需要额外的内存开销，需要临时列表
    
    堆排序：在快的排序算法中相对较慢

排序方法      最坏情况      平均情况    最好情况    稳定性
      
冒泡排序        O(n2)      O(n2)       O(n)      稳定
直接选择排序     O(n2)      O(n2)      O(n2)     不稳定
直接插入排序     O(n2)      O(n2)      O(n2)      稳定
快速排序        O(n2)     O(nlogn)    O(nlogn)   不稳定
堆排序        O(nlogn)    O(nlogn)    O(nlogn)   不稳定    
归并排序      O(nlogn)    O(nlogn)    O(nlogn)    稳定

稳定性是指;当有重复数据式，位置换不换，稳定的不换，不稳定的换。
            
比如有下表，姓名和年龄，姓名不同，年龄相同。
            alex  38
            wusir 38
先按姓名排，如上表，再按年龄排，本来不用动，但稳定性不好的排序就会排成
            wusir 38
            alex  38
'''
