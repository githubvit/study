# #派生：子类定义自己新的属性，如果与父类同名，以子类自己的为准
# class OldboyPeople:
#     school = 'oldboy'
#
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def f1(self):
#         print('爹的f1')
# class OldboyTeacher(OldboyPeople):
#     def change_score(self):
#         print('teacher %s is changing score' %self.name)
#
#     def f1(self):
#         print('儿子的f1')
#
# tea1 = OldboyTeacher('egon', 18, 'male')
# tea1.f1()
#
#



class OldboyPeople:
    school = 'oldboy'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def f1(self):
        print('爹的f1')

class OldboyTeacher(OldboyPeople):
    def __init__(self,name,age,sex,level,salary):
        self.name=name
        self.age=age
        self.sex=sex

        self.level=level
        self.salary=salary

    def change_score(self):
        print('teacher %s is changing score' %self.name)

    def f1(self):
        print('儿子的f1')

tea1 = OldboyTeacher('egon', 18, 'male',9,3.1)
print(tea1.name,tea1.age,tea1.sex,tea1.level,tea1.salary)


