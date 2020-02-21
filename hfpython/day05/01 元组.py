#什么是元组：“元组就是一个不可变的列表”


# 1 用途：存多个值，但是只有读的需求，没有改的需求
#     强调：在元素个数相同的情况下，使用元组更加节省空间

# 2 定义方式
t=(1,2,3,4) #t=tuple((1,2,3,4))

# print(id(t),type(t),t)


# 3 常用操作+内置的方法
#优先掌握的操作：
#1、按索引取值(正向取+反向取)：只能取
#2、切片(顾头不顾尾，步长)
# t=(1,2,3,4,5,6)
# print(t[1:4])

# print(tuple('hello'))
# for i in range(10000):
#     print(i)

# print(tuple(range(10000)))

#3、长度
#4、成员运算in和not in

#5、循环


# t=('a','b','c','c')
# # t[0]=1111
# print(t.index('a'))
# print(t.count('c'))
#
#
#
# '''
# #二：该类型总结
# 1 存多个值
#
# 2 有序
#
# 3 不可变
# '''
#
#
msg_dic={
'apple':10,
'tesla':100000,
'mac':3000,
'lenovo':30000,
'chicken':10,
}
goods=[]

while True:
    for name in msg_dic:
        print('商品名:%s   价钱：%s' %(name,msg_dic[name]))

    good_name=input('商品名>>: ').strip()
    if good_name not in msg_dic:
        continue
    price=msg_dic[good_name]

    while True:
        count=input('购买个数>>: ').strip()
        if count.isdigit():
            count=int(count)
            break

    # info=[good_name,price,count]
    # info={
    #     'good_info':(good_name,price),
    #     'count':count
    # }
    info={
        'good_name':good_name,
        'price':price,
        'count':count
    }

    goods.append(info)
    print(goods)







# goods=[
#     {'good_info': ('mac', 3000), 'count': 10}
# ]
# print(goods[0]['good_info'][1]
# )
#
# print(goods[0]['count'])
#
# print(goods[0]['good_info'][1] * goods[0]['count'])
#
#
#
#
#
# goods=[
#     {
#         'good_name':'mac',
#         'price':30000,
#         'count':10
#     },
#
# ]
#
# goods[0]['price']
# goods[0]['count']
