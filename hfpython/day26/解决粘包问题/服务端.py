from socket import *
import subprocess
import struct

server=socket(AF_INET,SOCK_STREAM)
server.bind(('127.0.0.1',8080))
server.listen(5)

while True:
    conn,client_addr=server.accept() #(连接对象，客户端的ip和端口)
    print(client_addr)
    while True:
        try:
            cmd=conn.recv(1024)
            obj=subprocess.Popen(cmd.decode('utf-8'),
                                 shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE
                                 )
            stdout=obj.stdout.read()
            stderr=obj.stderr.read()

            # 1、制作固定长度的报头
            total_size=len(stdout) + len(stderr)
            header=struct.pack('i',total_size)

            # 2、发送报头
            conn.send(header)

            #3、发送真实的数据
            conn.send(stdout)
            conn.send(stderr)
        except ConnectionResetError:
            break

    conn.close()
server.close()