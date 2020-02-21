menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}

# 方法一：
# tag=True
# while tag:
#     menu1=menu
#     for key in menu1:
#         print(key)
#
#     choice1=input('第一层>>: ').strip() # choice1='asdfkhsadjkfhsakdfja'
#     if choice1 == 'b':break
#     if choice1 == 'q':
#         tag = False
#         break
#     if choice1 not in menu1:continue
#
#     while tag:
#         menu2=menu1[choice1] #menu1['北京']
#         for key in menu2:
#             print(key)
#
#         choice2 = input('第二层>>: ').strip()
#         if choice2 == 'b':break
#         if choice2 == 'q':
#             tag=False
#             break
#         if choice2 not in menu2:continue
#
#         while tag:
#             menu3 = menu2[choice2]  #
#             for key in menu3:
#                 print(key)
#
#             choice3 = input('第三层>>: ').strip()  # choice3='五道口'
#             if choice3 == 'b':break
#             if choice3 == 'q':
#                 tag=False
#                 break
#             if choice3 not in menu3: continue
#
#             while tag:
#                 menu4 = menu3[choice3]  #
#                 for key in menu4:
#                     print(key)
#
#                 choice4 = input('第四层>>: ').strip()  # choice1='北京'
#                 if choice4 == 'b':break
#                 if choice4 == 'q':
#                     tag=False
#                     break
#
#                 if choice4 not in menu4: continue

#方法二：


#逻辑分析：
#1、拿到当前层的菜单字典
#2、循环打印字典的key
#3、接收用户输入
#4、进入下一层，需要先拿到下一次层的字典

layers=[menu,]
while True:
    if len(layers) == 0:break
    # 1、拿到当前层的菜单字典
    current_layer=layers[-1]
    # 2、循环打印字典的key
    for key  in current_layer:
        print(key)
    # 3、接收用户输入
    choice=input('>>: ').strip()
    if choice == 'q':break
    if choice == 'b':
        layers.pop(-1)
        continue
    if choice not in current_layer:continue
    # 4、进入下一层，需要先拿到下一次层的字典
    layers.append(current_layer[choice])

