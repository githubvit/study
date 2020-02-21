import time
def timmer(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        res=func(*args,**kwargs)
        stop_time=time.time()
        print(stop_time-start_time)
        return res
    return wrapper

@timmer #index=timmer(index)
def index():
    time.sleep(1)
    print('welcome to index page')
    return 122

@timmer # home=timmer(home)
def home(name):
    time.sleep(2)
    print('welcome %s to home page' %name)

# index()
home('egon')
