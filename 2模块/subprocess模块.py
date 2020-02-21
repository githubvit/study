# 在当前进程的子进程执行系统命令
# 解决了os.system调系统 命令结果只能输出到屏幕上没办法拿到结果
import os,subprocess

# os.system('dir') #命令输出只能到屏幕上没办法拿到结果

# subprocess.Popen('dir',shell=True) #默认也是输出到屏幕

#
# obj=subprocess.Popen('dir',shell=True,
# stdout=subprocess.PIPE,
# stderr=subprocess.PIPE)#这样屏幕就没有输出了，都输出到两个管道了。

# print('我先还是后...')

# # 从stdout管道取出数据
# print(obj.stdout.read().decode('gbk'))

# 从两个程序的管道交互
# 程序1执行把结果放入管道，程序2从管道中程序1的结果过滤出自己想要的内容。

# 方式一 
# obj1=subprocess.Popen('tasklist',shell=True,
# stdout=subprocess.PIPE,stderr=subprocess.PIPE)

# obj2=subprocess.Popen('findstr python',shell=True,
# stdin=obj1.stdout,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

# print(obj2.stdout.read().decode('gbk'))

# 方式二 用管道符命令链接两个程序 
obj1=subprocess.Popen('tasklist | findstr python',shell=True,
stdout=subprocess.PIPE,stderr=subprocess.PIPE)
print(obj1.stdout.read().decode('gbk'))
print('2',obj1.stdout.read().decode('gbk'))#管道中的内容已空。
