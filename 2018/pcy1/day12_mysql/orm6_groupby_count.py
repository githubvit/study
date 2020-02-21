#_*_coding:utf-8_*_

'''
6,count和分组统计group by

'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
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

# 3，创建与数据库的会话session，相当于操作文件的句柄。
Session_class = sessionmaker(bind=engine)# 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = Session_class()  # 生成session实例

# 4，看统计count怎么用
print (session.query(User).filter(User.name.in_(['Jack', 'rain'])).count())
# 结果为2，这是统计

# 5，分组统计group_by 看每个name出现的次数func.count(User.name)
from sqlalchemy import func
print(session.query(User.name,func.count(User.name)).group_by(User.name).all() )
# engine按"mysql+pymysql://root:another333@localhost/test"写，结果如下
# [('AlexLi', 1), ('jack', 1), ('Rain', 1)] 元组列表
# engine按"mysql+pymysql://root:another333@localhost/test?charset=utf8"写，结果如下
# [(u'AlexLi', 1), (u'jack', 1), (u'Rain', 1)]
