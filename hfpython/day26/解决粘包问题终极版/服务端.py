from socket import *
import subprocess
import struct
import json

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

            # 1、制作报头
            header_dic={
                'total_size':len(stdout) + len(stderr),
                'md5':'123svsaef123sdfasdf',
                'filename':'a.txt'
            }
            header_json = json.dumps(header_dic)
            header_bytes = header_json.encode('utf-8')

            # 2、先发送报头的长度
            header_size=len(header_bytes)
            conn.send(struct.pack('i',header_size))

            # 3、发送报头
            conn.send(header_bytes)

            # 4、发送真实的数据
            conn.send(stdout)
            conn.send(stderr)
        except ConnectionResetError:
            break

    conn.close()
server.close()