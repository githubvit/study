#-*- coding:utf8 -*-

import sys
import os

print sys.path    #打印当前文件的相对路径，sys.path是list
print os.path.abspath(__file__)   #打印当前文件的绝对路径
print os.path.dirname(os.path.abspath(__file__))    #去掉文件名，保留目录名，返回上一级目录，不是module2所在目录
print os.path.dirname(os.path.dirname(os.path.abspath(__file__)))     #再向上返回上一级目录package2，到达module2所在目录
path_module2=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path_module2)   #把module2所在路径加入sys.path路径列表，当然也可以用列表的insert（0，path）方法加入列表的第一位。
print sys.path

import module2 #成功引入会显示'终于找到我’
module2.test1()