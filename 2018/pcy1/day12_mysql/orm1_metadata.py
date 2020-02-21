#_*_coding:utf-8_*_

'''
据说是py中牛逼的orm
1，建表方式二，metadata不继承基类。
'''
from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapper
# 1，连接数据库
engine = create_engine("mysql+pymysql://root:another333@localhost/test?charset=utf8",
                       encoding='utf-8', echo=True)
#2，创建user表
metadata = MetaData()
#
user1 = Table('user1', metadata,
             Column('id', Integer, primary_key=True),
             Column('name', String(50)),
             Column('fullname', String(50)),
             Column('password', String(12))
             )

#3，创建User类
class User1(object):#不继承基类
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

#4，关联user表和User类，建立了映射关系。
mapper(User1,user1)  # 通过mapper关联User对象和user表

#5,创建表结构，即在mysql上创建该表
metadata.create_all(engine)

'''
mysql上查询结果：
mysql> show tables;
+----------------+
| Tables_in_test |
+----------------+
| a              |
| b              |
| student1       |
| study_record   |
| user           |
| user1          |
+----------------+
6 rows in set (0.00 sec)

mysql> desc user1;
+----------+-------------+------+-----+---------+----------------+
| Field    | Type        | Null | Key | Default | Extra          |
+----------+-------------+------+-----+---------+----------------+
| id       | int(11)     | NO   | PRI | NULL    | auto_increment |
| name     | varchar(50) | YES  |     | NULL    |                |
| fullname | varchar(50) | YES  |     | NULL    |                |
| password | varchar(12) | YES  |     | NULL    |                |
+----------+-------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)

'''