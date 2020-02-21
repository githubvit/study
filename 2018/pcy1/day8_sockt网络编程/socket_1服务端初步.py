#_*_coding:utf-8_*_

'''
socket服务端初步
'''
import socket
server =socket.socket()#声明socket地址簇及类型，默认为ipv4和tcp，同时生成socket连接对象
server.bind(('localhost',6969))#绑定要监听的地址和端口
server.listen(5)#监听,python2.x必须要有个整数是最大异步通信连接数；python3不用，可以为空。
print ('开始等电话')
conn,addr=server.accept()#等待,accept会有两个值，电话的实例conn和地址addr
# conn就是客户端连过来而在服务器端为其生成的一个连接实例
print (conn,addr)
print ('电话来了')
data=conn.recv(1024)#接收
print '收到的消息recv:',data.decode('utf-8') #打印接收的消息
conn.send(data.upper())#发送，将收到的消息变成大写发回去。
server.close()