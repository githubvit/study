#一：基本使用
# int用途:年龄,等级,各种号码
# 定义方式:
age=10 #age=int(10)

# float用途:身高,体重,薪资
# 定义方式:
height=1.81 #height=float(1.81)

# 常用操作+内置的方法
# print(bin(3)) #十进制转成二进制,0b11
# print(oct(8)) #十进制转成八进制,0o10
# print(10) #10
# print(hex(16)) #十进制转成十六进制,0x10


#二：int与float类型总结
# 存一个值or存多个值
#     只能存一个值

# 可变or不可变(了解:可变==不可hash,不可变==可hash)
#     ！！！可变：值变，id不变。
#     ！！！不可变：值变，id就变。
#
# age=18
# print(id(age))
# age=19
# print(id(age))


# salary=3.1
# print(id(salary))
# salary=3.2
# print(id(salary))


# print(hash(10))
# print(hash([1,2,3]))