#_*_coding:utf-8_*_
'''
比对秘钥
返回结果
'''
import json
def check_key(password,userfile):
    with open(userfile,'r') as f:
        userfile_data = json.load(f)#数据还原：用load(f)相当于loads（f.read()）
        print userfile_data['password'].encode('utf-8')
    if password==userfile_data['password'].encode('utf-8'):
        return 1
    else:
        return 0
