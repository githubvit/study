import socket

HOST = 'localhost'  # The remote host
PORT = 8001 # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    msg = raw_input(">>:")
    if len(msg)== 0:continue
    s.sendall(msg.decode('utf-8').encode('utf-8'))
    data = s.recv(1024)

    print'Received', data
s.close()
