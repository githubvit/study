#_*_coding:utf-8_*_

'''
多外键关联
一张表有两个外键关联另一张表的同一个字段。

2,插入数据
从建表的程序中导入engine和Customer类、Address类
顾客表中的账单邮寄地址和货物邮寄地址都关联地址表中的id字段
'''


from sqlalchemy.orm import sessionmaker
import mfk1_create

# 1，创建与数据库的会话session，相当于操作文件的句柄。
Session_class = sessionmaker(bind=mfk1_create.engine)# 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = Session_class()  # 生成session实例

# 2，插入数据
#2.1 要先插入主表 主表是address
# 定义主表数据
addr1=mfk1_create.Address( street='tiantongyuan',city='changping',state='BJ')
addr2=mfk1_create.Address( street='wudaokou',city='haidian',state='BJ')
addr3=mfk1_create.Address( street='yanjiao',city='langfang',state='HB')
#插入主表
session.add_all([addr1,addr2,addr3])
#2.2 再插入从表
'''
2.2.1
要先在mfk1_create模块的相应类Customer中加入下面两条关系定义，
这样明确了关系，才可以在定义数据时，使用billing_address=addr1这样的关系型定义
billing_address = relationship("Address", foreign_keys=[billing_address_id])
shipping_address = relationship("Address", foreign_keys=[shipping_address_id])
为什么要使用关系型定义;
因为主从表一起插入数据的时候，主表主键id都还没有，也就是addr1不见得是id=1，有可能是id=2。
使用关系型定义，不管addr1是id1还是id2，都错不了。
通过关系来找id，如果addr1是id2，那么billing_address_id字段的值就是2。
'''
#2.2.2
c1=mfk1_create.Customer(name='alex',billing_address=addr1,shipping_address=addr2)
c2=mfk1_create.Customer(name='jack',billing_address=addr3,shipping_address=addr3)

session.add_all([c1,c2])

# 3,提交
session.commit()

'''
执行结果
mysql> select * from customer;
+----+------+--------------------+---------------------+
| id | name | billing_address_id | shipping_address_id |
+----+------+--------------------+---------------------+
|  1 | alex |                  4 |                   5 |
|  2 | jack |                  6 |                   6 |
+----+------+--------------------+---------------------+
2 rows in set (0.00 sec)

mysql> select * from address;
+----+--------------+-----------+-------+
| id | street       | city      | state |
+----+--------------+-----------+-------+
|  4 | tiantongyuan | changping | BJ    |
|  5 | wudaokou     | haidian   | BJ    |
|  6 | yanjiao      | langfang  | HB    |
+----+--------------+-----------+-------+
3 rows in set (0.00 sec)

mysql>

'''