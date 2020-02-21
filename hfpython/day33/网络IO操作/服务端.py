from socket import *

s = socket()
s.bind(('127.0.0.1',8080))
s.listen(5)

while True:
    conn, addr = s.accept()
    print(addr)
    while True:
        try:
            data = conn.recv(1024)
            if not data: break
            print('from client msg: ',data)
        except ConnectionResetError:
            break
    conn.close()

