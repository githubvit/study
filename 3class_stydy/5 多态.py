# 多态性的应用 类比于 java中的接口
import abc

# 将父类定义为抽象类： 
# 1. 即规定其元类metaclass为abc.ABCMeta
# 2. 用语法糖@abc.abstractclassmethod定义必须有的接口 
class Animal(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def speak(self): 
        pass

# 抽象类的子类必须详细定义父类中的接口，否则报错    
class Dog(Animal):
    def speak(self):
        print('wang...')
class Cat(Animal):
    def speak(self):
        print('miao...')
class Pig(Animal):
    def speak(self):
        print('heng...')

#写一个接口函数 统一调用各个对象
def speak(obj):
    obj.speak()

# 实例化各个对象
d1=Dog()
c1=Cat()
p1=Pig()

speak(d1)
speak(c1)
speak(p1)
