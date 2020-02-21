# -*- coding: utf-8 -*-
'''
版面到期控制，输出版面需要的queryset。
# 判断期限：
    定义显示列表adv_li = [],
    更牛逼的做法定义显示字典：adv_dic={} 首位：[对象列表]
    # 1，从状态为‘上线’即1的queryset对象中去取，取得上线内容列表；
    
    # 2，循环该内容列表，用期数字段去获取每个对象的到期时间，
        #注意时区,Django配置DateTimeField使用timezone的datetime格式，而datetime.now是不包含timezone信息的。
        #2.1，取得对象的到期时间=更新日期+期数*每期时间
        #2.2，注意时区转换，转换为本地时间
        #2.3，将本地时间转为时间戳
        
    # 3，和当前时间比较，
        #3.1,未到期继续留用，将该对象加入显示列表
        #3.2,到期，找到替补新对象，注意是该位置的对象，不是其他位置的，
        #从状态为‘预备’即0的对象中去取替补，按id正向取，即先取最小的，将其状态置改为上线为1，填补被剔除的对象。
            #3.2.1 如果替补对象不存在，会报异常，处理异常，让当前对象继续使用，加入显示列表，直到新对象进来；或者搞个专门用来替换的，比如用来宣传本公司的宣传画面，加入显示列表。
            #3.2.2 如果存在，就让到期对象下线，将状态置为‘过期下线’即2；新对象上线，将状态置‘上线’即为2，加入显示列表；
            
        
    
'''
from models import *
import datetime,time

def advcrl(advobject):
    # 判断期限：
    # 定义显示列表
    # adv_li = []
    # 定义首位位置字典：首位：[对象列表] row.advtp.advposition1
    adv_dic={}
    # 1，从允许发布且状态为上线即1的queryset对象中去取，取得上线内容列表
    # 用select_related(外键)一次性过滤出首页要的所有参数.
    adv_list = advobject.objects.filter(is_Delete=1).filter(advstatus=1).select_related('advtp', 'advuser','advgt','advgoods','advgoods__gmgoods','advgoods__goodscrfd')#advgoods__gmsales是商品管理对象的多对多字段，不能用外键这样处理。也就是select_related实现不了多对多的一次性获取。
    #用select_related(外键)提高性能，是对象套对象的格式

    # 2，循环该内容列表，用期数字段去获取每个对象的到期时间，
    # 注意时区,Django配置DateTimeField使用timezone的datetime格式，而datetime.now是不包含timezone信息的。
    for row in adv_list:
        # 取得对象允许的时间=更新日期+期数*每期时间
        print row.utime  # 注意该时间显示是UTC时间
        allowtime = row.utime + datetime.timedelta(row.advnum * 5)#默认是day，可以用minutes=row.advnum * 5，hours=row.advnum * 5，second=row.advnum * 5
        allowtime_local = timezone.localtime(allowtime)  # 注意时区转换，转换为本地时间
        print allowtime  # 注意该时间显示是UTC时间
        print allowtime_local
        # 转为时间戳
        allow = time.mktime(allowtime.timetuple())
        allow_local = time.mktime(allowtime_local.timetuple())  # 本地时间戳
        print allow
        print allow_local
        print datetime.datetime.now()
        print time.time()
        # 如果不存在该key，就建立
        if not adv_dic.has_key(row.advtp.advposition1):
            adv_dic[row.advtp.advposition1] = []
        # 3，和当前时间比较，
        if time.time() < allow_local:  # 要和本地时间戳比较
            # 把对象加入列表
            # adv_li.append(row)
            # 把列表加入字典
            adv_dic[row.advtp.advposition1].append(row)
        else:
            # 到期了，找到替补新对象，注意是该位置的对象，不是其他位置的。
            # 从状态为预备的对象中去取替补，按id正向取，即先取最小的，将其状态置改为上线为1，填补被剔除的对象。
            #
            # 先获取当前对象位置
            p1 = row.advtp.advposition1
            p2 = row.advtp.advposition2

            try:
                adv = advobject.objects.filter(is_Delete=1).filter(advstatus=0).\
                filter(advtp__advposition1=p1,advtp__advposition2=p2).select_related('advtp', 'advuser','advgt','advgoods','advgoods__gmgoods','advgoods__goodscrfd').order_by('id')[0]
                # 新对象存在，就让到期对象下线，新对象上线，则将状态置为过期下线即2，
                row.advstatus = 2  # 到期下线
                row.save()
                adv.advstatus = 1  # 新对象上线
                adv.save()
                # 显示新对象
                # adv_li.append(adv)
                adv_dic[row.advtp.advposition1].append(adv)
            except Exception, e:
                print e
                print '新对象不存在'
                # adv_li.append(row)  # 新对象不存在，没有，尽管过期，可以沿用上一期的，直到新对象进来，或者搞两个专门用来替换的，用来宣传本公司的宣传画面
                adv_dic[row.advtp.advposition1].append(row)
    # 传回显示列表
    # return adv_li
    # 传回位置显示字典******
    return adv_dic