#_*_coding:utf-8_*_

'''
多外键关联
一张表有两个外键关联另一张表的同一个字段。

1，建表
顾客表中的账单邮寄地址和货物邮寄地址都关联地址表中的id字段
'''

from sqlalchemy import create_engine,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,DATE,Enum
from sqlalchemy.orm import sessionmaker,relationship

# 1，连接数据库
engine = create_engine("mysql+pymysql://root:another333@localhost/test_1",
                       encoding='utf-8')
#mysql+pymysql表示采用pymysql执行原生sql，
#echo=True表示显示创建过程，可以看到生成的原生sql。

# 2，创建表和类的映射
Base = declarative_base()  # 生成orm基类


class Customer(Base):#顾客表
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    billing_address_id = Column(Integer, ForeignKey("address.id"))#账单邮寄地址 关联 地址表id
    shipping_address_id = Column(Integer, ForeignKey("address.id"))#货物邮寄地址 同样关联地址表id
    # 下面的两条在建表时没用，写入这两条是因为插入和查询程序要引用本程序中的该类，事先定义好，当然也可以引用到的时候再加，没有关系。
    billing_address = relationship("Address", foreign_keys=[billing_address_id],backref='billing_name')
    shipping_address = relationship("Address", foreign_keys=[shipping_address_id],backref='shipping_name')
    def __repr__(self):
        return 'name:%s'%(self.name)



class Address(Base):#地址表
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String(64))
    city = Column(String(64))
    state = Column(String(64))
    def __repr__(self):
        return '%s-%s-%s'%(self.street,self.city,self.state)

# 3，在数据库中创建表
Base.metadata.create_all(engine) # 创建表结构

'''
执行结果
mysql> show tables;
+------------------+
| Tables_in_test_1 |
+------------------+
| address          |
| customer         |
| student          |
| study_record     |
+------------------+
4 rows in set (0.00 sec)

mysql> show create table customer;
| customer | CREATE TABLE `customer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) DEFAULT NULL,
  `billing_address_id` int(11) DEFAULT NULL,
  `shipping_address_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `billing_address_id` (`billing_address_id`),
  KEY `shipping_address_id` (`shipping_address_id`),
  CONSTRAINT `customer_ibfk_1` FOREIGN KEY (`billing_address_id`) REFERENCES `address` (`id`),
  CONSTRAINT `customer_ibfk_2` FOREIGN KEY (`shipping_address_id`) REFERENCES `address` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 |
mysql> desc customer;
+---------------------+-------------+------+-----+---------+----------------+
| Field               | Type        | Null | Key | Default | Extra          |
+---------------------+-------------+------+-----+---------+----------------+
| id                  | int(11)     | NO   | PRI | NULL    | auto_increment |
| name                | varchar(32) | YES  |     | NULL    |                |
| billing_address_id  | int(11)     | YES  | MUL | NULL    |                |
| shipping_address_id | int(11)     | YES  | MUL | NULL    |                |
+---------------------+-------------+------+-----+---------+----------------+
4 rows in set (0.07 sec)

mysql> desc address;
+--------+-------------+------+-----+---------+----------------+
| Field  | Type        | Null | Key | Default | Extra          |
+--------+-------------+------+-----+---------+----------------+
| id     | int(11)     | NO   | PRI | NULL    | auto_increment |
| street | varchar(64) | YES  |     | NULL    |                |
| city   | varchar(64) | YES  |     | NULL    |                |
| state  | varchar(64) | YES  |     | NULL    |                |
+--------+-------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)


'''
