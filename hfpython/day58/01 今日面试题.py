"""
封装、继承、多态

1. 谈谈你对面向对象的理解？
2. Python面向对象中的继承有什么特点？
3. 面向对象深度优先和广度优先是什么？
4. 面向对象中super的作用？
5. 列举面向对象中特殊成员(带双下划线的特殊方法，如：__new__、__init__、__call__等)
6. 静态方法和类方法区别？
"""

# 谈谈你对面向对象的理解？
# 扩展方便，...

# Python面向对象中的继承有什么特点？
# 方便代码重用，可以多继承

# 面向对象深度优先和广度优先是什么？


# 面向对象中super的作用？



class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return "呵呵"



class Male(Person):
    def __init__(self, name, age):
        super().__init__(name, age)



# 列举面向对象中特殊成员(带双下划线的特殊方法，如：__new__、__init__、__call__等)
# __new__
# __init__
# __call__
# __str__   print打印一个对象时  __unicode__
# __repr__
# __doc__
# __getattr__
# __setattr__
# __del__


# 静态方法和类方法区别？
# 1. 静态方法： 相当于普通函数
# 2. 类方法： 通过类调用，第一个参数默认是类本身