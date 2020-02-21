#-*- coding:utf8 -*-

import sys

# sys.path方法，可以列表形式得到当前文件运行的环境变量，也就是一个路径列表
# 标准库在lib目录下，第三方库一般会安装在lib\site-packages下。
print(sys.path)
# 返回操作系统平台名称
print sys.platform


# 标准输出
sys.stdout.write('please:') #在标准输出设备屏幕上输出please：对应print
# 标准输入
val = sys.stdin.readline()[:3] #在标准输入设备上输入，相当于raw_input,-1表示全部接收和默认的一样，0表示关闭，1表示接收1个字节，
#因为utf8一个中文就是3个字节，所以输入两个’中文‘字，var只会取出第1个’中‘字
sys.stdout.write(val)
print type(val)