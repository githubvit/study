
while True:
    msg="""
    1 注册
    2 查看
    """
    print(msg)
    choice=input('输入编号>>: ').strip()
    if choice == "1":
        # print('\033[45m注册。。。\033[0m')
        phone=input('手机号>>: ').strip()
        name=input('用户名>>: ').strip()
        pwd=input('密码>>: ').strip()
        sex=input('性别>>: ').strip()
        with open('db.txt','at',encoding='utf-8') as f:
            f.write('%s,%s,%s,%s\n' %(phone,name,pwd,sex))
    elif choice == '2':
        # print('\033[44m查看。。。。。\033[0m')

        phone=input('请输入你的手机号：').strip()
        with open('db.txt','rt',encoding='utf-8') as f:
            for line in f:
                if line.startswith(phone):
                    print(line,end='')
                    break
    else:
        print('\033[43m输入非法编号...\033[0m')