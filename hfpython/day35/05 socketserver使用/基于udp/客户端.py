import socket
import os

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    msg='%s hello' %os.getpid()
    client.sendto(msg.encode('utf-8'),('127.0.0.1',8080))

    res,server_addr=client.recvfrom(1024)
    print(res)