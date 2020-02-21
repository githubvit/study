#-*- coding:utf8 -*-

import module1
# print module1.name
# module1.sayhai()
print module1



# from module1 import *
#
# def logger():
#     print 'in import_m1'
#
# logger()
'''
这样，会运行本脚本下的logger（），
要运行module1中的logger（），
就要把from module1 import *写在def logger（）的后面
后面的def logger（）会覆盖前面的。
'''

# 从module1单独引入logger，另起别名log，就解决了冲突

# from module1 import logger as log
# def logger():
#     print 'in import_m1'
#
# logger()
# log()