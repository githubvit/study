#一：基本使用
# str用途:描述性的数据,比如名字\国籍\学历\家庭住址

# 定义方式:在单引号或双引号或三引号内的一串字符
name='egon' #name=str('egon')
#掌握:
# str(10) #int('10')


#了解知识
# res=str(10)
# res=str([1,2,3,4])
# print(res,type(res))
# int('10')
# res=float('10.3')
# print(res,type(res))


# 常用操作+内置的方法
#优先掌握的操作：
#1、按索引取值(正向取+反向取) ：只能取
name='egon你好'
# print(name[0])
# print(name[4])
# print(name[1000])

# print(name[-1])
# print(type(name[-2]))
# name[-1]='坏'

#2、切片(顾头不顾尾，步长)
# msg='alex say my name is sb'
# print(msg[0:6])
# print(msg[0:6:2]) #alex s
#                   ae

#了解:
# print(msg[0:5:1])
# print(msg[3:1:-1])
# print(msg[-1:-5:-1])
# msg='alex is sb'
# print(msg[0:10:1])
# print(msg[:])
# print(msg[::1])
# print(msg[::-1])

#3、长度len
# msg='alex say my name is sb'
# print(len(msg)) # 字符的个数
#4、成员运算in和not in
# msg='alex say my name is sb'
# print('alex' in msg)
# print('alex' not in msg)

#5、移除空白strip
# s='*****egon****'
# print(s.strip('*'))
# s=s.strip('*')
# print(s)

# name='    egon     '
# print(name.strip())

# 改进
# name=input('用户名>>: ').strip()
# print(len(name))
# name=name.strip()
# if name == 'alex':
#     print('用户名正确')

#6、切分split
# info='egon:123:admin'
# res=info.split(':')
# print(res,type(res))
# print(res[0])
#
# cmd='get|a.txt|32123123'
# print(cmd.split('|'))

#7、循环
# msg='alex'

# i=0
# while True:
#     if i < len(msg):
#         print(msg[i])
#         i+=1
#     else:
#         break



# msg='alex'
#
# i=0
# while True:
#     if i == len(msg):
#         break
#     print(msg[i])
#     i+=1


# msg='alex'
#
# i=0
# while i < len(msg):
#     print(msg[i])
#     i+=1

msg='alex'
for item in msg: #item='l'
    print(item)

# for item in 11111: # 只有字符串,列表,字典
#     print(item)























# #二：该类型总结
# 存一个值or存多个值
#     只能存一个值
#     可以存多个值，值都可以是什么类型
# 有序or无序
# 可变or不可变
#     ！！！可变：值变，id不变。可变==不可hash
#     ！！！不可变：值变，id就变。不可变==可hash