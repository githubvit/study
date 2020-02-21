#_*_coding:utf-8_*_
'''
socket ftp服务器
1,读取客户端client发过来的文件名
2，检查文件是否存在
3，打开文件
4，检测文件大小
5，发送文件大小给客户端
6，等客户端确认（克服粘包）
7，开始边读边发数据
8，发送md5
'''
import socket,os
import hashlib
server=socket.socket()
server.bind(('localhost',9998))#只能有一个参数,用元组。
server.listen(5)
while True:
    conn,addr=server.accept()
    print '新连接建立：',addr
    while True:
        print '1,读取客户端client发过来的文件名'
        data=conn.recv(1024)#python 3.x必须decode，否则报错。而python2.7不能decode，否则报错。
        if not data:
            print ('客户端已断开')
            break
        cmd, file_name = data.split()
        assert cmd=='get'  # 判断命令，用断言来卡住
        print('2,检查%s文件是否存在' % file_name)
        file_name=file_name.decode('utf-8')#要用decode解码成Unicode，否则os.path.isfile和os.stat都会判断错误

        '''
        检查文件是否存在->用os模块中的isfile，因为要判断是否是文件，就要先判断是否存在。
        '''

        if os.path.isfile(file_name):
            print('4，检测文件大小')
            file_size = os.stat(file_name).st_size
            print ('5，发送大小%s给客户端'%file_size)
            conn.send(str(file_size).encode())
            print '6，等客户端确认（克服粘包）'
            conn.recv(1024)
            print ('7，开始边读边发数据')
            m=hashlib.md5()#建立md5对象
            with open(file_name, 'rb') as f:
                for line in f:
                    conn.send(line) #在for循环中，line已经是二进制格式，因为文件是用二进制格式打开的。
                    m.update(line) #逐行计算md5
            print '8，发送md5的十六进制值',m.hexdigest()
            conn.send(m.hexdigest())
        else:
            conn.send('%s文件不存在'%file_name)
            print ('%s文件不存在'%file_name)


        print '发送完毕'
server.close()
