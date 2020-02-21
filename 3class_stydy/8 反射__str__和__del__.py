# 一 内置函数补充

# 1 谁(对象)是谁（类）的实例 isinstance
class Foo:
    pass

obj=Foo()
print(isinstance(obj,Foo)) # 推荐使用该函数来判断一个函数的类型

# 2 谁（子类）是谁（父类）的子类
print(issubclass(Foo,object))


# 二 反射：通过操作字符串来操作对象或类的属性。
#  hasattr setattr getattr delattr

# class People:
    country="China"
    def __init__(self,name):
        self.name=name
    def tell(self):
        print('%s is aaa' %self.name)

obj=People('egon')

# 1、hasattr
# print(hasattr(People,'country'))
# print('country' in People.__dict__)

# print(hasattr(obj,'name'))
# print(hasattr(obj,'country'))
# print(hasattr(obj,'tell'))

# 2、getattr 
# 第三个参数 None 是用来防止对象或类没有'字符串'属性的时候报错。
# x=getattr(People,'country1',None)
# print(x)

# f=getattr(obj,'tell',None)#obj.tell
# print(f == obj.tell)
# f()
# obj.tell()


# 3、setattr
# People.x=111
# setattr(People,'x',111)
# print(People.x)

# obj.age=18
# setattr(obj,"age",18)
# print(obj.__dict__)

# 4、delattr
# del People.country
# delattr(People,"country")
# print(People.__dict__)

# del obj.name
# delattr(obj,"name")
# print(obj.__dict__)



# 用户下载功能示例

class Foo:
    def run(self):
        while True:
            cmd=input('cmd>>: ').strip()
            # print('%s run...' %cmd)
            if hasattr(self,cmd):
                func=getattr(self,cmd)
                func()

    def download(self):
        print('download....')

    def upload(self):
        print('upload...')

# obj=Foo()
# obj.run()

# 三 __str__ 返回值
class People:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def __str__(self):
        # print('========>')
        return '<名字：%s 年龄：%s 性别：%s>' %(self.name,self.age,self.sex)

obj=People('egon',18,'male')
print(obj) #print(obj.__str__())

# l=list([1,2,3])
# print(l)

# 四 __del__ 在对象被回收del之前执行的方法(钩子函数)

# import time
#
# class People:
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#
#     def __del__(self): # 在对象被删除的条件下，自动执行
#         print('__del__')
#
#
# obj=People('egon',18,'male')
#
# del obj #之前会执行obj.__del__()
#
# time.sleep(5) 