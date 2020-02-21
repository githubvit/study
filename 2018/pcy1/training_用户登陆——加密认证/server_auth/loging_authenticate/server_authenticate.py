#_*_coding:utf-8_*_
'''
服务端多用户连接认证模块主程序
'''
import SocketServer
import auth
import json

from log import server_logger
# 创建日志记录器，这里有个重点就是：
# server_logger.logger(name)中的name必须和
# conf中setting.py中LOG_TYPES字典的key保持一致，否则出错。
access_logger=server_logger.logger('access')
# 创建用户空临时字典列表，只在内存中
'''每个用户只允许单个在线
    2.1 先在内存中建立临时用户字典列表，{‘user_id’:[]}，成功登陆后就append进去用户id，退出登陆就remove该用户id。
    2.2 用户登陆时，先去内存中看状态，没有在列表中则进行登陆，有则不允许登录，从而保证1个id只有1个用户在线'''
user_id_list = {'user_id':[],}

# 1,创建一个请求处理类，并且这个类要继承BaseRequestHandler,并且还有重写父类里的handler()
class Myhanlde(SocketServer.BaseRequestHandler):

    def handle(self):
        access_logger.info("ip:%s   port:%s connected" %(self.client_address[0], self.client_address[1]))
        print "ip:%s   port:%s connected" %(self.client_address[0], self.client_address[1])
        con = 0
        while True:
            con += 1
            self.data=self.request.recv(1024).strip()
            print("{} wrote:".format(self.client_address[0]))
            print(self.data)
            print type(self.data)
            if not self.data:
                print '客户端已断开',self.client_address
                if server_rec_userdic['user_id'].encode('utf-8') in user_id_list['user_id']:
                    user_id_list['user_id'].remove(server_rec_userdic['user_id'].encode('utf-8'))
                access_logger.info("ip:%s   port:%s break" % (self.client_address[0], self.client_address[1]))
                break
            #     json反序列化
            server_rec_userdic = json.loads(self.data)
            print server_rec_userdic
            print type(server_rec_userdic)
            print "次数",con

            if con > 2:
                print '次数太多'
                access_logger.error("ip:%s   port:%s    repeat_log:次数太多"%(self.client_address[0], self.client_address[1]))
                break
            elif server_rec_userdic['user_id'].encode('utf-8') in user_id_list['user_id']:
                # 用户登陆检查 如果已登录就断开
                repeat_log="%s 已经在线,请换个账号"%(server_rec_userdic['user_id'].encode('utf-8'))
                print repeat_log
                self.request.send(repeat_log.decode('utf-8').encode('utf-8'))
                access_logger.error( "ip:%s   port:%s   user_id:%s " % ( self.client_address[0], self.client_address[1],repeat_log))
                continue
            else:
                # 连接认证模块auth.py,获取认证结果
                authenticate_res= auth.authenticate(server_rec_userdic,user_id_list)
                access_logger.info("ip:%s   port:%s     user:%s res:%s " % (self.client_address[0], self.client_address[1],server_rec_userdic['user_id'].encode('utf-8'), authenticate_res))
                print user_id_list
                # 发送认证结果给客户端
                self.request.send(authenticate_res.decode('utf-8').encode('utf-8'))




def run():#这里才是最后从启动程序调用成功的关键，开始没有这一行，后面定义了该run（），把下面的2,3,4往左缩进。

# 2,实例化TCPServer ，并且传递server ip 和上面创建的请求处理类 给这个TCPServer
    server=SocketServer.ThreadingTCPServer(('localhost',6970),Myhanlde)
#ThreadingTCPServer开启并发多线程


# 3,call serve_forever() #处理多个请求，永远执行
    server.serve_forever()

# 4,call server_close() close the socket
    server.server_close()