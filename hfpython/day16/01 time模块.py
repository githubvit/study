import time

# 时间分为三种形式
#1、时间戳
# print(time.time())
# start_time=time.time()
# time.sleep(3)
# stop_time=time.time()
# print(stop_time-start_time)


#2、格式化的字符串
# print(time.strftime('%Y-%m-%d %H:%M:%S %p'))
# print(time.strftime('%Y-%m-%d %X %p'))

#3、struct_time对象
# print(time.localtime()) # 上海：东八区
# print(time.localtime().tm_year)
# print(time.localtime().tm_mday)

# print(time.gmtime()) # UTC时区


# 了解的知识
# print(time.localtime(1111111111).tm_hour)
# print(time.gmtime(1111111111).tm_hour)


# print(time.mktime(time.localtime()))

# print(time.strftime('%Y/%m/%d',time.localtime()))
# print(time.strptime('2017/04/08','%Y/%m/%d'))


# print(time.asctime(time.localtime()))
# print(time.ctime(12312312321))





