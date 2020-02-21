#什么时候应该有返回值：
#函数体代码运行完毕后需要有一个返回结果给调用者

#返回值有三种形式:

#1 没有return，返回值None
# def func():
#     pass
#
# res=func()
# print(res)

#2 return后跟一个值,返回该值本身
# def func1():
#     return 1
#
# res=func1()
# print(res)

#3 return可以逗号分隔，返回多个值,会返回一个元组给调用者
# def func2():
#     return 1,2,[1,2,3]
#
# res=func2()
# print(res)


# return注意点：
#1、return返回值的值，没有类型限制
#2、return是函数结束的标志，函数内可以写多个return，但
#执行一次，函数就立刻结束，并把return后的值作为本次调用的返回值

def func3():
    print('first')
    return 1
    print('second')
    return 2
    print('third')
    return 3

res=func3()
print(res)
