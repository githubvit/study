''''
1、类
    对象是特征与技能的结合体，那类就是一系列对象相同的特征与技能的结合体

2、在现实世界中：一定先有对象，后来随着人类文明的发展总结出的类
            对象是具体存在的，而类只是一种抽象概念

3、在程序中,务必保证：先定义类，后调用类来产生对象


现实生活中的对象：
    对象1：
        特征：
            school="Oldboy"
            name="马冬梅"
            age=18
            sex="female"
        技能：
            学习
            选课

    对象2：
        特征：
            school="Oldboy"
            name="甜蜜蜜"
            age=21
            sex="male"
        技能：
            学习
            选课

    对象3：
        特征：
            school="Oldboy"
            name="原石开"
            age=22
            sex="male"
        技能：
            学习
            选课

现实生活中的老男孩学生类：
     相同的特征
            school="Oldboy"
     相同的技能
            学习
            选课
'''
#1、程序中的类
class OldboyStudent:
    # 用变量表示特征
    school="Oldboy"

    # stu1, "马冬梅", 18, 'female'
    def __init__(self,name,age,sex): #self=stu1     name= "马冬梅"   age=18     sex="female"
        # print('==========init run=============>')
        self.name=name # stu1.name = "马冬梅"
        self.age=age  # stu1.age = 18
        self.sex=sex  # stu1.sex = "female"


    #  用函数表示技能
    def learn(self):
        print('is learning...',self)

    def choose(self):
        print('choose course...')

# 在程序中：必须先定义类 - -----》调用类 - -----》对象

# stu1=OldboyStudent()
# stu1.NAME='马冬梅'
# stu1.AGE=18
# stu1.SEX="female"
#
# stu2=OldboyStudent()
# stu2.NAME='甜蜜蜜'
# stu2.AGE=21
# stu2.SEX="male"
#
# stu3=OldboyStudent()
# stu3.NAME='原石开'
# stu3.AGE=22
# stu3.SEX="male"
#
# print(stu1.NAME,stu1.school)
# print(stu2.NAME,stu2.school)
# print(stu3.NAME,stu3.school)
# 上述产生的三个对象都一样了


# 调用类发生哪些事：
#1、首先会产生一个空对象stu1
#2、会自动触发类内部的__init__函数
#3、然后将空对象stu1连同调用类时括号内的参数组成（stu1,"马冬梅",18,'female'）,将这四个参数一起传给__init__函数

stu1=OldboyStudent("马冬梅",18,'female')  #OldboyStudent.__init__(stu1,"马冬梅",18,'female')
stu2=OldboyStudent("甜蜜蜜",21,'male') #OldboyStudent.__init__(stu2,"甜蜜蜜",21,'male')
stu3=OldboyStudent("原石开",22,'male')


# print(stu1.name,stu1.age,stu1.sex)
# print(stu2.name,stu2.age,stu2.sex)
# print(stu3.name,stu3.age,stu3.sex)

