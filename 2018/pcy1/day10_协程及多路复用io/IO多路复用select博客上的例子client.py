#_*_coding:utf-8_*_
__author__ = 'Alex Li'


import socket
import sys

messages = [ b'This is the message. ',
             b'It will be sent ',
             b'in parts.',
             ]
# 连linux要iptables -F 清空防火墙
# server_address = ('192.168.2.240', 6698)
server_address=('localhost', 8001)

#  连接windows 的socket server，最大极限就是500个，linux到了8000个连接，没敢往上加。
socks = [ socket.socket(socket.AF_INET, socket.SOCK_STREAM) for i in range(1000)]

# Connect the socket to the port where the server is listening
print('connecting to %s port %s' % server_address)
for s in socks:
    s.connect(server_address)

for message in messages:

    # Send messages on both sockets
    for s in socks:
        print('%s: sending "%s"' % (s.getsockname(), message) )
        s.send(message)

    # Read responses on both sockets
    for s in socks:
        data = s.recv(1024)
        print( '%s: received "%s"' % (s.getsockname(), data) )
        if not data:
            print(sys.stderr, 'closing socket', s.getsockname() )