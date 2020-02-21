# 通过描述符机制来实现类型限制功能
class Typed:
    def __init__(self,name,expected_type):
        self.name=name
        self.expected_type=expected_type
        # print(self.name,self.expected_type)
    def __get__(self, instance, owner):
        # print('get--->',instance,owner)
        # 解决描述符用作为类属性调用时，保证给None，只有实例属性调用才可用。
        if instance is None:
            return None
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        # print('set--->',instance,value)
        # 保证传入的类型：即value是否是self.expected_type)
        if not isinstance(value,self.expected_type):
            # 如果不是就激发异常 报 self.expected_type类型错误
            raise TypeError('Expected %s' %str(self.expected_type))
        instance.__dict__[self.name]=value
    def __delete__(self, instance):
        print('delete--->',instance)
        instance.__dict__.pop(self.name)


class People:
    name=Typed('name',str)
    age=Typed('age',int)
    salary=Typed('salary',float)
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

# p1=People(123,18,3333.3)
# p1=People('egon','18',3333.3)
# p1=People('egon',18,3333)
# p1=People('egon',18,3333.0)
# print(p1.name,p1.age,p1.salary)
# print (People.name,People.age,People.salary)