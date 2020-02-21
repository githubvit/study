from conf import settings
from lib import common

# logger1=common.get_logger('atm')
logger2=common.get_logger('boss')

def login():
    print('登录....')
    with open(settings.DB_PATH,encoding='utf-8') as f:
        for line in f:
            print(line)

def register():
    print('注册....')

def shop():
    print('购物....')

def pay():
    print('支付...')

def transter():
    print('转账...')
    # common.logger('刘清政给他爹egon转账10000')
    # logger1.debug('刘清政给他爹egon转账10000')
    # logger1.error('刘清政给他爹egon转账10000,转账失败')
    logger2.error('刘清政给他爹egon转账10000,转账失败')

def run():
    while True:
        print("""
        1 登录
        2 注册
        3 购物
        4 支付
        5 转账
        """)

        choice=input('>>: ').strip()
        if choice == '1':
            login()
        elif choice == '2':
            register()
        elif choice == '3':
            shop()
        elif choice == '4':
            pay()
        elif choice == '5':
            transter()
        else:
            print('输入错误指令')


