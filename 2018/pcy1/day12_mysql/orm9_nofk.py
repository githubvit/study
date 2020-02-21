#_*_coding:utf-8_*_

'''
9,实验——数据库中非外键关联的表，怎么反查
第一步，在建表时不建立外键
第二步，插入数据
第三步，反查时，在类中建立外键、relationship，看可不可以反查。
建立test_1数据库
mysql> create database test_1 charset 'utf8';
Query OK, 1 row affected (0.13 sec)
实验结果是成功的，这就说明在mysql数据库中没有外键关联的表一样可以通过orm方式实现反查

'''

from sqlalchemy import create_engine,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,DATE,Enum
from sqlalchemy.orm import sessionmaker,relationship
#-----------第一步，建表-----------------
# 1，连接数据库
engine = create_engine("mysql+pymysql://root:another333@localhost/test_1",
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
    def __repr__(self):
        return 'id%s name:%s register_date:%s'%(self.id,self.name,self.register_date)

class StudyRecody(Base):#建立考勤表
    __tablename__='study_record'
    id=Column(Integer,primary_key=True)
    day=Column(Integer,nullable=False)
    status=Column(String(32),nullable=False)
    # stu_id=Column(Integer,nullable=False)# 3，先不建立外键
    stu_id = Column(Integer, ForeignKey('student.id'))#反查时建立外键

    student = relationship('Student', backref='my_record')

    def __repr__(self):
        return 'student:%s record day:%s status:%s ' % (self.student.name, self.day, self.status)

# 4，在数据库中创建表
# Base.metadata.create_all(engine) # 创建表结构

'''
执行结果
mysql> use test_1;
Database changed
mysql> show tables;
Empty set (0.00 sec)

mysql> show tables;
+------------------+
| Tables_in_test_1 |
+------------------+
| student          |
| study_record     |
+------------------+
2 rows in set (0.01 sec)

mysql> show create table study_record;
| study_record | CREATE TABLE `study_record` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `day` int(11) NOT NULL,
  `status` varchar(32) NOT NULL,
  `stu_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 |
'''

#-------------第二步插入数据————————————————————

# 3，创建与数据库的会话session，相当于操作文件的句柄。
Session_class = sessionmaker(bind=engine)# 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = Session_class()  # 生成session实例

# # 4，插入数据
# #学生表数据
# s1=Student(name='alex',register_date='2015-05-21')
# s2=Student(name='jack',register_date='2014-03-21')
# s3=Student(name='rain',register_date='2014-02-21')
# s4=Student(name='eric',register_date='2013-02-20')
#
# #考勤表数据 alex有3条记录，jack有1条
# sr1=StudyRecody(day=1,status='yes',stu_id=1)
# sr2=StudyRecody(day=2,status='yes',stu_id=2)
# sr3=StudyRecody(day=2,status='no',stu_id=1)
# sr4=StudyRecody(day=2,status='yes',stu_id=1)
# #插入数据
# session.add_all([s1,s2,s3,s4,sr1,sr2,sr3,sr4])
#
# # 5，提交
# session.commit()
'''
执行结果
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

#--------------------------第三步 反查 建立foreign key和relationship ----------------
stu_obj=session.query(Student).filter(Student.id==1).first()
print stu_obj
print stu_obj.my_record
'''
执行结果：成功反查。
id1 name:alex register_date:2015-05-21
[student:alex record day:1 status:yes , student:alex record day:2 status:no , student:alex record day:2 status:yes ]

最后，看一下study_record表的结构变了没有
mysql> show create table study_record;
| study_record | CREATE TABLE `study_record` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `day` int(11) NOT NULL,
  `status` varchar(32) NOT NULL,
  `stu_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 |
看到和开始一样，反查时建立的外键并没有改变没有该表的结构。
'''