#_*_coding:utf-8_*_
# 三层嵌套实现语法糖带参数的装饰器,以便对不同的方法实现不同的装饰效果
#这就需要再来一层嵌套，来传递语法糖参数
# 根据auth_type参数判断，home登陆用local方式，bbs登陆用ldap方式，实现不同的认证，添加认证。
import time
user,passwd = 'alex','abc123'
def auth(auth_type):
    print("auth func:",auth_type)
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
#             print("wrapper func args:", *args, **kwargs)
            if auth_type == "local":
                username = raw_input("Username:").strip()
                password = raw_input("Password:").strip()
                if user == username and passwd == password:
                    print("\033[32;1m User has passed authentication \033[0m")
                    res = func(*args, **kwargs)  # 为了保留原函数的return：采用赋值方式得到原函数的return值from home，再在下面return这个值。
                    print("---after authenticaion ")
                    return res
                else:
                    print("\033[31;1m Invalid username or password \033[0m")
                    exit()
                    #0黑、1红、2绿、3黄、4蓝、5紫、6中绿、7h灰、8和现有字体一致、9黑
            elif auth_type == "ldap":
                print("搞毛线ldap,不会。。。。")
                exit()
        return wrapper
    return outer_wrapper

def index():
    print("welcome to index.html page")
#语法糖带参数实现不同装饰效果
@auth(auth_type="local")#  home=outer_wrapper(home)= wrapper
def home():
    print("welcome to home  page")
    return "from home"

@auth(auth_type="ldap")
def bbs():
    print("welcome to bbs  page")
'''
@auth(auth_type="local")  # home=outer_wrapper(home)= wrapper
def home():
三层嵌套实现带参数语法糖解析（以def home():为例）：
最外层def auth(auth_type)：auth(auth_type="local")传递语法糖参数
1,print("auth func:",auth_type)
2,定义outer_wrapper
3,返回outer_wrapper地址

中间层def out_wrapper(func)：outer_wrapper(home) 传递被装饰函数home的地址，返回装饰函数wrapper的地址
1，把home的地址传outer_wrapper函数
1，定义wrapper
2，返回wrapper地址

最内层def wrapper(*args, **kwargs)：实现功能扩展，以赋值方式调用被装饰函数home（），返回home（）的return值，保证原函数的值不变

语法糖：实现home=outer_wrapper(home)=wrapper，偷梁换柱， 实现原来的home()=现在的wrapper()，从而保证调用方式不变，实现功能扩展
'''

# index.html()
print(home()) #wrapper()
# bbs()
