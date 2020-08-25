# 一 描述符的定义：
# 描述符本质就是一个新式类,在这个新式类中,至少实现了__get__(),__set__(),__delete__()中的一个,这也被称为描述符协议
# __get__():调用一个属性时,触发
# __set__():为一个属性赋值时,触发
# __delete__():采用del删除属性时,触发

#描述符Str
class Str:
    def __get__(self, instance, owner):
        print('Str调用',instance,owner)
    def __set__(self, instance, value):
        print('Str设置...',instance, value)
    def __delete__(self, instance):
        print('Str删除...')

#描述符Int
class Int:
    def __get__(self, instance, owner):
        print('Int调用')
    def __set__(self, instance, value):
        print('Int设置...')
    def __delete__(self, instance):
        print('Int删除...')

# 二 描述符Str的使用

#何地？：定义成另外一个类的类属性

#何时？：且看下列演示

class People:
    name=Str() #定义成str描述符对象
    age=Int()
    def __init__(self,n,a): #name被Str类代理,age被Int类代理,
        self.name=n #设置时就会执行描述符的_set_()方法
        self.age=a

p1=People('alex',18)
# Str设置... <__main__.People object at 0x0000022C2A893408> alex
# Int设置...


# #描述符Str的使用
# p1.name         #Str调用 <__main__.People object at 0x000001E94CBA14C8> <class '__main__.People'>
# p1.name='egon'  #Str设置...  <__main__.People object at 0x000001E94CBA14C8> egon 
# del p1.name
print(p1.name,p1.age) # None None
print(People.name,People.age) # None None
# #描述符Int的使用
# p1.age
# p1.age=18
# del p1.age

# #我们来瞅瞅到底发生了什么
print(p1.__dict__)
#对象的名称空间为空 {} 里面的参数被类属性描述符代理了，所以为空
# print(People.__dict__)
#类的名称空间多了两个对象：即类属性描述符对象
# {'name': <__main__.Str object at 0x0000018A547980C8>, 
# 'age': <__main__.Int object at 0x0000018A54798108>,}

#基于上面的演示,我们已经知道,在一个类中定义描述符它就是一个类属性,
# 存在于类的属性字典中,而不是实例的属性字典

# #补充
# print(type(p1) == People) 
#type(obj)其实是查看obj是由哪个类实例化来的
# print(type(p1).__dict__ == People.__dict__)

# print(People.name)#Str调用 None 调用了描述符的__get__
# People.name='egon'#更改了类的name属性，覆盖掉了描述符
# print(People.name)# 已经不会再调用描述符的__get__方法了。