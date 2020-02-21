
class Person(object):

    def __init__(self, name):
        self.name = name


    def sleep(self):
        print("{} 在睡觉！".format(self.name))
        return self


    def play_majiang(self):
        print("{} 在打麻将".format(self.name))
        return self


p1 = Person("张学友")
# 链式调用 原理就是 调用一个实例化方法返回的是当前的实例对象
p1.sleep().play_majiang()
