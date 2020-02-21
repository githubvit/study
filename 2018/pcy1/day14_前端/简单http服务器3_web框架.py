#_*_coding:utf-8_*_
'''
简单http网页服务器3

web框架
数据库获取数据，然后替换到HTML文件的指定位置，干这事的就是web框架。

'''

import socket,time
#2，客户端处理函数
def handle_request(client):
    buf=client.recv(1024)
    client.send(bytes("HTTP/1.1 200 OK\r\n\r\n".decode('utf8').encode('utf8')))
    #把字符串加上浏览器能识别的标签，写在文件index里。这个就是前端干的事。
    with open('index2','r') as f:
        #读出来
        s=f.read()#因为用r模式读出来的，是个str
    r=str(time.ctime())
    #把@@@@字符串替换成服务器当前时间,静态变成了动态，如果把r变成从数据库读出数据，在规定的地方显示不同的数据。
    sr=s.replace('@@@@',r)
    #把读出来的发给客户端
    client.send(bytes(sr.decode('utf8').encode('utf8')))

#1，服务端监听
def main():
    server=socket.socket()
    server.bind(('localhost',8000))
    server.listen(5)
    while True:
        conn,addrs=server.accept()
        #一有请求，就把请求发给客户端处理函数
        handle_request(conn)
        conn.close()


if __name__ == '__main__': main()