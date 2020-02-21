#-*- coding:utf8 -*-
'''
用random模块实现验证码功能
验证码由整数和英文字符组成
'''

import random

# 首先定义验证码字符串
checkcode=''

# 实现4位验证码
for i in range(4):
    checkcode+=str(i)

# 实现4位随机数字验证码
for i in range(4):
    # 生成随机数字
    current=random.randint(0,9)
    checkcode+=str(current)

# 实现4位随机字母数字验证码
for i in range(4):
    # 生成一个随机数字，范围与上面相同
    current=random.randrange(4)
    #字母-->猜中了，就使用字母
    if i==current:
        #生成大写字母对应ascii码的随机整数
        tmp=random.randint(65,90)
        #把整数转成字母
        tmp=chr(tmp)
    # 数字-->没猜中，就使用数字
    else:
        tmp=random.randint(0,9)
    checkcode+=str(tmp)



print checkcode