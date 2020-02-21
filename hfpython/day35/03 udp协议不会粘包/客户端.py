import socket

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

client.sendto('hello'.encode('utf-8'),('127.0.0.1',8080))
client.sendto('wolrd'.encode('utf-8'),('127.0.0.1',8080))
client.sendto('oldboy123456'.encode('utf-8'),('127.0.0.1',8080))

