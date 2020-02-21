# import m1
# m1.f1()
# 模块的查找顺序是：
# 1、内存中已经加载的模块
# 2、内置模块
# 3、sys.path路径中包含的模块
# import time
#
# import m1
# m1.f1()
#
# time.sleep(15)
# import m1
# m1.f1()


# import sys
# print('time' in sys.modules)
# import time
# time.sleep(2)
# print('time' in sys.modules)

import sys
sys.path.append(r'D:\code\SH_fullstack_s1\day14\dir1')

import m1
m1.f1()


# 强调强调强调强调强调强调强调强调强调强调强调强调
# sys.path的第一个路径是当前执行文件所在的文件夹