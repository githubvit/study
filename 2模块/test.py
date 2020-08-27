import time,datetime
a1=['a','b']
b1=['c','d']
if 'b' in a1 and 'd'==b1[a1.index('b')]:
    print('ok')
else:
    print('no')
# for a in a1:
#     b1.append(a)
# a1=[]
# print(b1)
# 取下标
# print(a1[0])
# print(a1.index('b'))
# a2=[0.01,0.02,0.03]
# if a2:
# 求和
#     print(sum(a2))
# else:
#     print('keyi')
# 取时间格式
# time1=datetime.datetime.now()
# y=str(time1.year)
# m=str(time1.month)
# d=str(time1.day)
# h=str(time1.hour)
# mt=str(time1.minute)
# time_code=''.join((y,m,d,h,mt))#要用列表或元组框一下，否则报错
# pwd='710102'
# print(f'{pwd[0]}')
# print(time_code)#年取后两位，月取两位，时取两位 ，分取两位
# 
# t1=time.time()
# print(t1)#1597995398.2831595
# time.sleep(1)
# t2=time.time()
# 
# print(t2>t1)
# 
# print(time.localtime(t1))# 生成时间的元组  time.struct_time(tm_year=2020, tm_mon=8, tm_mday=21, tm_hour=15, tm_min=41, tm_sec=29, tm_wday=4, tm_yday=234, tm_isdst=0)
# 将时间的元组格式生成时间戳 精确到秒。
# print(time.mktime(time.localtime(t1)))#1597995398.0 已经小于t1了，只能精确到秒，舍弃小数部分，没有四舍五入。
# 获取当前时间的日期 加上 23:45:00 组成 %Y-%m-%d %X 格式 
# t_f=f'{y}-{m}-{d} 23:45:00'
# 将该格式 转为元组 再转为 时间戳
# t_c=time.mktime(time.strptime(t_f,'%Y-%m-%d %X'))
# t_n=time.time()
# 
# dt=t_c-t_n
# h,ys=divmod(dt,3600)
# m,s=divmod(ys,60)
# print(f'当前距离23:45分 还有{h:.0f}小时{m:.0f}分钟{s:.0f}秒')




