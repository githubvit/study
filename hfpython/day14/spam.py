#spam.py
print('from the spam.py')
__all__=['money','read1'] # from .. import *

money=1000

def read1():
    print('spam模块.read1：',money)

def read2():
    print('spam模块.read2')
    read1()

def change():
    global money
    money=0



# print(__name__)
# __name__的值
#1、在文件被直接执行的情况下，等于'__main__'
#2、在文件被导入的情况下，等于模块名

if __name__ == '__main__':
    # print('文件被当中脚本执行啦。、。')
    read1()
else:
    print('文件被导入啦')