# 三 描述符分两种
# 1. 数据描述符:至少实现了__get__()和__set__()
class Foo:
     def __set__(self, instance, value):
         print('set')
     def __get__(self, instance, owner):
         print('get')

# 2. 非数据描述符:没有实现__set__()
class Foo:
    def __get__(self, instance, owner):
         print('get')

# 四 注意事项
# 1. 描述符本身应该定义成新式类,被代理的类也应该是新式类
# 2. 必须把描述符定义成这个类的类属性，不能为定义到构造函数中
# 3. 要严格遵循该优先级,优先级由高到底分别是
#   3.1.类属性
#   3.2.数据描述符
#   3.3.实例属性
#   3.4.非数据描述符
#   3.5.找不到的属性触发__getattr__()

# (1) 数据描述符>实例
class Foo:
    def __set__(self, instance, value):
        print('set')
    def __get__(self, instance, owner):
        print('get')
class Room:
    name=Foo()
    def __init__(self,name,width,length):
        self.name=name
        self.width=width
        self.length=length


#name是一个数据描述符,因为name=Foo()而Foo实现了get和set方法,因而比实例属性有更高的优先级
#对实例的属性操作,触发的都是描述符的
r1=Room('厕所',1,1)
r1.name
r1.name='厨房'

# (2) 实例>非数据描述符
class Foo:
    def __get__(self, instance, owner):
        print('get')
class Room:
    name=Foo()
    def __init__(self,name,width,length):
        self.name=name
        self.width=width
        self.length=length


#name是一个非数据描述符,因为name=Foo()而Foo没有实现set方法,因而比实例属性有更低的优先级
#对实例的属性操作,触发的都是实例自己的
r1=Room('厕所',1,1)
print(r1.name)
r1.name='厨房'
print(r1.name)

# (3) 非数据描述符>找不到 触发__getattr__()

class Foo:
    def func(self):
        print('我胡汉三又回来了')

    def __getattr__(self, item):
        print('找不到%s了当然是来找我啦'%item)
f1=Foo()

f1.xxxxxxxxxxx