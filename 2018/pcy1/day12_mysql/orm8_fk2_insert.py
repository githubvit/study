#_*_coding:utf-8_*_

'''
8,外键foreign key
8.2插入数据

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
    # 3，外键关联，关联student表的id字段
    stu_id=Column(Integer,ForeignKey('student.id'))

# 3，创建与数据库的会话session，相当于操作文件的句柄。
Session_class = sessionmaker(bind=engine)# 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = Session_class()  # 生成session实例

# 4，插入数据
#学生表数据
s1=Student(name='alex',register_date='2015-05-21')
s2=Student(name='jack',register_date='2014-03-21')
s3=Student(name='rain',register_date='2014-02-21')
s4=Student(name='eric',register_date='2013-02-20')

#考勤表数据 alex有3条记录，jack有1条
sr1=StudyRecody(day=1,status='yes',stu_id=1)
sr2=StudyRecody(day=2,status='yes',stu_id=2)
sr3=StudyRecody(day=2,status='no',stu_id=1)
sr4=StudyRecody(day=2,status='yes',stu_id=1)
#插入数据
session.add_all([s1,s2,s3,s4,sr1,sr2,sr3,sr4])

# 5，提交
session.commit()
'''
 stu_id 字段为null，说明插入时应该用字符的形式stu_id=‘1’
mysql> select * from student;
+----+------+---------------+
| id | name | register_date |
+----+------+---------------+
|  1 | alex | 2015-05-21    |
|  2 | jack | 2014-03-21    |
|  3 | rain | 2014-02-21    |
|  4 | eric | 2013-02-20    |
+----+------+---------------+
4 rows in set (0.00 sec)

mysql> select * from study_record;
+----+-----+--------+--------+
| id | day | status | stu_id |
+----+-----+--------+--------+
|  1 |   1 | yes    |      1 |
|  2 |   2 | yes    |      2 |
|  3 |   2 | no     |      1 |
|  4 |   2 | yes    |      1 |
+----+-----+--------+--------+
4 rows in set (0.00 sec)

mysql>
'''




