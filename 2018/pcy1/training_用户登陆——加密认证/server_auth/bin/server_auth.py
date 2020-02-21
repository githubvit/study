#_*_coding:utf-8_*_
'''
服务端验证启动程序
'''


import sys,os
# 获取当前绝对路径
present_abs_path=os.path.abspath(__file__)#'__file__'表示当前文件，绝对不能少，否则报错
# 路径寻找，用目录名方法dirname逐级向上
Base_path=os.path.dirname(os.path.dirname(present_abs_path))
# 把找到的路径添加到sys.path环境列表
sys.path.append(Base_path)

from loging_authenticate import server_authenticate

server_authenticate.run()




