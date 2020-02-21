import socket

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #udp


# 收发 通信循环
while  True:
    msg=input('>>:')
    client.sendto(msg.encode('utf-8'),('127.0.0.1',8081))
    back_msg,se_addr=client.recvfrom(1024)
    print (back_msg)