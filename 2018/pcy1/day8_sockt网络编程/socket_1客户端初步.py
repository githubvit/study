#_*_coding:utf-8_*_

'''
socket客户端初步
'''
import socket
client=socket.socket()#声明socket地址簇及连接协议类型，默认为ipv4和tcp，同时生成socket连接对象
client.connect(('localhost',6969))#连接本机的6969端口，ip地址和端口要用元组包起来当一个值传进去
client.send('问个好 hello'.decode('utf-8').encode('utf-8'))#发送消息,
# 在py3所有数据的收发，只能用bytes类型，即————>'问个好 hello'.encode('utf8'),encode成bytes类型
data=client.recv(1024) #接收服务器发过来的消息，缓存大小为1024个字节即1k。
print 'recv:',data#打印收到的信息
client.close()#关闭连接