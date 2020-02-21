#_*_coding:utf-8_*_
'''
客户端接收文件,每次0.5k，这是ftp
'''
import socket
client=socket.socket()
client.connect(('localhost',6969))
i=0
while True:
    # msg=raw_input('>>:')
    msg = input('>>:')
    client.send(msg)
    data = client.recv(1024)
    if i==0:#把第一次服务器传过来的文件名作为客户端文件名的一部分
        f = open(data+'.bak', 'a')
    else:
        f.write(data)
        f.flush()
    i+=1
client.close()