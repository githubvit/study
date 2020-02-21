import socket
import subprocess
import json
import struct

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# print(server)

#服务端和客户端都需要有ip和port，但 只有服务端才绑定ip和port
server.bind(('127.0.0.1',8080))
server.listen(5) # 半连接池：限制的是请求数，而不是连接数

while True:
    conn,client_addr=server.accept() # 等待客户端发来连接请求
    print(conn)
    while True:
        try:
            data=conn.recv(1024) #b'get a.txt'
            if not data:break #针对linux系统

            #==========================
            obj=subprocess.Popen(data.decode('utf-8'),
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             )

            stdout=obj.stdout.read()
            stderr=obj.stderr.read()
            print(len(stdout)+len(stderr))
            #=================================

            #制作报头
            header_dic = {
                'filename': 'a.txt',
                'md5': 'asdf1231xcv123',
                'total_size': len(stdout) + len(stderr)
            }
            header_json = json.dumps(header_dic)
            header_bytes = header_json.encode('utf-8')

            # 1、发送报头的长度
            res=struct.pack('i', len(header_bytes))
            conn.send(res)

            #2、发送报头
            conn.send(header_bytes)


            # 发送真实数据
            conn.send(stdout)
            conn.send(stderr) # 注意：收发都是以bytes为单位

            # with open('a.txt','rb') as f:
            #     for line in f:
            #         conn.send(line)

        except ConnectionResetError:
            break
    conn.close()
server.close()