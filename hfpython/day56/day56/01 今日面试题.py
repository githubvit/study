
from functools import wraps


def wrapper(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print("start")
        ret = func(*args, **kwargs)
        print("end")
        return ret
    return inner

@wrapper
def f(*args, **kwargs):
    """
    这是一个测试装饰器的函数，没什么其他的用法
    :param args:
    :param kwargs:
    :return:
    """
    print("2018-06-04")

# 每次调用f的时候 在打印"2018-06-04" 之前打印一句 开始， 之后再打印一句 结束


f()  # inner()
print(f.__doc__)
print(f.__name__)


# 装饰器的相关知识点
# 1.装饰器的原理及为什么要用装饰器
# 2. 装饰器的基本用法
# 3. 带参数的装饰器
# 4. 被装饰的函数有返回值怎么处理
# 5. 多个装饰器的执行顺序
# 6. 装饰类的装饰器
