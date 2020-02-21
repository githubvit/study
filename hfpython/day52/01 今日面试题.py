"""
SH Python全栈1期 每日面试题02

"""
# def extend_list(v, li=[]):  #
#     li.append(v)
#     return li
#
# list1 = extend_list(10)
# print(list1)
# list2 = extend_list(123, [])
# list3 = extend_list('a')
#
# print(list1)  # [10, 'a']
# print(list2)  # [123, ]
# print(list3)  # [10, 'a']
#
# print(list1 is list3)  # True
#
# # 第二题：问以下代码的输出结果是什么？
# list1 = ["a", "b", "c", "d", "e"]
# print(list1[10:])  # []
#
#
# # 第三题：如何打乱一个有序的列表？
# list4 = [11, 22, 33, 44, 55]
# import random
# random.shuffle(list4)
# print(list4)
# list4.sort()
# print(list4)
# 快速复制一个列表
list5 = [11, 22, [33, [44, 55]]]
# list6 = list5
# print(list6)
# list5[2][1][0] = 444
# print(list6)
list7 = list5[:]
print(list7)
list5[2][1][0] = 444
print(list7)
print(id(list7), id(list5))


# 直接赋值、拷贝、深拷贝、切片赋值
