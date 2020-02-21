#_*_coding:utf-8_*_
'''
经典语句：程序就是算法加数据结构。
算法（Algorithm）：一个计算机的计算过程，用来解决问题的方法
'''
'''
一，递归：
    1，调用自身
    2，规模收敛
    3，结束条件

二，时间复杂度
    时间计量单位：秒、分、小时、日、月、年
    时间复杂度就是程序运行快慢的计量单位：用来评估算法运行效率的单位
    效率从高排到低，复杂度越来越高。
    O(1),O(logn)二分法,O(n),前面就是基本单位，这两个就是组合O(nlogn),O(n2)
    循环减半就是O(logn).
    几次循环就是n的几次方的复杂度。

三，空间复杂度
    用来评估算法内存占用大小的式子
    变量 O(1)
    列表 O(n)
    二维列表 O(n2)
    依次类推

四，列表查找 复杂度
    1，需求：从列表中查找指定元素
            输入：列表、待查找元素
            输出：元素下标或未找到
        
    2，顺序查找：O(n)
        从列表第一个元素开始，顺序进行搜索，知道找到为止。
        
    3，二分查找：有序，中间值，每次折半。O(logn)
        从有序列表的候选区data[0:n]开始，通过对待查找的值与候选区中间值的比较，可以使候选区减少一半。
        
    
'''
#一， 递归
# def func1(x):
#     if x>0:
#         print x
#         func1(x-1)
# func1(5)
# '''
# 5
# 4
# 3
# 2
# 1
# '''
#
# def func2(x):
#     if x > 0:
#         func2(x-1)
#         print x
# func2(5)
# '''
# 1
# 2
# 3
# 4
# 5
# '''
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

# 二，有序列表二分查找
'''
需求：从列表中查找指定元素
            输入：列表olist、待查找元素v
            输出：元素下标或未找到
1,用循环+指针实现有序列表二分查找
定义low和high、mid分别对应有序列表的最低下标和最高下标，以及中间下标三个指针

开始，low=0，high=len（olist）-1，mid=low+high/2
如果，v>olist[mid],就要到mid的右边找，就是把low=mid+1，high不变，mid=low+high/2，
如果，v<olist[mid],就要到mid的左边找，就是把high=mid-1，low不变，mid=low+high/2，
如果，v=olist[mid]，就找到了，return这个mid，就是元素下标
没找到就return ，就是返回None

'''
@call_time
def bin_serach(olist,v):
    #初始化指针
    low=0
    high=len(olist)-1
    mid=(low+high)/2
    while low<=high:#每一轮low、high、mid都在变化，就是不断的折半
        #这里不能用while True，否则如果没有陷入死循环
        if v==olist[mid]:
            return  mid
        elif v>olist[mid]:#在右边，把low指针左移
            low=mid+1
            mid=(low+high)/2
            continue
        else:#在左边，把high指针右移
            high=mid-1
            mid = (low + high) / 2
            continue
    return #这里用return表示没找到，返回‘None'


'''
2，用递归实现有序列表二分查找
注意：
  递归函数用装饰器，装饰器也会递归，会在里面也使用，会出问题。
因此，做个函数把递归包起来，把装饰器给这个函数，就没问题了。
和上面的循环二分算法比较。
'''

def binary_search(dataset, find_num):

    if len(dataset) > 1:
        mid = int(len(dataset) / 2)
        if dataset[mid] == find_num:  # find it
            return dataset[mid]
        elif dataset[mid] > find_num:  # 找的数在mid左面
            # print("\033[31;1m找的数在mid[%s]左面\033[0m" % dataset[mid])
            return binary_search(dataset[0:mid], find_num)
        else:  # 找的数在mid右面
            # print("\033[32;1m找的数在mid[%s]右面\033[0m" % dataset[mid])
            return binary_search(dataset[mid + 1:], find_num)
    else:
        if dataset[0] == find_num:  # find it
            pass
            # print "找到数字啦", dataset[0]
        else:
            print "没的分了,要找的数字[%s]不在列表里" % find_num


@call_time
def bin_serchdg(olist,v):
    return binary_search(olist,v)

# 生成有序列表
olist=list(range(10000000))
bin_serach(olist,155)
bin_serchdg(olist,155)

'''
time cost: bin_serach 0.0
time cost: bin_serchdg 0.138999938965
可以看到递归慢，这是因为，在递归时，传递了切片dataset[0:mid]、dataset[mid + 1:]
当把切片做为值时，是要在内存里另起一个临时空间，对原表进行克隆的，
相当于var1=dataset[0:mid]，var2=dataset[mid + 1:]，因此慢。

但是，对于把切片做为被赋值对象时，不慢，写法更简练。
dataset[0:mid]=li，这种不慢，等效于下面：
for i in range(mid+1):
    dataset.append(li(i))
。

因此应该用循环+指针做二分查找算法。

'''

#三，二分查找算法应用
'''
现有一个学员信息列表（按id增序排列），格式为：
[
{id:1001,name:'张三',age:20}
...
{id:1998,name:'赵六',age:22}
]
修改二分查找代码，输入学生id，输出该学生在列表中的下标，并输出完整学生信息。
'''

'''
1，生成学生列表
'''
import  random
# 生成学生列表函数
def stuli(n):
    res=[]
    ids=list(range(1001,1001+n))#这里生成了id的有序列表
    n1=['赵','钱','孙','李','周','武','郑','王','刘','何']
    n2=['丽','晓','小','','爱','','纪','','国','建']
    n3=['强','国','峰','兵','亮','浩','明','荣','忠','飞']

    for i in range(n):
        id=ids[i]#依序从id的有序列表中取出来，这就保证了字典在列表中是按字典中的id有序排列的。
        # 随机取出上面三个文字列表的字组成name
        name=random.choice(n1)+random.choice(n2)+random.choice(n3)
        # 从18到61的数字中随机取出1个数字做为年龄
        age=random.randint(18,61)
        stu = {}#建立学生信息字典
        stu['id']=id
        stu['name']=name
        stu['age']=age
        res.append(stu)#将学生字典添加进学生列表
    return res#返回学生列表

# 生成学生列表
suli=stuli(1000)
# for j in suli:
#     print j['id'],j['name'],j['age']

'''
2，用二分法查找
'''
@call_time
def stu_serach(olist,v):
    low=0
    high=len(olist)-1
    mid=(low+high)/2
    while low<=high:#每一轮low、high、mid都在变化，就是不断的折半
        if v==olist[mid]['id']:
            return mid
        elif v>olist[mid]['id']:
            low=mid+1
            mid=(low+high)/2
            continue
        else:
            high=mid-1
            mid = (low + high) / 2
            continue
    return
#传入学生列表和学生id号，注意输入是id不是下标，输出是下标
s1=stu_serach(suli,1199)
print s1
if s1:#如果s1有结果,就是取到了下标
    print suli[s1]['id'],suli[s1]['name'],suli[s1]['age']