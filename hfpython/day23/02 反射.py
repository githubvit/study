#下述四个函数是专门用来操作类与对象属性的，如何操作？
#通过字符串来操作类与对象的属性，这种操作称为反射
class People:
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
















