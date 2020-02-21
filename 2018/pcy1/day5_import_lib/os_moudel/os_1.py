#-*- coding:utf8 -*-

import os,sys
# os模块提供对操作系统进行调用的接口，实现对文件或目录的增删改查：
# 1,获取当前工作目录，即当前python脚本工作的目录路径，类似linux下的pwd
# print os.getcwd()
# 2，切换目录，相当于shell下的cd
# os.chdir('..')
# print os.getcwd()
# # # 3，返回当前目录：（‘.’）
# # os.curdir
# # print os.getcwd()
# #
# # # 4，获取当前目录的父目录的字符串名：（‘..’）
# print os.pardir
# # # 5，生成多层递归目录
# # # os.makedirs(r'd:\a\b\c\d')
# # # 6，递归删除空目录，从d到a用来清理空文件夹。
# # # os.removedirs(r'd:\a\b\c\d')
# # # 7，生成单级目录
# # # os.mkdir(r'd:\a')
# # # 8，删除单级空目录
# # # os.rmdir(r'd:\a')
# # # 9，列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
# print os.listdir(r'.')
# # # 10，删除一个文件
# # # os.remove(r'd:\a.txt')
# # # 11，重命名文件/目录
# # # os.rename(r'd:\a.txt',r'b.txt')#'d:\a.txt'没了，在当前目录下D:\wksp1\pcy1\day5_import_lib多了个b.txt。
# # # 12，获取文件/目录信息
# print os.stat(r'b.txt')
# # # 13，输出操作系统特定的路径分隔符，win下为'\\',linux下为'/',可实现跨平台。
# print os.sep
# # # 14,输出当前平台的行终止符，win下为'\r\n',linux下为'\n'
# # print os.linesep
# # 15，当有多个路径时，输出用于分割文件路径的字符串，win下为';'，linux下为':'
# print os.pathsep
# # >>> os.linesep
# # '\r\n'
# # >>> os.sep
# # '\\'
# # >>> os.pathsep
# # ';'
# # 16，输出当前平台类型名字的字符串。win->'nt',linux->'posix'
# # >>> os.name
# # 'nt'
# # 17，运行shell命令，直接显示
# # os.system('dir')#调用系统命令,不保存结果，返回0值，和linux一样表示执行成功
# #
# # cms=os.popen('dir').read() # popen调用系统命令,保存结果在内存临时地址，通过read读出来
# # print cms.decode('gbk')
# # 18，获取系统环境变量os.environ
x=os.environ #字典格式
for i in x:
    print i,'=',x[i]
#对比sys.path获取的是当前程序及相关支持文件的路径列表
for j in sys.path:
    print j
# # 19，获取当前文件的绝对路径
# print  os.path.abspath(__file__)
# # 20，将path分割成目录和文件名二元组返回
# print os.path.split(r'c:\a\b\c\a.txt')#('c:\\a\\b\\c', 'a.txt')
#
# # 21，返回上一级目录。
# print os.path.dirname(os.path.abspath(__file__))
# # 22，只取path最后的文件名。如果path以/或\结尾，那么就会返回空值，即os.path.spilt(path)的第二个元素
# print os.path.basename(os.path.abspath(__file__))
# # 23，如果path存在，返回True，如果path不存在，返回False。
# print os.path.exists(r'c:\a\b\c\a.txt')
# print os.path.exists(os.path.abspath(__file__))
# # 24，如果path是绝对路径，返回True win下有多个根c:\,d:\等，linux下只有一个根/.
# print os.path.isabs(r'c:\a')
# # >>> os.path.isabs(r'c:\a')
# # True
# # >>> os.path.isabs(r'c:')
# # False
# # >>> os.path.isabs(r'/a/b/c')
# # True
# # 25，如果path是一个存在的文件，返回True，等于做了两件是1，存在吗，2，是文件吗
# # >>> os.path.isfile(r'c:\a.txt')#这个文件不存在
# # False
# # >>> os.path.isfile(r'c:\sparkraw.log')
# # True
#
# # 26，如果path是一个存在的目录，返回True
# # >>> os.path.isdir(r'c:')
# # True
#
# # 27，将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
# # >>> os.path.join('c:','\a','b','c.txt')#没有r
# # 'c:\x07\\b\\c.txt'
# # >>> os.path.join('c:','a','b','c.txt')#没有r也没有\
# # 'c:a\\b\\c.txt'
# # >>> os.path.join('c:',r'\a','b','c.txt')#对于win，在盘符后跟r'\'
# # 'c:\\a\\b\\c.txt'
# # 28，返回path所指向的文件或者目录的最后存取时间
# # >>> os.path.getatime(r'c:\sparkraw.log')
# # 1482173508.5647464
#
# # 29，返回path所指向的文件或者目录的最后修改时间
# # >>> os.path.getmtime(r'c:\sparkraw.log')
# 1503641703.3386898