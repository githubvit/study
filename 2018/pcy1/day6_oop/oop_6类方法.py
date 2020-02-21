#_*_coding:utf-8_*_
'''
类方法通过@classmethod装饰器实现，
类方法和普通方法的区别是， 类方法只能访问类变量，不能访问实例变量.
'''


class Dog(object):
    name = "我是类变量"

    def __init__(self, name):
        self.name = name

    @classmethod
    def eat(self):
        print("%s is eating" % self.name)


d = Dog("ChenRonghua")
d.eat()