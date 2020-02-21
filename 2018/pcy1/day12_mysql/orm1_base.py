#_*_coding:utf-8_*_

'''
据说是py中牛逼的orm
1，建表方式一，建表方式2是metadata。
方式1是对方式2的再封装
'''
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
# 1，连接数据库
engine = create_engine("mysql+pymysql://root:another333@localhost/test?charset=utf8",
                       encoding='utf-8', echo=True)
#mysql+pymysql表示采用pymysql执行原生sql，
#echo=True表示显示创建过程，可以看到生成的原生sql。

# 2，创建User类和user表的映射
Base = declarative_base()  # 生成orm基类
#

class User(Base):#继承基类
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

# 3，在数据库中创建表
Base.metadata.create_all(engine)  # 创建表结构
'''
mysql上查询结果：
mysql> show tables
    -> ;
+----------------+
| Tables_in_test |
+----------------+
| a              |
| b              |
| student1       |
| study_record   |
| user           |
+----------------+
5 rows in set (0.02 sec)

mysql> desc user;
+----------+-------------+------+-----+---------+----------------+
| Field    | Type        | Null | Key | Default | Extra          |
+----------+-------------+------+-----+---------+----------------+
| id       | int(11)     | NO   | PRI | NULL    | auto_increment |
| name     | varchar(32) | YES  |     | NULL    |                |
| password | varchar(64) | YES  |     | NULL    |                |
+----------+-------------+------+-----+---------+----------------+
3 rows in set (0.00 sec)

mysql>


'''