# 同一个程序执行多次是多个进程
import time
import os

print('爹是：',os.getppid())
print('me是: ',os.getpid())
time.sleep(500)