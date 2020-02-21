# 描述符是可以实现大部分python类特性中的底层魔法,
# 包括@classmethod,@staticmethd,@property甚至是__slots__属性

# 描述符是很多高级库和框架的重要工具之一,
# 描述符通常是使用到装饰器或者元类的大型框架中的一个组件.

# 1 回顾property 把方法当静态属性

# class Room:
#     def __init__(self,name,width,length):
#         self.name=name
#         self.width=width
#         self.length=length

#     @property
#     def area(self):
#         return self.width * self.length

# r1=Room('alex',1,1)
# print(r1.area)

# 2 自定制 
# class Lazyproperty:
#     def __init__(self,func):
#         self.func=func
#         print('描述符初始化。。')
#     def __get__(self, instance, owner): #用__get__方法做装饰器，装饰类中的函数
#         if instance is None:
#             return None
        
#         print('这是我们自己定制的静态属性,r1.area实际是要执行r1.area()')
#         return self.func(instance) #此时你应该明白,到底是谁在为你做自动传递self的事情

# class Room:
#     def __init__(self,name,width,length):
#         self.name=name
#         self.width=width
#         self.length=length

#     @Lazyproperty 
#     #area=Lazyproperty(area) 相当于定义了一个类属性,即描述符
#     # 在Room类定义阶段 就完成了描述符对象Lazyproperty(area) 的初始化
#     def area(self):
#         return self.width * self.length

# r1=Room('alex',2,3)
# print(Room.area)
# print(r1.area)

# 3 加缓存功能
# class Lazyproperty:
#     def __init__(self,func):
#         self.func=func
#     def __get__(self, instance, owner):
        
#         if instance is None:
#             return None
#         else:
#             print('这是我们自己定制的静态属性,r1.area实际是要执行r1.area()')
#             print('--->')
#             value=self.func(instance)
#             setattr(instance,self.func.__name__,value) #计算一次就缓存到实例的属性字典中
#             return value

# class Room:
#     def __init__(self,name,width,length):
#         self.name=name
#         self.width=width
#         self.length=length

#     @Lazyproperty #area=Lazyproperty(area) 相当于'定义了一个类属性,即描述符'
#     def area(self):
#         return self.width * self.length

# r1=Room('alex',1,1)
# print(r1.__dict__)#{'name': 'alex', 'width': 1, 'length': 1}
# print(r1.area) #先从自己的属性字典找,没有再去类的中找,然后触发了area的__get__方法，将结果缓存。
# print(r1.__dict__)#{'name': 'alex', 'width': 1, 'length': 1, 'area': 1}
# print(r1.area) #先从自己的属性字典找,找到了,是上次计算的结果,这样就不用每执行一次都去计算

# 4 如果加上set方法，就会导致缓存无用
# 因为加上set方法，就变成了数据描述符，而数据描述符>实例，
# 就不会先从自己的属性字典找，都是从描述符开始查找，因此就没法使用缓存了。
class Lazyproperty:
    def __init__(self,func):
        self.func=func
    def __get__(self, instance, owner):
        print('这是我们自己定制的静态属性,r1.area实际是要执行r1.area()')
        if instance is None:
            return None
        else:
            value=self.func(instance)
            instance.__dict__[self.func.__name__]=value
            return value
        
    def __set__(self, instance, value):
        print('hahahahahah')

class Room:
    def __init__(self,name,width,length):
        self.name=name
        self.width=width
        self.length=length

    @Lazyproperty #area=Lazyproperty(area) 相当于定义了一个类属性,即描述符
    def area(self):
        return self.width * self.length

print(Room.__dict__)

r1=Room('alex',1,1)
print(r1.__dict__)
print(r1.area)
print(r1.__dict__)
print(r1.area) 
print(r1.area) 
print(r1.area) 
#缓存功能失效,每次都去找描述符了,
# 为何,因为描述符实现了set方法,
# 它由非数据描述符变成了数据描述符,
# 数据描述符比实例属性有更高的优先级,
# 因而所有的属性操作都先去找描述符了