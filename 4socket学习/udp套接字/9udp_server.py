# UDP协议：
#   数据报协议
#   特点：
#       无连接，
#   优点：
#       发送效率高，不粘包。但有效传输的数据量最多为512字节，因此导致
#   dns的跟服务器最多13台。


#   缺点：
#       不可靠：发送数据，无需对确认，容易丢包

#   注意：
#       接收的缓冲区要大于发送数据的大小，否则windows系统会报错。

#   应用场景：
#       通常应用于查询的操作，比如dns的查询、ntp同步。


#   一发对应一收
import socket

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #udp
server.bind(('127.0.0.1',8081))

# 收发 通信循环
while  True:
    data,addr=server.recvfrom(1024)
    print(addr)
    server.sendto(data.upper(),addr)