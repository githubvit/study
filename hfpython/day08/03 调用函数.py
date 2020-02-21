#函数的使用必须遵循：先定义，后调用的原则
#注意：没事先定义函数而直接调用，就相当于在引用一个不存在的变量名

#定义阶段：在定义阶段只检测语法，不执行函数体代码
#调用阶段：根据函数名找到函数的内存地址，然后执行函数体代码

# def func():
#     xxx
    # print('sadfsadf'



#函数名加括号即调用函数
# def bar():
#     print('from bar')
#
# def foo():
#     print('from foo')
#     bar()
#
# foo()





# #定义阶段
# def foo():
#     print('from foo')
#     bar()
#
# def bar():
#     print('from bar')
#
# #调用阶段
# foo()



# #定义阶段
# def foo():
#     print('from foo')
#     bar()
#
# #调用阶段
# foo()
#
# def bar():
#     print('from bar')


# 调用函数的三种形式
#1、
# def func():
#     print('from func')
#
# func()


#2、
# def max2(x,y):
#     if x > y:
#         return x
#     else:
#         return y
#
# res=max2(10,3)
# print(res)

#3、

def max2(x,y):
    if x > y:
        return x
    else:
        return y

# res=max2(10,3)*100
# print(res)

#4、

res=max2(max2(10,3),11)
print(res)