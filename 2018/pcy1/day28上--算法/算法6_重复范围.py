#_*_coding:utf-8_*_
'''
经典语句：程序就是算法加数据结构。
算法（Algorithm）：一个计算机的计算过程，用来解决问题的方法
'''
'''
给定一个升序列表和一个整数，返回该整数在列表中的下标范围。
例如：列表[1,2,3,3,3,4,4,5]，若查找3，则返回(2,4)；若查找1，则返回(0,0)。
思路：
因为是有序，所以可以用二分查找找到3，
找到3后，定义左右两个指针，左指针左移，看是不是3，是就继续左移，直到不是就退出。
右指针同理，最后返回左右两指针，就得到了范围。
注意，指针不能越界

'''
def bin_serach_sum(olist,v):
    #初始化指针
    low=0
    high=len(olist)-1
    mid=(low+high)/2
    while low<=high:#每一轮low、high、mid都在变化，就是不断的折半
        #这里不能用while True，否则如果没有陷入死循环
        if v==olist[mid]:
            left= mid
            right=mid
            while left>=0 and olist[left]==v:
            #注意：这里定义范围不能用left>=low，right<=high
            # 初始的low和high已经变化了
                left-=1
            while right<=len(olist)-1 and olist[right]==v:
                right+=1
            return  (left+1,right-1)
        elif v>olist[mid]:#在右边，把low指针左移
            low=mid+1
            mid=(low+high)/2
            continue
        else:#在左边，把high指针右移
            high=mid-1
            mid = (low + high) / 2
            continue
    return #这里用return表示没找到，返回‘None'

li=[1,2,3,3,3,4,4,5]

print bin_serach_sum(li,1)

