class People:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def __str__(self):
        # print('========>')
        return '<名字：%s 年龄：%s 性别：%s>' %(self.name,self.age,self.sex)

obj=People('egon',18,'male')
print(obj) #print(obj.__str__())

# l=list([1,2,3])
# print(l)


