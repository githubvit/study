import time
current_user={
    'username':None,
    # 'login_time':None
}

def auth(engine):
    # engine='file'
    def auth2(func):
        # func=index
        def wrapper(*args,**kwargs):
            if engine == 'file':
                if current_user['username']:
                    print('已经登陆过了')
                    res=func(*args,**kwargs)
                    return res

                uname=input('用户名>>: ').strip()
                pwd=input('密码>>: ').strip()
                if uname == 'egon' and pwd == '123':
                    print('登陆成功')
                    current_user['username']=uname
                    res=func(*args,**kwargs)
                    return res
                else:
                    print('用户名或密码错误')
            elif engine == 'mysql':
                print('基于MyQL的认证')
            elif engine == 'ldap':
                print('基于LDAP的认证')
        return wrapper
    return auth2

@auth('ldap') #@auth2 #index=auth2(index) #index=wrapper
def index():
    time.sleep(1)
    print('welcome to index page')
    return 122


index() # wrapper()