#_*_coding:utf-8_*_
'''
web框架路径处理函数，html文件路径按主程序相对路径，统一放入templet模板目录
'''
from model import mdata#引入数据模块
def handle_index():
    # 读取模板
    f=open('templet/index.html','r')
    data=f.read()
    f.close()
    # 读取数据
    dt=str(mdata.dt)
    # 把数据填入模板
    data1=data.replace("index",dt)
    return data1
def handle_date():
    f = open('templet/date.html', 'r')
    data = f.read()
    f.close()
    return data