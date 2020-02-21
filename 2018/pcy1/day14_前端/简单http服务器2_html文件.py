#_*_coding:utf-8_*_
'''
简单http网页服务器2 html文件

后缀名可以不是HTML，但是现在很多IDE对HTML有较好的支持，如果你编写的时候告诉IDE，
那么就可以提高不少效率。


'''

import socket
#客户端处理函数
def handle_request(client):
    buf=client.recv(1024)
    client.send("HTTP/1.1 200 OK\r\n\r\n")
    #把字符串加上浏览器能识别的标签，写在文件index里。这个就是前端干的事。
    with open('html2.html','rb') as f:
        #读出来
        s=f.read()
    #把读出来的发给客户端
    client.send(s)

#服务端监听
def main():
    server=socket.socket()
    server.bind(('',8000))
    server.listen(5)
    while True:
        conn,addrs=server.accept()
        #一有请求，就把请求发给客户端处理函数
        handle_request(conn)
        conn.close()


if __name__ == '__main__': main()