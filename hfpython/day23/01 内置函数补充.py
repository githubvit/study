class Foo:
    pass

obj=Foo()
# print(isinstance(obj,Foo)) # 推荐使用该函数来判断一个函数的类型
# print(type(obj) is Foo)

# print(isinstance('abc',str))
# print(isinstance(123,int))


print(issubclass(Foo,object))