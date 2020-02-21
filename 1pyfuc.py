# python 内置函数
# import os
# print(dir(os)) #看os有多少种方法
# print (divmod(10,3)) #10/3的商和余数组成的元组 (3, 1)

# li=['a','b','c','d']

# print(enumerate(li)) #给可迭代对象添加序号

# for index,value in enumerate(li):
#     print (index,value)

# #eval 将字符串形式的列表或字典转换回来 exec没有返回值
# # res=eval('[1,2,3]')
# res=eval("{'a':1,'b':[1,2,3]}")
# print(res,type(res)) # [1, 2, 3] <class 'list'>
# print(res['b'][1]) # 2



# 二.  堆排序
import heapq #该模块提供了堆排序算法的实现

# 1. 创建堆

# heapq有两种方式创建堆， 一种是使用一个空列表，
# 然后使用heapq.heappush()函数把值加入堆中，
# 另外一种就是使用heap.heapify(list)转换列表成为堆结构
# 第一种
"""
函数定义：
heapq.heappush(heap, item)
    - Push the value item onto the heap, maintaining the heap invariant.
heapq.heappop(heap)
    - Pop and return the smallest item from the heap, maintaining the heap invariant.
    If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].
"""
# nums = [2, 3, 5, 1, 54, 23, 132]
# heap = []
# for num in nums:
#     heapq.heappush(heap, num)  # 加入堆

# print(heap[0])  # 如果只是想获取最小值而不是弹出，使用heap[0]
# print([heapq.heappop(heap) for _ in range(len(nums))])  # 堆排序结果
# out: [1, 2, 3, 5, 23, 54, 132]


# 第二种
# nums = [2, 3, 5, 1, 54, 23, 132]
# heapq.heapify(nums)
# print([heapq.heappop(heap) for _ in range(len(nums))])  # 堆排序结果
# out: [1, 2, 3, 5, 23, 54, 132]

# heapq 模块还有一个heapq.merge(*iterables) 方法，
# 用于合并多个排序后的序列成一个排序后的序列， 返回排序后的值的迭代器。
# 类似于sorted(itertools.chain(*iterables))，但返回的是可迭代的。
"""
函数定义：
heapq.merge(*iterables)
    - Merge multiple sorted inputs into a single sorted output (for example, merge timestamped entries from multiple log files). Returns an iterator over the sorted values.
    - Similar to sorted(itertools.chain(*iterables)) but returns an iterable, does not pull the data into memory all at once, and assumes that each of the input streams is already sorted (smallest to largest).
"""

# num1 = [32, 3, 5, 34, 54, 23, 132]
# num2 = [23, 2, 12, 656, 324, 23, 54]
# num1 = sorted(num1)
# num2 = sorted(num2)

# res = heapq.merge(num1, num2)
# print(list(res))



# 2. 访问堆
# 堆创建好后，可以通过`heapq.heappop() 函数弹出堆中最小值。
nums = [2, 43, 45, 23, 12]
heapq.heapify(nums)
print(heapq.heappop(nums))
# out: 2

# 如果需要所有堆排序后的元素
# result = [heapq.heappop(nums) for _ in range(len(nums))]
# print(result)
# out: [12, 23, 43, 45]

# 如果需要删除堆中最小元素并加入一个元素，可以使用heapq.heaprepalce() 函数
# nums = [1, 2, 4, 5, 3]
# heapq.heapify(nums)
# heapq.heapreplace(nums, 23)
# print([heapq.heappop(nums) for _ in range(len(nums))])
# out: [2, 3, 4, 5, 23]


# 3. 获取堆最大或最小值
# 如果需要获取堆中最大或最小的范围值，
# 则可以使用heapq.nlargest() 或heapq.nsmallest() 函数
# """
# 函数定义：
# heapq.nlargest(n, iterable[, key])¶
#     - Return a list with the n largest elements from the dataset defined by iterable. 
#     - key if provided, specifies a function of one argument that is used to extract a comparison key from each element in the iterable: key=str.lower
#     - Equivalent to: sorted(iterable, key=key, reverse=True)[:n]
# """

# nums = [1, 3, 4, 5, 2]
# print(heapq.nlargest(3, nums))
# print(heapq.nsmallest(3, nums))

# """
# 输出：
# [5, 4, 3]
# [1, 2, 3]
# """


# 这两个函数还接受一个key参数，用于dict或其他数据结构类型使用
# import heapq
# from pprint import pprint
# portfolio = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
# cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
# expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
# pprint(cheap)
# pprint(expensive)

# """
# 输出：
# [{'name': 'YHOO', 'price': 16.35, 'shares': 45},
#  {'name': 'FB', 'price': 21.09, 'shares': 200},
#  {'name': 'HPQ', 'price': 31.75, 'shares': 35}]
# [{'name': 'AAPL', 'price': 543.22, 'shares': 50},
#  {'name': 'ACME', 'price': 115.65, 'shares': 75},
#  {'name': 'IBM', 'price': 91.1, 'shares': 100}]
# """


#  三.   双向队列 deque
from collections import deque
d=deque()
# 1 左、右增加元素
# append(往右边添加一个元素)
# appendleft（往左边添加一个元素）
# d.append(1)
# d.appendleft(2)
# print(d) #deque([2, 1])

# 2 左、右扩展列表
# extend(从队列右边扩展一个列表的元素)
# extendleft(从队列左边扩展一个列表的元素)

# d.append(1)
# d.extend([3,4,5])
# print(d) # deque([1, 3, 4, 5])

# d.append(1)
# d.extendleft([3,4,5])
# print(d)#deque([5, 4, 3, 1])

# 3 pop（获取最右边一个元素，并在队列中删除）
# d.extend(['a','b','c','d','e'])
# x = d.pop()
# print(x,d)#e deque(['a', 'b', 'c', 'd'])

# 4 popleft（获取最左边一个元素，并在队列中删除）
# d.extend(['a','b','c','d','e'])
# x = d.popleft()
# print(x,d) # a deque(['b', 'c', 'd', 'e'])

# 5 rotate（把右边元素放到左边）
# d.extend(['a','b','c','d','e'])
# d.rotate(2)   #指定次数，默认1次
# print(d) #deque(['d', 'e', 'a', 'b', 'c'])
