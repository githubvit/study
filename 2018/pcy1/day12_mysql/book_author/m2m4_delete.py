# _*_coding:utf-8_*_

'''
4多对多删除

删除数据时不用管book_m2m_authors映射表， sqlalchemy会自动帮你把对应的数据删除
'''
import m2m1_bk_au_create
from sqlalchemy.orm import sessionmaker
from sqlalchemy import bindparam

# 1，创建与数据库的会话session，相当于操作文件的句柄。
Session_class = sessionmaker(bind=m2m1_bk_au_create.engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = Session_class()  # 生成session实例


# 2，直接删除作者
'''
在mysql直接删不了
mysql> delete from authro where id=6;
ERROR 1451 (23000): Cannot delete or update a parent row: a foreign key constraint fails (`test_1`.`book_m2m_author`, 
CONSTRAINT `book_m2m_author_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `authro` (`id`))
'''
authro_obj=session.query(m2m1_bk_au_create.Authro).filter(m2m1_bk_au_create.Authro.id==6)\
    .first()
'''用session.delete直接删就可以，映射表不用管，会自动更新'''
session.delete(authro_obj)
session.commit()
'''
删除成功：book_m2m_author自动更新

mysql> select * from authro;
+----+-------------+
| id | author_name |
+----+-------------+
|  1 | Alex        |
|  2 | Jack        |
|  3 | Rain        |
|  4 | Alex        |
|  5 | Jack        |
+----+-------------+
5 rows in set (0.00 sec)

mysql> select * from book_m2m_author;
+------+------+
| a_id | b_id |
+------+------+
|    3 |    1 |
|    3 |    2 |
|    2 |    2 |
|    1 |    1 |
|    4 |    4 |
+------+------+

mysql>
删除之前;
mysql> select * from authro;
+----+-------------+
| id | author_name |
+----+-------------+
|  1 | Alex        |
|  2 | Jack        |
|  3 | Rain        |
|  4 | Alex        |
|  5 | Jack        |
|  6 | Rain        |
+----+-------------+
mysql> select * from book_m2m_author;
+------+------+
| a_id | b_id |
+------+------+
|    3 |    1 |
|    3 |    2 |
|    2 |    2 |
|    1 |    1 |
|    4 |    4 |
|    6 |    4 |
+------+------+

'''