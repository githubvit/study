'''
1 什么是多态
    多态指的是同一种事物多种形态



2、为什要用多态
    用基类创建一套统一的规则，强制子类去遵循（使用抽象类实现），这样便可以
    在不用考虑对象具体类型的前提下而直接使用对象下的方法


3、如何用多态
'''

# class Animal:
#     def eat(self):
#         pass
#
#     def drink(self):
#         pass
#
#     def run(self):
#         pass
#
#     def bark(self):
#         pass
#
# class Cat(Animal):
#     def jiao(self):
#         print('喵喵喵')
#
# class Dog(Animal):
#     def speak(self):
#         print('汪汪汪')
#
# class Pig(Animal):
#     def han(self):
#         print('哼哼哼')
#
# c=Cat()
# d=Dog()
# p=Pig()
#
#
# # 多态性：可以在不用考虑对象具体类型的前提下而直接使用对象下的方法
# # c.eat()
# # d.eat()
# # p.eat()
# #
# # c.drink()
# # d.drink()
# # p.drink()
#
#
# # d.bark()
# # p.bark()
# # c.bark()
#
# d.speak()
# c.jiao()
# p.han()




import abc #abstract class
class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def eat(self):
        pass

    @abc.abstractmethod
    def drink(self):
        pass

    @abc.abstractmethod
    def run(self):
        pass

    @abc.abstractmethod
    def bark(self):
        pass

# obj=Animal() # 抽象基类本身不能被实例化

class Cat(Animal):
    def eat(self):
        print('cat eat')

    def drink(self):
        print('cat drink')

    def run(self):
        print('cat run')

    def bark(self):
        print('喵喵喵')

class Dog(Animal):
    def eat(self):
        print('dog eat')

    def drink(self):
        print('dog drink')

    def run(self):
        print('dog run')

    def bark(self):
        print('汪汪汪')

class Pig(Animal):
    def eat(self):
        print('pig eat')

    def drink(self):
        print('pig drink')

    def run(self):
        print('pig run')

    def bark(self):
        print('哼哼哼')

c=Cat()
d=Dog()
p=Pig()


# c.bark()
# d.bark()
# p.bark()


# def BARK(animal):
#     animal.bark()
#
#
# BARK(c)
# BARK(d)
# BARK(p)



s='hello'
l=[1,2,3]
t=(4,5,6)

s.__len__()
l.__len__()
t.__len__()


# def LEN(obj):
#     return obj.__len__()
#
# print(LEN(s))
# print(LEN(l))
# print(LEN(t))
print(len(l))
print(len(s))
print(len(t))