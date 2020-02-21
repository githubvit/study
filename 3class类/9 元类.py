# 一 exec 
# 执行字符串内代码 方法

# code="""
# global x
# x=0
# y=2
# """
# global_dic={'x':100000}
# local_dic={}
# 全局名称空间和局部名称空间
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
# 二  元类

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
# 2 元类：类的类就是元类，
#我们用class定义的类使用来产生我们自己的对象的
#内置元类type是用来专门产生class定义的类的

# class Foo: #Foo=type(...)
#     pass

# print(type(Foo))
# f=Foo
#
# l=[Foo,]
# print(l)

#3、用内置的元类type，来实例化得到我们的类
#  创建类 OldboyTeacher
# type()实例化类需要三个参数
# type(class_name,class_bases,class_dic)
#   1. 类名         class_name='OldboyTeacher'
#   2. 基类们        class_bases=(object,)
#   3. 类的名称空间   class_dic，而类的名称空间是执行类体代码得到的
    
# class_name='OldboyTeacher'

# class_bases=(object,)

# class_body='''
# school='oldboy'
# def __init__(self,name,age):
#     self.name=name
#     self.age=age
# def say(self):
#     print('%s says welcome to the oldboy to learn python'%(self.name))
# '''
# class_dic={}
# # 执行函数体，把变量和函数名都放入名称空间
# exec(class_body,{},class_dic)
# print(class_dic)
# # 得到OldboyTeacher类
# OldboyTeacher=type(class_name,class_bases,class_dic)

# # print (OldboyTeacher.__dict__)

# # 实例化该类
# teacher1=OldboyTeacher('egon',18)
# # 调用该类下的方法
# teacher1.say()

# 例2 创建类 Chinese
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

# 4、类的三大要素
# print(class_name,class_bases,class_dic)

# Chinese=type(class_name,class_bases,class_dic)
# print(Chinese)

# p=Chinese('egon',18,'male')
# print(p.name,p.age,p.sex)


#5、储备知识__call__
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


# 三 自定义元类：控制类对象的创建

class Mymeta(type):
    # 来控制类Foo的创建
    def __init__(self,class_name,class_bases,class_dic): #self=Foo
        # print(class_name)
        # print(class_bases)
        # print(class_dic)
        if not class_name.istitle():
            raise TypeError('类名的首字母必须大写傻叉')

        if not class_dic.get('__doc__'):
            raise TypeError('类中必须写好文档注释，大傻叉')

        super(Mymeta,self).__init__(class_name,class_bases,class_dic)

    # 控制类Foo的调用过程，即控制实例化Foo的过程
    def __call__(self, *args, **kwargs): #self=Foo,args=(1111,) kwargs={}
        # print(self)
        # print(args)
        # print(kwargs)

        #1 造一个空对象obj
        obj=object.__new__(self)

        #2、调用Foo.__init__,
        # 将obj连同调用Foo括号内的参数一同传给__init__
        self.__init__(obj,*args,**kwargs)

        return obj



#Foo=Mymeta('Foo',(object,),class_dic)
class Foo(object,metaclass=Mymeta):
    """
    文档注释
    """
    x=1
    def __init__(self,y):
        self.Y=y

    def f1(self):
        print('from f1')

print (type(Foo))# <class '__main__.Mymeta'>就不是type了。
# obj=Foo(1111) #Foo.__call__()

# print(obj)
# print(obj.y)
# print(obj.f1)
# print(obj.x)





# 四 单例模式 对于相同的内容可以节约空间

# import settings

#方式一:定义一个类方法实现单例模式
# class MySQL:
#     __instance=None
#     def __init__(self,ip,port):
#         self.ip=ip
#         self.port=port

#     @classmethod
#     def singleton(cls):
#         if not cls.__instance:
#             obj=cls(settings.IP, settings.PORT)
#             cls.__instance=obj
#         return cls.__instance

# obj1=MySQL('1.1.1.2',3306)
# obj2=MySQL('1.1.1.3',3307)
# obj3=MySQL('1.1.1.4',3308)

# # obj4=MySQL(settings.IP,settings.PORT)
# # print(obj4.ip,obj4.port)

# obj4=MySQL.singleton()
# obj5=MySQL.singleton()
# obj6=MySQL.singleton()

# print(obj4 is obj5 is obj6)

#方式二：定制元类实现单例模式
import settings

class Mymeta(type):
    def __init__(self,name,bases,dic): #定义类Mysql时就触发

        # 事先先从配置文件中取配置来造一个Mysql的实例出来
        self.__instance = object.__new__(self)  # 产生对象
        self.__init__(self.__instance, settings.HOST, settings.PORT)  # 初始化对象
        # 上述两步可以合成下面一步
        # self.__instance=super().__call__(*args,**kwargs)


        super().__init__(name,bases,dic)

    def __call__(self, *args, **kwargs): #Mysql(...)时触发
        if args or kwargs: # args或kwargs内有值
            obj=object.__new__(self)
            self.__init__(obj,*args,**kwargs)
            return obj

        return self.__instance




class Mysql(metaclass=Mymeta):
    def __init__(self,host,port):
        self.host=host
        self.port=port



obj1=Mysql() # 没有传值则默认从配置文件中读配置来实例化，所有的实例应该指向一个内存地址
obj2=Mysql()
obj3=Mysql()

print(obj1 is obj2 is obj3)

obj4=Mysql('1.1.1.4',3307)



#方式三:定义一个装饰器实现单例模式
# import settings

# def singleton(cls): #cls=Mysql
#     _instance=cls(settings.HOST,settings.PORT)

#     def wrapper(*args,**kwargs):
#         if args or kwargs:
#             obj=cls(*args,**kwargs)
#             return obj
#         return _instance

#     return wrapper


# @singleton # Mysql=singleton(Mysql)
# class Mysql:
#     def __init__(self,host,port):
#         self.host=host
#         self.port=port

# obj1=Mysql()
# obj2=Mysql()
# obj3=Mysql()
# print(obj1 is obj2 is obj3) #True

# obj4=Mysql('1.1.1.3',3307)
# obj5=Mysql('1.1.1.4',3308)
# print(obj3 is obj4) #False