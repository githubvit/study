#_*_coding:utf-8_*_
'''
服务器文件发送 ftp
'''
import socket
server=socket.socket()
server.bind(('localhost',6969))
server.listen(5)
print '等待连接'
s=raw_input('传输的文件名：')
# s=r'%s'%s 本来是解决输入的路径中的符号问题，但不需要，关闭这条代码，路径也没问题。

conn,addr=server.accept()
conn.send(s.decode('utf8').encode('gbk'))
#第一次发送文件名，首先把utf8的输入解码成Unicode，再编码成系统能识别的字符集
# 解决了中文文件名的问题
print '开始发送文件'
while True:
    data=conn.recv(1024)
    # if not data:
    #     break

    f = open(s.decode('utf8'), 'r')  # 打开文件
    s1 = f.read()  # 读出文件
    print (len(s1))
    # f.close()

    conn.sendall(s1)#发送结果

server.close()
