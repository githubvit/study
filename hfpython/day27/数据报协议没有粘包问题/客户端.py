import socket

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # 数据报协议

client.sendto(b'hello',('127.0.0.1',8080))
client.sendto(b'world',('127.0.0.1',8080))
client.sendto(b'egon',('127.0.0.1',8080))
