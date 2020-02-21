import sys
sys.path.append('D:\\pyj\\st\\找到我') #加入系统路径，便于文件查找
print (sys.path)
# 函数在python中是第一类对象？

#1、可以被引用
# x=1
# y=x

# def bar():
#     print('from bar')
#
# f=bar
# f()

#2、可以当中参数传入
# x=1
# def func(a):
#     print(a)
#
# func(x)



# def bar():
#     print('from bar')
#
# def wrapper(func): #func=bar
#     func() #bar()
#
# wrapper(bar)


#3、可以当中函数的返回值
# x=1
# def foo():
#     return x
#
# res=foo()
# print(res)



# def bar():
#     print('from bar')
#
# def foo(func): #func=<function bar at 0x00000225AF631E18>
#     return func #return <function bar at 0x00000225AF631E18>
#
#
# # print(bar)
# f=foo(bar) #f=<function bar at 0x00000225AF631E18>
# # print(f)
# f()


#4、可以当中容器类型的元素
# x=1
# l=[x,]
#
# print(l)

# def get():
#     print('from get')
#
# def put():
#     print('from put')
#
# l=[get,put]
#
# # print(l)
# l[0]()










# def func():
#     print('from func')

#1、func可以被引用
# f=func
# f()

#2、func可以当作参数传给x
# def bar(x):
#     print(x)
#     x()
#
# bar(func)

#3、func还可以当作返回值
# def bar(x): # x=func
#     return x #return func

# res=bar(func) #res=func
# print(res)
# res()


#4 可以当中容器类型的元素
# def auth():
#     print('登陆。。。。。')

# def reigster():
#     print('注册。。。。。')

# def search():
#     print('查看。。。。')

# def transfer():
#     print('转账。。。。')

# def pay():
#     print('支付。。。。')

# dic={
#     '1':auth,
#     '2':reigster,
#     '3':search,
#     '4':transfer,
#     '5':pay
# }

# print(dic)
# dic['2']()

# def interactive():
#     while True:
#         print("""
#         1 认证
#         2 注册
#         3 查看
#         4 转账
#         5 支付
#         """)
#         choice=input('>>: ').strip()
#         if choice in dic:
#             dic[choice]()
#         else:
#             print('退出')
#             break


# interactive()

# l=[auth,reigster,search,interactive]
# print(l)