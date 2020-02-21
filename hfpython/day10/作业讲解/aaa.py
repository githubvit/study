
uname='wxx'
with open('db.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print('===========>', uname)
        uinfo = line.strip('\n').split(',')
        print(uinfo)
        if uname == uinfo[0]:
            print('\033[45m用户名已存在...\033[0m')
            break
    else:
        print('不重复')