上节课复习
    1、继承
        什么是继承？
            继承是一种新建类的方式，新建的类称为子类或派生类
            父类又称为基类、超类

            子类可以“遗传”父类的属性，从而可以减少代码冗余

        如何寻找继承关系？
            先抽象，再继承，继承描述的就是 一种父子关系/从属关系

        继承的语法
            class Foo1:
                pass
            class Foo2:
                pass

            class Bar(Foo1,Foo2):
                pass

            class Bar: # 在python3中没有继承任何类的类，默认继承object
                pass

        派生
            class Parent:
                x=1
                def f1(self):
                    pass

            class Sub(Parent):
                def f2(self):
                    pass
                def f1(self):
                    pass

        新式类与经典类：
            新式类：继承object类的子类，以及该子类的子类。。。
                在python3中全都是新式类

            经典类：没有继承object的子类，以及该子类的子类。。。
                只有在python2中才有经典类，在python2中没有继承任何类的子类不会
                默认继承object类
                class Foo(object):
                    pass


            经典类与新式类的区别：在菱形继承上
                经典类：深度优先查找
                新式类：广度优先查找
                    Foo.mro()

        在子类定义的方法中重用父类的功能：
            方式一：与继承无关
                指定道姓地调用某一个类的函数：
                    类名.函数名(对象,参数1，参数2,...)

            方式二：严格依赖继承
                super(自己的类名,self).绑定方法(参数1，参数2，。。。)


        组合
            作用：
                 组合与继承的作用一样，都是用来减少类与类之间的重复代码

            定义：
                A类的对象具备某一个属性，该属性的值是B类的对象
                基于这种方式就把A类与B类组合到一起
                对象既能使用A类中的数据与功能，也能使用B类中的数据与功能


    2、封装
        什么是封装？
            封装（从字面意思理解）就是隐藏，隐藏指的是在类内部将一个属性藏起来
            让类外部的使用者无法直接用到。在py中就是用__开头将一个属性藏起来.

            补充说明：封装绝对不是单纯意义的隐藏
            需知定义属性的目的就是为了让使用者去用，使用者要想使用类内部隐藏的属性
            需要类的设计者在类内部开一个接口（定义一个方法），在该方法内访问隐藏的属性
            ，使用者以后就通过该方法来“间接地”访问内部隐藏的属性
            作为类的设计者可以在接口之上附加任意逻辑从而严格控制类的使用者对属性的操作


            class People:
                def __init__(self,name):
                    self.__name=name

                def tell_name(self):
                    # 添加逻辑
                    return self.__name

            obj=People('egon')
            #obj.__name
            obj.tell_name()

            封装函数属性:隔离复杂度
            class ATM:
                def __card(self):
                    print('插卡')
                def __auth(self):
                    print('用户认证')
                def __input(self):
                    print('输入取款金额')
                def __print_bill(self):
                    print('打印账单')
                def __take_money(self):
                    print('取款')

                def withdraw(self):
                    self.__card()
                    self.__auth()
                    self.__input()
                    self.__print_bill()
                    self.__take_money()





今日内容
    1、property
    2、多态
    3、classmethod，staticmethod


