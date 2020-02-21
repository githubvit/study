# print(abs(-1))
# print(all([1,'a',True])) # 列表中所有元素的布尔值为真，最终结果才为真
# print(all('')) # 传给all的可迭代对象如果为空，最终结果为真

# print(any([0,'',None,False])) #列表中所有元素的布尔值只要有一个为真，最终结果就为真
# print(any([])) # 传给any的可迭代对象如果为空，最终结果为假

# print(bin(11)) #十进制转二进制
# print(oct(11)) #十进制转八进制
# print(hex(11)) #十进制转十六进制

# print(bool(0)) #0,None,空的布尔值为假

# res='你好egon'.encode('utf-8') # unicode按照utf-8进行编码，得到的结果为bytes类型
# res=bytes('你好egon',encoding='utf-8') # 同上
# print(res)

# def func():
#     pass
# print(callable('aaaa'.strip)) #判断某个对象是否是可以调用的，可调用指的是可以加括号执行某个功能

# print(chr(90)) #按照ascii码表将十进制数字转成字符
# print(ord('Z')) #按照ascii码表将字符转成十进制数字


# print(dir('abc')) # 查看某个对象下可以用通过点调用到哪些方法

# print(divmod(1311,25)) # 1311 25

# 将字符内的表达式拿出运行一下，并拿到该表达式的执行结果
# res=eval('2*3')
# res=eval('[1,2,3,4]')
# res=eval('{"name":"egon","age":18}')
# print(res,type(res))

# with open('db.txt','r',encoding='utf-8') as f:
#     s=f.read()
#     dic=eval(s)
#     print(dic,type(dic))
#     print(dic['egon'])


# s={1,2,3}
# s.add(4)
# print(s)

# 不可变集合
# fset=frozenset({1,2,3})

# x=111111111111111111111111111111111111111111111111111111111111111111111111111111111111
# # print(globals()) # 查看全局作用域中的名字与值的绑定关系
# # print(dir(globals()['__builtins__']))
# def func():
#     x=1
#     print(locals())
# # func()
# print(globals())

# 字典的key必须是不可变类型
# dic={[1,2,3]:'a'}
# 不可hash的类型list,dict,set==  可变的类型
# 可hash的类型int,float,str,tuple ==  不可变的类型
# hash()

def func():
    """
    帮助信息
    :return:
    """
    pass

# print(help(max))


# len({'x':1,'y':2}) #{'x':1,'y':2}.__len__()

# obj=iter('egon') #'egon'.__iter__()
# print(next(obj)) #obj.__next__()





















# 面向对象里讲
classmethod
staticmethod
property

delattr
hasattr
getattr
setattr

exec

isinstance
issubclass