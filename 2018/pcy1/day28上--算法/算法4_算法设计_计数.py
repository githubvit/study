#_*_coding:utf-8_*_
'''
经典语句：程序就是算法加数据结构。
算法（Algorithm）：一个计算机的计算过程，用来解决问题的方法
'''

'''
现在有一个列表，列表中的数范围都在0到100之间，列表长度大约为100万。
设计算法在O(n)时间复杂度内将列表进行排序。
'''
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
import random,copy
# 建表
li=[ random.randint(0,100) for i in range(100)]
li1=copy.deepcopy(li)
# print li
'''
计数排序
100万数据的最大值就是100，因此有很多重复的数据，不能用快排，别的高级排序都是nlogn，
我们可以设计一个表位置从0到100，值都是None，叫计数表。
然后遍历100万的表，将每个数据出现的次数，记录为计数表相应位置的值。复杂度为n
最后遍历计数表，根据每个位置的值n，输出n次计数表该位置的下标写回原数据表，这个复杂度也是n
完成100万数据量的排序，总复杂度是2n，为O（n）。
'''

@call_time
def counts_sort(li,max_num):
    # 1,我们可以设计一个表位置从0到100，值都是None，叫计数表。
    cn=[0 for i in range(max_num+1)]
    # 2,然后遍历100万的表，将每个数据出现的次数，记录为计数表相应位置的值。复杂度为n
    for i in li:
        cn[i]+=1
    # 3,最后遍历计数表，根据每个位置的值num，输出num次计数表该位置的下标i给原表li，这个复杂度也是n
    k=0
    for i,num in enumerate(cn):
        if num!=0:
            for j in range(num):
                li[k]=i#直接写回到li
                k+=1
#------------------------------python自带-----------------
@call_time
def sys_sort(data):
    return data.sort()
#---------------------------------------------------------

counts_sort(li,100)

sys_sort(li1)
# print li
'''
计数time cost: counts_sort 0.125
自带time cost: sys_sort    0.261999845505
我们设计的计数算法打败了python自带的sort，
因为我们的算法复杂度是n，而python自带的sort是nlogn。
前提是因为有了最大值的限制，使得我们可以建立计数列表。
'''
