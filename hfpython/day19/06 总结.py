#一、类的实例化：调用类产生对象的过程称为类的实例化，实例化的结果是一个对象，或称为一个实例
class People:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def run(self):
        print('%s is running' %self.name)

#实例化做了三件事
#1、先产生一个空对象
#2、自动触发类内部__init__函数的执行
#3、将空对象，以及调用类括号内传入的参数，一同传给__init__，为对象定制独有的属性
# obj=People('egon',18,'male') #People.__init__(obj,'egon',18,'male')

# 会产生对象的名称空间,如何查看
# print(obj.__dict__)

#二；对象的操作
# print(obj.name) #obj.__dict__
# obj.education='哈佛'
# del obj.name
# obj.age=19
# print(obj.__dict__)


#三：对象属性的查找顺序:先找对象自己的名称空间----》类的名称空间
class People:
    x=1
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def run(self): #self=obj
        print('%s is running' %self.name) #obj.name

obj=People('egon',18,'male') #People.__init__(obj,'egon',18,'male')
obj1=People('egon1',18,'male') #People.__init__(obj,'egon',18,'male')
obj2=People('egon2',18,'male') #People.__init__(obj,'egon',18,'male')

#1、类的数据属性:是给对象用的，而且直接共享给所有对象用的，内存地址都一样
# print(People.x)
# People.x=11111

# print(id(People.x),People.x)
# obj.x='obj================》'
# print(id(obj.x),obj.x)
# print(id(obj1.x),obj1.x)
# print(id(obj2.x),obj2.x)


#2、类的函数属性：也是给对象用，但是绑定给对象用的，绑定到不同的对象就是不同的
#绑定方法，内存地址都不一样，但其实只想都是同一个功能
# print(People.run) #<function People.run at 0x00000226E7C78A60>
# People.run(123123)
# People.run(obj)

# print(obj.run)
# print(obj1.run)
# print(obj2.run)

#四：绑定方法的特殊之处：
#1、 绑定给谁就应该由谁来调用，
#2、谁来调用就会把谁当做第一个参数传入
class People:
    x=1
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def run(self): #self=obj
        print('%s is running' %self.name) #obj.name

    def f1():
        print('from f1')

    def f2(self):
        pass

obj=People('egon',18,'male') #People.__init__(obj,'egon',18,'male')
# obj1=People('egon1',18,'male') #People.__init__(obj,'egon',18,'male')
# obj2=People('egon2',18,'male') #People.__init__(obj,'egon',18,'male')
#
# obj.run()
# obj1.run()
# obj2.run()

# print(People.f1)
# People.f1()
# print(obj.f1)
# obj.f1() #People.f1(obj)


#五：一切皆对象:在python3中统一了类与类型的概念，类即类型
l=list([1,2,3])
# print(type(l))

# print(type(obj))

l.append(4)
