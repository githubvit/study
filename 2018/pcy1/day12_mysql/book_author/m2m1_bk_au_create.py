#_*_coding:utf-8_*_

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
1，建表
'''


from sqlalchemy import create_engine,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,DATE,Table
from sqlalchemy.orm import sessionmaker,relationship
#-----------第一步，建表-----------------
# 1，连接数据库
engine = create_engine("mysql+pymysql://root:another333@localhost/test_1?charset=utf8",
                       encoding='utf-8')
#mysql+pymysql表示采用pymysql执行原生sql，
#echo=True表示显示创建过程，可以看到生成的原生sql。

# 2，创建表和类的映射
Base = declarative_base()  # 生成orm基类

#2.1 创建作者表
class Authro(Base):
    __tablename__='authro'
    id=Column(Integer,primary_key=True)
    author_name=Column(String(32),nullable=False)
    # 下面这一行是在第三步查询数据时添加的，定义查询该类对象的返回格式
    def __repr__(self):
        return 'author_name:%s '%(self.author_name)

#2.3 最重要的来了，采用方式2创建图书-作者映射表，因为只需要在数据库有这张表，并且这张表的增删改查无需关心，
# 因此，不需要对该表映射类。
# 为什么把2.3移到2.2的前面来，因为在m2m2_bk_au_add_insert.py插入数据时，报book_m2m_author未定义。
book_m2m_author=Table('book_m2m_author',Base.metadata,
                Column('a_id', Integer, ForeignKey('authro.id')),
                Column('b_id', Integer, ForeignKey('books.id')),

             )

#2.2 创建图书表
class Books(Base):
    __tablename__='books'
    id=Column(Integer,primary_key=True)
    book_name=Column(String(64),nullable=False)
    pub_date=Column(DATE,nullable=False)

    # 下面这一行是在第二步插入数据时添加的，有两个作用：
    # 1，定义Books和Authro类通过book_m2m_author表来关联。
    # 2，backref='books'定义反查本类的关键字，比如author.books查询作者有哪些书
    authors = relationship('Authro', secondary=book_m2m_author, backref='books')

    # 下面这一行是在第三步查询数据时添加的，定义查询该类对象的返回格式
    def __repr__(self):
        return 'book_name:%s pub_date:%s'%(self.book_name,self.pub_date)



# 3，在数据库中创建表
Base.metadata.create_all(engine) # 创建表结构
'''
查看运行结果：
mysql> show tables;
+------------------+
| Tables_in_test_1 |
+------------------+
| address          |
| authro           |
| book_m2m_author  |
| books            |
| customer         |
| student          |
| study_record     |
+------------------+
7 rows in set (0.00 sec)

mysql> desc authro;
+-------------+-------------+------+-----+---------+----------------+
| Field       | Type        | Null | Key | Default | Extra          |
+-------------+-------------+------+-----+---------+----------------+
| id          | int(11)     | NO   | PRI | NULL    | auto_increment |
| author_name | varchar(32) | NO   |     | NULL    |                |
+-------------+-------------+------+-----+---------+----------------+
2 rows in set (0.00 sec)

mysql> desc books;
+-----------+-------------+------+-----+---------+----------------+
| Field     | Type        | Null | Key | Default | Extra          |
+-----------+-------------+------+-----+---------+----------------+
| id        | int(11)     | NO   | PRI | NULL    | auto_increment |
| book_name | varchar(64) | NO   |     | NULL    |                |
| pub_date  | date        | NO   |     | NULL    |                |
+-----------+-------------+------+-----+---------+----------------+
3 rows in set (0.00 sec)

mysql> desc book_m2m_author;
+-------+---------+------+-----+---------+-------+
| Field | Type    | Null | Key | Default | Extra |
+-------+---------+------+-----+---------+-------+
| a_id  | int(11) | YES  | MUL | NULL    |       |
| b_id  | int(11) | YES  | MUL | NULL    |       |
+-------+---------+------+-----+---------+-------+
2 rows in set (0.00 sec)

mysql> show create table book_m2m_author;
| book_m2m_author | CREATE TABLE `book_m2m_author` (
  `a_id` int(11) DEFAULT NULL,
  `b_id` int(11) DEFAULT NULL,
  KEY `a_id` (`a_id`),
  KEY `b_id` (`b_id`),
  CONSTRAINT `book_m2m_author_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `authro` (`id`),
  CONSTRAINT `book_m2m_author_ibfk_2` FOREIGN KEY (`b_id`) REFERENCES `books` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 |
我们从上面的三张表看出，author和books两张表平平常常，就是普通的表。
处理多对多关系的奥秘就在book_m2m_author第三张表上，没有主键id，仅有的两个键都是外键，
分别关联`authro` (`id`)和`books` (`id`)。

处理多对多关系，建表很平常，关键就是多对多的映射表。
接下来，是插入数据，疑问就是多对多映射表的处理。


'''