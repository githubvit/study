#_*_coding:utf-8_*_
'''
不用密码登陆，用秘钥对RSA
'''

import paramiko
# 指定私钥文件
'''
实现windows下用秘钥登陆linux服务器：
1，在xshell上用ssh登陆某一台linux机器，该机器已经实现了秘钥登陆服务器，拷贝该linux机器的私钥,
    sz ~/.ssh/id_ras
2，在windows当前盘的download目录下，找到拷贝过来的私钥文件id_ras，
3，复制到当前目录下重命名为id_rsa31.txt。
'''
private_key = paramiko.RSAKey.from_private_key_file('id_rsa31.txt')

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='10.0.0.41', port=52113, username='gongli', pkey=private_key)

# 执行命令
stdin, stdout, stderr = ssh.exec_command('df')
result = stdout.read()
print(result.decode())
stdin, stdout2, stderr = ssh.exec_command('ifconfig')
# 获取命令结果
result2 = stdout2.read()
print(result2.decode())

# 关闭连接
ssh.close()