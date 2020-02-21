'''
1、什么是封装
    装就是把一堆属性存起来，封的概念就把这些属性给隐藏起来
    强调：封装单从字面意思去看等同于隐藏，但其实封装绝对不是单纯意义的隐藏

2、为什么要用封装


3、如何用封装

'''
# 如何把属性隐藏起来，就在属性前面加上__开头（注意不要加__结尾）
# 注意：
#1、其实这种隐藏只是一种语法上的变形,对外不对内
# 为一个属性名加__开头（注意不要加__结尾），会在类定义阶段将属性名统一变形：_自己的类名__属性名

class Foo:
    __x=1111 #_Foo__x=1111
    def __init__(self,y):
        self.__y=y #self._Foo__y=y

    def __f1(self): #_Foo__f1
        print('Foo.f1')

    def get_y(self):
        print(self.__y) # print(self._Foo__y)

obj=Foo(22222)
# print(obj.x)
# print(obj.__x)
# obj.__f1()
# print(obj.y)
# print(obj.__y)
# print(Foo.__dict__)
# print(obj._Foo__x)
# print(obj._Foo__y)
# obj._Foo__f1()

# obj.get_y()


#2、这种语法意义上变形，只在类定义阶段发生一次，类定义之后，新增的__开头的属性都没有变形的效果

# Foo.__aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa=1
# print(Foo.__dict__)

# obj.__bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb=2
# print(obj.__dict__)


#3、如果父类不想让子类覆盖自己的方法，可以在方法名前加__开头
class Foo:
    def __f1(self): #_Foo__f1
        print('Foo.f1')

    def f2(self):
        print('Foo.f2')
        self.__f1() #obj._Foo__f1()

class Bar(Foo):
    def __f1(self): #_Bar__f1
        print("Bar.f1")

obj=Bar()

obj.f2()



























#封装的终极奥义：明确地区分内外，对外是隐藏的，对内是开放的