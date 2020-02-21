# 4月26：
# 	1、基友于进程实现并发的套接字通信，完成如下功能：
# 		1、客户端链接功成功后，先登录，登录成功后才可以执行其他功能
# 		2、登录成功后可以执行下载功能
# 		3、登录成功后可以执行上传功能
import os,json
from multiprocessing import Process,Queue,Lock
import settings,common
from socket import *
import time,random,struct
from threading import Thread



registered_dic={'name':'afen','password':'123'}

server=socket(AF_INET,SOCK_STREAM)
server.bind((settings.HOST_server,settings.PORT_server))
server.listen(5)

#验证登陆
def login():
    while True:
        login_bytes=conn.recv(1024)
        login_dic=common.get_dic(login_bytes)
        if registered_dic['name']==login_dic['name'] and registered_dic['password']==login_dic['password']:
            reback_dic={'res':True,'msg':'login success'}
            reback_bytes=common.get_bytes(reback_dic)
            conn.send(reback_bytes)
            break
        else:
            reback_dic = {'res': False, 'msg': 'login failure'}
            reback_bytes=common.get_bytes(reback_dic)
            conn.send(reback_bytes)
            continue

    #上传下载功能/

def upload(head_dic):
    file_size=head_dic['file_size']
    path=os.path.join(settings.Base_dir,'待传文件')
    file_path=os.path.join(path,head_dic['file_name'])
    if os.path.exists(file_path):
        head_dic['file_name']+='-副本'
        file_path=os.path.join(path,head_dic['file_name'])
    with open(file_path,'ab') as f:
        count=head_dic['file_size']
        count_u=0
        while count_u<count:
            str=conn.recv(1024)
            print(str.decode('utf-8'))
            f.write(str)
            count_u+=1024
        f.flush()
    print('upload success')
    return

def update(head_dic):
    file_path = os.path.join(settings.Base_dir, '待传文件',head_dic['file_name'])
    if os.path.exists(file_path):
        file_size = 0
        count = 0
        with open(file_path, 'rb') as f:
            for line in f:
                file_size += len(line)
                count += 1
        head_dic_updata = {
                    'file_name': head_dic['file_name'],
                    'file_size': file_size,
                    }

        head_bytes_update = common.get_bytes(head_dic_updata)
        head_size_update = len(head_bytes_update)
        conn.send(struct.pack('i', head_size_update))

        conn.send(head_bytes_update)

        with open(file_path, 'rb') as f:
            for line in f:
                conn.send(line)
        print('update 成功！')
        return

def recv_older(conn,client_addr):
    try:
        login()
        while True:
            client_recv=conn.recv(1024)
            if client_recv:
                head_size=struct.unpack('i',client_recv)[0]
                head_bytes=conn.recv(head_size)
                head_dic=common.get_dic(head_bytes)
                server_dic={'1':upload,
                            '2':update,
                            'q':conn.close}
                server_dic[head_dic['choose']](head_dic)
            else:
                return
    except ConnectionResetError:
        return


if __name__ == '__main__':
    while True:
        conn, client_addr = server.accept()
        print('已连接！',client_addr)
        p=Thread(target=recv_older,args=(conn,client_addr))
        p.start()

