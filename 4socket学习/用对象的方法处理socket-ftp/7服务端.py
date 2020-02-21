import os,socket,subprocess,struct,json

#FTP 文件上传/下载
# 1 客户端输入 'put xxx.txt' 就是把xxx.txt文件上传到服务器的规定目录
# 2 客户端输入 'get xxx.txt' 就是从服务器规定的目录下载xxx.txt。
# cmd_dic={
#     'cmd':'put',
#     'parms':'xxx.txt',
# }

# 3 服务端接收到客户端的命令，要取出命令和参数。
# 4 根据取出的命令调用相应的方法，执行该方法。
class FtpServer:
    def __init__(self,host,port):
        self.host=host
        self.port=port
        self.server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.bind((self.host,self.port))
        self.server.listen(5)

    def run(self):
        print('starting...')
        while True:
            conn,client_addr=self.server.accept()
            print('链接对象：',conn,client_addr)
            while True:
                try:
                    # 先收客户端 报头长度
                    h_size=conn.recv(4)
                    if not h_size: break #针对 线路故障时，Linux抛空
                    cmd_headers_size=struct.unpack('i',h_size)[0]

                    # 一把接收客户端 报文数据 反序列化 取出命令cmd
                    cmd_bytes=conn.recv(cmd_headers_size)
                    cmd_json=cmd_bytes.decode('utf-8')
                    cmd_dic=json.loads(cmd_json)
                    cmd=cmd_dic['cmd']
                    parms=cmd_dic['parms']
                    
                    # 用反射判断 是否有该命令 有就调用 没有就报错
                    func=getattr(self,cmd,None)
                    print('有没有%s'%cmd,func)
                    if func:
                        func(parms)
                    else:
                        err_msg='没有%s命令'%cmd
                        print(err_msg)  

                except ConnectionResetError:
                    break
            print('回收实例：',conn,client_addr)    
            conn.close()
        self.server.close()
    def put(self,parms):
        print('上传...',parms)
        pass
    def get(self,parms):
        print('下载...',parms)
        pass

if __name__ == "__main__":
    ftp_server=FtpServer('127.0.0.1',8091)
    ftp_server.run()
