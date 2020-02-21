#-*- coding:utf8 -*-
'''
时间模块
时间戳
时间元组
格式化时间
'''

import time
print  time.time()#获取当前时间戳
time.sleep(1)#睡1秒
print time.time()
print int(time.time()/3600/24/365+1970) #时间戳换算成大概的年份,取整。unix1970年诞生。

print time.timezone #与UTC差值 -28800/3600=8
print time.altzone#与UTC夏令时差 -32400/3600=9
print time.daylight #是否使用夏令时0表示不使用

# 一，time时间戳和struct_time时间元组之间的转换
# 1，将时间戳转换成时间元组
print time.gmtime(123456789)#将时间戳转换成UTC时间的元组，不传时间戳，就将当前时间戳转成UTC时间元组。
print time.gmtime()#不传时间戳，就将当前时间戳转成UTC时间元组。
print time.localtime(123456789)#将时间戳转换成本地时间的元组
print time.localtime()#不传时间戳，就将当前时间戳转成本地时间元组。

# 从时间元组取值的方法
x=time.localtime()
print x.tm_year,x.tm_mon,x.tm_mday

#2，将时间元组转换成时间戳，不能为空
print time.mktime(x)

# 二，struct_time时间元组和时间的格式化字符串之间的转换
# 1，时间元组转成格式化时间
print time.strftime('%Y-%m-%d %H:%M:%S',x)#将x时间元组转换成自定义格式'%Y-%m-%d %H:%M:%S'的字符串
print time.strftime('%Y-%m-%d %X',x)#%X可以取代%H:%M:%S
# 2，格式化时间转成时间元组
print time.strptime('2017-08-26 08:42:24','%Y-%m-%d %H:%M:%S')#将自定义格式'%Y-%m-%d %H:%M:%S'的字符串转换成时间元组struct_time
print time.strptime('2017-08-26 08:42:24','%Y-%m-%d %X')#效果和上面一样

#将时间元组转换成'Sat Jun 06 16:26:11 1998'格式字符串，如果没传入，就将当前时间元组转换为该格式
print time.asctime(x)

#将时间戳转换成换成'Sat Jun 06 16:26:11 1998'格式字符串，如果没传入，就将当前时间戳转换为该格式
print time.ctime()