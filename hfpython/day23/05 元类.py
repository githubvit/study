# code="""
# global x
# x=0
# y=2
# """
# global_dic={'x':100000}
# local_dic={}
# exec(code,global_dic,local_dic)
#
# print(global_dic)
# print(local_dic)

#
# code="""
# x=1
# y=2
# def f1(self,a,b):
#     pass
# """
# local_dic={}
# exec(code,{},local_dic)
# print(local_dic)
#



#1、一切皆为对象：

# Chinese=type(...)
# class Chinese:
#     country="China"
#
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#
#     def speak(self):
#         print('%s speak Chinese' %self.name)
#
# print(Chinese)
# p=Chinese('egon',18,'male')
# print(type(p))

# print(type(Chinese))
# 元类：类的类就是元类，
#我们用class定义的类使用来产生我们自己的对象的
#内置元类type是用来专门产生class定义的类的

class Foo: #Foo=type(...)
    pass

# print(type(Foo))
# f=Foo
#
# l=[Foo,]
# print(l)

#2、用内置的元类type，来实例化得到我们的类
# class_name='Chinese'
# class_bases=(object,)
# class_body="""
# country="China"
# def __init__(self,name,age,sex):
#     self.name=name
#     self.age=age
#     self.sex=sex
# def speak(self):
#     print('%s speak Chinese' %self.name)
# """
# class_dic={}
# exec(class_body,{},class_dic)

# 类的三大要素
# print(class_name,class_bases,class_dic)

# Chinese=type(class_name,class_bases,class_dic)
# print(Chinese)

# p=Chinese('egon',18,'male')
# print(p.name,p.age,p.sex)


#3、储备知识__call__
# class Foo:
#     def __init__(self):
#         pass
#     def __str__(self):
#         return '123123'
#
#     def __del__(self):
#         pass
#
#     # 调用对象，则会自动触发对象下的绑定方法__call__的执行，
#     # 然后将对象本身当作第一个参数传给self，将调用对象时括号内的值
#     #传给*args与**kwargs
#     def __call__(self, *args, **kwargs):
#         print('__call__',args,kwargs)
#
#
# obj=Foo()
# # print(obj)
#
# obj(1,2,3,a=1,b=2,c=3) #


# #4 、自定义元类：
# class Mymeta(type):
#     # 来控制类Foo的创建
#     def __init__(self,class_name,class_bases,class_dic): #self=Foo
#         # print(class_name)
#         # print(class_bases)
#         # print(class_dic)
#         if not class_name.istitle():
#             raise TypeError('类名的首字母必须大写傻叉')
#
#         if not class_dic.get('__doc__'):
#             raise TypeError('类中必须写好文档注释，大傻叉')
#
#         super(Mymeta,self).__init__(class_name,class_bases,class_dic)
#
#     # 控制类Foo的调用过程，即控制实例化Foo的过程
#     def __call__(self, *args, **kwargs): #self=Foo,args=(1111,) kwargs={}
#         # print(self)
#         # print(args)
#         # print(kwargs)
#
#         #1 造一个空对象obj
#         obj=object.__new__(self)
#
#         #2、调用Foo.__init__,将obj连同调用Foo括号内的参数一同传给__init__
#         self.__init__(obj,*args,**kwargs)
#
#         return obj
#
#
#
# #Foo=Mymeta('Foo',(object,),class_dic)
# class Foo(object,metaclass=Mymeta):
#     """
#     文档注释
#     """
#     x=1
#     def __init__(self,y):
#         self.Y=y
#
#     def f1(self):
#         print('from f1')
#
#
# obj=Foo(1111) #Foo.__call__()
#
# # print(obj)
# # print(obj.y)
# # print(obj.f1)
# # print(obj.x)





# 单例模式
import settings

class MySQL:
    __instance=None
    def __init__(self,ip,port):
        self.ip=ip
        self.port=port

    @classmethod
    def singleton(cls):
        if not cls.__instance:
            obj=cls(settings.IP, settings.PORT)
            cls.__instance=obj
        return cls.__instance

obj1=MySQL('1.1.1.2',3306)
obj2=MySQL('1.1.1.3',3307)
obj3=MySQL('1.1.1.4',3308)

# obj4=MySQL(settings.IP,settings.PORT)
# print(obj4.ip,obj4.port)

obj4=MySQL.singleton()
obj5=MySQL.singleton()
obj6=MySQL.singleton()

print(obj4 is obj5 is obj6)

















