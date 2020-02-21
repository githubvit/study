import socket

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # 数据报协议
server.bind(('127.0.0.1',8080))

while True:
    client_data,client_addr=server.recvfrom(1024)
    server.sendto(client_data.upper(),client_addr)