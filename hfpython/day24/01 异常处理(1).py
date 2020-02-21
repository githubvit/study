'''
1、什么是异常
    异常是错误发生的信号，
    程序一旦出错，如果程序中还没有相应的处理机制
    那么该错误就会产生一个异常抛出来
    程序的运行也随之终止

2、一个异常分为三部分：
    1、异常的追踪信息
    2、异常的类型
    3、异常的值

3、异常的分类：
    1、语法异常：
        这类异常应该在程序执行前就改正
        print('start....')
        x=1
        x+=1
        if
        print('stop....')

    2、逻辑上的异常

'''
# IndexError
# l=['a','b']
# l[100]

# KeyError
# d={'a':1}
# d['b']

# AttributeError:
# class Foo:
#     pass
#
# Foo.x
# import os
# os.aaa


# ZeroDivisionError
# 1 / 0


# FileNotFoundError
# f=open('a.txt','r',encoding='utf-8')

# ValueError: I/O operation on closed file.
# f=open('a.txt','r',encoding='utf-8')
# f.close()
# f.readline()

#ValueError: invalid literal for int() with base 10: 'aaaaa'
# int('aaaaa')


# TypeError
# for i in 333:
#     pass

#NameError
# x
# func()




# def func():
#     import os
#     os.xxxx
#
# func()



# 语法：

# 单分支
# try:
#     print('start.....')
#     x=1
#     y
#     l=[]
#     l[3]
#     d={'a':1}
#     d['b']
#     print('end....')
# except NameError:
#     print('变量名没有定义')
#
#
# print('other.....')



# 多分支
# try:
#     print('start.....')
#     x=1
#     # y
#     l=[]
#     l[3]
#     d={'a':1}
#     d['b']
#     print('end....')
# except NameError:
#     print('变量名没有定义')
# except KeyError:
#     print('字典的key不存在')
# except IndexError:
#     print('索引超出列表的范围')
#
#
# print('other.....')




# 多种异常采用同一段逻辑处理
# try:
#     print('start.....')
#     x=1
#     # y
#     l=[]
#     # l[3]
#     d={'a':1}
#     d['b']
#     print('end....')
# except (NameError,KeyError,IndexError):
#     print('变量名或者字典的key或者列表的索引有问题')


# print('other.....')


# 万能异常
# try:
#     print('start.....')
#     x=1
#     # y
#     l=[]
#     # l[3]
#     d={'a':1}
#     # d['b']
#     import os
#     os.aaa
#     print('end....')
# except Exception:
#     print('万能异常---》')
#
#
# print('other.....')



# 获取异常的值
# try:
#     print('start.....')
#     x=1
#     y
#     l=[]
#     l[3]
#     d={'a':1}
#     d['b']
#     import os
#     os.aaa
#     print('end....')
# except Exception as e:
#     print('万能异常---》',e)
#
#
# print('other.....')




# try:
#     print('start.....')
#     x=1
#     # y
#     l=[]
#     l[3]
#     d={'a':1}
#     d['b']
#     import os
#     os.aaa
#     print('end....')
# except NameError as e:
#     print('NameError: ',e)
#
# except KeyError as e:
#     print('KeyError: ',e)
#
# except Exception as e:
#     print('万能异常---》',e)
#
#
# print('other.....')



# try....else...
# else: 不能单独使用，必须与except连用，意思是：else的子代码块会在被检测的代码没有出现过任何异常的情况下执行

# try:
#     print('start.....')
#     # x=1
#     # # y
#     # l=[]
#     # l[3]
#     # d={'a':1}
#     # d['b']
#     # import os
#     # os.aaa
#     print('end....')
# except NameError as e:
#     print('NameError: ',e)
#
# except KeyError as e:
#     print('KeyError: ',e)
#
# except Exception as e:
#     print('万能异常---》',e)
#
# else:
#     print('在被检测的代码块没有出现任何异常的情况下执行')
# print('other.....')


# try...finally....
# try:
#     print('start.....')
#     # x=1
#     # # y
#     # l=[]
#     # l[3]
#     # d={'a':1}
#     # d['b']
#     # import os
#     # os.aaa
#     print('end....')
# except NameError as e:
#     print('NameError: ',e)
#
# except KeyError as e:
#     print('KeyError: ',e)
#
# except Exception as e:
#     print('万能异常---》',e)
#
# else:
#     print('在被检测的代码块没有出现任何异常的情况下执行')
# finally:
#     print('无论有没有异常发生，都会执行')
# print('other.....')




# finally的子代码块中通常放回收系统资源的代码
# try:
#     f=open('a.txt',mode='w',encoding='utf-8')
#     f.readline()
#
# finally:
#     f.close()
#
# print('other....')




# 主动触发异常
# raise TypeError('类型错误')

# class People:
#     def __init__(self,name):
#         if not isinstance(name,str):
#             raise TypeError('%s 必须是str类型' %name)
#
#         self.name=name
#
# p=People(123)




# 断言
# print('part1........')
# # stus=['egon','alex','wxx','lxx']
# stus=[]
#
#
# # if len(stus) <= 0:
# #     raise TypeError
# assert len(stus) > 0
#
# print('part2.........')
# print('part2.........')
# print('part2.........')
# print('part2.........')
# print('part2.........')
# print('part2.........')



# 自定义异常
# class RegisterError(BaseException):
#     def __init__(self,msg,user):
#         self.msg=msg
#         self.user=user
#
#     def __str__(self):
#         return '<%s：%s>' %(self.user,self.msg)
#
# raise RegisterError('注册失败','teacher')
#





age=input('>>: ').strip() #age='aaa'

if age.isdigit():
    age=int(age)

    if age > 10:
        print('too big')
    elif age < 10:
        print('too small')
    else:
        print('you got it')


