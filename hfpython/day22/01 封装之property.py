'''
BMI指数（bmi是计算而来的，但很明显它听起来像是一个属性而非方法，如果我们将其做成一个属性，更便于理解）

成人的BMI数值：
过轻：低于18.5
正常：18.5-23.9
过重：24-27
肥胖：28-32
非常肥胖, 高于32
　　体质指数（BMI）=体重（kg）÷身高^2（m）
　　EX：70kg÷（1.75×1.75）=22.86

'''

class People:
    def __init__(self,name,weight,height):
        self.name=name
        self.weight=weight
        self.height=height

    @property
    def bmi(self):
        return self.weight / (self.height * self.height)

# egon=People('egon',75,1.80)
#
# egon.bmi=egon.weight / (egon.height * egon.height)
# print(egon.bmi)
#
# yl=People('yangli',85,1.74)
# yl.bmi=yl.weight / (yl.height * yl.height)
# print(yl.bmi)


# 首先需要明确。bmi是算出来的，不是一个固定死的值，也就说我们必须编写一个功能，每次调用该功能
#都会立即计算一个值
egon=People('egon',75,1.80)
yl=People('yangli',85,1.74)

# 但很明显人的bmi值听起来更像一个名词而非动词
# print(egon.bmi())
# print(yl.bmi())


# 于是我们需要为bmi这个函数添加装饰器，将其伪装成一个数据属性
# egon.weight=70
# print(egon.bmi) #21.604938271604937，调用egon.bmi本质就是触发函数bmi的执行，从而拿到其返回值
# print(yl.bmi)


# 了解

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

# print(obj.name)
# print(obj.name())

# print(obj.name)

# obj.name='EGON'

# print(obj.name)

# obj.name=123

del obj.name
obj.name