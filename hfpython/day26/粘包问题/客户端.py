from socket import *
import time
client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8080))
# print(client)

client.send(b'hello')
time.sleep(1)
client.send(b'world')

client.close()