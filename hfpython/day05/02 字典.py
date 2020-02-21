# 1 用途：以key：value的形式存多个值
#     优点：存取都快，每一个值都有对应的key


# 2 定义方式:{}内以逗号分隔多个元素，格式为key:value，
# 其中key必须为不可变类型，value可以是任意类型
# dic={'x':1,'y':1,'x':1111} #dic=dict({'x':1,'y':1,'x':1111})
# print(dic)

dic=dict(x=1,y=2,z=3)
print(dic)


# 3 常用操作+内置的方法
#优先掌握的操作：
#1、按key存取值：可存可取
# dic={'name':'egon'}
# dic['age']=10
# print(dic)
# dic['name']='EGON'
# print(dic)

# dic['name']=dic['name'].upper()
# print(dic)

#2、长度len
# dic={'name':'egon','age':18}
# print(len(dic))


#3、成员运算in和not in:判断的字典的key

#4、删除
# dic={'name':'egon','age':18}
# del dic['name']
# print(dic)
# res=dic.pop('name')
# print(res)
# print(dic)

# res=dic.pop('sex',None)
# print(res)

#5、键keys()，值values()，键值对items()
# dic={'name':'egon','age':18}
# print(dic.keys())
# print(dic.keys())
# for x in dic.keys():
#     print(x)
# print(list(dic.keys())[0])

# print(dic.values())

# for key in dic.keys():
#     print(key)
# for value in dic.values():
#     print(value)

# print(dic.items())
# for k,v in dic.items(): #k,v=('name', 'egon')
#     print(k,v)

# print(type(dic.items()))


#4、掌握的操作
dic={'name':'egon','age':18}
# print(dic.get('namexxxxxxxxxxx'))
# print(dic['namexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'])


# print(dic.popitem())

# dic.setdefault()
# dic.update({'x':1,'age':19})
#对与老字典来说，更新指的是，新字典中有而老字典中没有则添加，新有而老有，则覆盖
# print(dic)

# dic.fromkeys()
# good_info={
#     'name':None,
#     'price':None,
#     'count':None
# }
# 'mac'  20000  10
# good_info['name']='mac'
# print({}.fromkeys(['name','age','sex'],None))
#{'name':None,'age':None,'sex':None}


# list1=['name','age','sex']
# dic={}
# for x in list1:
#     dic[x]=None
# print(dic)

# print({}.fromkeys(list1,None))
# print({}.fromkeys(['name','age','sex'],'xxxxxx'))






#setdefaul的用处：
# 1、字典有中有key，则不修改，返回原key对应的原值
# dic={'name':'egon','age':18}
# res=dic.setdefault('name','EGON')
# print('返回值',res)
# print(dic)

# 2、没有对应的key，则添加，返回添加的key对应的value
# dic={'age':18}
# res=dic.setdefault('name','EGON')
# print('返回值',res)
# print(dic) #{'age': 18, 'name': 'EGON'}



#总结
#1、存多个值
#2、无序
#3、可变
# dic={'x':1}
# print(id(dic))
# dic['x']=2
# print(dic)
# print(id(dic))
