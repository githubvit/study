# def func():
#     print('from func')
#
#
# func()
# func()
# func()

# def foo(x,n): #foo=函数的内存地址
#     return x ** n
#
# f=lambda x,n:x ** n
# # print(f)
# print(f(2,3))
# print(f(2,4))

#强调：
#1 匿名的目的就是要没有名字，给匿名函数赋给一个名字是没有意义的
#2 匿名函数的参数规则、作用域关系与有名函数是一样的
#3 匿名函数的函数体通常应该是 一个表达式,该表达式必须要有一个返回值
# def func(x,y,z):
#     return x+y+z

# lambda x,y,z:x+y+z

#lambda匿名函数的应用：
#max,min,sorted,
salaries={
    'egon':3000,
    'alex':100000000,
    'wupeiqi':10000,
    'yuanhao':2000
}

# 求工资最高的那个人是谁
def get(k):
    return salaries[k]
# print(max(salaries,key=get)) #'egon' 3000
# for k in salaries:
#     print(k) # 告诉max，比较的依据，k,salaries[k]

# print(max(salaries,key=lambda x:salaries[x])) #'egon' 3000


# 求工资最低的那个人是谁
# print(min(salaries,key=lambda x:salaries[x]))

# 把薪资字典，按照薪资的高低排序
# nums=[1,11,9]
# nums=sorted(nums) #默认是升序
# print(nums)


salaries={
    'egon':3000,
    'alex':100000000,
    'wupeiqi':10000,
    'yuanhao':2000
}
# salaries=sorted(salaries) # 默认按照字典的键排序
# print(salaries)

# salaries=sorted(salaries,key=lambda x:salaries[x])  #默认是升序排
# salaries=sorted(salaries,key=lambda x:salaries[x],reverse=True) #降序
# print(salaries)

# lambda与map,reduce，filter
# nums=[1,2,3,4,5]
# res=map(lambda x:x**2,nums)
# print(list(res))

# names=['alex','wupeiqi','yuanhao']
# res=map(lambda x:x+'_SB',names)
# print(list(res))

# names=['alex','wupeiqi','yuanhao','egon']
# res=map(lambda x:x+'_NB' if x == 'egon' else x + '_SB',names)
# print(list(res))


from functools import reduce
# res=reduce(lambda x,y:x+y,range(1,101),100)
# res=reduce(lambda x,y:x+y,range(1,101))
# print(res)

# l=['my','name','is','alex','alex','is','sb']
# res=reduce(lambda x,y:x+' '+y+' ',l)
# print(res)

#filter
# names=['alex_sb','wxx_sb','yxx_sb','egon']
# res=filter(lambda x:True if x.endswith('sb') else False,names)
# res=filter(lambda x:x.endswith('sb'),names)
# print(list(res))

# ages=[18,19,10,23,99,30]
# res=filter(lambda n:n >= 30,ages)
# print(list(res))

salaries={
    'egon':3000,
    'alex':100000000,
    'wupeiqi':10000,
    'yuanhao':2000
}
res=filter(lambda k:salaries[k] >= 10000,salaries)
print(list(res))



















