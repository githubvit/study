#1、property：

class People:
    def __init__(self,name,weight,height):
        self.__name=name
        self.wt=weight
        self.ht=height

    @property
    def bmi(self):
        return self.wt / (self.ht ** 2)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,obj): #obj='EGON'
        if not isinstance(obj,str):
            raise TypeError('名字的值必须是str类型')
        self.__name=obj #self.__name='EGON'

    @name.deleter
    def name(self):
        del self.__name

# p=People('egon',75,1.80)
# print(p.bmi)

# print(p.name)
# p.name='EGON'
# p.name=123
# print(p.name)

# del p.name



#2、classmethod
#3、staticmethod

import settings
import uuid

class Mysql:
    def __init__(self,host,port):
        self.host=host
        self.port=port

    def tell_info(self):
        print("<%s:%s>" %(self.host,self.port))

    @classmethod
    def from_conf(cls):
        return cls(settings.HOST, settings.PORT)

    @staticmethod
    def create_id():
        return uuid.uuid4()
# conn1=Mysql('127.0.0.1',8080)
# conn1.tell_info()

conn2=Mysql.from_conf()
# conn3=Mysql.from_conf()
#
#
# conn2.tell_info()
# conn3.tell_info()
#
#

print(conn2.tell_info)
print(Mysql.from_conf)

print('#'*50)
# print(conn2.create_id)
# print(Mysql.create_id)

print(conn2.create_id())
print(Mysql.create_id())