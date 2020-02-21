from socket import *
import subprocess

server=socket(AF_INET,SOCK_STREAM)
server.bind(('127.0.0.1',8080))
server.listen(5)

conn,client_addr=server.accept()


res1=conn.recv(1)
print('第一次：',res1)
res2=conn.recv(1024)
print('第二次: ',res2)

conn.close()
server.close()