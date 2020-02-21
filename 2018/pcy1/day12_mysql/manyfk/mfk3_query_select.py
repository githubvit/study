#_*_coding:utf-8_*_

'''
多外键关联
一张表有两个外键关联另一张表的同一个字段。

3,查询反查
从建表的程序中导入engine和Customer类、Address类
顾客表中的账单邮寄地址和货物邮寄地址都关联地址表中的id字段
'''


from sqlalchemy.orm import sessionmaker
import mfk1_create

# 1，创建与数据库的会话session，相当于操作文件的句柄。
Session_class = sessionmaker(bind=mfk1_create.engine)# 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = Session_class()  # 生成session实例

# 2，在mfk1_create模块的相应类中定义查询的返回格式def __repr__及反查关键字'billing_name'和'billing_name'
'''
class Customer(Base):#顾客表
    billing_address = relationship("Address", foreign_keys=[billing_address_id],backref='billing_name')
    shipping_address = relationship("Address", foreign_keys=[shipping_address_id],backref='shipping_name')
    def __repr__(self):
        return 'name:%s'%self.name
        
class Address(Base):#地址表
    def __repr__(self):
        return '%s-%s-%s'%(self.street,self.city,self.state)
'''

# 3，正查：查询alex的账单地址、货物地址
data=session.query(mfk1_create.Customer).filter(mfk1_create.Customer.name=='alex').first()
print data.billing_address,data.shipping_address
'''账单地址、货物地址结果
tiantongyuan-changping-BJ wudaokou-haidian-BJ
'''

# 4，反查：查询address中id=5的货物地址顾客名字和id=5的账单地址顾客名字
data1=session.query(mfk1_create.Address).filter(mfk1_create.Address.id==5).first()
print data1
'''mfk1_create.Address.id==5地址为：
wudaokou-haidian-BJ'''
print data1.shipping_name
'''货物地址人结果：
[name:alex]'''
print data1.billing_name
'''账单地址人结果：
[]
说明address表中id=5的地址只是收货地址
当查询address表中id=6的地址时：
yanjiao-langfang-HB
data1.shipping_name：[name:jack]
data1.billing_name：[name:jack]
说明该地址既是货物地址又是账单地址
'''

# 查和所有顾客相关的地址，对于多外键关联，要关闭到只剩一个外键，在mfk1_create模块的Customer类中注释1个关联外键，再注释掉relationship即可。
# data2=session.query(mfk1_create.Address).join(mfk1_create.Customer).all()
##注释掉shipping_address_id结果[tiantongyuan-changping-BJ, yanjiao-langfang-HB]
# print data2