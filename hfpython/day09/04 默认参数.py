'''
1 默认参数
    在定义阶段,已经为某个形参赋值,那么该形参就称为默认参数

'''
#注意:
#1 定义阶段已经有值,意味着调用阶段可以不传值
# def register(name,age,sex='male'):
#     print(name,age,sex)
#
#
# register('egon',18,)
# register('alex',73,'female')
# register('wxx',84,)
# register('xxx',84)
# register('yy',84)

#2 位置形参必须在默认参数的前面
# def func(y=1,x): #错误
#     pass

#3 默认参数的值只在定义阶段赋值一次,也就是说默认参数的值再定义阶段就固定死了
# m=10
# def foo(x,y=m):
#     print(x,y)
#
# m='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
# foo(1)
# foo(1,11)

#4 记住:默认参数的值应该设置为不可变类型

# def register(name,hobby,l=[]): #name='wxx',hobby='play'
#     l.append(hobby) #l=['play']
#     print(name,l) # wxx ['play']

# register('wxx','play')  # wxx ['play']
# register('alex','read') # alex ['read']
# register('egon','music') # alex ['music']
#

# register('wxx','play',[])  # wxx ['play']
# register('alex','read',[]) # alex ['read']
# register('egon','music',[]) # alex ['music']


def register(name,hobby,l=None):
    if l is None:
        l=[]
    l.append(hobby) #l=['play']
    print(name,l) # wxx ['play']

register('wxx','play')  # wxx ['play']
register('alex','read') # alex ['read']
register('egon','music') # alex ['music']



# 应用:
# 对于经常需要变化的值,需要将对应的形参定义成位置形参
# 对于大多数情况值都一样的情况,需要将对应的形参定义成默认形参







