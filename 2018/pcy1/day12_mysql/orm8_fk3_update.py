#_*_coding:utf-8_*_

'''
8,外键foreign key
8.3修改数据

study_record考勤表在插入时stu_id字段为null，修改

'''

from sqlalchemy import create_engine,ForeignKey,bindparam
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,DATE,Enum
from sqlalchemy.orm import sessionmaker
# 1，连接数据库
engine = create_engine("mysql+pymysql://root:another333@localhost/test_db",
                       encoding='utf-8',echo=True)
#mysql+pymysql表示采用pymysql执行原生sql，
#echo=True表示显示创建过程，可以看到生成的原生sql。

# 2，创建表和类的映射
Base = declarative_base()  # 生成orm基类
class Student(Base):#建立学生表
    __tablename__='student'
    id=Column(Integer,primary_key=True)
    name=Column(String(32),nullable=False)
    register_date=Column(DATE,nullable=False)

class StudyRecody(Base):#建立考勤表
    __tablename__='study_record'
    id=Column(Integer,primary_key=True)
    day=Column(Integer,nullable=False)
    status=Column(String(32),nullable=False)
    # 3，外键关联，关联student表的id字段
    stu_id=Column(Integer,ForeignKey('student.id'))

# 3，创建与数据库的会话session，相当于操作文件的句柄。
Session_class = sessionmaker(bind=engine)# 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = Session_class()  # 生成session实例
# 4，修改考勤表 update(字典)
# 这是自己参考大量资料，摸索出来的批量更新方法，首先update有where，然后where要绑定参数，这就要在import上引入bindparam。
session.execute(
    StudyRecody.__table__.update().where(StudyRecody.id==bindparam('b_id')),
    [   {'b_id':1,'day':1,'status':'yes','stu_id':1},
        {'b_id':2,'day':1,'status':'yes','stu_id':2},
        {'b_id':3,'day':1,'status':'no','stu_id':3},
        {'b_id':4,'day':2,'status':'no','stu_id':1},
        ]


)
'''UPDATE study_record SET day=%(day)s, status=%(status)s WHERE study_record.id = %(b_id)s
这是批量修改的方法，execute可以执行多条数据插入或更新，但是数据的格式必须相同，不可以像：

[{'b_id':1,'day':1,'status':'yes'},
    {'b_id':3,'status':'no'}]
    
    这样无法执行，因为第2条需要的原生sql和第一条是不同的'''

'''
上面的执行结果如下：

mysql> select * from study_record;
+----+-----+--------+--------+
| id | day | status | stu_id |
+----+-----+--------+--------+
|  1 |   1 | yes    |      1 |
|  2 |   1 | yes    |      2 |
|  3 |   1 | no     |      3 |
|  4 |   2 | no     |      1 |
+----+-----+--------+--------+
4 rows in set (0.00 sec)

mysql>
'''

session.commit()