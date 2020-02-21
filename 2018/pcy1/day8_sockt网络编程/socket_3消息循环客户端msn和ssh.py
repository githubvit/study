#_*_coding:utf-8_*_
'''
消息循环客户端，发送命令给远程服务器，接收执行结果
'''
import socket

client=socket.socket()
client.connect(('localhost',8001))
#如果是连接linux 必须在linux服务端清空防火墙 iptables -F
# 否则连不上
# C:\Users\hp>ping 192.168.2.240:6969
# Ping 请求找不到主机 192.168.2.240:6969。请检查该名称，然后重试。
while True:#循环收发 输入为空则卡死
    msg=raw_input('>>:').strip()
    if not msg: continue #如果输入为空，则跳过本次，继续输入
    # if len(msg)==0:continue#这句和上面效果是一样的，判断输入的长度为0
    client.send(msg.decode('utf-8').encode('utf-8'))
    data=client.recv(1024)
    print data
    #从windows返回的命令结果是gbk字符集,解码成unic，编码成可识别的utf8字符集
client.close()