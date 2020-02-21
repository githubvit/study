#_*_coding:utf-8_*_

'''
8,外键foreign key
8.1建表
在mysql中新建数据库test_db
mysql> create database test_db charset 'utf8';
Query OK, 1 row affected (0.05 sec)
在数据库test_db下，有两张表，student学生表和study_record考勤表

'''

from sqlalchemy import create_engine,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,DATE,Enum
from sqlalchemy.orm import sessionmaker
# 1，连接数据库
engine = create_engine("mysql+pymysql://root:another333@localhost/test_db",
                       encoding='utf-8')
#mysql+pymysql表示采用pymysql执行原生sql，
#echo=True表示显示创建过程，可以看到生成的原生sql。

# 2，创建表和类的映射
Base = declarative_base()  # 生成orm基类
class Student(Base):#建立学生表
    __tablename__='student'
    id=Column(Integer,primary_key=True)
    name=Column(String(32),nullable=False)
    register_date=Column(DATE,nullable=False)

class StudyRecody(Base):#建立考勤表
    __tablename__='study_record'
    id=Column(Integer,primary_key=True)
    day=Column(Integer,nullable=False)
    status=Column(String(32),nullable=False)
    stu_id=Column(Integer,ForeignKey('student.id'))# 3，外键关联关联student表的id字段

# 4，在数据库中创建表
Base.metadata.create_all(engine) # 创建表结构

'''
mysql查询结果：
mysql> show tables;
+-------------------+
| Tables_in_test_db |
+-------------------+
| student           |
| study_record      |
+-------------------+
2 rows in set (0.00 sec)

mysql> show create table study_record;
+--------------+------------------------
| Table        | Create Table           
+--------------+------------------------
| study_record | CREATE TABLE `study_record` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `day` int(11) NOT NULL,
  `status` varchar(32) NOT NULL,
  `stu_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `stu_id` (`stu_id`),
  CONSTRAINT `study_record_ibfk_1` FOREIGN KEY (`stu_id`) REFERENCES `student` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 |
+--------------+------------------------
1 row in set (0.00 sec)

'''