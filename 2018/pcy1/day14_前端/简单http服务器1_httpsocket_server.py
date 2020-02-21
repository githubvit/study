#_*_coding:utf-8_*_
'''
简单http网页服务器

http网页服务的本质都是利用socket进行数据收发，
http服务端不管是Apache还是Nginx，本质就是一个socket服务端，
浏览器就是特殊的socket客户端；
服务端对浏览器提供的每次浏览器请求，交给请求处理函数，完成后就关闭。
一次请求，一次关闭。
'''

import socket
#客户端处理函数
def handle_request(client):
    buf=client.recv(1024)
    client.send(bytes("HTTP/1.1 200 OK\r\n\r\n".decode('utf8').encode('utf8')))
    client.send(bytes('hello,jion'.decode('utf8').encode('utf8')))
#服务端监听
def main():
    server=socket.socket()
    server.bind(('localhost',8000))
    server.listen(5)
    while True:
        conn,addrs=server.accept()
        #一有请求，就把请求发给客户端处理函数
        handle_request(conn)
        conn.close()


if __name__ == '__main__':
    main()