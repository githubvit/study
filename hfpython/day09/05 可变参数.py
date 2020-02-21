'''
1 什么是可变长度参数
    可变长度指的参数的个数可以不固定,实参有按位置定义的实参和按关键字定义的实参,
    所以可变长的实参指的就是按照这两种形式定义的实参个数可以不固定,
    然而实参终究是要给形参传值的
    所以形参必须有两种对应的解决方案来分别处理以上两种形式可变长度的实参
    形参:
        *
        **


'''
# foo(1,2)
# foo(1,2,3)
# foo(1,2,3,4)
#
# foo(x=1,y=2,)
# foo(x=1,y=2,z=3)
# foo(x=1,y=2,z=3,a=1)
# foo(x=1,y=2,z=3,a=1,b=2)


#==========================形参里包含*与**

#*会将溢出的位置实参全部接收,然后保存成元组的形式赋值给args
# def foo(x,y,z,*args): #args=(4,5,6,7,8)
#     print(x,y,z)
#     print(args)
#
# foo(1,2,3,4,5,6,7,8,)


#**会将溢出的关键字实参全部接收,然后保存成字典的形式赋值给kwargs
# def foo(x,y,z,**kwargs): # kwargs={'c':3,'a':1,'b':2}
#     print(x,y,z)
#     print(kwargs)
#
# foo(x=1,y=2,z=3,a=1,b=2,c=3)
#





#==========================实参里包含*与**
# 一旦碰到实参加*,就把该实参的值打散
# def foo(x,y,z,*args): #args=([4,5,6,7,8],)
#     print(x,y,z)
#     print(args)
#
# foo(1,2,3,*[4,5,6,7,8]) #foo(1,2,3,4,5,6,7,8)
# foo(1,2,3,*(4,5,6,7,8)) #foo(1,2,3,4,5,6,7,8)
# foo(1,2,3,*'hello') #foo(1,2,3,'h','e','l','l','o')
#

#
# def foo(x,y,z):
#     print(x,y,z)

# foo(*[1,2,3]) #foo(1,2,3)
# foo(*[1,2,3,4]) #foo(1,2,3,4) #报错
# foo(*[1,2,]) #foo(1,2,) #报错


# 一旦碰到实参加**,就把该实参的值打散
# def foo(x,y,z,**kwargs):
#     print(x,y,z)
#     print(kwargs)
#
# foo(1,2,3,**{'a':1,'b':2}) #foo(1,2,3,b=2,a=1)


# def foo(x,y,z):
#     print(x,y,z)

# foo(1,**{'z':3,'y':2}) #foo(1,z=3,y=2)
# foo(1,**{'z':3,'y':2,'x':111}) #foo(1,z=3,y=2,x=111)




# 组合使用
def index(name,age,gender):
    print('welcome %s %s %s' %(name,age,gender))

def wrapper(*args,**kwargs): #args=(1,2,3),kwargs={'x':1,'y':2,'z':3}
    # print(args)
    # print(kwargs)
    index(*args,**kwargs) # index(*(1,2,3),**{'x':1,'y':2,'z':3}) # index(1,2,3,z=3,y=2,x=2)

# wrapper(1,2,3,x=1,y=2,z=3)

# wrapper(name='egon',age=18,gender='male')
wrapper('egon',age=18,gender='male')
wrapper('egon',18,gender='male')
wrapper('egon',18,'male')












