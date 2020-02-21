#_*_coding:utf-8_*_

'''
7,连表join

'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,DATE,Enum
from sqlalchemy.orm import sessionmaker
# 1，连接数据库
engine = create_engine("mysql+pymysql://root:another333@localhost/test",
                       encoding='utf-8')
#mysql+pymysql表示采用pymysql执行原生sql，
#echo=True表示显示创建过程，可以看到生成的原生sql。

# 2，创建表和类的映射
Base = declarative_base()  # 生成orm基类
class User(Base):#继承基类
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):#用于查询时返回该对象你想要返回的值。
        return '<id %s name:%s password:%s>'%(self.id,self.name,self.password)
class Student1(Base):#映射mysql中已经存在的student1表
    __tablename__='student1'
    id=Column(Integer,primary_key=True)
    name=Column(String(32),nullable=False)
    register_date=Column(DATE,nullable=False)
    gender=Column(String(32),nullable=False)#把String(32)写成Enum('M','F')枚举，一样可以。
    def __repr__(self):#定义查询该对象时返回的格式
        return '<id %s name:%s register_date:%s gender:%s>'%\
               (self.id,self.name,self.register_date,self.gender)

# 3，创建与数据库的会话session，相当于操作文件的句柄。
Session_class = sessionmaker(bind=engine)# 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = Session_class()  # 生成session实例

# 4，连表查询 连student1和user两张表 就是连Student1和User两个类,条件是id相等
data=session.query(Student1,User).filter(Student1.id==User.id).all()
print  data
#[(<id 1 name:wangsen register_date:2016-06-12 gender:M>, <id 1 name:AlexLi password:shit happens>),
# (<id 2 name:zhouyi register_date:2016-06-12 gender:M>, <id 2 name:jack password:122>)]