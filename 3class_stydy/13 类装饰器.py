# 放在类名上的装饰器 就是个函数，绑定类，在类定义时就装饰了，名字并无规定
# def decorate(cls):
#     print('类的装饰器开始运行啦------>')
#     return cls

# @decorate #无参:People=decorate(People)
# class People:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary

# p1=People('egon',18,3333.3)

# #有参:必须是key=value 因此是**kwargs
# def typeassert(**kwargs):
#     def decorate(cls):
#         print('类的装饰器开始运行啦------>',kwargs)
#         return cls
#     return decorate
# @typeassert(name=str,age=int,salary=float) 

# # 1.运行typeassert(...)返回结果是decorate,此时参数都传给kwargs 
# # 2.People=decorate(People)
# class People:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary

# p1=People('egon',18,3333.3)

# 描述符结合装饰器 达到实现类型限制功能 终极大招 牛逼！
class Typed:
    def __init__(self,name,expected_type):
        self.name=name
        self.expected_type=expected_type
    def __get__(self, instance, owner):
        print('get--->',instance,owner)
        if instance is None:
            return None
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print('set--->',instance,value)
        if not isinstance(value,self.expected_type):
            raise TypeError('Expected %s' %str(self.expected_type))
        instance.__dict__[self.name]=value
    def __delete__(self, instance):
        print('delete--->',instance)
        instance.__dict__.pop(self.name)

def typeassert(**kwargs):
    def decorate(cls):
        print('类的装饰器开始运行啦------>',kwargs)
        # 循环装饰器的参数键值对key=value
        for name,expected_type in kwargs.items():
            setattr(cls,name,Typed(name,expected_type))
        return cls
    return decorate
@typeassert(name=str,age=int,salary=float) #有参:1.运行typeassert(...)返回结果是decorate,此时参数都传给kwargs 2.People=decorate(People)
class People:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

# print(People.__dict__)
p1=People('egon',18,3333.3)
print (People.name,People.age,People.salary)
# None None None
print(p1.name,p1.age,p1.salary)
# egon 18 3333.3