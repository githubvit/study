import socket

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # 数据报协议
server.bind(('127.0.0.1',8080))

while True:
    client_data,client_addr=server.recvfrom(1024)
    msg=input('回复%s:%s>>>:' %(client_addr[0],client_addr[1]))
    server.sendto(msg.encode('utf-8'),client_addr)