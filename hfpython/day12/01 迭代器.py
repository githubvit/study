#1、什么是迭代？：迭代是一个重复的过程，并且每次重复都是基于上一次的结果而来
# while True:
#     print('=------->')


# l=["a","b","c","d"]
# n=0
# while n < len(l):
#     print(l[n])
#     n+=1

# d={'x':1,'y':2}
# for item in d.items():
#     print(item)


#2、要想了解迭代器到底是什么？必须先了解一个概念，即什么是可迭代的对象？
#可迭代的对象:在python中，但凡内置有__iter__方法的对象，都是可迭代的对象
# num=1

#以下都是可迭代的对象
# str1='hello'
# list1=[1,2,3]
# tup1=(1,2,3)
# dic={'x':1}
# s1={'a','b','c'}
# f=open('a.txt','w',encoding='utf-8')



## 3、迭代器：迭代取值工具，可迭代的对象执行__iter__方法得到的返回值就是迭代器对象
dic={'x':1,'y':2,'z':3}
iter_dic=dic.__iter__()
print(iter_dic.__next__())
print(iter_dic.__next__())
print(iter_dic.__next__())
print(iter_dic.__next__())

# s1={'a','b','c'}
# iter_s1=s1.__iter__()
# print(iter_s1.__next__())
# print(iter_s1.__next__())
# print(iter_s1.__next__())
# print(iter_s1.__next__())

# list1=[1,2,3]
# iter_list1=list1.__iter__()
# print(iter_list1.__next__())
# print(iter_list1.__next__())
# print(iter_list1.__next__())


#4、可迭代的对象vs迭代器对象？
'''
可迭代的对象：str，list，tuple，dict，set，file
1、获取可迭代对象的方式：无须获取，python内置str，list，tuple，dict，set，file都是可迭代对象
2、特点：
    内置有__iter__方法的都叫可迭代的对象，执行该方法会拿到一个迭代器对象

 迭代器对象：文件对象本身就是迭代器对象
1、获取迭代器对象的方式：
    执行可迭代对象的__iter__方法，拿到的返回值就是迭代器对象
2、特点：
    内置有__next__方法，执行该方法会拿到迭代器对象中的一个值
    内置有__iter__方法，执行该方法会拿到迭代器本身

'''

# x='hello'

# iter_x=x.__iter__()
# iter_x.__next__
# print(iter_x.__iter__().__iter__().__iter__().__iter__() is iter_x)


# 文件本身就是迭代器对象
# str1='hello'
# list1=[1,2,3]
# tup1=(1,2,3)
# dic={'x':1}
# s1={'a','b','c'}
# f=open('a.txt','w',encoding='utf-8')
# f.__next__()


#5、迭代器的优缺点分析
#5.1 迭代器的优点：
#5.1.1、提供了一种可不依赖于索引的取值方式
# l=open('a.txt','r',encoding='utf-8')
# iter_l=l.__iter__()
# while True:
#     try:
#         print(iter_l.__next__())
#     except StopIteration:
#         break

# l=[1,2,3,4,4,5,5,6,6,6,6,6,6,6,6,6]
# iter_l=l.__iter__()
# print(iter_l)
# print(iter_l.__next__())
# f=open('a.txt')

#5.1.2 迭代器更加节省内存
# item=range(0,100000000000000000000000000000000000000000000)
# print(item)


#5.2迭代器的缺点：
#5.2.1、取值麻烦，只能一个一个取，只能往后取，
#5.2.2、并且是一次性的,无法用len获取长度

# x=[1,2,3]
# iter_x=x.__iter__()
# while True:
#     try:
#         print(iter_x.__next__())
#     except StopIteration:
#         break
# print('第二次=================================》')
# iter_x=x.__iter__()
# while True:
#     try:
#         print(iter_x.__next__())
#     except StopIteration:
#         break

#6. for循环原理分析：
#6.1、for 循环称之为迭代器循环，in后跟的必须是可迭代的对象
#6.2、for循环会执行in后对象的__iter__方法，拿到迭代器对象
#6.3、然后调用迭代器对象的__next__方法，拿到一个返回值赋值给line，执行一次循环体
#6.4、周而复始，直到取值完毕，for循环会检测到异常自动结束循环
# l=open('a.txt','r',encoding='utf-8')
# for line in l: #iter_l=l.__iter__()
#     print(line)

# for item in {'x':1,'y':2}:
#     print(item)


