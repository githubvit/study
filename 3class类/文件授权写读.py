#文件授权写读
# 实现授权的关键点就是覆盖__getattr__方法
import time
class FileHandle:
    def __init__(self,filename,mode='r',encoding='utf-8'):
        self.file=open(filename,mode,encoding=encoding)
    def write(self,line):
        t=time.strftime('%Y-%m-%d %T')
        self.file.write('%s %s' %(t,line))
    #定义该函数实际上就是给f1.seek(0)授权，不然文件对象无法操作光标，报错。
    def __getattr__(self, item): 
        return getattr(self.file,item)

#定义 写文件 读文件函数 用写读模式
def filew_r(name,content,model='w+'):
    f1=FileHandle(name,model)
    # 1 写下去
    f1.write(content)
    # 2 把光标拉回来
    #如果没有定义def __getattr__(self, item)，
    # f1.seek(0)报错：AttributeError: 'FileHandle' object has no attribute 'seek'
    f1.seek(0)
    # 3 读出来
    print(f1.read())
    f1.close()

name='b.txt'
content="你好啊"

filew_r(name,content)