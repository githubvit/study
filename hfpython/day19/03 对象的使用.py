school='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
class OldboyStudent:
    school='oldboy'

    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    #self=stu1
    def learn(self):
        print('%s is learning' %self.name)

    def choose(self,course):
        print('%s is choosing %s' %(self.name,course))

# 调用类---》产生类的对象，该对象也可以称为类的一个实例，调用类的过程也称为类的实例化
stu1=OldboyStudent('李三胖',18,'male') #OldboyStudent.__init__(stu1,'李三胖',18,'male')


# OldboyStudent.country='CHINA'
# print(OldboyStudent.country)

# print(OldboyStudent.__dict__)
# print(stu1.__dict__)
# print(stu1.__dict__['name'])
# print(stu1.name)
# print(stu1.school)
# print(school)

stu2=OldboyStudent('王大炮',28,'male')
# print(stu2.__dict__)



# 类内部定义的变量是给所有对象共享，所有对象指向的都是同一个内存地址
# print(id(stu1.school))
# print(id(stu2.school))
# print(id(OldboyStudent.school))





# 类内部定义的函数，类可以使用，但类来用的时候就是一个普通函数，普通函数有几个参就传几个参数
# print(OldboyStudent.learn)
# OldboyStudent.learn(123)

# 类内部定义的函数，其实是给对象使用的，而且是绑定给对象用，绑定给不同的对象就是不同的绑定方法
# print(stu1.learn)
# print(stu2.learn)
# 绑定方法的特殊之处在于，谁来调用，就会将谁当作第一个参数自动传入

# stu1.learn() # OldboyStudent.learn(stu1)
# stu2.learn() # OldboyStudent.learn(stu2)



# stu1.choose('python')
# stu2.choose('linux')












