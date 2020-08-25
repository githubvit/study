# 封装
# 1. __开头的属性只是语法意义上的变形，并不会真的限制外部的访问。
# 2. 这种变形只在类定义阶段发生一次，类定义之后再新增的__开头的属性不会变形。
# 3. 这种隐藏只对外不对内，因为类内部定义的属性在定义阶段统一发生了变形。
# 4. 如果父类不想让子类覆盖自己的方法，可以在方法名前加__开头。

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

obj.get_y()

'''

强调：封装单从字面意思去看等同于隐藏，但其实封装绝对不是单纯意义的隐藏

2、为什么要用封装


'''
#1 封装数据属性的目的：把数据属性封装起来，然后需要开辟接口给类外部的使用者使用，好处是
# 我们可以在接口之上添加控制逻辑，从而严格控制访问者对属性的操作
# class People:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#
#     def tell_info(self):
#         # u=input('user>>: ').strip()
#         # p=input('pwd>>: ').strip()
#         # if u == 'egon' and p == '123':
#             print(self.__name,self.__age)
#
#     def set_info(self,name,age):
#         if type(name) is not str:
#             raise TypeError('用户名必须为str类型')
#         if type(age) is not int:
#             raise TypeError('年龄必须为int类型')
#         self.__name=name
#         self.__age=age
#
# p=People('egon',18)
#
# # p.tell_info()
# # p.tell_info()
#
# # p.set_info('EGON',19)
# # p.tell_info()
#
# # p.set_info(353535353535353535,20)
# p.set_info('EGON','20')



#2 封装函数属性的目的：为了隔离复杂度

class ATM:
    def __card(self):
        print('插卡')
    def __auth(self):
        print('用户认证')
    def __input(self):
        print('输入取款金额')
    def __print_bill(self):
        print('打印账单')
    def __take_money(self):
        print('取款')

    def withdraw(self):
        self.__card()
        self.__auth()
        self.__input()
        self.__print_bill()
        self.__take_money()


obj=ATM()
obj.withdraw()



#封装的终极奥义：明确地 区分内外，对外是隐藏的，对内是开放的

#封装的property属性

# egon.bmi=123 # egon.bmi背后对应的是一个函数，所以不能赋值
class People:
    def __init__(self,name):
        self.__name=name


    @property
    def name(self): #obj.name
        print('您现在访问的是用户名。。。')
        return self.__name

    @name.setter #obj.name='EGON'
    def name(self,x):
        # print('=================',x)
        if type(x) is not str:
            raise TypeError('名字必须是str类型，傻叉')
        self.__name=x

    @name.deleter
    def name(self):
        # print('就不让你删')
        del self.__name

obj=People('egon')

print(obj.name)
# print(obj.name()) # 报错 TypeError: 'str' object is not callable

# print(obj.name)

# obj.name='EGON'

# print(obj.name)

# obj.name=123

del obj.name
obj.name