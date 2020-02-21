#_*_coding:utf-8_*_


class A(object):#父类 如果没有（object），就是经典类，那么在py2.7中继承就是深度优先，也就是说B过后就是A,A没有才是C。py3.x都是广度优先
    def __init__(self):
        print ('A')
    # pass

class B(A):
    pass
    # def __init__(self):
    #     print ('B')

class C(A):#新式类，广度优先。也就是说B过后就是从C。
    # pass
    def __init__(self):
        print ('C')

class D(B,C):#多继承，从左至右，只有1次初始化。
    pass


s=D() #实例化D
# 查看一个类型的父类，使用它的__bases__属性可以查看
print (D.__bases__)
print (D.__class__)