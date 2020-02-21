import socket

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.bind(('127.0.0.1',8081))
phone.listen(5)

print('start...')
while True: # 连接循环
    conn,client_addr=phone.accept()
    print('客户端 ',client_addr)

    while True: # 通信循环
        try:
            msg=conn.recv(1024)
            print('客户端的消息: ',msg)
            conn.send(msg+b'SB')
        except ConnectionResetError:
            break
    conn.close()
phone.close()
