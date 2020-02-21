import socket,struct

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# client.connect(('192.168.2.232',9090))
client.connect(('127.0.0.1',8090))

while True:
    cmd=input('>> ').strip()
    if not cmd:
        continue
    client.send(cmd.encode('utf-8'))
    # 解决 粘包 关键在于 保证每次 收发 都干净
    # 发：
    # 1 先把要发送字节的大小算出来
    # size=len(data)
    # 2 用struct模块按‘i’格式，把每次算出的大小统一封装成固定字节位数，就是4个bytes。
    # header=struct.pack('i',size)#对于数字用格式‘i’封    
    # 3 把上面的固定字节位数命名成报头heard
    # 4 发送报头
    # conn.send(header)
    # 5 发送数据
    # conn.send(dat    
    # 总结：上面实际定义了报文格式，根据tcp传输层nagle算法，
    # 因为报头数据足够小（4个bytes），报头和数据发送的时间间隔也足够小（ 连续发送），
    # 所以tcp传输层会把报头和数据一起发送。

    # 收
    # 接收方实际就收到了一次发送过来的，报头和数据在一起的打包数据。     
    # 那么接收方只要先取出4个bytes即报头，就可以知
    # 1 收报头
    header=client.recv(4)

    # 2 解包大小
    total_size=struct.unpack('i',header)[0]
    print('total_size:',total_size)

    # 3 循环接收数据
    size=0
    data=b''#定义空bytes
    while size<total_size:
       data+=client.recv(1024)
       size=len(data)
    #    size+=len(data) #错

    
    print(data.decode('gbk'))

client.close()