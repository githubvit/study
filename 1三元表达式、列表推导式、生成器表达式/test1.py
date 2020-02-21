def my_max(x,y):
    if x>=y:
        return x
    else:
        return y

#上面是条件判断的函数，根据不同的条件返回不同的值。用了5行。

#三元表达式： 1行
#格式：a= true的结果 if 条件 else false的结果

x=30
y=20
p=x if x>=y else y
print (p)

name=input(">>").strip()
res='sb' if name =='alex' else 'nb'
print (res)

#列表推导式 ：生成列表
#下10个蛋
egg=[]
for i in range(1,11):
    e='egg'+str(i)
    egg.append(e)
print (egg)    

egg2=['egg'+str(i) for i in range(1,11)]
print (egg2)

#下蛋升级版 只要6到10号蛋，前面的蛋不要
egg3=[]
for i in range(1,11):
    if i>=6:
        e='egg'+str(i)
        egg3.append(e)
print(egg3)

egg4=['egg'+str(i) for i in range(1,11) if i>=6]
print (egg4)

#生成器表达式
#下蛋终极版 无限下蛋 
# 与列表推导式的唯一区别就是括号。
#其结果是生成器generator对象。

egg5=('egg'+str(i) for i in range(1,100000000000000000000000000000))
print (egg5) # <generator object <genexpr> at 0x00000183E368A9C8>

print(next(egg5))
print(next(egg5))
print(next(egg5))
print(next(egg5))
print(next(egg5))
print(next(egg5))