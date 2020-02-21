#_*_coding:utf-8_*_


class Animal(object):
    def __init__(self,name):
        self.name=name

    @staticmethod   #静态属性方法，名义上归类管理，实际上跟类无关。
    def animal_talk(obj):#对外提供统一的接口
        obj.talk()#不同的对象会有不同的talk内容，也就是‘一种接口，多种实现’，实现的内容还是各自的类实现的。


class Dog(Animal):
    def talk(self):
        print ('%s is wo wo ..'%(self.name))

class Cat(Animal):
    def talk(self):
        print ('%s is miao miao ..'%(self.name))



d=Dog('alex')
c=Cat('jack')

# d.talk()#调用了Dog的talk
# c.talk()#调用了Cat的talk

Animal.animal_talk(d) #调用使用统一的talk接口,实际上还是在各自的类里面

Animal.animal_talk(c)