class OldboyPeople:
    school = 'oldboy'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def f1(self):
        print('爹的f1')
class OldboyTeacher(OldboyPeople):
    def change_score(self):
        print('teacher %s is changing score' %self.name)

tea1 = OldboyTeacher('egon', 18, 'male')
# print(tea1.__dict__)
# print(tea1.name)
# print(tea1.school)
# print(tea1.change_score)
# print(tea1.f1)



class Foo:
    def f1(self):
        print('Foo.f1')

    def f2(self): #self=obj
        print('Foo.f2')
        self.f1() #obj.f1()

class Bar(Foo):
    def f1(self):
        print('Bar.f1')

obj=Bar()
# print(obj.__dict__)
obj.f2()