#  接收方：
import socket,subprocess,struct,json

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8091))

while True:
    cmd=input('>>').strip()
    if not cmd: continue
    client.send(cmd.encode('utf-8'))

    #  1 用4字节先接收 报头大小
    # h_size=client.recv(4)
    #  解包
    headers_size=struct.unpack('i',client.recv(4))[0]

    #  2 根据headers_size一把接收 报头bytes文件，
    # 转换成报头字典，从报头取出 数据大小
    headers_bytes=client.recv(headers_size)
    headers_json=headers_bytes.decode()
    headers_dic=json.loads(headers_json)
    total_size=headers_dic['total_size']
    print(headers_dic)
    print(type(headers_dic))
    print('total_size:',total_size)
    
    #  3 按数据大小循环取数据。
    size=0
    data=b''
    while size<total_size:
        data += client.recv(1024)
        size = len(data)

    print(data.decode('gbk'))    
client.close()        