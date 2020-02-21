#_*_coding:utf-8_*_
'''
依赖注入解决对象之间的依赖问题
'''
#解决类依赖注入
class Mapper(object):
    #1，建立类和依赖的字典
    __map_relation={}
    #2，类和依赖注册，cls就是类，value就是依赖的对象
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
        obj.__init__(*arg_list,**kwargs)
        return obj

class Test1(object):
    def t(self):
        print ('t')

class Foo(object):
    __metaclass__ = MyType
    def __init__(self,t):
        self.t=t
    def f(self):
        print ('f')

class Bar(object):
    __metaclass__ = MyType
    def __init__(self,f):
        self.f=f
    def b(self):
        print ('b')



#类、参数注册,对象依赖注入
Mapper.register(Foo,Test1())
Mapper.register(Bar,Foo())

#用Mapper注册后，就不用输入依赖对象
b=Bar()
print (b.f) #Foo对象 <__main__.Foo object at 0x0000000004A05160>
print (b.f.t)#Test1对象 <__main__.Test1 object at 0x0000000004B850B8>
b.b()
b.f.f()#b.f就是Foo对象，调用f方法，输出f
b.f.t.t()#b.f.t就是Test1对象，调用t方法，输出t