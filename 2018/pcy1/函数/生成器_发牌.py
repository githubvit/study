#_*_coding:utf-8_*_
'''
用yield实现协程
协程是比线程更小的单位，寄生在线程里，
可以用单线程模拟出多线程并发，
实际上这就是异步io的雏形，
nginx为什么效率这么高，就是因为使用了异步io，其单线程的并发量比多线程还要多好多倍。
next()和send（）
next()唤醒generate，开始运行，遇到yield跳出generate。
send()唤醒generate，并传值给yield，首先传值给yield，再从yield的下一行开始运行，遇到yield跳出generate。
'''
# 典型生产-消费模型
# 边生产边消费
def napai(name): #消费
    print ('%s准备拿牌'%name)
    while True:
        pai=yield  #yield为空
        print ('%s拿了一张%s牌'%(name,pai))
def fapai(): #生产
    pai0=['红中','发财','白板','一万','二万','一饼','三饼','三条','六条','七条','东瓜','南瓜','西瓜','北瓜','七万','八万','九万',\
        '红中1','发财1','白板1','一万1','二万1','一饼1','三饼1','三条1','六条1','七条1','东瓜1','南瓜1','西瓜1','北瓜1','七万1',\
         '八万1','九万1','红中2','发财2','白板2','一万2','二万2','一饼2','三饼2','三条2','六条2','七条2','东瓜2','南瓜2','西瓜2',\
         '北瓜2','七万2','八万2','九万2','红中3','发财3','白板3','一万3','二万3','一饼3','三饼3','三条3','六条3','七条3','东瓜3','南瓜3',\
          '西瓜3','北瓜3','七万3','八万3','九万3',]
    print ('开始发牌')
    d='东'
    n='南'
    x='西'
    b='北'
#     定义dong、nan、xi、bei四个generator生成器。
    dong=napai(d)
    nan=napai(n)
    xi=napai(x)
    bei=napai(b)
    next(dong) #唤醒yield，打印 东准备拿牌  返回的yield的值为空
    next(nan)
    next(xi)
    next(bei)
    cnt=0  #计数器
    s=[j for j in range(52)] #每个人13张牌，共52，用列表生成式产生0到51的列表。
    for i in pai0:
        if cnt in s[0::4]:#根据计数器判断该谁拿牌，比如0该dong拿，下一次dong拿牌的计数器为4，因此步长为4.
            dong.send(i) #唤醒generate，并将pai0列表中的元素i传给yield。
        if cnt in s[1::4]:
            nan.send(i)
        if cnt in s[2::4]:
            xi.send(i)
        if cnt in s[3::4]:
            bei.send(i)
        cnt+=1
fapai()