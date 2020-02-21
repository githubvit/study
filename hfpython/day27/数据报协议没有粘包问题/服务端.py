import socket

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # 数据报协议
server.bind(('127.0.0.1',8080))



res1,client_addr=server.recvfrom(1024) #b'h'
print(res1)

res2,client_addr=server.recvfrom(1024) #b'wo'
print(res2)

res3,client_addr=server.recvfrom(1024) #b'ego'
print(res3)