import time
current_user={
    'username':None,
    # 'login_time':None
}

def auth(func):
    # func=index
    def wrapper(*args,**kwargs):
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
    return wrapper

@auth #index=auth(index)
def index():
    time.sleep(1)
    print('welcome to index page')
    return 122

@auth
def home(name):
    time.sleep(2)
    print('welcome %s to home page' %name)

index()
home('egon')