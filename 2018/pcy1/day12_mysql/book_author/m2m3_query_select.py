# _*_coding:utf-8_*_

'''
多对多关联

现在来设计一个能描述“图书”与“作者”的关系的表结构，需求是

        一本书可以有好几个作者 
        一个作者可以写好几本书

        书和作者之间的关系是多对多
解决办法:
    除了作者表（id,auth_name），
    图书表(id,book_name,pub_date);

    还要建立和作者表及图书表映射的第三张表--作者-图书映射表
    a_id,b_id,该表连id都没有。a_id和b_id两个都是外键，分别
    关联作者表的id和图书表的id.

3，正反查询
'''
import m2m1_bk_au_create
from sqlalchemy.orm import sessionmaker, relationship

# 1，创建与数据库的会话session，相当于操作文件的句柄。
Session_class = sessionmaker(bind=m2m1_bk_au_create.engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = Session_class()  # 生成session实例

# 2，定义查询结果的返回格式
'''
class Authro(Base):
    # 下面这一行是在第三步查询数据时添加的，定义查询该类对象的返回格式
    def __repr__(self):
        return 'author_name:%s '%(self.author_name)

class Books(Base):

    # 下面这一行是在第三步查询数据时添加的，定义查询该类对象的返回格式
    def __repr__(self):
        return 'book_name:%s pub_date:%s'%(self.book_name,self.pub_date)
'''

# 3，正查
#某本图书有哪些作者
book_obj=session.query(m2m1_bk_au_create.Books).filter(m2m1_bk_au_create.Books.id==2)\
    .first()
print book_obj
print book_obj.authors
'''
执行结果：
book_name:learn hook up girls with Alex pub_date:2015-06-12
[author_name:Rain , author_name:Jack , author_name:Alex ]
'''

# 4，反查
#某个作者写了哪几本书
author_obj=session.query(m2m1_bk_au_create.Authro).\
    filter(m2m1_bk_au_create.Authro.author_name=='Alex').first()
print author_obj
print author_obj.books

'''
执行结果：
author_name:Alex 
[book_name:learn python with Alex pub_date:2014-05-20,
 book_name:learn hook up girls with Alex pub_date:2015-06-12]
'''