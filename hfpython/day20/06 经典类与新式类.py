'''
1、新式类：
    继承object的类，以及该类的子类，都是新式类

    在python3中，如果一个类没有指定继承的父类，默认就继承object
    所以说python3中所有的类都是新式类

2、经典类(只有在python2才区分经典类与新式类)：
    没有继承object的类，以及该类的子类，都是经典类
'''

# print(object)

class Foo(object):
    pass

class Bar(Foo):
    pass

# print(Foo.__bases__)
print(Bar.__bases__)
