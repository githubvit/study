#_*_coding:utf-8_*_

class Dog(object):
    def __init__(self,name):
        self.name=name

    def talk(self):
        print ('%s talking is wang wang ...'%self.name)


d=Dog('chengronghua')

# print d.name
# d.talk()

# 下面通过输入来调用
chioce=raw_input('>>')#输入name
# print d.chioce #报错 AttributeError: 'Dog' object has no attribute 'chioce'

# 1,判断有没有输入的属性或方法 hasattr(obj,str)

# print hasattr(d,chioce)

# 2,调用输入的属性或方法getattr(obj,str)
#
# 调用属性getattr(obj,str)
# print getattr(d,chioce)
#
# 调用方法getattr(obj,str)（）
# getattr(d,chioce)()

# 3,设定输入的属性或方法 setattr(obj,str,value)

# 给d对象设定age属性
setattr(d,chioce,'a')
print getattr(d,chioce)

# 给d对象设定eat方法
# def eat(self):
#     print ('%s is eating 骨头...'%self.name)
# if hasattr(d,chioce):
#     getattr(d, chioce)()
# else:
#     setattr(d,chioce,eat)
#     getattr(d,chioce)(d)

# 4,删除输入的属性或方法delattr(obj,str)
# 删除属性
# setattr(d,chioce,22)
# print getattr(d,chioce)
# delattr(d,chioce)
# print getattr(d,chioce)#会报错AttributeError: 'Dog' object has no attribute 'age'
# 删除方法
#