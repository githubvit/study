# class Foo:
#     n=0
#     def __init__(self):
#         Foo.n+=1 # Foo.n=3
#
#
# obj1=Foo()
# obj2=Foo()
# obj3=Foo()
# print(obj1.__dict__)
# print(obj2.__dict__)
# print(obj3.__dict__)
#
# print(obj1.n)
# print(obj2.n)
# print(obj3.n)


# class Bar:
#     n=1111111111
#     def __init__(self,x):
#         self.x=x
#
# obj=Bar(111)
#
# # print(obj.__dict__)
# # print(obj.n)
# obj.y=2
# obj.n=3
# print(obj.__dict__)
# print(obj.n)
#
# obj.x=123
# del obj.x
# print(obj.x)


'''
现实中的对象：
    人1
        特征：
            名字='刘晴政'
            攻击力=60
            生命值=100
        技能：
            咬

    人2
        特征：
            名字='王苗璐'
            攻击力=50
            生命值=100
        技能：
            咬

现实中的人类
    相同的特征
    相同的技能
        咬
'''



'''
现实中的对象：
    狗1
        特征：
            名字='武培其'
            品种="京巴"
            攻击力=80
            生命值=50
        技能：
            咬

    人2
        特征：
            名字='李杰'
            品种="藏獒"
            攻击力=200
            生命值=200
        技能：
            咬

现实中的狗类
    相同的特征
    相同的技能
        咬
'''
class People:
    def __init__(self, name, aggresivity, life_value=100):
        self.name = name
        self.aggresivity = aggresivity
        self.life_value = life_value

    def bite(self, enemy): #self=p1   enemy=d1
        enemy.life_value-=self.aggresivity
        print("""
        人[%s] 咬了一口狗 [%s]
        狗掉血[%s]
        狗还剩血量[%s]
        """ %(self.name,enemy.name,self.aggresivity,enemy.life_value)
        )

class Dog:
    def __init__(self, name, dog_type, aggresivity, life_value):
        self.name = name
        self.dog_type = dog_type
        self.aggresivity = aggresivity
        self.life_value = life_value

    def bite(self, enemy): #self = d1    enemy= p1
        enemy.life_value-=self.aggresivity
        print("""
        狗[%s] 咬了一口人 [%s]
        人掉血[%s]
        人还剩血量[%s]
        """ %(self.name,enemy.name,self.aggresivity,enemy.life_value)
        )


p1 = People('刘清政', 60)
d1=Dog('李杰',"藏獒",200,200)


# p1.bite(d1)

d1.bite(p1)
