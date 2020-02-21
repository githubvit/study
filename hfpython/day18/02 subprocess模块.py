import subprocess
# import time
#
# time.sleep(500)


# dos命令
# tasklist | findstr python
# taskkill /?
#D:\code>tasklist | findstr python
# python.exe                   12360 Console                    1     11,024 K
#
# D:\code>taskkill /F /PID 12360


# linux系统（了解）
# ps aux | grep python
# kill -9 PID


# import os
# while True:
#     cmd=input('>>>: ').strip()
#     if not cmd:continue
#     # print('%s run' %cmd)
#     res=os.system(cmd)

    # network.send(res)



# import os
#
# res=os.system('dixCVr')
# print('运行结果：',res)

import subprocess

obj=subprocess.Popen('dir',
                     shell=True,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE
                     )

# print(obj)

res1=obj.stdout.read()
print('正确结果1111: ',res1)

res2=obj.stdout.read()
print('正确结果2222: ',res2) #只能取一次，取走了就没有了

# res2=obj.stderr.read()
# print('错误结果：',res2.decode('gbk'))