"""
%和format的区别？
"""

# 定义一个敌人的坐标
c = (250, 250)
# 利用%进行字符串格式化
# print("向他开炮：%s" % c)
# print("向他开炮：%s" % (c, ))


# 用format进行字符串的格式化
# print("向他开炮：{}".format(c))


# format的常见用法
# l1 = ["Egon", 18]
# # s = "{} is {} years old.".format(l1[0], l1[1])
# s = "{} is {} years old.".format(*l1)
# print(s)

# 通过关键字
# d1 = {"name": "Egon", "age": 18}
# # s = "{name} is {age} years old.".format(d1["name"], d1["age"])
# s = "{name} is {age} years old.".format(**d1)
# print(s)


# 通过对象属性
# class Person():
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return "{self.name} - {self.age}".format(self=self)
#
#
# p1 = Person("Egon", 18)
# print(p1)


# 通过下标
# l1 = ["Egon", 18]
# # s = "{} is {} years old. {} 不要脸。".format(l1[0], l1[1], l1[0])
# # s = "{0} is {1} years old. {0} 不要脸。".format(l1[0], l1[1])
# s = "{0[0]} is {0[1]} years old. {0[0]} 不要脸。".format(l1)
# print(s)


# 填充与对齐
# print("egon".center(20, "*"))
# print("{:>10}".format("egon"))
# print("{:0>10}".format("egon"))
# print("{:*>10}".format("egon"))
# print("{:*^10}".format("egon"))
# print("{:*<10}".format("egon"))

# print("egon".zfill(18))

# print("{:.2f}".format(3.141592653))
# print("{:b}".format(10))
# print("{:d}".format(10))
# print("{:o}".format(10))
# print("{:x}".format(10))


# print("{:,}".format(1000000))