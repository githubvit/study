#_*_coding:utf-8_*_

'''
静态方法是不可以直接访问实例变量的，
可以通过类名来访问，包括私有变量。
其实相当于跟类本身已经没什么关系了，
它与类唯一的关联就是需要通过类名来调用这个方法
用静态方法实现依赖注入
'''

#
# class Dog(object):
#     __map_relation={'k':'v'}
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod  # 把eat方法变为静态方法
#     def eat(self):#这里的self可以是任意的，比如obj、a、b、c等等，
#         # 因为静态方法不能访问实例变量和类变量，与类无关
#         #可以访问私有变量
#         print (Dog.__map_relation['k'])
#         print("%s is eating" % self.name)
#
#
# d = Dog("ChenRonghua")
# # 调用时主动传递实例本身给eat方法，即d.eat(d)
# d.eat(d)


#解决类依赖注入
class Mapper(object):
    #1，建立类和依赖的字典
    __map_relation={}
    #2，类和依赖注册，cls就是类，value就是依赖
    @staticmethod
    def register(cls,value):
        Mapper.__map_relation[cls]=value
    #3，判断该类是否注册
    @staticmethod
    def exist(cls):
        if cls in Mapper.__map_relation:
            return True
        else:
            return False
    #4，取得类的依赖
    @staticmethod
    def value(cls):
        return Mapper.__map_relation[cls]

class MyType(type):
    def __call__(cls, *args, **kwargs):
        obj=cls.__new__(cls, *args, **kwargs)
        arg_list=list(args)
        if Mapper.exist(cls):
            value=Mapper.value(cls)
            arg_list.append(value)
            print (value)
        obj.__init__(*arg_list,**kwargs)
        return obj

class Foo(object):
    __metaclass__ = MyType
    def __init__(self,name):
        self.name=name
    def f1(self):
        print (self.name)

class Bar(object):
    __metaclass__ = MyType
    def __init__(self,name):
        self.name=name
    def f1(self):
        print (self.name)

# 没有Mapper这个类，建立Foo对象和Bar对象时，就必须有参数，init时要求：name
# f=Foo('23' )
# b=Bar('45' )

#类、参数注册
Mapper.register(Foo,'666')
Mapper.register(Bar,'999')
# print (type(Foo))
#用Mapper注册后，就不用输入参数
f=Foo('22')
b=Bar('YU' )

f.f1()
b.f1()

import abc