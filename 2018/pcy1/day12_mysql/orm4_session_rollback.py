#_*_coding:utf-8_*_

'''
4,回滚rollback
session操作默认就是事务性的
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
# 4，插入数据
fake_user = User(name='Rain', password='12345')
session.add(fake_user)

print(session.query(User).filter(User.name.in_(['Jack', 'rain'])).all())  # 这时看session里有你刚添加和修改的数据
#[<id 2 name:jack password:122>, <id 4 name:Rain password:12345>]
# 5，回滚
session.rollback()  # 此时你rollback一下
#[<id 2 name:jack password:122>]
print(session.query(User).filter(User.name.in_(['Jack', 'rain'])).all())  # 再查就发现刚才添加的数据没有了。

# 6,正式插入，注意id，说明刚刚的id用过了。和MySQL的事务，id无法回滚是一样的
fake_user = User(name='Rain', password='12345')
session.add(fake_user)
session.commit()
print (session.query(User).filter(User.name.in_(['Jack', 'rain'])).all()) #id没有回滚
# [<id 2 name:jack password:122>, <id 5 name:Rain password:12345>]
'''
mysql 查询结果：注意id
mysql> select * from user ;
+----+--------+--------------+
| id | name   | password     |
+----+--------+--------------+
|  1 | AlexLi | shit happens |
|  2 | jack   | 122          |
|  5 | Rain   | 12345        |
+----+--------+--------------+
3 rows in set (0.00 sec)

mysql>

'''