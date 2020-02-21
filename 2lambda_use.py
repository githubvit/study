#一、匿名函数

# def func(a,b):
#     return a+b
# print (func(1,2))    
# print (lambda x,y : x+y) # 地址 即 func <function <lambda> at 0x0000013AC76A5558>
# print((lambda x,y : x+y)(1,2))  # 地址+() = func()  得到结果 3

#二、匿名函数 应用场景 callable
# 经常和max、min、sorted、map、filter、reduce等可迭代对象函数结合使用

#1. max、min

#取出工资最高或最低的人名
# salaries={
#     'egon':3000,
#     'alex':100000000,
#     'wupeiqi':10000,
#     'yuanhao':2000
# }

# print(max(salaries)) # yuanhao 很明显是错的，因为字典默认比的是key

# # 利用max函数的第二个参数key（不是字典的key），告诉max比较的是value不是key

# # 第二个参数是个callable(key: Callable[[_T], Any]=...)，会把每次next出来的对象call一下，
# # 再把call出来的结果交给max去比较。

# #定义callable：‘字典默认每次next取出来的是key，因此salaries[k]就是值了。
# # def get_value(k):
# #     return salaries[k]

# # print (max(salaries,key=get_value))

# #因为该callable只是給max用的，如果还要定义个函数体，再调用就麻烦了，因此就用lambda定义callable

# print(max(salaries,key=lambda k: salaries[k]))
# print(min(salaries,key=lambda k: salaries[k]))

# #2. sorted

# #按名字排序
# print(sorted(salaries))#默认就是 ['alex', 'egon', 'wupeiqi', 'yuanhao']
# #按收入排序 使用第二个参数key
# print(sorted((salaries),key=lambda k: salaries[k]))

# #按名字排序 并输出（key,value）列表
# #字典dic.items()经过.__iter__()可以把字典变成迭代器，
# # 该迭代器每次next出来的是（key，value）元组。
# print(salaries.items().__iter__().__next__()) # ('egon', 3000)

# print(sorted(salaries.items())) #默认就是拿名字比较，因为名字在元组的0号下标。
# # [('alex', 100000000), ('egon', 3000), ('wupeiqi', 10000), ('yuanhao', 2000)]

# #按收入排序 并输出（key,value）列表
# print(sorted(salaries.items(),key=lambda t: t[1]))
# # [('yuanhao', 2000), ('egon', 3000), ('wupeiqi', 10000), ('alex', 100000000)]

# #按收入从高到低派  使用第三个参数 reverse=true
# print(sorted(salaries.items(),key=lambda t: t[1],reverse=True))
# # [('alex', 100000000), ('wupeiqi', 10000), ('egon', 3000), ('yuanhao', 2000)]

# #3. 常用的 map reduce filter

# #3.1 map 映射 
# #对可迭代对象的每个元素，用第一个参数callable去call，得到新的迭代器。
# names=['alex','wpq','egon']

# n2=map(lambda i: 'oldboy_%s'%i,names)

# print (n2) #迭代器 <map object at 0x0000021D91B87308>

# print(list(n2)) #用列表看下 ，会把n2的元素都取空，因此下面的for就是空的，无输出。

# # ['oldboy_alex', 'oldboy_wpq', 'oldboy_egon']

# # (venv) D:\pyj\st>

# for item in n2:
#     print (item)

# #3.2 filter 过滤
# # 对可迭代对象的每个元素，用第一个参数callable去call，
# # 如果call的结果是True，就留下，从而得到新的迭代器。   
# names_f=['oldboy_alex', 'oldboy_wpq', 'oldboy_egon','sbq']

# nf=filter(lambda i: i.startswith('oldboy'),names_f)
# # nf=filter(lambda i: not i.startswith('oldboy'),names_f)

# print(nf)
# print(list(nf))

# #3.3 reduce 依次处理
# # 如果没有第三个参数（初始值），就先从可迭代对象next取一个初始值，
# # 接着还要next一下取第二个值，用第一个参数callable去call这两个值，
# # 后面只要next一下即可，用前面call的结果和新来的值接着call。
# from functools import reduce
# print(reduce(lambda x,y: x+y,range(1,101))) # 5050
# print(reduce(lambda x,y: x+y,range(1,101),100)) # 给定初值100 5150


