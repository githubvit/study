import json
from conf import settings
# D:\code\SH_fullstack_s1\day15\上午\ATM\db
def insert(dic):
    f_abs_path=r'%s\%s' %(settings.DB_PATH,dic['name'])
    with open(f_abs_path,'w',encoding='utf-8') as f:
        json.dump(dic,f)

def update():
    pass

def delete():
    pass

def select():
    pass

