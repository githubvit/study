#_*_coding:utf-8_*_

'''
8,外键foreign key
8.4 通过外键关联查询
relationship 关系



'''

from sqlalchemy import create_engine,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,DATE,Enum
from sqlalchemy.orm import sessionmaker,relationship
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
    def __repr__(self):
        return 'id%s name:%s register_date:%s'%(self.id,self.name,self.register_date)

class StudyRecody(Base):#建立考勤表
    __tablename__='study_record'
    id=Column(Integer,primary_key=True)
    day=Column(Integer,nullable=False)
    status=Column(String(32),nullable=False)
    # 3，外键关联，关联student表的id字段
    stu_id=Column(Integer,ForeignKey('student.id'))
    student=relationship('Student',backref='my_record')#这个nb，允许你在student表里通过backref字段反向查出所有它在addresses表里的关联项
    # 正向是关联了Student这个类，还可以在Student类里通过backref反查该类。
    # relationship实际上只是内存关联，与数据库没关联。
    def __repr__(self):#注意这里通过虚拟字段student取到Student里的name
        return 'student:%s record day:%s status:%s '%(self.student.name,self.day,self.status)



# 3，创建与数据库的会话session，相当于操作文件的句柄。
Session_class = sessionmaker(bind=engine)# 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = Session_class()  # 生成session实例


# 4，查alex的考勤记录

stu_obj=session.query(Student).filter(Student.name=='alex').first()
print stu_obj
print stu_obj.my_record#在主表Student通过从表StudyRecody的relationship中的backref关键字反查到了从表，并返回了从表对象的值。
'''[student:alex record day:1 status:yes , student:alex record day:2 status:no ]'''