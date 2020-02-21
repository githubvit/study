'''
1  继承是类与类之间的关系，寻找这种关系需要先抽象再继承

'''
class OldboyPeople:
    school = 'oldboy'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class OldboyTeacher(OldboyPeople):
    def change_score(self):
        print('teacher %s is changing score' %self.name)

class Oldboystudent(OldboyPeople):
    def choose(self):
        print('student %s choose course' %self.name)


tea1 = OldboyTeacher('egon', 18, 'male') #OldboyTeacher.__init__(...)
stu1=Oldboystudent('alex',73,'female')

print(tea1.name,tea1.age,tea1.sex)
# print(stu1.name)