# 解决类与类之间代码冗余问题有两种解决方案：1、继承 2、组合
# 1、继承：描述的是类与类之间，什么是什么的关系

# 2、组合：描述的是类与类之间的关系，是一种什么有什么关系
# 一个类产生的对象，该对象拥有一个属性，这个属性的值是来自于另外一个类的对象

class Date:
    def __init__(self,year,mon,day):
        self.year = year
        self.mon = mon
        self.day = day

    def tell_birth(self):
        print('出生年月日<%s-%s-%s>' % (self.year, self.mon, self.day))

class OldboyPeople:
    school = 'oldboy'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

class OldboyTeacher(OldboyPeople):
    def __init__(self,name,age,sex,level,salary):
        super().__init__(name,age,sex)
        self.level=level
        self.salary=salary

    def change_score(self):
        print('teacher %s is changing score' %self.name)

class Oldboystudent(OldboyPeople):
    def __init__(self,name,age,sex,course,):
        super().__init__(name,age,sex,)
        self.course=course

    def choose(self):
        print('student %s choose course' %self.name)


tea1=OldboyTeacher('egon',18,'male',9,3.1)
date_obj=Date(2000,1,1)
# date_obj.tell_birth()

tea1.birth=date_obj
# print(tea1.birth)
# tea1.birth.tell_birth()
# tea1.change_score()

stu1=Oldboystudent('张三',16,'male','linux')
stu1.birth=Date(2002,3,3)
stu1.birth.tell_birth()



