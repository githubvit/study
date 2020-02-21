#_*_coding:utf-8_*_

'''
分页操作
'''

def sqlexec(nid, is_next):
    import pymysql

    conn = pymysql.connect(host='192.168.12.29', port=3306, user='root', passwd='123', db='IndexDB', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 执行存储过程,获取存储过程的结果集，将返回值设置给了  @_存储过程名_序号 =
    if is_next:
        cursor.execute('select * from tb1 where nid>%s limit 10', nid)
        result = cursor.fetchall()
    else:
        cursor.execute('select * from tb1 where nid<%s order by nid desc limit 10', nid)
        #如果不order by nid desc，默认排序是从小到大，
        # 那么取得的就是0-9（这样说不准确但是是这个意思），这时候limit 10--》就是第一页
        #所以要倒转过来order by nid desc，从大到小，再用limit10，就是上一页的数据，取得相应的结果集。
        result = cursor.fetchall()
        result = list(reversed(result))

    conn.commit()
    cursor.close()
    conn.close()
    return result


current_last_nid = 0
current__first_nid = 0
while True:
    p = input('1、上一页; 2、下一页\n')
    if p == '2':
        # 点击下一页
        is_next = True
        ret = sqlexec(current_last_nid, is_next)
    else:
        # 点击上一页
        is_next = False
        ret = sqlexec(current_first_nid, is_next)
    current_first_nid = ret[0]['nid']
    current_last_nid = ret[-1]['nid']
    for i in ret:
        print(i)