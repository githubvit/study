#_*_coding:utf-8_*_

'''
使用pymysql模块操作mysql数据库
'''

import pymysql

#1， 连接数据库 创建socket连接
conn = pymysql.connect(host='192.168.2.191', port=3306, user='root', passwd='another333', db='test')

#2， 创建游标
cursor = conn.cursor()

#3，执行SQL，并返回收影响行数
# effect_row = cursor.execute("select * from student1")

# print effect_row
#执行多条sql,向student1插入三条数据
# 定义sql语句
sql="insert into student1 (name,register_date,gender) values (%s,%s,%s)"
# 定义数据变量
data=[
    ('n1','2015-05-20','M'),
    ('n2','2015-05-21','M'),
    ('n3','2015-05-22','F'),
]
# 执行多条sql
effect_row=cursor.executemany(sql,data)

#4， 提交，select查询不需要commit
conn.commit()#不提交，在mysql上没有

#5，关闭连接
conn.close()

'''
以上程序执行后，在mysql里，查询结果：
mysql> select * from student1;
+----+---------+---------------+--------+
| id | name    | register_date | gender |
+----+---------+---------------+--------+
|  1 | wangsen | 2016-06-12    | M      |
|  2 | zhouyi  | 2016-06-12    | M      |
| 16 | n1      | 2015-05-20    | M      |
| 17 | n2      | 2015-05-21    | M      |
| 18 | n3      | 2015-05-22    | F      |
+----+---------+---------------+--------+
5 rows in set (0.00 sec)

mysql>
'''

# #用光标读取一条数据，一条元组数据
# print cursor.fetchone()
#
# #用光标再读取一条数据
# print cursor.fetchone()#和文件一样有指针
'''
注：在fetch数据时按照顺序进行，可以使用cursor.scroll(num,mode)来移动游标位置，如：

cursor.scroll(1,mode='relative')  # 相对当前位置移动,1往下走，-1往上走
cursor.scroll(2,mode='absolute') # 相对绝对位置移动
# 游标设置为字典类型 重要
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
因为这样查询的结果就是字典，列名就是key，并且列名可以按sql定制，方便取值。
# 获取最新自增ID
new_id = cursor.lastrowid
'''

# #用光标读取多3条数据
# print cursor.fetchmany(3)
#
# print '-------------'

#用光标读取全部数据 一条元组数据，里面嵌套了多个元组元素
# print cursor.fetchall()
