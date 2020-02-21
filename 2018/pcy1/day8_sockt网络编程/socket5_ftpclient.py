#_*_coding:utf-8_*_
'''
ftp客户端，发送文件名给远程服务器，下载文件
1，发送要下载的文件名
2，接收服务端发送过来的文件的大小
3，发送确认信号
4，接收文件,边收边写，直到大小相等
'''
import socket,hashlib

client=socket.socket()
client.connect(('localhost',9998))

while True:#循环收发 输入为空则卡死
    print ('1，发送要下载的文件名')
    cmd_file=raw_input('>>:').strip()
    if len(cmd_file)==0: continue #如果输入为空，则跳过本次，继续输入
    assert cmd_file.startswith('get')#用断言来卡住
    client.send(cmd_file.decode('utf-8').encode('utf-8'))
    file_name=cmd_file.split()[1].decode('utf-8')#如果不用decode，发现文件名就是乱码

    print ('2，接收服务端发送过来的文件的大小')
    recv_data=client.recv(1024).decode('utf-8')
    if recv_data.isdigit():
        recv_size=int(recv_data)#接收的大小是字符串，要int，在py3.x中要decode后才能转int。
    else:
        print recv_data
        break
    print ('3，发送已收到文件大小为%s的确认信号'%recv_size)
    client.send(b'ok')#克服粘包
    print ('4，接收文件,边收边写')
    res_size=0
    f=open(file_name+'.bak','wb')
    m=hashlib.md5()
    while res_size<recv_size:#比较每次收的大小，和第一次收到的大小对比，保持同步
        '''用如下recv(size)套路杜绝下一次发送的ser_md5粘包'''
        if recv_size-res_size > 1024:#如果size太大会超出recv的限制
            size=1024
        else:
            size=recv_size-res_size#如果size不超出recv的限制

        res=client.recv(size)#用size这个动态变量来杜绝ser_md5粘包
        res_size+=len(res)#每次收到的有可能小于1024，所以必须用len判断
        f.write(res)
        m.update(res)
        # print '每次收到的大小：',res_size
    else:
        f.close()
        print'接收完毕，总大小：',res_size
        print '接收到文件的md5',m.hexdigest()
    ser_md5=client.recv(1024)
    print '发送端文件的md5',ser_md5

client.close()