#首次导入模块发生三件事
#1、创建一个模块的名称空间
#2、执行模块对应文件，将产生的名字存放于1中的名称空间
#提示：from 。。。 import。。与import前两件事一模一样
#3、在当前名称空间中直接拿到模块中的名字，可以直接使用，不用加任何前缀

# import spam # spam.名字

#

# from spam import money,read1,read2,change
# print(money)
# read1()
# read2()
# change()

# import spam
# print(money)

# 注意：
# 1、同import，执行模块中的功能，始终以模块的名称空间为准
# money=1111111111
# change()
# print(money)

#2、from ... import 名字，拿到的名字可以不加前缀直接使用，使用起来更加方便
#当问题是容易与当前执行文件中相同的名字冲突
# money=1111111111111111
# print(money)
# read1=1111111
# read1()



# 起别名
# from spam import money as m
# print(m)

# 在一行导入多个
# from spam import money,read1,read2


#from ... import *
# from spam import *
#
# print(money)
# print(read1)
# print(read2)
# print(change)

# from spam import *
# print(money)
# print(read1)
# print(read2)





import spam

