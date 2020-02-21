import os,json,struct
from multiprocessing import Process,Queue,Lock
import settings,common
from socket import *
from threading import Thread


client=socket(AF_INET,SOCK_STREAM)
client.connect((settings.HOST_server,settings.PORT_server))


#验证登陆
def login_client():
    while True:
        name=input('please input your name>>:')
        password=input('please input your password>>:')
        user_dic={'name':name,'password':password}
        user_bytes=common.get_bytes(user_dic)
        client.send(user_bytes)
        reback_bytes=client.recv(1024)
        reback_dic=common.get_dic(reback_bytes)
        if reback_dic['res']:
            print('%s'%reback_dic['msg'])
            break
        else:
            print('%s'%reback_dic['msg'])
            continue

#上传功能
def upload():
    path = os.path.join(settings.Base_dir, '文件存放')
    file_list = os.listdir(path)
    file_dic = {}
    for i, file_name in enumerate(file_list):
        print('%s:%s' % (i, file_name))
        file_dic['%s' % i] = file_name
    choose = input('idcard>>:')
    if choose in file_dic:
        uplode_file_name = file_dic[choose]
        file_path = os.path.join(path, uplode_file_name)
        file_size=0
        with open(file_path, 'rb') as f:
            for line in f:
                file_size += len(line)
        head_dic={'choose':'1',
                  'file_name':uplode_file_name,
                  'file_size':file_size,
                    }

        head_bytes=common.get_bytes(head_dic)
        head_size=len(head_bytes)
        client.send(struct.pack('i',head_size))

        client.send(head_bytes)

        with open(file_path,'rb') as f:
            for line in f:
                client.send(line)
        print('上传成功！')
        return
    else:
        print('input illegal!')

#下载功能
def update():
    head_dic={'choose':'2',
              'file_name':'b.txt'}
    head_bytes = common.get_bytes(head_dic)
    head_size = len(head_bytes)
    client.send(struct.pack('i', head_size))
    client.send(head_bytes)

    head_size_update = struct.unpack('i', client.recv(1024))[0]
    head_bytes_update = client.recv(head_size_update)
    head_dic_update = common.get_dic(head_bytes_update)

    file_size_update = head_dic_update['file_size']
    path = os.path.join(settings.Base_dir, '文件存放')
    file_path = os.path.join(path, head_dic_update['file_name'])
    if os.path.exists(file_path):
        head_dic_update['file_name'] += '-副本'
        file_path = os.path.join(path, head_dic_update['file_name'])
    with open(file_path,'ab') as f:
        count=head_dic_update['file_size']
        count_u=0
        while count_u<count:
            str=client.recv(1024)
            f.write(str)
            count_u+=1024
        f.flush()
    print('update success')
    return

#主程序
def run_client():
    login_client()
    while True:
        print('''
            1 上传
            2 下载
            q 退出
            ''')
        choose=input('please input choose')
        if choose=='1':
            print('uplode')
            upload()

        elif choose=='2':
            print('update')
            update()

        elif choose=='q':
            break

        else:
            print('illegal input!')
    pass


run_client()