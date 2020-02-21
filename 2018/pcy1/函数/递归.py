#_*_coding:utf-8_*_
'''
递归特性:

1. 必须有一个明确的结束条件

2. 每次进入更深一层递归时，问题规模相比上次递归都应有所减少

3.有return和没有return的递归
 return 自己( ) 单边步进，因为return就关闭了上层，直接运行下层，运行一层就丢弃。运行过程就像台阶一步一步走下来，取名-台阶递归
 自己( ) 逐层回归，从最外面开始运行，从最里面逐层结束。运行过程像鸟的翅膀，双翼展开，取名-大雁递归
'''
def sumTree(aList):
	tot=0
	for item in aList:
		if not isinstance(item,list):#isinstance用来判断item是不是列表类型
			tot+=item
		else:
			tot+=sumTree(item)
	return tot
'''
第一层
[1,[2,[3],4],5]
1, 1 not  tot 0+1=1
2,[2,[3],4] else  tot 1+
                        第二层
                       ([2,[3],4]
                        1,2  not  tot 0+2=2
                        2,[3] else tot 2+
                                        第三层
                                        ([3]    
                                         1,3  not  tot 0+3=3
                                         return 3)
                            tot=5 
                        3,4  not  tot  5+4=9
                        return 9)
    tot=10
3, 5 not  tot 10+5=15
return 15
'''

# a=[1,[2,[3,[4,[5,6],7],8],9],10]
b=[1,[2,[3],4],5]
sumTree(b)