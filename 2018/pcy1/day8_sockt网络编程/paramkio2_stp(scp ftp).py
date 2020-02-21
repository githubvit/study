#_*_coding:utf-8_*_
'''
paramiko 传送文件 模拟linux下scp命令
scp是linux下利用ssh进行文件拷贝的工具，
scp -rp -P端口号 文件名 用户@ip：目录 这里r是目录，p是指权限
'''
import paramiko
# 一，建立传输通道
#1，建立传输对象
transport = paramiko.Transport(('10.0.0.31', 52113))
#2，建立传输连接
transport.connect(username='root', password='123456')
#二，在通道上建立sftp客户端，实现上传put和下载get
sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
#sftp.put('笔记', '/tmp/test_from_win')
# 将remove_path 下载到本地 local_path
sftp.get('/root/oldgirl.txt', 'fromlinux.txt')
#三，关闭传输通道
transport.close()