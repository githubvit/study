'''
1 绑定方法：
    在类内部定义的函数，默认就是给对象来用，而且是绑定给对象用的,称为对象的绑定方法
    绑定对象的方法特殊之处：
        应该由对象来调用，对象来调用，会自动将对象当作第一个参数传入

    绑定到类的方法特殊之处：
        应该由类来调用，类来调用，会自动将类当作第一个参数传入


'''
import settings

class People:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def tell(self):
        print('%s：%s' %(self.name,self.age))

    @classmethod
    def from_conf(cls):
        return cls(settings.NAME,settings.AGE)


# p=People('egon',19)
# p.tell()

# p1=People(settings.NAME,settings.AGE)
# p1.tell()

# p2=People(settings.Name,settings.AGE)


# p3=People('alex',74)
# p3.tell()

# print(People.from_conf)
# p4=People.from_conf(People)
# print(People.from_conf)
# p4=People.from_conf()
# p4.tell()


#2、staticmethod:非绑定方法，就是一个普通函数
#特性：既不跟类绑定，也不跟对象绑定，这意味着谁都能用
#谁来用都是一个普通函数，也就是说没有自动传值的特性了
import settings
import hashlib
import time

class People:
    def __init__(self,name,age):
        self.uid=self.create_id()
        self.name=name
        self.age=age

    def tell(self):
        print('%s: %s：%s' %(self.uid,self.name,self.age))

    @classmethod
    def from_conf(cls):
        return cls(settings.NAME,settings.AGE)

    @staticmethod
    def create_id():
        m=hashlib.md5()
        m.update(str(time.clock()).encode('utf-8'))
        return m.hexdigest()

obj=People('egon',18)
# print(obj.uid,obj.name,obj.age)
# obj.tell()

# print(obj.create_id)
# print(People.create_id)

print(obj.create_id())
print(People.create_id())