# class Foo:
#     __x=1 #_Foo__x=1
#     def __init__(self,name):
#         self.__name=name #self._Foo__name=name
#
#     def __f1(self): #_Foo__f1
#         print('from f1')
#
#
#     def tell_name(self):
#         print(self.__name) #print(self._Foo__name)
#
# obj=Foo('egon')
# # print(obj.__dict__)
# # print(Foo.__dict__)
#
# obj.tell_name()



# class Foo:
#     def __f1(self): #_Foo__f1
#         print('Foo.f1')
#
#     def f2(self): #self=b
#         print('Foo.f2')
#         self.__f1() #self._Foo__f1
#
# class Bar(Foo):
#     def f1(self):
#         print('Foo.f1')
#
#
# b=Bar()
# b.f2()


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





