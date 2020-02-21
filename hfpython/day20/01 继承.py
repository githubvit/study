'''
1、什么是继承？
    继承一种新建类的的方式，在python中支持一个儿子继承多个爹
    新建的类称为子类或者派生类，
    父类又可以称为基类或者超类

    子类会”遗传“父类的属性

2、为什么要用继承
    减少代码冗余

3、怎么用继承
'''
class ParentClass1:
    pass

class ParentClass2:
    pass

class Subclass1(ParentClass1):
    pass

class Subclass2(ParentClass1,ParentClass2):
    pass

# print(Subclass1.__bases__)
print(Subclass2.__bases__)



# 在python2中有经典类与新式类之分
# 在python3中全都为新式类
