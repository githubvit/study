#一：基本使用
# 1 用途：存放多个值

# 2 定义方式：[]内以逗号为分隔多个元素，列表内元素无类型限制
# l=['a','b','c'] #l=list(['a','b','c'])
# l1=list('hello')
# print(l1)

# 3 常用操作+内置的方法
#优先掌握的操作：
#1、按索引存取值(正向存取+反向存取)：即可改也可以取
l=['a','b','c']
# print(id(l))
# print(l[-1])
# l[0]='A'
# print(id(l))
# print(l)
# l[3]='d' # 报错


#2、切片(顾头不顾尾，步长)
# stus=['alex','egon','wxx','yxx','lxx']

# print(stus[1:3])

#3、长度
# stus=['alex','egon','wxx','yxx','lxx']
# print(len(stus))

#4、成员运算in和not in
# stus=['alex','egon','wxx','yxx','lxx']
# print('alex' in stus)

#5、追加
# stus=['alex','egon','wxx','yxx','lxx']
# stus.append('wupei')
# stus.append('peiqi')
# print(stus)
# 插入
# stus=['alex','egon','wxx','yxx','lxx']
# stus.insert(1,'艾利克斯')
# print(stus)

#6、删除
stus=['alex','egon','wxx','yxx','lxx']
# del stus[1]
# print(stus)
# stus.remove('alex')
# print(stus)

# stus.pop(1)
# stus.pop() # 默认删除末尾
# print(stus)

# res1=stus.remove('alex') # 单纯的删除
# print(res1)
# res2=stus.pop(0) # 取走一个值
# print(res2)

#7、循环
# stus=['alex','egon','wxx','yxx','lxx']
#依赖索引
# i=0
# while i < len(stus):
#     print(stus[i])
#     i+=1

# for i in range(len(stus)):
#     print(i,stus[i])

# 不依赖索引
# for item  in stus:
#     print(item)


#补充for循环
# for i in range(0,5,2): #0  2  4
#     print(i)
# for i in range(10):#默认从零起始
#     print(i)

# for i in range(10,-2,-1):
#     print(i)


# 需要掌握的操作
stus=['alex','egon','alex','wxx','yxx','lxx']
# print(len(stus)) # stus.__len__()

# print(stus.count('alex'))
# stus.extend(['a','b','c'])
# print(stus)
# stus.append(['a','b','c'])
# print(stus)


# print(stus.index('alex',1,5))

# stus.reverse()
# print(stus)

# l=[1,10,3,12]
# l.sort(reverse=True)
# print(l)


# 大前提：只能同类型直接比较大小，对于有索引值直接的比较是按照位置一一对应进行比较的
# s1='hello'
# s2='hf'
# print(s1 > s2)

# l1=[3,'a','b','c']
# l2=['xxx','d']
# print(l1 > l2)



# print('Z' > 'a')
#A-Za-z
# print('a' > 'B')






# 了解
# stus.clear()
# print(stus)
# l=stus.copy()
# print(l)



#练习：
#队列：先进先出
l1=[]

#入队
# l1.append('first')
# l1.append('second')
# l1.append('third')
# print(l1)
#出队
# print(l1.pop(0)) #['second', 'third']
# print(l1.pop(0)) #['third']
# print(l1.pop(0)) #[]

#堆栈：先进后出
l1=[]
#入栈
l1.append('first')
l1.append('second')
l1.append('third')
#出栈
print(l1.pop())
print(l1.pop())
print(l1.pop())


#总结列表类型：
'''
1 存多个值

2 有序

3 可变
'''















