# stus_linux=['alex','egon','张全蛋','李铁蛋','oldboy']
# stus_python=['李二丫','wxx','liudehua','alex','egon']
#
# stus_py_lx=[]
# for stu in stus_linux:
#     if stu in stus_python:
#         stus_py_lx.append(stu)
#
# print(stus_py_lx)

#用途
#1、 关系运算
#2、去重
# s1=set('hello')
# print(s1)

# l=['a','b',1,'a','a']
# print(list(set(l)))



#想去重还想保证原来的顺序：了解
# l = ['a', 'b', 1, 'a', 'a']
# l_new=[]
# s=set()

# for item in l:
#     if item not in s:
#         s.add(item) #s={'a','b',1}
#         l_new.append(item) #l_new=['a','b',1]




#定义方式:在{}内用逗号分隔开一个个元素
#注意的问题
#1、集合内没有重复的元素
#2、集合的元素必须是不可变类型

# s={1,2,3,4,4,4,4,4,4,4,'a'} #s=set({1,2,3,4,'a'})
# print(id(s),type(s),s)

# s={[1,2,3],'aa'}

#常用操作与内置方法
stus_linux={'alex','egon','张全蛋','李铁蛋','oldboy'}
stus_python={'李二丫','wxx','liudehua','alex','egon'}

#既报名linux又报名python的学生：交集
# print(stus_linux & stus_python)
# print(stus_linux.intersection(stus_python))

#所有的学生：并集
# print(stus_linux | stus_python)
# print(stus_linux.union(stus_python))


# 只报名linux，没有报名python的：差集
# print(stus_linux - stus_python)
# print(stus_linux.difference(stus_python))


# print(stus_python -  stus_linux)
# print(stus_python.difference(stus_linux))

# 没有同时报名两门课程的学生姓名：交叉补集
# print(stus_linux ^ stus_python)
# print(stus_linux.symmetric_difference(stus_python))


#优先掌握，循环取值
#长度len
#成员运算in和not in


# 查看
# s1={1,'a','b','c','d'}
# for item in s1:
#     print(item)

# 增加
s1={'a','b','c'}
# s1.add() # 一次添加一个值
# s1.add(4)
# print(s1)


# s1.update({3,4,5}) #一次添加多个值
# print(s1)

# 删除
# s1.discard() ## 当删除的元素不存在的时候，不会报错
# s1.discard(4)
# print(s1)

# s1.remove() # 当删除的元素不存在的时候，报错
# s1.remove(4)


# s1.pop() #随机取走一个元素
# res=s1.pop()
# print(res)





#了解的方法
# s1={1,2,3}
# s2={1,2}
# s1=s1.difference(s2)
# print(s1)
# s1.difference_update(s2)
# print(s1)




# s1.isdisjoint() #如果两个集合没有交集则返回True
# s1={1,2,3}
# s2={4,5,6}
# print(s1.isdisjoint(s2))
# print(s2.isdisjoint(s1))



# 了解的知识点
#父集:爹包含儿子
# s1={1,2,3}
# s2={1,2}
# print(s1.issubset(s2))
# print(s2.issubset(s1))
# print(s1.issuperset(s2))


# print(s1 > s2) # 代表s1包含s2，s1是s2父集
# print(s2 < s1) # s2是s1子集

# s3={1,2,3}
# s4={1,2,3}
# print(s3.issuperset(s4))
# print(s4.issuperset(s3))
# print(s3 == s4)
# print( s3 >= s4)
# print( s4 >= s3)



#总结