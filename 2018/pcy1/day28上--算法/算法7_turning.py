#_*_coding:utf-8_*_
'''
经典语句：程序就是算法加数据结构。
算法（Algorithm）：一个计算机的计算过程，用来解决问题的方法
'''
'''
给定一个列表(数是唯一的)和一个整数，设计算法找到两个数的下标，使得两个数之和为给定的整数。
保证肯定仅有一个结果。
例如，列表[1,2,5,4]与目标整数3，1+2=3，结果为(0, 1).
https://leetcode.com/problems/two-sum/?tab=Description
'''
'''
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
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
nums=list(range(1000))
random.shuffle(nums)
# li1=copy.deepcopy(nums)
# li2=copy.deepcopy(nums)
li3=copy.deepcopy(nums)
# li4=copy.deepcopy(nums)
li5=copy.deepcopy(nums)

# 方法1
@call_time
def twoSum1(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in nums:
        if target-i in nums[nums.index(i)+1:]:
            # print i
            return (i,target-i),[nums.index(i),nums.index(target-i)]
#方法2
@call_time
def twoSum2(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return (nums[i],nums[j]),[i,j]

#方法3 值_下标列表法
@call_time
def value_index(nums, target):
    # 先建立原表的最大值两倍下标的列表，这样可以保证不报越界错误，IndexError: list index out of range
    # 因为是两数的和，max*2应该是最大的和，大于target。
    # 保证nums_index[target-nums[i]]不越界。
    nums_index=['N' for i in range(max(nums)*2+1)]
    # print nums_index
    for i in range(len(nums)):
        # 1，把nums列表中的值，做为nums_index列表的下标，
        # 2，把nums列表中的下标，做为nums_index列表的值，
        nums_index[nums[i]]=i
        #前n1+后n2=target，开始，当i指向n1时，target-nums[i]=n2,这时nums_index[n2]是N，
        #只有，当nums[i]=n2时，i指向n2，target-nums[i]=n1,这时nums_index[n1]不是n，有返回。
        if nums_index[target-nums[i]]!='N' and target-nums[i]!=nums[i] :
            #当target是其中一个值的两倍的时候，不能重复指向这个值，因此target-nums[i]!=nums[i]
            #比如nums=[9,5,1],target=10,正确的是输出[0,2]，不是[1,1]
            # 因此target-nums[i]!=nums[i]
            # 当i指向9时，nums_index[9]=0，这时，nums_index[10-9]='N'，无返回
            # 当i指向1时，nums_index[1]=2，这时，nums_index[10-1]=0，有返回。
            return (target-nums[i],nums[i]),[nums_index[target-nums[i]],nums_index[nums[i]]]

#方法4 二分查找
@call_time
def twoSum4(nums, target):
    #1，先深度拷贝，把拷贝的排序
    nums_cp=copy.deepcopy(nums)
    nums_cp.sort()
    # 2，对target-i进行二分查找
    for i in range(len(nums_cp)):
        v=target-nums_cp[i]
        low=i+1
        high=len(nums_cp)-1
        while low<=high:#二分查找不能用for，因为low和high碰到一起才找到，区间在不断变化。
            # print low,high
            mid=(low+high)/2
            if nums_cp[mid]==v:
                # print nums_cp[i],nums_cp[mid]
                return (nums_cp[i],nums_cp[mid]),[nums.index(nums_cp[i]),nums.index(nums_cp[mid])]
            elif nums_cp[mid]>v:
                high=mid-1
            else:
                low=mid+1

#方法5 字典下标 和方法3值_下标列表法几乎一样，这个更经典，不用什么max
@call_time
def value_key(nums,target):
    #1,建立nums的值-下标：key-value字典
    dict_list={}
    for i,v in enumerate(nums):
        dict_list[v]=i
        # print dict_list
        try:#一定要处理异常，因为当建立dict_list[v]=i时，
            # dict_list[target - v]不存在，会报keyerr，但这其实不是错误，到了后面就会建立
            if dict_list[target - v]and (target-v)!=v:
                #跟方法3一样，target - v一定在v的前面
                return (target - v,v),[dict_list[target - v],dict_list[v]]
        except Exception :
            # print e
            continue

# print nums
target=8989
# print target
# print twoSum1(li1,target)
# print twoSum2(li2,target)

# print twoSum4(li4,target)
print value_key(li5,target)
print value_index(li3,target)
'''
一百万数据量比较
88
普通方法1：time cost: twoSum1         88.5279998779
            ((83, 5), [791, 37086])
普通方法2：time cost: twoSum2         140.631000042
            ((83, 5), [791, 37086])
值-下标法：time cost: value_index     0.276000022888
（建表）     ((83, 5), [791, 37086])
二分法：   time cost: twoSum4         2.79699993134
            ((0, 88), [519042, 867805])
值-键法：  time cost: value_key       0.0410001277924
 （建字典）   ((83, 5), [791, 37086])

胜出的是：value_key  value_index

一千万数据量比较：

time cost: value_index 3.18600010872
((22, 66), [97044, 539462])
time cost: value_key 2.54600000381
((22, 66), [97044, 539462])

time cost: value_index 2.93600010872
((1887, 7001), [77664, 111444])
time cost: value_key 1.85099983215
((1887, 7001), [77664, 111444])

time cost: value_key 2.07699990273
((5710, 3279), [68298, 181217])
time cost: value_index 3.06399989128
((5710, 3279), [68298, 181217])


最终胜出的是值做键法：

这种把值做为列表下标或字典的key，把原表的下标做为值的方法，使得算法的复杂度为O(logn).

'''