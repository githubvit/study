#1、函数的嵌套调用：在函数内又调用了其他函数
# def max2(x,y):
#     if x > y:
#         return x
#     else:
#         return y
#
# def max3(x,y,z):
#     res1=max2(x,y)
#     res2=max2(res1,z)
#     return res2
#
# print(max3(11,199,2))


#2、函数的嵌套定义：在函数内又定义其他函数
# def func1():
#     print('from func1')
#     def func2(): #func2=内存地址
#         print('from func2')
#
#     print(func2) #<function func1.<locals>.func2 at 0x0000024907A098C8>
#     func2()
#     func2()
#     func2()
#
# func1()

# print(func2)



def f1():
    print('f1')
    def f2():
        print('f2')
        def f3():
            print('f3')
        f3()
    f2()
f1()

'''
f1
f2
f3
'''