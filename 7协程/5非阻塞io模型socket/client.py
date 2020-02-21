# 非阻塞IO模型 client
import socket,os

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8081))

while True:
    msg='%s say hi'%os.getpid()
    client.send(msg.encode('utf-8'))
    print(msg)
    res=client.recv(1024)
    print(res.decode('utf-8'))