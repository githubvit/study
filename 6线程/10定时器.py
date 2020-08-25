# 定时器一，指定n秒后执行某操作（起某个线程）
from threading import Timer,current_thread
 
 
def hello(name):
    print(f"hello, world {name}",current_thread().getName())
print('主',current_thread().getName()) 
t = Timer(3, hello,('bq',))# 参数必须是元组方式
t.start()  # after 3 seconds, "hello, world" will be printed

# 结果
# 主 MainThread
# hello, world bq Thread-1

# 验证码案例
from threading import Timer
import random,time
t_list=[]
class Code:
    def __init__(self):
        # 实例化时 直接获取验证码
        self.make_cache()
        
    def make_cache(self,interval=10):
        # 获取验证码
        self.cache=self.make_code()
        print(self.cache)
        
        # 设置定时器线程 5秒后启动 自身线程 递归
        self.t=Timer(interval,self.make_cache)
        # 启动定时器
        t_list.append(self.t)

        print(t_list)
        for i in t_list:
            print(i.finished)
        self.t.start()
        self.check()

    def make_code(self,n=4):
        # 4位验证码
        res=''
        for i in range(n):
            s1=str(random.randint(0,9)) #数字
            s2=chr(random.randint(65,90)) #字母
            res+=random.choice([s1,s2]) #从数字和字母中随机取一个
        return res

    def check(self):
        # 输入验证码
        inp=input('>>: ').strip()
        # if inp.upper() ==  self.cache:
        if inp == 'q':
            # print('验证成功',end='\n')
            print('验证成功')
            # 清除定时器线程
            self.t.cancel()
            # break
        else:
           print(self.t.finished) 


if __name__ == '__main__':
    obj=Code()
    # obj.check()
