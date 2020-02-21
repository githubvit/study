#_*_coding:utf-8_*_

# 1.命令 __doc__　　表示类的描述信息

# class Foo:
#     """ 描述类信息，__doc__"""
#
#     def func(self):
#         pass
#
#
# print (Foo.__doc__)


# --------------------------------------

#2.命令 __module__ 和  __class__
# 　__module__ 表示当前操作的对象在那个模块
# 　__class__  表示当前操作的对象的类是什么


# from lib.aa import C #从lib这个python包下的aa.py文件里引入class C这个类
# obj = C()
# print (obj.__module__ ) # 输出 lib.aa，即：输出模块
# print (obj.__class__  )    # 输出 lib.aa.C，即：输出类


# --------------------------------------

# 3，类方法定义__call__ 对象后面加括号（），触发执行。

# 注：构造方法的执行是由创建对象触发的，
# 即：对象 = 类名() ；
# 而对于 __call__ 方法的执行是由对象后加括号触发的，即：对象() 或者 类()()

# class Foo:
#     def __init__(self, *args, **kwargs):
#         print ('这是__init__方法')
#
#     def __call__(self, *args, **kwargs):
#         print ('这是__call__方法')
#
#
# obj = Foo(12345)  # 执行 __init__
# obj()  # 执行 __call__

# --------------------------------------


#4. 命令__dict__ 查看类内存或对象内存中的所有成员
#
# class Province:
#     country = 'China'
#
#     def __init__(self, name, count):
#         self.name = name
#         self.count = count
#
#     def func(self, *args, **kwargs):
#         print ('%s func'%self.name)
#
#
# # 获取类的成员，即：静态字段、方法、
# print (Province.__dict__)
# # 输出：{'country': 'China',
# #  '__module__': '__main__',
# #  'func': <function func at 0x10be30f50>,
# #  '__init__': <function __init__ at 0x10be30ed8>,
# # '__doc__': None}
#
# obj1 = Province('HeBei', 10000)
# print (obj1.__dict__)
# # 获取 对象obj1 的成员
# # 输出：{'count': 10000, 'name': 'HeBei'}
#
# obj2 = Province('HeNan', 3888)
# obj2.func()#这个方法不存在对象的内存中，因此obj2.__dict__不会出现该方法
# print (obj2.__dict__)
# 获取 对象obj2 的成员
# 输出：{'count': 3888, 'name': 'HeNan'}

# --------------------------------------


#5.类方法定义__str__，定义类的显示
# 如果一个类中定义了__str__方法，
# 那么在打印对象时，
# 默认输出该方法的返回值。
# class Foo:
#     def __str__(self):
#         return 'alex li'
#
#
# obj = Foo()
# print obj
# 输出：alex li

# --------------------------------------

# 6.类方法定义__getitem__、__setitem__、__delitem__

# 用于索引操作，如字典。以上分别表示获取、设置、删除数据，把一个类变成了字典。

# class Foo(object):#可以自己写一个类，封装字典，实例化，让用户以字典的形式调用。
#     def __init__(self):
#         self.__data={  #要封装字典要把该字典定义为私有变量，不然外部可以绕过进行修改
#             'name':'alex',
#             'age':22,
#             'sex':'M'
#         }
#     def show_dict(self):
#         print self.__data
#
#     def __getitem__(self, key):
#         print('__getitem__', key)
#         return self.__data.get(key)
#
#     def __setitem__(self, key, value):
#         print '你不能这样做'
#         # print('__setitem__', key, value)
#         # self.__data[key]=value
#
#     def __delitem__(self, key):
#         print '你无权删除'
#         # print('__delitem__', key)
#         # del self.__data[key] #如果不写就不会删除
#
#
#
# obj = Foo()
# print obj['name']
#
# obj.show_dict()
#
# obj['id']=123#这样是不能赋值的，会提示你不能这样做
# obj.data['id']=123 #如果没有将字典定义为私有变量，这样赋值就饶过了，直接对字典赋值。
# obj.show_dict()
# del obj['id'] #这样是不能删除的，会提示你无权删除
# del obj.data['id'] #如果没有将字典定义为私有变量，这样删除就饶过了，直接对字典删除。
# print obj.data
# # result = obj['k1']  # 自动触发执行 __getitem__
# # obj['k2'] = 'alex'  # 自动触发执行 __setitem__
# # del obj['k1']       # 自动触发执行 __delitem__
# obj['name']='alex'
# print obj['name']
# print obj.data
# del obj['name']
# print obj.data

# print Foo.__dict__
# print obj.__dict__

# --------------------------------------

#7. __new__ \ __metaclass 创建自己的数据类型
# 7.1 类也是对象，是由type类实例化产生的
# class Foo(object):
#     def __init__(self, name):
#         self.name = name
#
#     def func(self):
#         print ('hello %s'%self.name)
#
# f = Foo("alex")
#
# f.func()
#
# print type(f) # 输出：<class '__main__.Foo'>  表示，obj 对象由Foo类创建
# print type(Foo) # 输出：<type 'type'> 表示，Foo类对象由 type 类创建
# f对象是Foo类的一个实例，Foo类对象是 type 类的一个实例，
# 即：Foo类对象 是通过type类的构造方法创建。
# 那么，创建类就可以有两种方式，上面是普通方式，下面是特殊方式，当然这也就是个装逼方式，
# 这种方式用来装配类。
# def func(self):
#     print("hello %s"%self.name)
#
# def __init__(self,name,age):
#     self.name = name
#     self.age = age
#
# Foo = type('Foo',(object,),{'func':func,'__init__':__init__})
# # object后面的‘,’不能省，因为该参数必须是元组，加了‘,’就是元组。
# # 把上面的两个函数装配进名字为Foo继承自object的类。
#
# f = Foo("jack",22)
# f.func()
#如果上面定义改成{'a':func,'__init__':__init__},是可以的
# 那么f.func()就要改写成f.a()
# 但是'__init__':__init__不可以改成'b':__init__，否则就无法实例化。

# 7.2 创建自己的数据类型
'''
那么问题来了，类默认是由 type 类实例化产生，type类中如何实现的创建类？
类又是如何创建对象？

答：类中有一个属性’元类‘ __metaclass__，其用来表示该类由 谁 来实例化创建，
所以，我们可以为 __metaclass__ 设置一个type类的派生类，从而查看类创建的过程。
'''
# 用type方法创建自己的数据类型MyType
class MyType(type):
    def __init__(self,*args, **kwargs):
        print("Mytype __init__ 2")
        super(MyType,self).__init__(*args, **kwargs)#继承type的__init__

    def __call__(self, *args, **kwargs):#当对象+（）时（即类对象创建对象时）触发，f = Foo("Alex")触发，规定了Foo做为类实例化的过程
        print("Mytype __call__ 3", args, kwargs)
        obj = self.__new__(self)#类对象实例化第一件事就是new，一定要有，不然无法实例化
        obj.data={'name':1111}#给每一个Foo的对象设定了
        print("obj ",obj,args, kwargs)
        print('self',self)
        self.__init__(obj,*args,**kwargs)##类对象实例化第二件事就是init，一定要有，不然无法实例化
        return obj #把类对象的实例化对象

    def __new__(cls, *args, **kwargs):
        print("Mytype __new__ 1",args,kwargs)
        return type.__new__(cls, *args, **kwargs)#继承type的__new__

# print (type(MyType))
print('here...')

class Foo(object):
    '''
    用__metaclass__方法把该类定义为MyType是Foo的元类，即Foo是MyType这个类的对象
    也就是说Foo是MyType这个类的实例化对象，是object的子类
    站在对象的角度：Foo是MyType这个类的对象。就像f是Foo这个类的对象一样，但你不能说f是Foo的子类，因为f不是一个类。
    站在类的角度：Foo这个类是object的子类，它继承object父类的属性和方法'''

    __metaclass__ = MyType
    #写到这里就完成了实例化Foo=MyType(), MyType的__new__和__init__都会执行
    # -------------------------------------------------------------Foo的type就是MyType

    def __init__(self,name):
        #构造方法是创建实例的第二个阶段
        self.name = name
        print("Foo __init__5")
        # return object.__init__(self)

    def __new__(cls, *args, **kwargs):
        #new是用来创建实例的，是创建实例的第一个阶段

         print("Foo __new__4",cls, args, kwargs)
         # print object.__new__(cls)
         return object.__new__(cls) #用return方法去继承父类object的__new__方法，去创建实例。
         #return object.__new__(cls)是创建实例的第一个阶段，不继承就无法实例化。
         #cls实际上就是类对象Foo。class self
print ('Foo的类型',type(Foo)) #MyType
print ('Foo的父类',Foo.__bases__ )#object
f = Foo("Alex")
# print  'f的类型',f.__class__ ,type(f)#Foo
# # print f.__bases__#AttributeError: 'Foo' object has no attribute '__bases__',只有类才有__bases__,用来查看父类

# print("f",f.data)//py3中没有用，会报错
#
# print("fname",f.name)
