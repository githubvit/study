#1、列表生成式

# l=[]
# for i in range(100):
#     l.append('egg%s' %i)
# print(l)

# l=['egg%s' %i for i in range(100)]
# l=['egg%s' %i for i in range(1000) if i > 10]
# print(l)


#2、生成器表达式
# l=('egg%s' %i for i in range(1000) if i > 10)
# print(next(l))
# print(next(l))
# print(next(l))

#3、练习题
# names=['egon','alex_sb','wupeiqi','yuanhao','lxx']
# res=map(lambda x:x.upper(),names)
# names=list(res)
# print(names)

# names=['egon','alex_sb','wupeiqi','yuanhao','lxx']
# names=[name.upper() for name in names]
# print(names)

# names=['egon','alex_sb','wupeiqi','yuanhao','lxx']
# names=[len(name) for name in names if not name.endswith('sb')]
# print(names)

# nums=[]
# with open('a.txt','r',encoding='utf-8') as f:
#     for line in f:
#         # print(len(line))
#         nums.append(len(line))
#
# print(max(nums))


with open('a.txt','r',encoding='utf-8') as f:
    # nums=(len(line) for line in f)

    # print(nums)
    # print(next(nums))
    # print(next(nums))
    # print(next(nums))
    # print(max(nums))
    # print(max(nums))


    # max((len(line) for line in f))
    print(max(len(line) for line in f))