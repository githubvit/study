#可读可写
#r+t
with open('b.txt','r+t',encoding='utf-8') as f:
    # print(f.readable())
    # print(f.writable())
    print(f.readline())
    f.write('\n吴大炮你也号\n')
#w+t

#a+t

#U

