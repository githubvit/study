import socket

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',8080))
server.listen(5)

while True:
    conn,client_addr=server.accept()
    print(client_addr)

    while True:
        try:
            data=conn.recv(1024)
            if not data:break # 针对linux系统
            conn.send(data.upper())
        except ConnectionResetError:
            break
    conn.close()

server.close()