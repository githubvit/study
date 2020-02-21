# class Foo:
#     def f1(self):
#         print('Foo.f1')

#     def f2(self):
#         print('Foo.f2')
#         self.f1()

# class Bar(Foo):
#     def f1(self):
#         print('f1')


# b=Bar()
# b.f2()

# 多继承 py3 天生新式类 广度优先
class Goo:
    def f1(self):
        print('Goo.f1')

class Foo:
    def f2(self):
        print('Foo.f2')
        self.f1() # Sub.f1 从对象空间出发 按就近原则搜索
        super().f1() # Goo.f1 按类的mro列表路径方向搜索

class Bar:
    def f1(self):
        print('Bar.f1')

class Sub(Bar,Foo,Goo):
    def f1(self):
        print('Sub.f1')

print(Sub.mro())
# [<class '__main__.Sub'>, 
# <class '__main__.Bar'>, 
# <class '__main__.Foo'>, 
# <class '__main__.Goo'>, 
# <class 'object'>]
s=Sub()
s.f2()
