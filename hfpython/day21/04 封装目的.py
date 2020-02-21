'''

强调：封装单从字面意思去看等同于隐藏，但其实封装绝对不是单纯意义的隐藏

2、为什么要用封装


'''
#1 封装数据属性的目的：把数据属性封装起来，然后需要开辟接口给类外部的使用者使用，好处是
# 我们可以在接口之上添加控制逻辑，从而严格空间访问者对属性的操作
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



#封装的终极奥义：明确地区分内外，对外是隐藏的，对内是开放的
