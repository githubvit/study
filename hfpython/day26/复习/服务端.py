from socket import *

server=socket(AF_INET,SOCK_STREAM)
server.bind(('127.0.0.1',8080))
server.listen(5)

while True:
    conn,client_addr=server.accept() #(连接对象，客户端的ip和端口)
    print(client_addr)
    while True:
        try:
            data=conn.recv(1024)
            conn.send(data.upper())
        except ConnectionResetError:
            break

    conn.close()
server.close()