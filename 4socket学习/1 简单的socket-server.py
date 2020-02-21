import socket

#1 实例化socket对象 - 买手机
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#socket.AF_INET 表示基于网络通信的套接字
#socket.AF_UNIX 表示基于文件通信的套接字（一台机器上的不同程序之间的通信，unix就是基于文件的）
#socket.SOCK_STREAM 流式协议-表示基于tcp协议的报文格式
#socket.SOCK_DGRAM  广播协议-表示基于udp协议的报文格式

#2 绑定ip和port - 手机插sim卡  
phone.bind(('127.0.0.1',9090))
# 参数使用元组方式把ip和端口组成一个参数 
# 计算机端口 0~65535，0~1024是系统预留的，1024~65535是给应用程序用的。

#3 监听 - 开机
phone.listen(5)
# 半连接池数量最多是5个

#4 等待 - 等电话打进来
while True: #链接循环 
    print('starting')
    conn,client_addr=phone.accept()
    #返回链接对象conn、客户端地址client_address
    print(conn,client_addr)

    #5 收/发 - 通话
    while True: #通信循环
        try:#网络异常时：针对windows抛ConnectionResetError的处理
            data=conn.recv(1024) #1024bytes,最大收1024
            if not data:break #网络异常时：针对Linux循环抛空的处理
            print('收到客户端消息',data)
            conn.send(data.upper())
        except ConnectionResetError:#链接异常
            break
    #6 挂机 关闭本次通信
    conn.close()

#7 关机
phone.close()
