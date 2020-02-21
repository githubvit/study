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

def timmer(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        res=func(*args,**kwargs)
        stop_time=time.time()
        print(stop_time-start_time)
        return res
    return wrapper

@timmer # timmer 统计的是auth+index的执行时间
@auth
def index():
    time.sleep(1)
    print('welcome to index page')
    return 122

index()
