# _*_coding:utf-8_*_
'''
paramiko 执行命令
'''
import paramiko

# 1,创建SSH对象
ssh = paramiko.SSHClient()

# 允许连接不在know_hosts文件中的主机，know_hosts文件在家目录中隐藏目录.ssh下
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 2,连接服务器
ssh.connect(hostname='192.168.2.240', port=22, username='root', password='another333')
# 3,执行命令 会有三种标准输入、标准输出、标准错误
while True:
    s=raw_input('>>')
    stdin, stdout, stderr = ssh.exec_command(s)#不要执行top，否则永远返回不了了，只能执行top -bn 1，执行1次
    # 4,获取命令结果
    res,err = stdout.read(),stderr.read()
    result = res if res else err

    print(result.decode())

# 5,关闭连接
ssh.close()
