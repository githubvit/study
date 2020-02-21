'''
1 面向过程的编程思想
    核心是'过程'二字，过程即解决问题的步骤，即先干什么，再干什么。。。。
    基于面向过程编写程序就好比在设计一条流水线，是一种机械式的思维方式。


2、示范：

3、总结优缺点：
    优点：复杂的问题流程化，进而简单化
    缺点：修改一个阶段，其他阶段都有可能需要做出修改，牵一发而动全身，即扩展性极差
    应用：用于扩展性要求低的场景

'''
#1、步骤一：拿到用户输入的合法的信息：用户名、密码、余额、年龄
db_path='db.txt'

def get_uname():
    while True:
        uname=input('用户名>>：').strip()
        if not uname.isalpha():
            print('\033[45m用户名必须为英文字母...\033[0m')
            continue
        with open(r'%s' %db_path,'r',encoding='utf-8') as f:
            for line in f:
                uinfo=line.strip('\n').split(',')
                if uname == uinfo[0]:
                    print('\033[45m用户名已存在...\033[0m')
                    break
            else:
                return uname

def get_pwd():
    while True:
        pwd1=input('请输入密码>>: ').strip()
        pwd2=input('再次输入密码>>: ').strip()
        if pwd1 == pwd2:
            return pwd1
        else:
            print('\033[45m两次输入的密码不一致，请重新输入...\033[0m')

def get_bal():
    while True:
        bal=input('请输入余额: ').strip()
        if bal.isdigit():
            # bal=int(bal)
            return bal
        else:
            print('\033[45m钱必须是数字，傻叉...\033[0m')

def get_age():
    pass

#2、步骤二：写入文件
def file_hanle(uname,pwd,bal,age):
    with open(r'%s' %db_path,'a',encoding='utf-8') as f:
        f.write('%s,%s,%s,%s\n' %(uname,pwd,bal,age))

# 注册功能
def register():
    #步骤1：
    uname=get_uname() #拿到合法的用户名
    pwd=get_pwd() #拿到合法的密码
    bal=get_bal() #拿到合法的余额
    #步骤2：
    file_hanle(uname,pwd,bal) #写入文件

