class OldboyPeople:
    school = 'oldboy'

    def __init__(self, name, age, sex,):
        self.name = name
        self.age = age
        self.sex = sex

class OldboyTeacher(OldboyPeople):
    def __init__(self,name,age,sex,level,salary):
        super().__init__(name,age,sex)
        self.level=level
        self.salary=salary

        self.courses=[]

    def change_score(self):
        print('teacher %s is changing score' %self.name)

    def tell_course_info(self):
        print(('老师%s 教授的课程信息如下' %self.name).center(50,'='))
        for course_obj in self.courses:
            course_obj.info()


class Oldboystudent(OldboyPeople):
    def __init__(self,name,age,sex):
        super().__init__(name,age,sex,)
        self.courses=[]

    def choose(self):
        print('student %s choose course' %self.name)

    def tell_course_info(self):
        print(('学生%s 学习的课程信息如下' % self.name).center(50, '='))
        for course_obj in self.courses:
            course_obj.info()

class Course:
    def __init__(self,cname,period,price):
        self.cname=cname
        self.period=period
        self.price=price

    def info(self):
        print('课程信息<名字：%s 周期：%s  价钱：%s>' %(self.cname,self.period,self.price))


tea1=OldboyTeacher('egon',18,'male',9,3.1)
stu1=Oldboystudent('张三',16,'male')

python=Course('Python全栈开发','5mons',3000)
linux=Course('Linux高级架构师','5mons',2000)
go=Course('Go开发工程师','3mons',1000)


# # 给老师添加课程
# tea1.courses.append(python)
# tea1.courses.append(linux)

# print(tea1.courses)
# tea1.courses[0].info()
# for course_obj in tea1.courses:
#     course_obj.info()

# tea1.tell_course_info()


# 给学生添加课程
stu1.courses.append(python)
stu1.courses.append(go)
stu1.courses.append(linux)
stu1.tell_course_info()