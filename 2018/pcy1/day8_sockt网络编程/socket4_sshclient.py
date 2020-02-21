#_*_coding:utf-8_*_
'''
ssh客户端，发送命令给远程服务器，接收执行结果
'''
import socket

client=socket.socket()
client.connect(('localhost',9999))
# client.connect(('192.168.2.240',9999))#多客户端时，要用close 即x(而不是stop即□)，选断开连接disconnect(而不能选terminal)。
#如果是连接linux 必须在linux服务端清空防火墙 iptables -F
# 否则连不上
# C:\Users\hp>ping 192.168.2.240:6969
# Ping 请求找不到主机 192.168.2.240:6969。请检查该名称，然后重试。
while True:#循环收发 输入为空则卡死
    cmd=raw_input('>>:').strip()
    if len(cmd)==0: continue #如果输入为空，则跳过本次，继续输入
    client.send(cmd.decode('utf-8').encode('utf-8'))
    recv_size=int(client.recv(1024))#接收的大小是字符串，要int,py3要用int(client.recv(1024).decode('utf-8')).
    client.send(b'ok')#克服粘包
    print '应收总大小：',recv_size
    res_size=0
    res_data=b''#建立空的二进制字符串
    while res_size<recv_size:#比较每次收的大小，和第一次收到的大小对比，保持同步
        res=client.recv(1024)
        res_size+=len(res)#每次收到的有可能小于1024，所以必须用len判断，这里就是bytes二进制的大小
        res_data += res#把每次收到的二进制数据加入事先定义的空二进制字符
        # print res

        print '每次收到的大小：',res_size
    else:
        print'接收完毕，总大小：',res_size
        print res_data.decode('utf-8')

client.close()