#-*- coding:utf8 -*-
import datetime,time
# 有date类：年月日；time类：时分秒；datetime类：年月日 时分秒
# 就用datetime类。
# 获取当前时间now
print datetime.datetime.now()
# 获取3天后的时间 datetime.timedelta(3)，该方法不能单独使用
print datetime.datetime.now()+datetime.timedelta(3)#传递了位置参数3给datetime.timedelta(3)方法，说明该方法的第一个参数是day。
# 获取3天前的时间
print datetime.datetime.now()+datetime.timedelta(-3)
# 获取3小时后的时间，关键字hours=3
print datetime.datetime.now()+datetime.timedelta(hours=3)
# 3分钟后的时间，关键字minutes=3
print datetime.datetime.now()+datetime.timedelta(minutes=3)
# 替换当前时间
c_time=datetime.datetime.now()
r_time=c_time.replace(year=2018,hour=3,minute=30)
#替换了年、小时和分钟，c_time不会被修改,
# 当然可用c_time=c_time.replace(year=2018,hour=3,minute=30)，修改。
print r_time
print c_time

print time.time()