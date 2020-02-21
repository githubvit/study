#_*_coding:utf-8_*_

'''
3,数据查询query和数据修改
session.query()实现select
直接赋值实现update
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

# 4,用session对User类进行查询，结果为User对象的列表，filter为过滤条件
data=session.query(User).filter(User.name=='alex').all()#当过滤条件为空，就是select * from table。
'''
session.query(User)=select * from user;
session.query(User).filter(User.name=='alex')相当于
select * from user where name='alex';
mysql运行结果：
mysql> select * from user where name='alex';
+----+------+----------+
| id | name | password |
+----+------+----------+
|  1 | alex | alex3714 |
+----+------+----------+
1 row in set (0.00 sec)

mysql>
'''

print data #data就是User对象的列表
#[<id 1 name:alex password:alex3714>] 列表
print type(data)
#<type 'list'>
for i in data:#循环这个列表 取出每个元素
    print i
    #<id 1 name:alex password:alex3714>这就是User对象的返回结果
    print type(i)
    #<class '__main__.User'> 属于User类
    print i.name,i.password
    #alex alex3714
# 5，修改，直接赋值，实现表单update
#first()获取的就是单个对象，不是列表
data2=session.query(User).filter(User.name=='alex').first()#
#直接修改对象的属性实现对表的修改upate
data2.name='AlexLi'
data2.password='shit happens'
session.commit()
'''
mysql查询结果：
mysql> select * from user ;
+----+--------+--------------+
| id | name   | password     |
+----+--------+--------------+
|  1 | AlexLi | shit happens |
|  2 | jack   | 122          |
+----+--------+--------------+
2 rows in set (0.00 sec)

mysql>
'''