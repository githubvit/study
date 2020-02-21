from socket import *
import struct

client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8080))
# print(client)

while True:
    cmd=input('>>>: ').strip()
    if not cmd:continue
    client.send(cmd.encode('utf-8'))
    #1、先收固定长度的报头
    header=client.recv(4)
    #2、解析报头
    total_size=struct.unpack('i',header)[0]
    print(total_size) #1025
    #3、根据报头内的信息，收取真实的数据

    recv_size=0
    res=b''
    while recv_size < total_size:
        recv_data=client.recv(1024)
        res+=recv_data
        recv_size+=len(recv_data)

    print(res.decode('gbk'))
client.close()