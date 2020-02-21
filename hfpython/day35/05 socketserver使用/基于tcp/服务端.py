import socketserver

# 通信循环
class MytcpHandler(socketserver.BaseRequestHandler):
    def hahahahahahahh(self):
        while True:
            try:
                data = self.request.recv(1024)  # 1024 接收数据的最大限制
                if not data: break  # 针对linux系统
                self.request.send(data.upper())  # 注意：收发都是以bytes为单位
            except ConnectionResetError:
                break
        self.request.close()


if __name__ == '__main__':
    #连接循环
    server=socketserver.ThreadingTCPServer(('127.0.0.1',8080),MytcpHandler)
    server.serve_forever()

    print(server.server_address)
    print(server.RequestHandlerClass)
    print(server.socket)



#conn,client_addr=sock.accpet()
# request, client_address = self.get_request()

# self.process_request(conn, client_address)

# self.finish_request(conn, client_address)

# obj=MytcpHandler(conn,client_address,server)

