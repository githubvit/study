
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

stu2=OldboyStudent('王大炮',28,'male')

# print(id(stu2))
# print(type(stu2)) # 类与类型是一个概念
# print(stu2)

l1=[1,2,3] #l1=list([1,2,3])
# print(type(l1))
# l1.append(4)
list.append(l1,4)
print(l1)

l2=['a','b','c']
l2.append('d')
# list.append('d')
print(l2)

print(int)
print(str)
print(dict)
print(tuple)
print(set)
print(OldboyStudent)