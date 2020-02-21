import socket

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 买电话
phone.bind(('127.0.0.1',8081)) #插手机卡，补充：0-65535 0-1024给系统用的
phone.listen(5) # 开机

print('start...')
conn,client_addr=phone.accept() # 等电话连接
print('连接来了：',conn,client_addr)

# 收发消息
msg=conn.recv(1024) #收消息，1024是一个最大的限制
print('客户端的消息: ',msg)
conn.send(msg+b'SB')


# 挂电话
conn.close()
# 关机
phone.close()
