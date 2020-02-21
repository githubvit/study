import socket

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(('127.0.0.1',8080))


res1,client_addr=server.recvfrom(1024) #b'hello'
print(res1)

res2,client_addr=server.recvfrom(1024) #b'wolrd'
print(res2)

res3,client_addr=server.recvfrom(1024) #b'oldboy123456'
print(res3)