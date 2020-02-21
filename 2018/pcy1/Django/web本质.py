# _*_ coding:utf-8 _*_
'''
web本质就是一个socket，接收bytes，发送bytes。
'''

__author__ = "vite"
__date__ = '2019/1/30 15:28'

import socket

def handle_request(connt):
    buf=connt.recv(1024)
    connt.send('HTTP/1.1 200 OK\r\n\r\n')
    connt.send('Hello, Seven')
def main():
    sock=socket.socket()
    sock.bind(('localhost',8000))
    sock.listen(5)
    while True:
        connt,address=sock.accept()
        handle_request(connt)
        connt.close()

if __name__=='__main__':
    main()