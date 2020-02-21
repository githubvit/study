#_*_coding:utf-8_*_
'''
socketserver与socket_3消息循环客户端msn和ssh连用
'''
import SocketServer

# 1,创建一个请求处理类，并且这个类要继承BaseRequestHandler,并且还有重写父类里的handler()
class Myhanlde(SocketServer.BaseRequestHandler):
    def handle(self):#每一个连接请求过来都会走这里,处理和客户端的交互
        print("%s,%s connect:" % (self.client_address[0], self.client_address[1]))
        while True:
            try:
                self.data=self.request.recv(1024).strip()#每一个连接请求过来都会实例化该类Myhanlde
                print("%s,%s wrote:"% (self.client_address[1],self.client_address[0]))
                print(self.data)
                if not self.data: #服务端收不到客户端的数据，代表客户端已断开，break。该实例被释放
                    print '客户端已断开',self.client_address
                    break
                self.request.send(self.data.upper().decode('utf-8').encode('utf-8'))
            except Exception as e:
                print "未知错误",e
                break
# 2,实例化TCPServer ，并且传递server ip 和上面创建的请求处理类 给这个TCPServer
server=SocketServer.ThreadingTCPServer(('localhost',6968),Myhanlde)
#每一个连接请求过来都会实例化上面创建的请求处理类 Myhanlde，然后拿这个类的def handle和客户端去交互
#ThreadingTCPServer开启并发多线程监听

# 3,call serve_forever() #处理多个请求，永远执行
server.serve_forever()
# 4,call server_close() close the socket
server.server_close()