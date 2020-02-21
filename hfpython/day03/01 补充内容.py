#1、赋值方式：
#1.1 链式赋值
# x=1
# y=x
# y=x=a=b=c=1
# print(id(y),id(c))

#1.2 交叉赋值
m=1
n=2

# temp=m
# m=n
# n=temp
# print(m,n)
# m,n=n,m
# print(m,n)

#1.3 变量的解压
# salaries=[11,12,13,14,15]
# mon1_sal=salaries[0]
# mon2_sal=salaries[1]
# mon3_sal=salaries[2]
# mon4_sal=salaries[3]
# mon5_sal=salaries[4]

# mon1_sal,mon2_sal,mon3_sal,mon4_sal,mon5_sal=salaries
#
# print(mon1_sal)
# print(mon2_sal)
# print(mon3_sal)
# print(mon4_sal)
# print(mon5_sal)
#
# salaries=[11,12,13,14,15,16,17]
# mon1_sal,mon2_sal,mon3_sal,mon4_sal,mon5_sal=salaries
#
# salaries=[11,12]
# mon1_sal,mon2_sal,mon3_sal,mon4_sal,mon5_sal=salaries



salaries=[11,12,13,14,15]
# mon1_sal,mon2_sal,_,_,mon5_sal=salaries

# mon1_sal,_,_,_,mon5_sal=salaries
# mon1_sal,*_,mon5_sal=salaries
# print(mon1_sal,mon5_sal)


# *_,x,y=salaries
# print(x,y)


#2、input与raw_input
#在python3中：
    # input() #把用户输入的内容全都存为字符串类型

#在python2中：
    # raw_input() #把用户输入的内容全都存为字符串类型
    # input('>>: ') #必须输入明确的数据类型,输入什么就存成什么类型
    # int(input('>>:::::'))

#3、while+else

count=1
while count < 6:
    if count == 4:
        break
    print(count)
    count+=1
    # break
else:
    print('else的代码块只有在while循环没有被break打断的情况下才执行(最后执行)')












