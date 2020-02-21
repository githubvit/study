# 项目的核心代码
import re,hashlib,json
from conf import settings
from lib import common
logon_logger=common.get_logger('logon')
register_logger=common.get_logger('register')
# 登录 读文件 hashlib
def login():
    print('登录....')
    while True:
        user=input('username>>: ').strip()
        with open(settings.USER_PATH,'r',encoding='utf-8') as f:
            u_data=f.read()
        if u_data:
            udic=json.loads(u_data)
            #在db目录库下，找到user.json，在文件中查找用户名
            #找不到，就报用户名错误，重输
            if user in udic:
                #找到了，核对文件中的密码
                #如果密码不对，就报密码错误，重输
                #如果密码对了，就打印登录成功！
                while True:
                    pwd=input('password>>: ').strip()
                    # 加密输入的密码
                    m=hashlib.md5()
                    m.update(pwd.encode('utf-8'))
                    mpwd=m.hexdigest()
                    if mpwd==udic[user]:
                        print('恭喜，登录成功！')
                        # 添加日志
                        logon_logger.info('%s--登录'%(user))
                        return
                    else:
                        print('密码错误，请重新输入')
                        # 添加错误日志
                        logon_logger.error('%s--密码错误'%(user))
                        continue  
            else:
                print ('用户名错误,请重试')
                continue
        else:
            print('用户数据库为空不能登录')
            return
    
    
# 注册 写文件 hashlib
def register():
    print('注册....')
    while True:
        print('请输入：以字母或下划线开头，由数字和字母组成的6-16位字符串。')
        user=input('username>>: ').strip()
        # 检查用户名的合法性。
        if not re.match(r'^[_a-zA-Z]{1}[\w]{5,15}$',user):
            print('用户名输入错误，请重试')
            continue
        # 检查用户名是否已存在 这一步只能在服务器做，不然，还会有重名错误。
        is_u=False
        with open(settings.USER_PATH,'r',encoding='utf-8') as f:
            # 第一次数据为空
            u_data=f.read()
        if u_data:
            udic=json.loads(u_data)
            print(type(udic))
            if user in udic:
                is_u=True
        else:
            udic={}    
        if is_u:
            print('用户名已存在')    
            continue
        #输入密码
        while True:
            print('请输入密码，密码由6-18位数字和字母组成')
            pwd=input('password>>: ').strip()
            # 检查密码的合法性。
            if not re.match(r'^[\w]{6,18}$',pwd):
                print('密码输入错误，请重试')
                continue
            break
        break

    # 密码加密
    m=hashlib.md5()
    m.update(pwd.encode('utf-8'))
    mpwd=m.hexdigest()
    # 序列化
    udic_item={user:mpwd}
    udic.update(udic_item)
    with open(settings.USER_PATH,'w',encoding='utf-8') as f:
        f.write('%s'%json.dumps(udic))
    #添加日志    
    register_logger.info('%s--注册'%(user))
# 购物
def shop():
    print('购物....')
    pass
# 支付
def pay():
    print('支付...')
    pass
# 转账
def transter():
    print('转账...')
    pass

# 运行
def run():
    # 菜单
    msg='''
    1 登录
    2 注册
    3 购物
    4 支付
    5 转账
    6 退出
    '''
    run_dic={
        '1':login,
        '2':register,
        '3':shop,
        '4':pay,
        '5':transter,
    }
    flg=True
    while flg:
        print(msg)
        choice=input('>>:')
        if choice in run_dic:
            run_dic[choice]()
        elif choice=='6':
            flg=False
        else:
            print('输入错误,请重新输入')      
        # if choice=='1':
        #     login()
        # elif choice=='2':
        #     register()
        # elif choice=='3':
        #     shop()
        # elif choice=='4':
        #     pay()
        # elif choice=='5':
        #     transter()
        # elif choice=='6':
        #     flg=False
        # else:
        #     print('输入错误')

# run()