#_*_coding:utf-8_*_

'''
属性方法的作用就是通过@property把一个方法变成一个静态属性
'''

#
# class Dog(object):
#     def __init__(self, name):
#         self.name = name
#
#     @property
#     def eat(self):
#         print(" %s is eating" % self.name)
#
#
# d = Dog("ChenRonghua")
# '''
# d.eat()
# 调用会出以下错误，
# 说NoneType is not callable,
# 因为eat此时已经变成一个静态属性了，
# 不是方法了，想调用已经不需要加()号了，直接d.eat就可以了
# '''
# d.eat
# --------------
'''
好吧，把一个方法变成静态属性有什么卵用呢？
既然想要静态变量，那直接定义成一个静态变量不就得了么？
well, 以后你会遇到很多场景是不能简单通过定义静态属性来实现的，

比如 ，你想知道一个航班当前的状态，是到达了、延迟了、取消了、还是已经飞走了， 

想知道这种状态你必须经历以下几步:

1. 连接航空公司API查询

2. 对查询结果进行解析 

3. 返回结果给你的用户

因此这个status属性的值是一系列动作后才得到的结果，
所以你每次调用时，其实它都要经过一系列的动作才返回你结果，
但这些动作过程不需要用户关心，用户只需要调用这个属性就可以了。
隐藏实现细节
'''


class Flight(object):
    def __init__(self, name):
        self.flight_name = name
        self.__status=None #私有变量，定义状态，模拟航空公司API航班状态接口

    def checking_status(self):#模拟连接航空公司API查询
        print("checking flight %s status " % self.flight_name)
        return self.__status

    @property #属性方法，把方法变成属性
    def flight_status(self):
        status = self.checking_status()#模拟 1，连接航空公司API查询
        # status=0
        # status=self.__status
        if status ==None:     #模拟 2，对查询结果进行解析
            print("flight got canceled...") #模拟 3，返回解析结果给你的用户
        elif status == 1:
            print("flight is arrived...")
        elif status == 2:
            print("flight has departured already...")
        else:
            print("cannot confirm the flight status...,please check later")

    @flight_status.setter  # 给属性赋值，修改status，模拟航班状态变化
    def flight_status(self, status):
        self.__status=status
        status_dic = {
            None: "canceled",
            1: "arrived",
            2: "departured"
        }
        print("\033[31;1mHas changed the flight status to \033[0m", status_dic.get(status))

    @flight_status.deleter  # 删除self.__status，模拟航班状态断开
    def flight_status(self):
        del self.__status
        print("status got removed...")


f = Flight("CA980")#实例化，模拟航班
f.flight_status #使用属性方式，模拟航班状态查询
f.flight_status = 2  # 触发@flight_status.setter，人工给status赋值，模拟航班接口状态变化了。
f.flight_status #变化后，再次查询航班状态
# del f.flight_status  # 触发@flight_status.deleter，删除status的值，模拟航空公司航班接口断开。
# f.flight_status #接口断开后，再次查询航班状态，应该报错。

