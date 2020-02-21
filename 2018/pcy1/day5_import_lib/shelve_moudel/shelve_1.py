#-*- coding:utf8 -*-

import shelve
import datetime

# shelve模块是一个简单的k,v将内存数据通过文件持久化的模块，可以持久化任何pickle可支持的python数据格式
d = shelve.open('shelve_test')  # 打开一个文件，建立shelve对象

# 序列化
# info={'age':22,'job':'it'}
# name=[1,2,'alex']
# d['info']=info #持久化字典 相当于pickle的dump
# d['name']=name #持久化列表
# d['now_time']=datetime.datetime.now() #持久化datetime
# d.close()

# # 反序列化
print (d.get('info')) #相当于pickle的load
print (d.get('name'))
print (d.get('now_time'))
print (d.items()) #一次性读取序列化中的所有元素。
d.close()