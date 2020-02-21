import aaa


# print(aaa.m1)
# aaa.m1.f1()

# print(aaa.m2)
# aaa.m2.f2()


# print(aaa.bbb)
aaa.bbb.m3.f3()


# 强调：
#1、在导入时带点的，点的左边必须是一个包,这是导入包特有的语法
#2、包内，模块直接的导入应该使用from。。。import 。。。
#3、from 。。。 import。。。，import后必须是一个明确的名字，没有任何的前缀
from a.b.c.d.f import g.h.x #错误

#1、f左边必须都是包
#2、import后的名字不能有任何前缀