# 在子类派生出的新方法中重用父类的功能
#方式一：指名道姓地调用（其实与继承没有什么关系的）
# OldboyPeople.__init__(self,name, age, sex)

# class OldboyPeople:
#     school = 'oldboy'
#
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def tell_info(self):
#         print("""
#         ===========个人信息==========
#         姓名：%s
#         年龄：%s
#         性别：%s
#         """ %(self.name,self.age,self.sex))
#
#
# class OldboyTeacher(OldboyPeople):
#     #            tea1,'egon', 18, 'male', 9, 3.1
#     def __init__(self, name, age, sex, level, salary):
#         # self.name = name
#         # self.age = age
#         # self.sex = sex
#         OldboyPeople.__init__(self,name, age, sex)
#
#         self.level = level
#         self.salary = salary
#
#     def tell_info(self):
#         OldboyPeople.tell_info(self)
#         print("""
#         等级：%s
#         薪资：%s
#         """ %(self.level,self.salary))
#
# tea1 = OldboyTeacher('egon', 18, 'male', 9, 3.1)
# # print(tea1.name, tea1.age, tea1.sex, tea1.level, tea1.salary)
#
#
# tea1.tell_info()



#方式二：super()调用（严格依赖于继承）
#super()的返回值是一个特殊的对象，该对象专门用来调用父类中的属性

#了解：在python2中，需要super(自己的类名,self)
class OldboyPeople:
    school = 'oldboy'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell_info(self):
        print("""
        ===========个人信息==========
        姓名：%s
        年龄：%s
        性别：%s
        """ %(self.name,self.age,self.sex))


class OldboyTeacher(OldboyPeople):
    #            tea1,'egon', 18, 'male', 9, 3.1
    def __init__(self, name, age, sex, level, salary):
        # OldboyPeople.__init__(self,name, age, sex)
        super(OldboyTeacher,self).__init__(name,age,sex)

        self.level = level
        self.salary = salary

    def tell_info(self):
        # OldboyPeople.tell_info(self)
        super().tell_info()
        print("""
        等级：%s
        薪资：%s
        """ %(self.level,self.salary))

tea1 = OldboyTeacher('egon', 18, 'male', 9, 3.1)
# print(tea1.name, tea1.age, tea1.sex, tea1.level, tea1.salary)
tea1.tell_info()