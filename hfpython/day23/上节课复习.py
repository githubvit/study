上节课复习：
    1 property
        用来将类内的函数伪装成一个数据属性

        class Foo:
            @property
            def name(self):
                pass

            @name.setter
            def name(self,value):
                pass

            @name.deleter
            def name(self):
                pass

        obj=Foo()
        obj.name

    2、classmethod
        将类中的一个函数绑定给类


    3、staticmethod
       将类中的一个函数解除绑定


    4、多态与多态性
        多态：同一种事物有多种形态
            在程序中用继承可以表现出多态

        多态性：
            可以在不考虑对象具体的类的情况下直接参考基类的标准使用对象

        python推崇鸭子类型：
            class Txt:
                def read(self):
                    pass

            class Disk:
                def read(self):
                    pass
            












今日内容：
    1、反射
    2、class机制提供的内置方法
        __str__
        __del__
        __call__

    3、元类（了解）

    4、异常处理
