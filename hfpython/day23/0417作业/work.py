# 第一题
# # isinstance() 判断参数1是不是参数2的实例
# ss='123'
# print(type(ss) is str)
# print(isinstance(ss,str))
#
# # issubclass() 判断参数1是不是参数2的子类
# class Foo:
#     pass
#
# class Bar(Foo):
#     pass
#
# print(issubclass(Bar,Foo))

# 第二题：
# class FtpClient:
#     'ftp客户端,但是还么有实现具体的功能'
#     def __init__(self,addr):
#         print('正在连接服务器[%s]' %addr)
#         self.addr=addr
#
#
# f1=FtpClient('192.168.1.1')
# if hasattr(f1,'get'):
#     func_get=getattr(f1,'get')
#     func_get()
# else:
#     print('---->不存在此方法')
#     print('处理其他的逻辑')
# 第三题
# class Teacher:
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#
#     def __str__(self):
#         return '<name:%s age:%s sex:%s>'%(self.name,self.age,self.sex)
#
# teacher=Teacher('lqz',18,'male')
# print(teacher)

# 第四题：
# class MyOpen:
#     def __init__(self, path, mode='r', encode='utf-8'):
#         self.f = open(path, mode=mode, encoding=encode)
#
#     def write(self, line):
#         self.f.write(line)
#
#     def read(self):
#         return self.f.read()
#
#     def __del__(self):
#         self.f.close()
#
#     def __getattr__(self, item):
#         return getattr(self.f, item)
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.f.close()
#
#
# f = MyOpen('a.txt', mode='w')
# f.write('00')
# f.flush()
# f=MyOpen('a.txt',mode='r')
# print(f.read())
# with MyOpen('a.txt','r') as re:
#     print(re.read())


#第五题
# class Mymetaclass(type):
#     # def __new__(cls,name,bases,attrs):
#     #     if '__doc__' not in attrs or not attrs.get('__doc__').strip():
#     #         raise TypeError('必须为类指定文档注释')
#     #
#     #     if not name.istitle():
#     #         raise TypeError('类名首字母必须大写')
#     #     update_attrs={}
#     #     for k,v in attrs.items():
#     #         if not callable(v) and not k.startswith('__'):
#     #             update_attrs[k.upper()]=v
#     #         else:
#     #             update_attrs[k]=v
#     #     return type.__new__(cls,name,bases,update_attrs)
#     def __init__(cls,name,bases,attrs):
#         if '__doc__' not in attrs or not attrs.get('__doc__').strip():
#             raise TypeError('必须为类指定文档注释')
#
#         if not name.istitle():
#             raise TypeError('类名首字母必须大写')
#         update_attrs={}
#         for k,v in attrs.items():
#             if not callable(v) and not k.startswith('__'):
#                 update_attrs[k.upper()]=v
#             else:
#                 update_attrs[k]=v
#         super().__init__(name,bases,update_attrs)
#
# class Chinese(metaclass=Mymetaclass):
#     '''
#     d
#     '''
#
#     country='China'
#     tag='Legend of the Dragon' #龙的传人
#     def walk(self):
#         print('%s is walking' %self.name)
#
#
#
# print(Chinese.__dict__)

# 第六题
# #settings.py文件内容如下
# HOST='1.1.1.1'
# PORT=3306
#
# #方式一:定义一个类方法实现单例模式
# import settings
#
# class Mysql:
#     __instance=None
#     def __init__(self,host,port):
#         self.host=host
#         self.port=port
#
#     @classmethod
#     def singleton(cls):
#         if not cls.__instance:
#             cls.__instance=cls(settings.HOST,settings.PORT)
#         return cls.__instance
#
#
# obj1=Mysql('1.1.1.2',3306)
# obj2=Mysql('1.1.1.3',3307)
# print(obj1 is obj2) #False
#
# obj3=Mysql.singleton()
# obj4=Mysql.singleton()
# print(obj3 is obj4) #True
#
#
#
# #方式二：定制元类实现单例模式
# import settings
#
# class Mymeta(type):
#     def __init__(self,name,bases,dic): #定义类Mysql时就触发
#
#         # 事先先从配置文件中取配置来造一个Mysql的实例出来
#         self.__instance = object.__new__(self)  # 产生对象
#         self.__init__(self.__instance, settings.HOST, settings.PORT)  # 初始化对象
#         # 上述两步可以合成下面一步
#         # self.__instance=super().__call__(*args,**kwargs)
#
#
#         super().__init__(name,bases,dic)
#
#     def __call__(self, *args, **kwargs): #Mysql(...)时触发
#         if args or kwargs: # args或kwargs内有值
#             obj=object.__new__(self)
#             self.__init__(obj,*args,**kwargs)
#             return obj
#
#         return self.__instance
#
#
#
#
# class Mysql(metaclass=Mymeta):
#     def __init__(self,host,port):
#         self.host=host
#         self.port=port
#
#
#
# obj1=Mysql() # 没有传值则默认从配置文件中读配置来实例化，所有的实例应该指向一个内存地址
# obj2=Mysql()
# obj3=Mysql()
#
# print(obj1 is obj2 is obj3)
#
# obj4=Mysql('1.1.1.4',3307)



# 方式三:定义一个装饰器实现单例模式
# import settings
#
# def singleton(cls): #cls=Mysql
#     _instance=cls(settings.HOST,settings.PORT)
#
#     def wrapper(*args,**kwargs):
#         if args or kwargs:
#             obj=cls(*args,**kwargs)
#             return obj
#         return _instance
#
#     return wrapper
#
#
# @singleton # Mysql=Singleton(Mysql)
# class Mysql:
#     def __init__(self,host,port):
#         self.host=host
#         self.port=port
#
#
#
# obj1=Mysql()
# obj2=Mysql()
# obj3=Mysql()
# print(obj1 is obj2 is obj3) #True
#
# obj4=Mysql('1.1.1.3',3307)
# obj5=Mysql('1.1.1.4',3308)
# print(obj3 is obj4) #Fals
