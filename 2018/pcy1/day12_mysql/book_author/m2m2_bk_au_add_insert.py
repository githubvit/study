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
    
2，插入数据
'''
import m2m1_bk_au_create
from sqlalchemy.orm import sessionmaker,relationship

# 1，创建与数据库的会话session，相当于操作文件的句柄。
Session_class = sessionmaker(bind=m2m1_bk_au_create.engine)# 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = Session_class()  # 生成session实例

# 2，定义图书表数据
# b1=m2m1_bk_au_create.Books(book_name='learn python with Alex',pub_date='2014-05-20')
# b2=m2m1_bk_au_create.Books(book_name='learn zhuangbiliti with Alex',pub_date='2013-04-21')
# b3=m2m1_bk_au_create.Books(book_name='learn hook up girls with Alex',pub_date='2015-06-12')
b4=m2m1_bk_au_create.Books(book_name='跟Alex去泰国',pub_date='2016-06-12')
'''
注意运行结果，顺序有变;b2图书的id为3，b3图书的id为2
mysql> select * from books;
+----+-------------------------------+------------+
| id | book_name                     | pub_date   |
+----+-------------------------------+------------+
|  1 | learn python with Alex        | 2014-05-20 |
|  2 | learn hook up girls with Alex | 2015-06-12 |
|  3 | learn zhuangbiliti with Alex  | 2013-04-21 |
+----+-------------------------------+------------+
'''
# 3，定义作者表数据
# a1=m2m1_bk_au_create.Authro(author_name='Alex')
# a2=m2m1_bk_au_create.Authro(author_name='Jack')
# a3=m2m1_bk_au_create.Authro(author_name='Rain')

# 4，接下来最重要，就是第三张表映射表的数据来源
'''
4.1 首先要在图书表中增加一行
authors = relationship('Authro',secondary=book_m2m_author,backref='books')
定义图书表的作者authors关联作者表'Author'，
secondary=book_m2m_author，表示图书表和作者表的关联通过book_m2m_author这张表建立，
backref='books'，是表示反查本类时的关键字
'''

# 4.2 映射数据，即给book_m2m_author添加了数据，因为该表是根据映射自动添加数据。
# b1.authors=[a1,a3]#b1这本书的作者是a1、a2
# b3.authors=[a1,a2,a3]#b3这本书的作者是a1、a2、a3
# 5，插入数据
# session.add_all([b1,b2,b3,a1,a2,a3])
session.add(b4)
# 6，提交数据
session.commit()
'''
查看结果：
mysql> select * from book_m2m_author;
+------+------+
| a_id | b_id |
+------+------+
|    3 |    1 |
|    3 |    2 |
|    2 |    2 |
|    1 |    1 |
|    1 |    2 |
+------+------+
5 rows in set (0.00 sec)

mysql> select * from books;
+----+-------------------------------+------------+
| id | book_name                     | pub_date   |
+----+-------------------------------+------------+
|  1 | learn python with Alex        | 2014-05-20 |
|  2 | learn hook up girls with Alex | 2015-06-12 |
|  3 | learn zhuangbiliti with Alex  | 2013-04-21 |
+----+-------------------------------+------------+
3 rows in set (0.00 sec)

mysql> select * from authro;
+----+-------------+
| id | author_name |
+----+-------------+
|  1 | Alex        |
|  2 | Jack        |
|  3 | Rain        |
+----+-------------+
3 rows in set (0.00 sec)

mysql>

'''
