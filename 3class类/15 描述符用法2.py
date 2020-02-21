# 一 利用描述符原理完成一个自定制@classmethod
# class ClassMethod:
#     def __init__(self,func):
#         self.func=func

#     def __get__(self, instance, owner): #类来调用,instance为None,owner为类本身,实例来调用,instance为实例,owner为类本身,
#         def feedback():
#             print('在这里可以加功能啊...')
#             return self.func(owner)
#         return feedback

# class People:
#     name='linhaifeng'
#     @ClassMethod # say_hi=ClassMethod(say_hi)
#     def say_hi(cls):
#         print('你好啊,帅哥 %s' %cls.name)

# People.say_hi()

# p1=People()
# p1.say_hi()
#疑问,类方法如果有参数呢,好说,好说

class ClassMethod:
    def __init__(self,func):
        self.func=func

    def __get__(self, instance, owner): #类来调用,instance为None,owner为类本身,实例来调用,instance为实例,owner为类本身,
        def feedback(*args,**kwargs):
            print('在这里可以加功能啊...')
            return self.func(owner,*args,**kwargs)
        return feedback

class People:
    name='linhaifeng'
    @ClassMethod # say_hi=ClassMethod(say_hi)
    def say_hi(cls,msg):
        print('你好啊,帅哥 %s %s' %(cls.name,msg))

# People.say_hi('你是那偷心的贼')

p1=People()
p1.say_hi('你是那偷心的贼')

# 二 利用描述符原理完成一个自定制的@staticmethod

class StaticMethod:
    def __init__(self,func):
        self.func=func

    def __get__(self, instance, owner): #类来调用,instance为None,owner为类本身,实例来调用,instance为实例,owner为类本身,
        def feedback(*args,**kwargs):
            print('在这里可以加功能啊...')
            return self.func(*args,**kwargs)
        return feedback

class People:
    @StaticMethod# say_hi=StaticMethod(say_hi)
    def say_hi(x,y,z):
        print('------>',x,y,z)

People.say_hi(1,2,3)

p1=People()
p1.say_hi(4,5,6)