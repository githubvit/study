#_*_coding:utf-8_*_
'''
普通类、接口类、抽象类
'''

#1， 普通类 无约束
# class Foo:
#     def f1(self):
#         print 123
#
#
# class Bar(Foo):
#     pass
# b=Bar()
# b.f1()

#2，接口类：接口中的方法不能写任何代码，只能主动触发异常，遵循接口的规则
# class IFoo:
#     def f1(self):
#         raise Exception('错误了。。。')  # 主动触发异常
#
# class Bar(IFoo):
#     pass
# b=Bar()
# b.f1()

#3，抽象类 抽象方法 既可以实现普通类的功能，又可以实现约束
import abc
#class Foo(metaclass=abc.ABCMeta):#pthony3.x写法
class Foo(object):
    __metaclass__ = abc.ABCMeta#定义抽象类
    def f1(self):
        print 123
    def f2(self):
        print 456
    @abc.abstractmethod#定义抽象方法，就是接口
    def f3(self):
        '''
        干嘛的
        :return: 
        '''
class Bar(Foo):#Bar中必须定义def f3

    def f3(self):
        pass
b=Bar()
#Bar中如果没有定义def f3报如下错误
#TypeError: Can't instantiate abstract class Bar with abstract methods f3
