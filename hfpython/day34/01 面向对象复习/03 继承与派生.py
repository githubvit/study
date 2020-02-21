'''
1、什么是继承？
    继承创建类的方式，创建的字类可以遗传父类功能或属性
    特点：
        python支持多继承



    优点：
        1、减少代码冗余
    缺点：
        1、把子类与父类强耦合到一起







'''
#
# class Foo:
#     def f1(self):
#         print('Foo.f1')
#
#     def f2(self): #self=b
#         print('Foo.f2')
#         self.f1() #b.f1()
#
# class Bar(Foo):
#     def f1(self):
#         print('Foo.f1')
#
#
# b=Bar()
# b.f2()



#A没有继承B,但是A内super会基于C.mro()继续往后找
class A(object):
    def test(self):
        super().test()
class B(object):
    def test(self):
        print('from B')
class C(A,B):
    pass

c=C()
c.test()

print(C.mro())



