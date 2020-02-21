#_*_coding:utf-8_*_

'''
客户端登陆基础类
'''

import socket
import hashlib
import json

class client_loging(object):
    '''
    客户端登陆
    1，实现和服务器的连接，先实例化，
        要给定ip和port参数
    2，登录，调用loging功能
        要输入用户名和密码
        接收服务端验证结果
    3，断开与服务器的连接，调用close功能
        
    '''
    def __init__(self,ip,port,*args,**kwargs):
        self.client=socket.socket()
        self.client.connect((ip,port))
    def loging(self):
        while True:
            user_id = raw_input('your_id>>:')
            user_password = raw_input('password>>:')
            if not (user_id and user_password):continue
            # 对密码取md5
            m=hashlib.md5()
            m.update(user_password.decode('utf-8').encode('utf-8'))
            user_dict={
                'user_id':user_id,
                'user_password':m.hexdigest()
            }
            user_json=json.dumps(user_dict)
            #发送用户登录的用户名和密码的md5
            self.client.send(user_json.decode('utf-8').encode('utf-8'))
            # 接收服务端发来的用户认证结果
            user_authenticate = self.client.recv(1024)
            print user_authenticate
    #         if user_authenticate:
    #             print ("user_id:%s login sucess " % (user_id))
    #
    #         else:
    #             print ('user_id or user_password is error')
    def close(self):
        self.client.close()

# -----------test
# ip=raw_input('ip>>:')
# port=raw_input('port>>:')
client_loger=client_loging('localhost',6970)#实例化
try:
    client_loger.loging()
except Exception as e:
    print e

# print client_loging.__doc__