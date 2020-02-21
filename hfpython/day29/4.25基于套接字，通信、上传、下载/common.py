import json,os
from multiprocessing import Process,Queue
#传入字典变成bytes
def get_bytes(user_dic):
    user_json=json.dumps(user_dic)
    user_bytes=user_json.encode('utf-8')
    return user_bytes

#传入bytes变回字典
def get_dic(user_bytes):
    user_json=user_bytes.decode('utf-8')
    user_dic=json.loads(user_json)
    return user_dic


q=Queue()

