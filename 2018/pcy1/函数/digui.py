#_*_coding:utf-8_*_

def merage_sort(low,high) :
    if low<high:
        # 分解
        mid=(low+high)//2
        # print mid
        # merage_sort(low,mid-1)
        # merage_sort(mid,high)#这样永远无法结束递归

        merage_sort(low,mid)
        merage_sort(mid+1,high)

        print mid

merage_sort(0,10)

'''
5 
     05 2 
   02      35 
     1       4
 01  22   34 55
   0       3
00 11      33 44

    6 10 8
 68   9 10
   7      9 
 67 88   99 1010
   6
 66 77  
 
 
0
1
3
4
2
6
7
9
8
5

 01        56
 02 34     57  89
 04        59
 09

'''