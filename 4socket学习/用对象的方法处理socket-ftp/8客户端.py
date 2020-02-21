import os,socket,subprocess,struct,json

#FTP 文件上传/下载
# 1 客户端输入 'put xxx.txt' 就是把xxx.txt文件上传到服务器的规定目录
# 2 客户端输入 'get xxx.txt' 就是从服务器规定的目录下载xxx.txt到规定目录。
# cmd_dic={
#     'cmd':'put',
#     'parms':'xxx.txt',
# }

# 报头 长度 bytes文件
def headers_serialize(headers_dic):
    # 序列化
    headers_json=json.dumps(headers_dic)
    headers_bytes=headers_json.encode('utf-8')
    # 封包长度 
    headers_size=struct.pack('i',len(headers_bytes))
    return [headers_size,headers_bytes]

class FtpClient:
    def __init__(self,host,port):
        self.host=host
        self.port=port
        self.client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.connect((self.host,self.port))
        
    def interactive(self):
        while True:
            data=input('>>').strip()
            if not data:
                continue
            # 空格分隔字符串得到列表 要求目录和文件名中不能有空格
            # ‘put d:/dfa/sdfa/sdf.txt’
            data_list=data.split() 
            # cmd,*parms=data_list # 因为有可能有多个参数所以加*
            cmd,parms=data_list # 单个参数就不用加*
            cmd_dic={
                'cmd':cmd,
                'parms':parms,
            }
            print(cmd_dic)
            # 如果是上传等本地要执行的文件 ，就要在客户端调put程序进行上传
            func=getattr(self,cmd_dic['cmd'],None)
            if func:
                func(cmd_dic['parms'])
            
            # 否则，就 
            else:
                # 序列化 得到 报头 长度 bytes报文 
                cmd_headers_size,cmd_bytes=headers_serialize(cmd_dic)
                # 发送 长度
                self.client.send(cmd_headers_size)
                # 发送 报文
                self.client.send(cmd_bytes)
        self.client.close()    

    def put(self,parms):
        
        print(parms)
        pass
        # 判别文件是否存在
        # 打开文件 读一行 发一行

if __name__ == "__main__":
    ftp_client=FtpClient('127.0.0.1',8091)
    ftp_client.interactive()