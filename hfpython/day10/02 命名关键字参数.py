


def auth(*args,**kwargs):
    """
    使用方式auth(name="egon",pwd="123")
    :param args:
    :param kwargs:
    :return:
    """
    # print(args,kwargs)
    if len(args) !=0:
        print('必须用关键字的形式传参')
        return
    if 'name' not in kwargs:
        print('必须用指定的key名name')
        return
    if 'pwd' not in kwargs:
        print('必须用指定的key名pwd')
        return

    name=kwargs['name']
    pwd=kwargs['pwd']
    print(name,pwd)

# auth('egon','123')
# auth(name='egon',pwd='123') #约束函数的调用者必须用key=value的形式传值
# auth('egon',pwd='123')


# auth(name='egon',pwd='123')
# auth('egon',123)

# auth(x='egon',y='123')
# print(help(auth))

#什么是命名关键字参数？
#格式：在*后面参数都是命名关键字参数
#特点：
#1 必须被传值
#1 约束函数的调用者必须按照key=value的形式传值
#2 约束函数的调用者必须用我们指定的key名

# def foo(x,y,*,z):
#     print(x,y,z)
# foo(1,2)
# foo(1,2,3)
# foo(1,2,aaa=3)
# foo(1,2,z=3)

# def foo(y=1,x):
#     pass

def auth(*args,name,pwd):
    print(name,pwd)

#
# auth(pwd='213',name='egon')



# def register(name,age):
#     print(type(name),type(age))
#
# register(123,[1,2,3])