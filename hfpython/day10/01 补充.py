# *的应用场景

# def sum2(*args): #args=(1,2,3)
#     res=0
#     for num in args:
#         res+=num
#     return res
#
# print(sum2(1,2,3,4,5,6,7))

# ** 的应用场景
# def auth(name,pwd,**kwargs):
#     print(name)
#     print(pwd)
#     print(kwargs)
#
#
# # auth('egon','123')
# auth(name='egon',pwd='123',group='group1')





# def foo(x,y=1,*args,z,**kwargs):
#     pass



def foo(x,y=1):
    pass

def foo(x,*args,**kwargs):
    pass











