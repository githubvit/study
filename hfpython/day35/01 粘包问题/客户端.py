import socket
import struct
import json

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('127.0.0.1',8080))

while True:
    cmd=input('>>: ').strip() #get a.txt
    if not cmd:continue
    client.send(cmd.encode('utf-8')) #client.send(b'dir')

    # 先收报头长度
    header_size=struct.unpack('i',client.recv(4))[0]

    # 根据报头长度收出报头
    header_bytes=client.recv(header_size)
    header_json=header_bytes.decode('utf-8')
    header_dic=json.loads(header_json)

    print(header_dic)
    total_size=header_dic['total_size']
    res=b''
    recv_size=0
    while recv_size < total_size:
        data=client.recv(1024)
        res+=data
        recv_size+=len(data)
    print(res.decode('gbk'))

client.close()