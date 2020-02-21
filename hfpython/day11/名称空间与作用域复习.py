# x=0
# def f1():
#     x=1
#     def f2():
#         x=2
#         def f3():
#             x=3
#             def f4():
#                 x=4
#                 print(x)
#             f4()
#         f3()
#     f2()
# f1()



# def outter():
#     x = 1
#
#     def inner():
#         print(x)
#
#     return inner
#
#
# func = outter()  # func=inner
# x=1111111111111111
# func()




#为函数体传值的两种方式：
#方式一：直接为该函数添加相对应的参数

# def inner(name):
#     print(name)
#
#
# inner('egon')
# inner('egon')

#方式二：

# def outter(name):
#     # name='egon'
#     def inner():
#         print(name)
#     return inner

# f=outter('egon')  # f=inner
# f()
# f()

# f1=outter('alex')
# f1()
# f1()
# outter()()