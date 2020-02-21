#-*- coding:utf8 -*-

'''
简单cs游戏，
有警察和恐怖分子两种角色，
我们接下来为每个角色开发以下几个功能
1，被打中后就会掉血的功能
2，开枪功能
3，换子弹
4，买枪
5，跑、走、跳、下蹲等动作
6，保护人质（仅适用于警察）
7，不能杀同伴
。。。
'''
class Role(object):
    #定义一个类， class是定义类的语法，Role是类名，(object)是新式类的写法，必须这样写，以后再讲为什么

    lif=456#类变量
    __life = 123#私有类变量
    def __init__(self,name,role,weapon,life_value=100,money=15000):
        #构造函数-z作用就是实例化，或叫类初始化函数，在生成一个角色时要初始化的一些属性就填写在这里
        #self：在类初始化时的对象名
        #实例变量：在类构造函数定义的self.变量，在类实例化（也就是初始化）时会生成该实例的变量。作用域就是实例本身。
        self.name = name
        self.role = role
        self.weapon = weapon
        self.__life_value = life_value #玩家不能随便改生命值，加__,就定义了该属性为私有，
        # 玩家看不到该属性，也不能通过d.name进行访问，因此也就没有办法改.这就是封装。
        self.__money = money #玩家不能随便改资金，因此也要封装

    def show_life_value(self):#你封装了生命值，但玩家有权查看自己的生命值，就要给他一个接口，因为在类的内部是可以访问私有属性。
        print ('%s life_value is %s'%(self.name,self.__life_value))
        print 'lei',self.__life #调用私有类变量

    def show__money(self):#money查看接口
        print ('%s money is %s'%(self.name,self.__money))

    def shot(self): #开枪
        print("%s is shooting..."%self.name)

    def got_shot(self):#被击中减血
        print("ah...,%s got shot..."%self.name)
        self.__life_value-=50

    def buy_gun(self, gun_name): #买枪功能实现
        print('%s has just bought %s' %(self.name,gun_name))
        self.__money -= 500

#1，把一个类变成一个具体对象的过程叫实例化
r1 = Role('Alex','police','AK47') #生成一个角色 , 会自动把参数传给Role下面的__init__(...)方法
r2 = Role('Jack','terrorist','B22')  #生成一个角色

#2，
r1.buy_gun('B21') #alex 买枪
r1.show__money()#查看alex的money少了500
r1.show_life_value()#查看alex的生命值
r2.shot()#jack射击
r1.got_shot()#alex中枪
r1.show_life_value()#alex的生命值少了50
print (r1.lif)