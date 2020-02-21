#_*_coding:utf-8_*_


'''
消息循环服务端,远程命令
'''
# import os
import socket
server=socket.socket()#声明
server.bind(('localhost',6969))#绑定
server.listen(5)#监听
print '等待消息'
while True:#当一个连接实例断开后，连接下一个实例，alex在windows上试不出来（是因为点了stop方形，应该点close’X’），在linux下可以，满足多用户在线
    conn,addr=server.accept()#实例化连接，阻塞点
    print '开始收发',addr
    while True:#在一个实例中循环收发
        re=conn.recv(1024).decode('utf8').encode('utf8')
        print 'recv:',re
        if not re: #收到的为空就跳出
            print 'client is lost...'
            break #避免死循环，因为客户端一断开，conn.recv就不断的收到空数据，从而进入死循环。
        conn.send('from server %s'%re)
        # res=os.popen(re).read()#popen是os执行命令的方法，read是获取执行的结果
        # conn.send(res)

server.close()