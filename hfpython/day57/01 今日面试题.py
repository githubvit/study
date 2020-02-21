#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/6/4


"""
1. os和sys都是干什么的？
2. 你工作中都用过哪些内置模块？
3. 有没有用过functools模块？
"""

# os是系统相关的，sys是与系统交互

import os
# BASE_DIR = os.path.abspath(__file__)  # 取当前文件的绝对路径
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 取当前文件的父目录的路径
#
# path = os.path.join(BASE_DIR, "abc")  # 在当前父目录下拼接一个abc的文件夹路径
#
# path = BASE_DIR + "\\abc"  # 不推荐使用硬编码的形式拼接路径

import sys

# sys.path.append()  # 向当前运行的环境变量中添加一个指定的路径



# 2. 你工作中都用过哪些内置模块？

# re json hashlib time datetime socket thread functools

from functools import partial

def f(a, b):
    return a + b

f(1, 2)
f(100, 200)
f3 = partial(f,3)  # 利用partial和f生成一个默认加3 的一个f3函数
ret = f3(100)  # 默认加3
print(ret)


# if __name__ == '__main__':
#     print(sys.argv)
#     print(sys.argv[1])
#     print(sys.argv[2])