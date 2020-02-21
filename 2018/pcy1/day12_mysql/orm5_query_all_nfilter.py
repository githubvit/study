#_*_coding:utf-8_*_

'''
5,查询全部 和 多条件查询

'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
# 1，连接数据库
engine = create_engine("mysql+pymysql://root:another333@localhost/test?charset=utf8",
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

# 4，获取所有数据
print(session.query(User).all())
#[<id 1 name:AlexLi password:shit happens>, <id 2 name:jack password:122>, <id 5 name:Rain password:12345>]

# 5，多条件查询多个filter
objs = session.query(User).filter(User.id > 0).filter(User.id < 5).all()
print objs
#[<id 1 name:AlexLi password:shit happens>, <id 2 name:jack password:122>]
# 上面2个filter的关系相当于
# user.id > 0 AND user.id < 5 的效果

# 6，删,因为最后没commit，所以实际没有删。
session.delete(objs[0])
print (session.query(User).all())
#[<id 2 name:jack password:122>, <id 5 name:Rain password:12345>]