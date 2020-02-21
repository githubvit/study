#1、拿到用户输入的合法的信息：用户名、密码、余额
def get_uname():
    while True:
        uname=input('用户名>>：').strip()
        if uname.isalpha(): #uname='egon'
            return uname

# uname=get_uname()
# print(uname,type(uname),uname.isalpha())

def get_pwd():
    while True:
        pwd1=input('请输入密码>>: ').strip()
        pwd2=input('再次输入密码>>: ').strip()
        if pwd1 == pwd2:
            return pwd1
        else:
            print('\033[45m两次输入的密码不一致，请重新输入...\033[0m')

# pwd=get_pwd()

def get_bal():
    while True:
        bal=input('请输入余额: ').strip()
        if bal.isdigit():
            # bal=int(bal)
            return bal
        else:
            print('\033[45m钱必须是数字，傻叉...\033[0m')

# bal=get_bal()

#2、写入文件
def file_hanle(uname,pwd,bal,db_path='db.txt'):
    with open(r'%s' %db_path,'a',encoding='utf-8') as f:
        f.write('%s,%s,%s\n' %(uname,pwd,bal))

# file_hanle('egon','123','300','C:\a\n\b\db.txt')
# file_hanle('alex','123','300',)

# 注册功能
def register():
    uname=get_uname() #拿到合法的用户名
    pwd=get_pwd() #拿到合法的密码
    bal=get_bal() #拿到合法的余额
    file_hanle(uname,pwd,bal) #写入文件


register()