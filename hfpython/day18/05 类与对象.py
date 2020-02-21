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

    #  用函数表示技能
    def learn(self):
        print('is learning...')

    def choose(self):
        print('choose course...')

    # print('======>')

# 注意：在定义类的阶段会立刻执行类体内的代码，然后将产生的名字存放于类名称空间中
# print(OldboyStudent.__dict__)
# print(OldboyStudent.__dict__['school'])
# print(OldboyStudent.__dict__['learn'])
# OldboyStudent.__dict__['learn'](123)

# print(OldboyStudent.school) # OldboyStudent.__dict__['school']
# print(OldboyStudent.learn) # OldboyStudent.__dict__['learn']
# OldboyStudent.learn('xxx')
# OldboyStudent.learn('xxx')


OldboyStudent.country='China'
OldboyStudent.school='偶的博爱'

del OldboyStudent.country
print(OldboyStudent.__dict__)


# 2、调用类，产生程序中的对象