from socket import *
import os

client = socket()
client.connect(('127.0.0.1', 8080))

while True:
    data='%s say hello' %os.getpid()
    client.send(data.encode('utf-8'))
    res=client.recv(1024)
    print(res.decode('utf-8'))
