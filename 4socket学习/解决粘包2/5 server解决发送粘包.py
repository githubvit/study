
# 发送方：
import socket,subprocess,struct,json

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',8091))
server.listen(5)

print('starting...')

while True:
    conn,addr=server.accept()
    print('来了新链接:',conn,addr)

    while True:
        try:
            cmd=conn.recv(1024)
            if not cmd: break
            cmd=cmd.decode()
            res=subprocess.Popen(cmd,shell=True,
            stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            stdout=res.stdout.read()
            stderr=res.stdout.read()

            # 1 用字典定义报头，解决报头内容问题，
            #  把报文数据大小total_size放入，解决数字限制问题。
            headers_dic={
            'filepath':'d:/xxx/x.txt',
            'md5':'afasdfafsfa',
            'total_size':len(stdout)+len(stderr),
            }
            print('total_size:',headers_dic['total_size'])
            # 2 把报头字典转为json字符串，再把json字符串encoding成bytes。
            headers_json=json.dumps(headers_dic)
            headers_bytes=headers_json.encode('utf-8')
            
            # 3 用headers_size=struct.pack('i',len(报头bytes文件))
            # 由于报头bytes文件数据都比较小，
            # 此时用struct封装报头文件长度就没问题了。
            headers_size=struct.pack('i',len(headers_bytes))

            #  4 发送：
            #  先发 报头长度headers_size
            conn.send(headers_size)
            #  再发 报头bytes文件
            conn.send(headers_bytes)
            #  最后发 数据
            conn.send(stdout)
            conn.send(stderr)
        except ConnectionResetError:
            break
    conn.close()
server.close()