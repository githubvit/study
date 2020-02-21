DB_PATH=r'D:\code\SH_fullstack_s1\day15\db.txt'
LOG_PATH=r'D:\access.log'

def logger():
    pass

def login():
    print('登录....')
    with open(DB_PATH,encoding='utf-8') as f:
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


run()