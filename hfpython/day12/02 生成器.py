
#生成器：
# 函数内包含有yield关键字，
# 再调用函数，就不会执行函数体代码，拿到的返回值就是一个生成器对象
def chicken():
    print('=====>first')
    yield 1
    print('=====>sencond')
    yield 2
    print('=====>third')
    yield 3


obj=chicken()
# print(obj)
# 生成器本质就是迭代器，也就是说生成器的玩法其实就是迭代器的玩法
# print(obj.__iter__() is obj)
# res=obj.__next__()
# print(res)
#
# res1=obj.__next__()
# print(res1)
#
# res2=obj.__next__()
# print(res2)
#
# obj.__next__()


# 1、iter_obj=obj.__iter__()，拿到迭代器
#2、出发iter_obj.__next__()，拿到该方法的返回值，赋值给item
#3、周而复始，直到函数内不在有yield，即取值完毕
#4、for会检测到StopIteration异常，结束循环
# for item in obj:
#     print(item)


#总结yield：
#1、为我们提供了一种自定义迭代器的方式，
#    可以在函数内用yield关键字，调用函数拿到的结果就是一个生成器，生成器就是迭代器
#2、yield可以像return一样用于返回值，区别是return只能返回一次值，而yield可返回多次
#    因为yield可以保存函数执行的状态

# def my_range():
#     print('start........')
#     n=0
#     while True:
#         yield n
#         n+=1

# obj=my_range()
# print(obj)

# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())

# for i in my_range():
#     print(i)


def my_range(start,stop,step=1):
    n=start
    while n < stop:
        yield n #yield 4
        n+=step #5


# obj=my_range(3,7,2) #3,5,
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())


for item in my_range(5,10,2):
    print(item)