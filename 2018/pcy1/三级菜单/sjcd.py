#_*_coding:utf-8_*_
'''
三级菜单：和递归（雁式）应用密切相关
1，启动时进入一级菜单，选择下一级菜单，到最后一层时提示到了最后一层。
2，每层可以循环
3，每层可以返回上一级
4，每层可以结束
'''
# 定义三级菜单，注意嵌套字典的写法
pmc = {
    'jx': {
        'jdz': {
            'zs': ['xc', 'ch', 'zs'],
            'cj': ['ys', 'ly', 'jz'],
        },
        'nc': {
            'ncx': ['a', 'b', 'c'],
            'bygc': ['d', 'e', 'f'],
        },
        'jj': {
            'sl': ['jxgd', 'gy', 'blh'],
            'ls': ['tcc', 'dm', 'sd'],
        },
    },
    'hb': {
        'wh': {
            'gg': ['hz', 'rs', 'yk'],
            'dh': ['ip', 'wg'],
        },
        'xg': {
            'jk': ['dd'],
            'dq': [1, 2, 3],
        },
    },
}
# 一，笨办法：三级菜单，38-95有5行注释，四级或更多级则需要更多行代码。

# 1，启动时进入一级菜单，循环
# flag = True  # 定义循环标志位
# # 开始循环
# while flag:
#     # 打印第一级菜单
#     for i in pmc:
#         print i
#     # 选择下一级菜单 或 退出
#     nm1 = raw_input('next level 1 menu or stop input "q" -->>> ')
#     if nm1 in pmc:  # 判断nm1是否正确，如果不正确呢，这里没有else，实际就是把本级循环再次执行一遍，等你再次输入，直到正确，往下执行。
#         while flag:
#             for i2 in pmc[nm1]:
#                 print "\t", i2
#             # 选择下一级菜单 或 返回上一级 或 退出
#             nm2 = raw_input('next level 2 menu or return input "r" and stop input "q" -->>> ')
#             if nm2 in pmc[nm1]:
##                 while flag:
#                     for i3 in pmc[nm1][nm2]:
#                         print "\t\t", i3
##                     nm3 = raw_input('next level 3 menu or return input "r" and stop input "q" -->>> ')
#                     if nm3 in pmc[nm1][nm2]:
#                         print'this is last level'.center(50, '*')  # 提示这是最后一级，50个字符居中，其余用*补齐。
#                         while flag:
#                             for i4 in pmc[nm1][nm2][nm3]:
#                                 print "\t\t\t", i4
#                             nm4 = raw_input('next level 4 menu or return input "r" and stop input "q" -->>> ')
#                             if nm4 == 'r':
#                                 break
#                             elif nm4 == 'q':  # 实现在本级按q键，退出所有循环。
#                                 flag = False
#                                 break
#                             else:
#                                 print 'input error'
#                                 continue
#                     elif nm3 == 'r':
#                         break
#                     elif nm3 == 'q':  # 实现在本级按q键，退出所有循环。
#                         flag = False
#                         break
#                     else:
#                         print 'input error'
#                         continue
#             elif nm2 == 'r':
#                 break
#             elif nm2 == 'q':
#                 flag = False
#                 break
#             else:
#                 print 'input error'
#                 continue
#     elif nm1 == 'r':
#         break
#     elif nm1 == 'q':
#         flag = False
#         break
#     else:
#         print 'input error'
#         continue
# # 二，以下是使用函数的方法实现用字典实现三级菜单，避免上面的重复代码，97-146有9行注释，对于任意级字典菜单均适用。
# cnt=0#层数
# cnt_ly_list = []#字典层数和相应字典组成的元组的列表，开始就是空列表
# def choice_fun(cnt,y,cnt_ly_list):
#     '''
#     字典选择函数
#     如果value是字典就输入key ，展开value，循环
#     否则就打印‘到了最后一级’，返回上一级或退出
#     :param cnt: int，字典级别,从0级开始，0-最高层
#     :param y: dict，多级别字典
#     :param cnt_ly_list: list，字典层数和相应字典组成的元组的列表
#     :return:
#     '''
#     cnt_ly=(cnt,y)#层级、字典元组
#     if cnt_ly in cnt_ly_list:#如果有（在列表中存在）就过了，没有就把层级、字典元组增加到列表，这样会形成层级和字典元组形式的有序列表
#         pass
#     else:
#         cnt_ly_list.append(cnt_ly)
#     print cnt_ly_list
#     for i in y:
#         print '\t'*cnt,i
#     flag=True
#     while flag:
#         x=raw_input("输入'r'返回上一级，输入'q'退出:>>>")
#         if x in y:
#             if isinstance(y[x], dict):
#                 cnt+=1
#                 return choice_fun(cnt,y[x],cnt_ly_list)#单边递归
#             else:
#                 print '到了最后一级'
#                 for j in y[x]:
#                     print '\t'*(cnt+1),j
#                 ch = raw_input("输入任意字符返回上一级，输入'q'退出:>>>")
#                 if ch == 'q':
#                     flag = False
#                     break
#                 else:
#                     return choice_fun(cnt,cnt_ly_list[cnt][1],cnt_ly_list)
#         elif x=='r':
#             if (cnt-1)>=0:
#                 return choice_fun(cnt-1,cnt_ly_list[cnt-1][1],cnt_ly_list)
#             else:
#                 print "这是第1层，输入‘r'还是在这一层"
#                 return choice_fun(0,cnt_ly_list[0][1],cnt_ly_list)
#         elif x=='q':
#             flag=False
#             break
#         else:
#             print '输入错误,重新输入'
#             return choice_fun(cnt,cnt_ly_list[cnt][1],cnt_ly_list)
# choice_fun(cnt,pmc,cnt_ly_list)



# 三，正解（不用return的递归）雁式递归实现三级菜单（更多级都行）

cnt=0
def choice_fun_2(cnt,y):
    '''
    字典选择函数
    如果value是字典就输入key ，展开value，循环
    否则就打印‘到了最后一级’，返回上一级或退出
    :param cnt: int，字典级别,从0级开始，0-最高层
    :param y: dict，多级别字典

    :return: 
    '''

    while True:
        for i in y:
            print  '\t'*cnt,i
        if cnt==0:
            x = raw_input("输入'q'退出:>>>")
            if x=='r':
                x = 'q'
        else:
            x=raw_input("输入'r'返回上一级，输入'q'退出:>>>")
        if x in y:
            if isinstance(y[x], dict):
                # cnt+=1 #这是上面的写法，是错的，因为在还没有调用递归就已经把cnt加了1，就是在内存中没调用递归就改了上层的参数，在回归时就无法完全回归
                choice_fun_2(cnt+1,y[x])#不用return-用雁式递归，就可以保证完全回归
            else:
                print '到了最后一级'
                for j in y[x]:
                    print '\t'*(cnt+1),j
                ch = raw_input("输入任意字符返回上一级，输入'q'退出:>>>")
                if ch == 'q':
                    print ("game over")
                    exit()
                else:
                    continue
        elif x=='r':
            # break
            return #用return结束本级函数，就返回到了上一级
        elif x=='q':
            print ("game over")
            exit()
        else:
            print '输入错误,重新输入'
            continue

choice_fun_2(cnt,pmc)



