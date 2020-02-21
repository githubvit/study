#1 什么是模块？
# 模块就一系统功能的集合体，在python中，一个py文件就是一个模块，比如module.py,其中模块名module

#2 使用模块

#2.1 import 导入模块
#首次导入模块发生三件事
#1、创建一个模块的名称空间
#2、执行模块对应文件，将产生的名字存放于1中的名称空间
#3、在当前执行文件中拿到一个模块名，该模块名指向1的名称空间

x=1
def f1():
    pass

# import spam
#强调：之后的导入会直接引用第一次导入的结果，不会重复执行文件

# import spam
# import spam
# import spam
# import spam
# import spam

# print(spam)

# print(spam.money)
# spam.read1()


# 模块中功能的执行始终以模块自己的名称空间为准
# read1=111111
# print(spam.read1)

# money=1111111111111
# spam.read1()

# read1=11111111111111111111111111
# spam.read2()

# money=1111111111111111
# spam.change()
# print(money)
# spam.read1()


#3、为模块起别名
# import spam as sm
#
# print(sm.money)
# sm.read1()


engine=input('>>: ').strip()
if engine == 'mysql':
    import mysql as db
elif engine == 'oracle':
    import oracle as db
db.parse()


#4、一行导入多个模块(不推荐使用)
# import spam,mysql,oracle

#推荐写成多行
import spam
import mysql
import orcacle





