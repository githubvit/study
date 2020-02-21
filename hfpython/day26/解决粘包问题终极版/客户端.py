from socket import *
import struct
import json

client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8080))
# print(client)

while True:
    cmd=input('>>>: ').strip()
    if not cmd:continue
    client.send(cmd.encode('utf-8'))
    #1、先收报头的长度
    header_size=struct.unpack('i',client.recv(4))[0]

    #2、接收报头
    header_bytes=client.recv(header_size)

    #3、解析报头
    header_json=header_bytes.decode('utf-8')
    header_dic=json.loads(header_json)
    print(header_dic)

    total_size=header_dic[ 'total_size']
    # print(total_size) #1025
    #4、根据报头内的信息，收取真实的数据

    recv_size=0
    res=b''
    while recv_size < total_size:
        recv_data=client.recv(1024)
        res+=recv_data
        recv_size+=len(recv_data)

    print(res.decode('gbk'))
client.close()