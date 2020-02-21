import socket


#1 实例化socket对象 - 买手机
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#2 连接服务端 - 拨电话
phone.connect(('192.168.2.232',9090))

#3 发/收消息
while True:
    msg=input('>>').strip()
    if not msg:
        continue
    phone.send(msg.encode('utf-8'))
    data=phone.recv(1024)
    print(data)

#4 挂断
phone.close()