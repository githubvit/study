#1、闭包函数


#闭：指的是定义在函数内部的函数
#！！！作用域关系 在函数定义阶段就规定死了，与调用位置无关
# def outter():
#     x=2
#     def inner():
#         # x=1
#         print('from inner',x)
#
#     return inner
#
#
# f=outter() #f=inner
# # print(f)
# # x=1111111111111111111
# # f()
#
#
# def foo():
#     x=1111111111111111111111111111
#     f()
#
# foo()

#闭包函数：
#1、定义在函数内部的函数
#2、 并且该函数包含对外部函数作用域中名字的引用，该函数就称为闭包函数

# def outter():
#     name='egon'
#     def inner():
#         print('my name is %s' %name)
#
#     return inner
#
#
# f=outter()
#




#了解：
# 为函数体传值的方式
#方式一：将值以参数的形式的传入
# import requests
#
# def get(url):
#     response=requests.get(url)
#     if response.status_code == 200:
#         print(response.text)
#
#
# get('https://www.baidu.com')


#方式二：


import requests
import time

# def outter(url): #url='https://www.baidu.com'
#
#     # url='https://www.baidu.com'
#     def get():
#         response=requests.get(url)
#         if response.status_code == 200:
#             print(response.text)
#
#     return get
#
#
#
# baidu=outter('https://www.baidu.com')
# python=outter('https://www.python.org')

# baidu()
# print('=====================>')
# time.sleep(3)
#
# baidu()









def outter(x):
    # x=1
    def foo():
        print(x)
    return foo



f_10=outter(10)

f_10()


f_100=outter(100)
f_100()