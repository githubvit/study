# 购物车程序实例
# 1，打印收入
# 2，打印商品列表
# 3，输入商品编号，购买商品,一次只能选一件数量。
# 4，继续购物或退出
# 5，打印总的购物清单和余额

# 创建用户列表
user_list=[{'name':'egon','salary':5000},]


# 创建商品列表
gs=[('iphone',5800),('mac pro',12000),('starbuck latte',31),('alex python',81),('bike',800)]

# 创建购物清单
sl={
    'gs':[],#[[id1,name1,prce1,num1],[id1,name1,prce1,num1],...]
    'num':0,#num=num1+num2+..
    'total':0,#total=prce1*num1+prce2*num2+...
}

# 打印余额
def output_ss(salary):
    print('您的当前余额 ：%s'%(salary))
 
# 打印商品列表
def output_gs(gs):
    print('%s 商品列表 %s'%('-'*15,'-'*15))
    print ('id\t name \t\t\t price')
    for index,item in enumerate(gs):
        res=len(item[0])
        if res <= 4:
            print(index,'\t',item[0],'\t\t\t',item[1])
        elif res <= 12:
            print(index,'\t',item[0],'\t\t',item[1])
        else:
            print(index,'\t',item[0],'\t',item[1])

# 打印购物清单
def output_sl(user,sl):
    print('%s 您的购物清单 %s'%('-'*19,'-'*19))
    print(('idx\t g_id\t name\t\t\t price\t num'))
    if sl['gs']:
        for index,item in enumerate(sl['gs']):
            res=len(item[1])
            if res <= 4:
                print(index,'\t',item[0],'\t',item[1],'\t\t\t',item[2],'\t',item[3])
            elif res <= 12:
                print(index,'\t',item[0],'\t',item[1],'\t\t',item[2],'\t',item[3])
            else:
                print(index,'\t',item[0],'\t',item[1],'\t',item[2],'\t',item[3])
        print('%s'%('-'*52))
        print('当前总共购买%s件商品，共计%s元。'%(sl['num'],sl['total']))
        print('您的当前余额：%d'%(user['salary']))
    else:
        print('当前未购物')

# 加入购物清单 item是经过整理后的列表 [id,name,prec]
def addsl(user,item):
    isno=True
    for i in sl['gs']:
        if item[0]==i[0]:#如果有就加数量
            isno=False
            i[3]+=1
    if isno: # 没有就把item添加1项数量1，再加入购物清单sl。
        item.append(1)
        sl['gs'].append(item)
    sl['num'] += 1
    sl['total']  += item[2]
    user['salary']  -=   item[2]
    # print (sl['gs'])
#商品输入
def input_gs(user,gs):
    i_err=True
    b_err=False
    while True:
        gs_id=input('please input goods id or input "n" quit>>')
        if gs_id == 'n':
            return gs_id
        for i in range(0,len(gs)):#输入判别
            if str(i) == gs_id:
                i_err=False
                if gs[i][1]>user['salary']:#余额不足
                    b_err=True
                    break
                else:
                    return gs_id
        #余额不足处理
        if b_err:
            print ("balance isn't enough,please reinput goods id")
        #输入不对，重输
        if i_err:
            print ('gs_id input error,please reinput goods id')       

#购买商品 user 用户 gs商品列表
def shopping(user,gs):
    #打印欢迎光临，当前余额
    print('欢迎%s光临，您当前余额%d，祝您购物愉快。'%(user['name'],user['salary']))
    while True:
        #打印商品列表
        output_gs(gs)

        #输入商品编号，购买商品
        gs_id=input_gs(user,gs)
        if gs_id=='n': 
            print ('game over,bye...')
            return 
        print('您选择的商品编号:',gs_id)

        #把商品加入购物清单 扣款
        #整理商品数据
        item=[gs_id,gs[int(gs_id)][0],gs[int(gs_id)][1]]
    
        # print (item)
    
        #把item加入清单
        addsl(user,item)

        # print (sl)

        # 打印购物清单
        output_sl(user,sl)

        # 是否继续购买
        print('continue?')
        answer=input('input "y" continue Input others quit>>')
        if answer=='y':
            continue
        return


shopping(user_list[0],gs)
