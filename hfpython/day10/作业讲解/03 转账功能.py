db_path='db.txt'

#1、源账户减钱
def cal_mon(src_user,money):
    pass

#2、目标账户加钱
def add_mon(dst_user,money):
    pass


def transfer(src_user,dst_user,money):
    cal_mon(src_user,money)
    add_mon(dst_user,money)


transfer('egon','alex',300)

