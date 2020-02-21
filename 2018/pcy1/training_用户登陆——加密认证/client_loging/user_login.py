#_*_coding:utf-8_*_
'''
用户登录模块
'''
import server_authenticate

def user_login():
    '''
    用户登录模块,
    用于客户端，
    输入用户名和密码，
    经验证成功后，
    实现登录

    '''
    # user_id=raw_input('your_id>>:')
    user_id='123'
    user_password=raw_input('password>>:')
    user_authenticate= server_authenticate.server_authenticate(user_id, user_password)
    print user_authenticate
    if user_authenticate:
        print ("user_id:%s login sucess "%(user_id))
    else:
        print ('user_id or user_password is error')


# user_login=user_login()


