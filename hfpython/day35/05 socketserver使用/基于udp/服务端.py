import socketserver

# 通信循环
class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # print(self.request)
        res=self.request[0]
        print('客户端发来的数据：',res)

        self.request[1].sendto(res.upper(),self.client_address)


if __name__ == '__main__':
    #连接循环
    server=socketserver.ThreadingUDPServer(('127.0.0.1',8080),MyUDPHandler)
    server.serve_forever()