import socket

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.sendto('hello'.encode('utf-8'),('127.0.0.1',8082))
client.sendto('world'.encode('utf-8'),('127.0.0.1',8082))