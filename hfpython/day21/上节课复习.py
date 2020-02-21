上节课复习：
    1、继承
       继承是一种新建类的方式
       新建的类称为子类或派生类
       父类称为基类或超类

       python中的继承的支持一个子类可以同时继承多个父类

    2、新式类与经典类
        新式类：
            继承object的类及其子类都是新式类

            在python3中如果一类没有继承任何父类
            那么默认继承object类，即在python3中所有的类都是
            新式类

        经典类：（只在python2中才有）
            not继承object的类及其子类都是经典类


        二者的区分：
            在菱形继承下
                经典类：深度优先查找
                新式类：广度优先查找

    3、如何查找继承关系；
        先抽象
            抽象对象之间相似之处得到了类
            再总结类与类之间的相似得到父类
        再继承
            子类继承父类，子类可以遗传父类的属性


    4、属性查找
        obj.x
        1、先从obj.__dict__
        2、对象的类.__dict__
        3、父类.__dict__
        ..........

    5、派生
       子类定义的名字会覆盖父类的同名属性
       class Parent:
            x=1
            def f1(self):
                print('from parent')

       class Sub(Parent):
            z=3

            def f1(self):
                #Parent.f1(self)
                super(Sub,self).f1() #super会检索Sub.mro()
                print('from sub')




今日内容：
    1、组合
    2、封装
    3、多态
