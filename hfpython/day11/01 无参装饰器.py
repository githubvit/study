'''
1 开放封闭原则
    软件一旦上线后，就应该遵循开放封闭原则，即对修改源代码是封闭的，对功能的扩展是开放的
    也就是说我们必须找到一种解决方案：
        能够在不修改一个功能源代码以及调用方式的前提下，为其加上新功能

        总结，
        原则如下：
            1、不修改源代码
            2、不修改调用方式
        目的：
            在遵循1和2原则的基础上扩展新功能

2、什么是装饰器？
    器指的工具，装饰指的是为被装饰对象添加新功能

    完整含义：
        装饰器即在不修改被装饰对象源代码与调用方式的前提下，为被装饰器对象添加新功能

        装饰器与被装饰的对象均可以是任意可调用的对象

        装饰器=》函数
        被装饰的对象=》函数

'''

# import time
#
# def index():
#     start_time=time.time()
#     time.sleep(3)
#     print('welcome to index page')
#     stop_time=time.time()
#     print('run time is %s' %(stop_time-start_time))
#
# index()


#修订1：
import time

def index():
    time.sleep(3)
    print('welcome to index page')

def home(name):
    time.sleep(5)
    print('welcome %s to home page' %name)

# start_time=time.time()
# index()
# stop_time = time.time()
# print('run time is %s' % (stop_time - start_time))
#
# start_time=time.time()
# home('egon')
# stop_time = time.time()
# print('run time is %s' % (stop_time - start_time))


# #修订2：
# import time
#
# def index():
#     time.sleep(3)
#     print('welcome to index page')
#
# def home(name):
#     time.sleep(5)
#     print('welcome %s to home page' %name)
#
# def wrapper(func): #func=index
#     start_time=time.time()
#     func() #index()
#     stop_time = time.time()
#     print('run time is %s' % (stop_time - start_time))
#
#
# wrapper(index) # 修改了原函数的调用方式



#修订3：
import time

def index():
    time.sleep(3)
    print('welcome to index page')

def outter(func): #func=最原始的index
    # func=最原始的index
    def wrapper():
        start_time=time.time()
        func()
        stop_time=time.time()
        print(stop_time-start_time)
    return wrapper


index=outter(index) # 新的index=wrapper

index() #wrapper()



