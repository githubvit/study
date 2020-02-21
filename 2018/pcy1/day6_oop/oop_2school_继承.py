 #_*_coding:utf-8_*_
'''1,建立学校：
    学校有校名、校址，
    有一群学生、一群老师
    
    可以给学生提供注册，让其入学；
    聘用老师提供，让其教学；
    
    可以开班授课
'''
class School(object):#相关类
    def __init__(self,sch_name,sch_addr):
        self.sch_name=sch_name
        self.sch_addr=sch_addr
        self.stu_number=[]
        self.terch_number=[]
        self.course_number=[]

    def enroll(self,stu_obj):
        '''学员注册'''
        print("\033[32;1m为学员[%s] 办理注册。\033[0m " % (stu_obj.name))
        self.stu_number.append(stu_obj)

    def hire(self,teach_obj):
        '''聘用老师'''
        print ("\033[32;1m聘用[%s] 老师。\033[0m " % (teach_obj.name))
        self.terch_number.append(teach_obj)

    def add_course(self,course_obj):
        '''开设课程'''
        self.course_number.append(course_obj)
    # def __del__(self):
    #     '''析构方法'''
    #     print("\033[31;1mmember [%s] is dead!\033[0m" % self.name)

class Course(object):#定义课程
    def __init__(self,co_name,co_tuition):
        self.co_name=co_name
        self.co_tuition=co_tuition



class SchoolMember(object):#父类,师生的父类

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell(self):
        print ('this is %s tell'%(self.name))
        # pass

    def __del__(self):
        '''析构方法'''
        print("\033[31;1mmember [%s] is dead...。\033[0m" % self.name)



class Teacher(SchoolMember):
    def __init__(self, name, age, course, salary,sch_obj):
        super(Teacher, self).__init__(name, age)#等于SchoolMember.__init__(name,age)
        self.course = course
        self.salary = salary
        self.sch_obj=sch_obj
        self.sch_obj.hire(self)

    def teaching(self):#定义子类自己的方法
        '''讲课方法'''
        print("Teacher [%s] is teaching [%s] for class [%s]" % (self.name, self.course, 's12'))

    def tell(self):#扩展父类的方法
        '''自我介绍方法'''
        SchoolMember.tell(self)#先继承父类的方法
        #下面是扩展父类的方法，如果没有上面的继承，就是覆盖了父类的方法
        msg = '''Hi, my name is [%s], works for [%s] as a [%s] teacher !''' % (self.name, self.sch_obj.sch_name, self.course)
        print(msg)


class Student(SchoolMember):
    def __init__(self, name, age, grade, sid,sch_obj):#扩展父类的初始化功能
        super(Student, self).__init__(name, age)#先继承父类的构造方法
        self.grade = grade#后扩展1，比如年级grade
        self.sid = sid#后扩展2，比如学号sid
        self.sch_obj=sch_obj
        self.sch_obj.enroll(self)#相关，把相关类的注册功能直接引入，这样学生在初始化时就登记注册

    def tell(self):#覆盖父类的tell方法
        '''自我介绍方法'''
        msg = '''Hi, my name is [%s], I'm studying [%s] in [%s]!''' % (self.name, self.grade, self.sch_obj.sch_name)
        print(msg)


# if __name__ == '__main__':
sc1=School('old_boy','沙河')

t1 = Teacher("Alex", 22, 'Python', 20000,sc1)
t2 = Teacher("TengLan", 29, 'Linux', 3000,sc1)

s1 = Student("Qinghua", 24, "Python S12", 1483,sc1)
s2 = Student("SanJiang", 26, "Python S12", 1484,sc1)

t1.teaching()
t2.teaching()

t1.tell()
t2.tell()

s1.tell()
s2.tell()


print  (sc1.stu_number[0].name,sc1.stu_number[1].name,sc1.terch_number[0].name,sc1.terch_number[1].name)

del s1 #析构方法没响应，因为就像linux，是个硬链接，有连接数，这个地址还有一个连接/
print  (sc1.stu_number)
# print s1.name
del sc1.stu_number[0] #删除这个后，这个内存地址的连接数为零，因此析构方法响应了。
print (sc1.stu_number,'---',s2)
print (sc1.stu_number[0].name,'---',s2.name)
print (sc1.stu_number[0].age,'---',s2.age)
print (sc1.stu_number[0].grade,'---',s2.grade)
print (sc1.stu_number[0].sid,'---',s2.sid)
print (sc1.stu_number[0].sch_obj.sch_name,'---',s2.sch_obj.sch_name)
print (sc1.stu_number[0].sch_obj.sch_addr,'---',s2.sch_obj.sch_addr)