'''
name='egon'
age=78

'''
# 数字类型：
#整型int
#用来表示：等级，年龄，身份证号，学号，id号
# level=10 #level=int(10)
# level=int(10)
# print(id(level),type(level),level)
# age=18
# empid=123123123213

#浮点型float
#用来表示：身高，体重，薪资
# salary=3.1 #salary=float(3.1)
# height=1.83
# print(id(salary),type(salary),salary)


# 字符串str：包含在引号（单引号，双引号，三引号）内的一串字符
# 用来表示：名字，家庭住址，描述性的数据
# s1='egon1'
# s2="egon1"
# s3="""
# egon3
# """
# s4='''
# egon3
# '''

# print(type(s1),type(s2),type(s3),type(s4))

# msg='helo "egon"'
# msg="helo 'egon'"
# print(msg)

#字符串拼接：+，*
# s1='hello            '
# s2='world'
# print(s1+s2)

# s1='hello            '
# print(s1*10)



#列表：定义在[]中括号内，用逗号分隔开多个值，值可以是任意类型
#用来存放多个值：多个爱好，多个人名
# stu_names=['asb','egon','wsb'] #stu_names=list(['asb','egon','wsb'])

# print(id(stu_names),type(stu_names),stu_names)
# print(stu_names[2])

# user_info=['egon',18,['read','music','dancing','play']]

# print(user_info[1])
# print(user_info[2][1])


#字典：定义{}内用逗号分隔开，每一个元素都是key:value的形式，其中value可以是任意类型，而key一定要是不可变类型
          #name    age    hobbies
# user_info={'name':'egon','age':18,'hobbies':['read','music','dancing','play']} #user_info=dict(...)
# # print(id(user_info),type(user_info),user_info)
#
# print(user_info['age'])
# print(user_info['hobbies'][3])



# info={
#     'name':'egon',
#     'hobbies':['play','sleep'],
#     'company_info':{
#         'name':'Oldboy',
#         'type':'education',
#         'emp_num':40,
#     }
# }
#
# print(info['company_info']['name'])


# students=[
#     {'name':'alex','age':38,'hobbies':['play','sleep']},
#     {'name':'egon','age':18,'hobbies':['read','sleep']},
#     {'name':'wupeiqi','age':58,'hobbies':['music','read','sleep']},
# ]
#
# print(students[1]['hobbies'][0])

# students={
#     'alex':{
#         'age':84,
#         'hobbies':['play','sleep']
#     },
#     'egon':{
#         'age':18,
#         'hobbies':['play',]
#     }
# }

# print(students['egon']['age'])


#布尔类型bool：True，False
#用途：判断
# age_of_oldboy=18
# inp_age=input('your age: ')
# inp_age=int(inp_age)
# if inp_age > age_of_oldboy:
#     print('猜大了')
# elif inp_age < age_of_oldboy:
#     print('猜小了')
# else:
#     print('猜对了')

# 布尔类型的重点知识！！！：所有数据类型，自带布尔值
#只有三种类型的值为False
    # 0
    # None
    # 空:'',[],{}
#其余全部为真

# if ['',]:
#     print('====>')
# l=[]
# print(l[0])

# if {'':'',}:
#     print('===?')

# if True:
#     print('===>?')


# 可变类型与不可变类型
# 可变：在id不变的情况，值可以改变
x=1
print(id(x),type(x),x)
x=2
print(id(x),type(x),x)

# x='abc'
# print(id(x),type(x),x)
# x='dec'
# print(id(x),type(x),x)


# x=['a','b','c']
# print(id(x),type(x),x)
# x[2]=10
# print(x)
# print(id(x),type(x),x)

# dic={'x':1,'y':2}
# print(id(dic),type(dic),dic)
# dic['x']=111111111
# print(dic)
# print(id(dic),type(dic),dic)


# 不可变类型：数字，字符串
# 可变类型：列表,字典
# dic={[1,2,3]:'a'}
