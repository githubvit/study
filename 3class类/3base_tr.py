class Teacher:
    '说明'
    school='oldbody'
    cont=0
    def __init__(self,name,age,sex,level,salary):
        self.name=name
        self.age=age
        self.sex=sex
        self.level=level
        self.salary=salary
        Teacher.cont +=1 #直接写cont不行，必须加类名

    def teach(self):
        print ('%s teach....'%self.name)

teach1=Teacher('egon',18,'男','1','2000')
teach2=Teacher('alex',28,'男','1','3000')
teach3=Teacher('wpq',38,'男','1','4000')

#查看老师的数量
print(dir(Teacher))

print(teach1.__dict__,Teacher.cont)
print(Teacher.__dict__)

