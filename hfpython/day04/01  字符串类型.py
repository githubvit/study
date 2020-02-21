# 需要掌握的方法

#1、strip,lstrip,rstrip
# print('**sss****'.lstrip('*'))
# print('**sss****'.rstrip('*'))

#2、lower,upper
# print('Egon'.lower())
# print('egon'.upper())

#3、startswith,endswith
# print('alex is sb'.startswith('alex'))
# print('alex is sb'.endswith('sb'))


#4、format的三种玩法
#第一种：{}
# s1='my name is %s my age is %s' %('egon',18)
# s2='my name is {} my age is {}'.format('egon',18)
# print(s1)
# print(s2)


# s1='my name is %s my age is %s' %('egon',18,19)
# s2='my name is {} my age is {}'.format('egon',18,19)
# print(s1)
# print(s2)

#第二种
# s2='my name is {0} my age is {1} {1} {1} {0} {1}'.format('egon',18,19)
# print(s2)

#第三种
# s2='my name is {name} my age is {age}'.format(age=18,name='egon')
# print(s2)


#5、split,rsplit
# cmd='get|C:\a.txt|3333'
# print(cmd.split('|',1))
# print(cmd.rsplit('|',1))


#6、join
cmd='egon:123:admin:rwx'
l=cmd.split(':')
# res=''.join(l)
# res=':'.join(l)
# res='          '.join(l)
# print(res,type(res))
# print(l)
# print('%s:%s-%s-%s' %(l[0],l[1],l[2],l[3]))

# ':'.join([1,2,3]) # join方法传入的列表必须只包含str类型的元素


#7、replace
# msg='wupeiqi say my name is wupeiqi'
# print(msg.replace('wupeiqi','SB'))
# print(msg.replace('wupeiqi','SB',1))

#8、isdigit
# print('10'.isdigit())

# age=10
# inp=input('>>: ').strip()
# if inp.isdigit():
#     inp=int(inp)
#     if inp > age:
#         print('too big')
# else:
#     print('输入数据非法')

# 其他操作（了解即可）
#1、find,rfind,index,rindex,count
# msg='my egon hegon 123'
# print(msg.find('sb'))
# print(msg.find('egon'))
# print(msg.find('egon',8,20))
# print(msg.rfind('egon'))

# print(msg.index('sb'))
# print(msg.index('egon'))


#2、center,ljust,rjust,zfill
# print('========================egon=======================')
# print('egon'.center(50,'*'))
# print('egon'.ljust(50,'*'))
# print('egon'.rjust(50,'*'))
# print('egon'.zfill(50))

#3、expandtabs
# msg='abc\tdef'
# print(msg.expandtabs(3))

#4、captalize,swapcase,title
# print('abeCdEF'.capitalize())
# print('abeCdEF'.swapcase())
# print('my name is egon'.title())

#5、is数字系列
num1=b'4' #bytes
num2=u'4' #unicode,python3中无需加u就是unicode
num3=u'肆' #中文数字
num4=u'Ⅳ' #罗马数字

#isdigit():bytes,unicode的阿拉伯数字
# print(num1.isdigit())
# print(num2.isdigit())
# print(num3.isdigit())
# print(num4.isdigit())

#isdecimal():unicode的阿拉伯数字
# print(num2.isdecimal())
# print(num3.isdecimal())
# print(num4.isdecimal())

#isnumberic:unicode的阿拉伯数字\中文数字\罗马数字
# print(num2.isnumeric())
# print(num3.isnumeric())
# print(num4.isnumeric())

#6、is其他
# print('asdfasdfasdfaAsfd'.isalpha()) #字符全由字母组成

# print('asdf'.isalnum()) #字符由字母或数字组成
# print('I Am Egon'.istitle())
# print('    '.isspace())
# print('print'.isidentifier())



#总结字符串类型：
'''
1 存一个值
    只能存一个值

2 有序or无序
    有序

3 可变or不可变
    ！！！不可变：值变，id就变。不可变==可hash
'''