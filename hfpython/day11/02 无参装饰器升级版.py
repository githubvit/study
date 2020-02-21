import time

def index():
    time.sleep(1)
    print('welcome to index page')
    return 122

def home(name):
    time.sleep(2)
    print('welcome %s to home page' %name)

#==============装饰器
def timmer(func):
    #func=最原始的home
    def wrapper(*args,**kwargs):
        start_time=time.time()
        res=func(*args,**kwargs) #调用最原始的home
        stop_time=time.time()
        print(stop_time-start_time)
        return res
    return wrapper


index=timmer(index) # 新的index=wrapper
home=timmer(home) #新的home=wrapper
# ==========================================

# res=index() #res=wrapper()
# print(res)

home(name='egon') #wrapper('egon')
index() #wrapper()








#装饰器模板
def outer(func): #func即被装饰函数名
    def inner(*args,**kwargs):
        #前置功能 ...
        res=func(*args,**kwargs)
        #后置功能 ...
        return res
    return inner