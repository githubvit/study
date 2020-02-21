'''
1、语法
def 函数名(参数1,参数2,...):
    """
    文档描述
    """
    代码1
    代码2
    代码3
    return 值

def:定义函数的关键字
函数名：是用来调用函数的，
    函数名的命名必须能反映出函数的功能
文档描述：推荐写上，来增强函数的可读性
代码块：函数的功能实现代码
return：函数的返回值

'''

# print('========================')
# print('hello egon')
# print('========================')
#1.1 定义阶段
def print_sym(sym,count): #print_sym=<function print_msg at 0x000001B2A33698C8>
    print(sym*count)
    print(sym*count)
    print(sym*count)
    print(sym*count)
    print(sym*count)
    print(sym*count)
    print(sym*count)
    print(sym*count)
    print(sym*count)
    print(sym*count)
    print(sym*count)
    print(sym*count)
    print(sym*count)
    print(sym*count)
    print(sym*count)
    print(sym*count)
    print(sym*count)
    print(sym*count)
    print(sym*count)
    print(sym*count)
    print(sym*count)
    print(sym*count)
    print(sym*count)

def print_msg(msg):
    print('\033[045m%s\033[0m' %msg)

#1.2 调用阶段:函数名加括号就是在调用函数

# print(print_sym)
# print_sym('#',30)
# print_msg('hello egon')
# print_sym('#',30)


#2 定义函数的三种类型：
#2.1 有参函数:参数是函数体代码用来接收外部传入值的
# def max2(x,y): #x=100,=y101
#     # x=10
#     # y=3
#     if  x > y:
#         print(x)
#     else:
#         print(y)
#
# max2(100,101)







#2.2 无参函数:当函数体的代码逻辑不需要函数的调用者掺入值的情况下，就无参
# def func():
#     print('----------------------')
#     print('---soft run-----------')
#     print('----------------------')
#
# def interactive():
#     name=input('username>>: ').strip()
#     pwd=input('password>>: ').strip()
#     print(name,pwd)
#
# interactive() #定义时无参，意味着调用时也无须传入参数
# interactive() #定义时无参，意味着调用时也无须传入参数
# interactive() #定义时无参，意味着调用时也无须传入参数


#练习：
# uname_of_db='egon'
# pwd_of_db='123'
#
# def interactive():
#     uname_of_inp=input('username>>: ').strip()
#     pwd_of_inp=input('password>>: ').strip()
#     return uname_of_inp,pwd_of_inp
#
# def auth(uname,pwd):
#     if uname == uname_of_db and pwd == pwd_of_db:
#         print('登陆成功')
#     else:
#         print('登陆失败')
#
#
# res=interactive()
# x=res[0]
# y=res[1]
# # print(x)
# # print(y)
#
# auth(x,y)


#2.3 空函数:函数体为pass
def auth():
    """
    这是一个认证功能
    :return:
    """
    pass

def put():
    """
    上传功能
    :return:
    """
    pass

def get():
    """
    下在功能
    :return:
    """
    pass


def ls():
    """
    list contents
    :return:
    """
    pass