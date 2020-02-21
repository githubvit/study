# import time
#
# class People:
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#
#     def __del__(self): # 在对象被删除的条件下，自动执行
#         print('__del__')
#
#
# obj=People('egon',18,'male')
#
# del obj #obj.__del__()
#
# time.sleep(5)




# class Mysql:
#     def __init__(self,ip,port):
#         self.ip=ip
#         self.port=port
#         self.conn=connect(ip,port) # 申请系统资源
#
#     def __del__(self):
#         self.conn.close()
#
# obj=Mysql('1.1.1.1',3306)


class MyOpen:
    def __init__(self,filepath,mode="r",encoding="utf-8"):
        self.filepath=filepath
        self.mode=mode
        self.encoding=encoding
        self.fobj=open(filepath,mode=mode,encoding=encoding)

    def __str__(self):
        msg="""
        filepath:%s
        mode:%s
        encoding:%s
        """ %(self.filepath,self.mode,self.encoding)
        return msg

    def __del__(self):
        self.fobj.close()

# f=open('a.txt',mode='r',encoding='utf-8')

f=MyOpen('aaa.py',mode='r',encoding='utf-8')
# print(f.filepath,f.mode,f.encoding)
# print(f)

# print(f.fobj)
res=f.fobj.read()
print(res)