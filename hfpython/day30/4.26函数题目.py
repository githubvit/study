# 4.26函数题：

# 1.设有函数：
def def1():
    res1='egon'
    def def2():
        res1='afen'
        return res1
    print('1')
    return def2
# 思考：执行函数def1()()的结果是什么。

# 2.什么是函数的递归？递归有什么特性和要求？

# 3.设有函数：
def foo1(n):
    print(n)
    if n>0:
        n-=1
        foo1(n)
    elif n==0:
        n-=2
        return n
    else:
        return 'oldboy'


def foo2():
    res=foo1(5)
    print(res)

# 思考foo2()最终能不能打印出res，如果能，得到的返回值是什么，如果不能，为什么？如何修改才能取到？

# 4.什么是形参，什么是实参，位置参数，关键字参数，默认参数，可变长参数，
#   关键字参数又是什么？他们之间有哪些注意点？

# 5.用递归算出1-100的和

# 6.独立写出1-50的积

# 7.时间多的同学可以写一个字符串计算器，以前的选做题
#     计算 ：
res='1-2*((-60-2*(-3+40.0/5)*(9-2*5/3+7/3*-99/4*2998+10*568/14))-(-4*3)/(16-3*2))'











# 1. 1  afen
#2.递归调用是函数嵌套调用的一种特殊形式，函数在调用时，直接或间接调用了自身，就是递归调用
# www.cnblogs.com/linhaifeng/articles/7580830.html
# 3.返回None,因为递归没有层层返回，应该在if n>0条件最后面改为return foo(n)
# 4.www.cnblogs.com/linhaifeng/articles/7531972.html
# 5   def foo(n,count=0,w=0):
#         w+=count
#         if count<n:
#             count+=1
#             foo(n,count,w)
#         else:
#             print(w)
#     foo(100)

# 6.略

# 7.# 阿枫计算器～～～～
#计算连一起的乘除，如p='-2*6*5/3'
import re
print('欢迎使用阿枫计算器～～～')
res=input('请输入您想计算的表达式：')

# 计算连一起的乘除，不限个数
def foo_mul_dicv(dv):
    list11=re.findall('[\*\/]?-?\d+\.?\d*',dv)
    list111=[]
    list121=[]
    for i in list11:
        if '/' not in i:
            if '*'in i:
                i=float(i[1:])
                list111.append(i)
            else:
                i=float(i)
                list111.append(i)
        else:
            i=float(i[1:])
            list121.append(i)
    count_11=1
    for i in list111:
        count_11*=i
    for i in list121:
        count_11/=i
    return count_11

#计算加减法
def foo_plus_cut(pc):
    if '--' in pc:
        pc = pc.replace('--', '+')
    res_pc=re.findall('-?\d+\.?\d*',pc)
    for i in res_pc:
        count=float(res_pc[0])+float(res_pc[1])
        return count

#没有括号的计算加减乘除
def digit(res2):
    if re.search('[\*\/]',res2):
        res21 = re.search('\d+\.?\d*[\/\*]-?\d+\.?\d*', res2).group()
        res22=foo_mul_dicv(res21)
        res_end=res2.replace(res21,str(res22))
        if re.search('[\+\-\*\/]',res_end):
            return digit(res_end)
        else:
            return res_end
    else:
        if re.search('-?\d+\.?\d*[\+\-]-?\d+\.?\d*',res2):
            res31=re.search('-?\d+\.?\d*[\+\-]-?\d+\.?\d*',res2).group()
            res32=foo_plus_cut(res31)
            res_end=res2.replace(res31,str(res32))
            if len(re.findall('-?\d+\.?\d*',res_end))>1:
                return digit(res_end)
            a=res_end
            return a
        else:
            return res2

# 找到最里边的括号：
def foo_Ncount(m):
    res1 = re.search('\(([\+\-\*\/]*\d+\.?\d*)+\)', m).group()
    res2 = res1[1:-1]
    count=digit(res2)
    res0 = m.replace(res1, str(count))
    return res0

#主运行程序
def foo_count(res):
    m=res
    if '(' in m:
        res=foo_Ncount(m)
        return foo_count(res)
    else:
        if re.search('[\+\-\*\/]',m):
            res=digit(m)
            return res
        else:
            return m

print('您得到的结果为%s'%foo_count(res))

