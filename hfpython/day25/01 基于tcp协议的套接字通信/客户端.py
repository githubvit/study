import socket

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 买电话
phone.connect(('127.0.0.1',8081)) # 拨电话，地址为服务端的ip和端口

phone.send('你好'.encode('utf-8')) # 发消息b'hello'
data=phone.recv(1024) #收消息

print(data.decode('utf-8'))

phone.close()