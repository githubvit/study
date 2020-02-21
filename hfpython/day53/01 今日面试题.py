"""
问:执行完下面的代码后,  l,m的内容分别是什么?
"""


# def func(m):
#     for k,v in m.items():
#         m[k+2] = v+2
#
#
# m = {1: 2, 3: 4}
# l = m  # 浅拷贝
# l[9] = 10
# func(l)
# m[7] = 8
#
#
# print("l:", l)
# print("m:", m)


# 在迭代一个列表或字典的时候，你不能修改列表或字典的大小！


# = 、 切片 、copy 、deepcopy

import copy

list1 = [11, 22, [33, 44]]
list2 = list1
list3 = list1[:]
list4 = copy.copy(list1)
list5 = copy.deepcopy(list1)

list1[2].append(55)
print("list2:",list2)  # [11, 22, [33, 44, 55]]
# 注释内容
# TODO： 这里没有考虑到
print("list3:",list3)  # [11, 22, [33, 44, 55]]
print("list4:",list4)  # [11, 22, [33, 44, 55]]
print("list5:",list5)  # [11, 22, [33, 44]]

"""
多行
注释
"""

def foo(name, age):
    """
    这个函数是干什么用的？
    :param name: 用户名，必须是字符串类型
    :param age:
    :return: None
    """
    print(name)
    print(age)


# join连接列表的元素

list_tmp = [11, 22, 33, 44]
# list_tmp2 = ["Alex", "DSB", "hehe", "haha"]
# ret = "".join(list_tmp2)
ret = ",".join([str(i) for i in list_tmp])
print(ret)


# python里面的三元运算
# 如果n > m，我就把n的值赋值给x,否则就把m的值赋值给x
n = 10
m = 5
x = n if n > m else m
print(x)
