#_*_coding:utf-8_*_

'''
2,插入数据
session_class是和数据库对话的类
实例化session_class,实现数据库的增删改查。
'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
# 1，连接数据库
engine = create_engine("mysql+pymysql://root:another333@localhost/test?charset=utf8",
                       encoding='utf-8', echo=True)
#mysql+pymysql表示采用pymysql执行原生sql，
#echo=True表示显示创建过程，可以看到生成的原生sql。

# 2，创建表和类的映射
Base = declarative_base()  # 生成orm基类

class User(Base):#继承基类
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

# 3，创建与数据库的会话session，相当于操作文件的句柄。
Session_class = sessionmaker(bind=engine)#创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例

# 4，用session实现数据库的增删改查
user_obj = User(name="alex", password="alex3714")  # 生成你要创建的数据对象
user_obj2 = User(name="jack", password="122")  # 生成你要创建的数据对象
print(user_obj.name, user_obj.id)  # 此时还没创建对象呢，不信你打印一下id发现还是None

Session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
Session.add(user_obj2)
print(user_obj.name, user_obj.id)  # 此时也依然还没创建,id发现还是None
# 5，用session提交事务 ,对于session.query()查--> 不需要提交。
Session.commit()  # 现此才统一提交，创建数据
print(user_obj.name, user_obj.id) #创建完成，id为1