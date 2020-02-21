# class Foo:
#     x=1
#     y=2
#
#     def func1(self,m,n):
#         print(m+n)


# print(Foo.__dict__['x'])
# print(Foo.__dict__['func1'])

# print(Foo.x)
# print(Foo.func1)

# print(Foo.aaa)



class Student:
    school='Oldboy'

    # Student.__init__(stu1, 'egon', 18, 'male')
    def __init__(self,name,age,sex):
        self.name=name #stu1.name='egon'
        self.age=age ##stu1.age=18
        self.sex=sex ##stu1.sex='male'

    def tell_info(obj):
        print(obj.name,obj.age,obj.sex,obj.school)


    def learn(obj):
        print('%s is learning' %obj.name)


    def eat(obj):
        print('%s is eating' %obj.name)


    def f1(obj):
        pass

    def f2(obj):
        pass


#  调用类来产生对象，
#1、会先产生一个空对象stu1
#2、将stu1，连同括号内的参数一起传给Student.__init__(stu1,'egon',18,'male')
stu1=Student('egon',18,'male')
stu2=Student('egon2',18,'male')

# print(stu1.__dict__)
# print(stu1.name)
# print(stu2.name)

# print(stu1.school)
# print(stu2.school)
# print(stu1.eat)


# 对象的本质与类一样，都是一个用来存放名字的容器，即名称空间



#访问功能


# Student.eat(stu1)
# Student.tell_info(stu1)
# print(stu1.eat)
stu1.eat() #Student.eat(stu1)
stu1.tell_info() #Student.tell_info(stu1)



stu2.eat











def teach():
    pass

def change_score():
    pass









