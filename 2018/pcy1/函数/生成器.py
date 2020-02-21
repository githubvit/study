#_*_coding:utf-8_*_
'''
简单生成器
函数式生成器 yield关键字
'''
def fib1(max):
    n1, a1, b1 = 0, 0, 1
    while n1 < max:
        # print b1
        yield b1#产生中断，并保存当前状态
        a1, b1 = b1, a1+ b1
        n1 = n1 + 1
        print ('这是n1:%s'%n1)
    # return   # 在python2.x中不能在return后跟参数，只能是空的 ；在3.x中可以写成return 'done'，可以跟参数，该参数是StopIteration异常的e值。
f1=fib1(4)#定义了生成器
                              #执行                                    yield b1
print f1.next()           #n1, a1, b1 = 0, 0, 1                      1
print '干点别的-------1'    #接着yield b1 继续运行1，-->>a1, b1 = b1,a1+ b1  2,-->>n1 = n1 + 1   3,-->>  print ('这是n1:%s'%n1)
print f1.next()           #n1, a1, b1 = 1, 1, 1   这是n1:1           1
print '干点别的-------2'    #接着yield b1 继续运行1，-->>a1, b1 = b1,a1+ b1  2,-->>n1 = n1 + 1   3,-->>  print ('这是n1:%s'%n1)
print f1.next()           #n1, a1, b1 = 2, 1, 2   这是n1:2           2
print '干点别的-------3'    #接着yield b1 继续运行1，-->>a1, b1 = b1,a1+ b1  2,-->>n1 = n1 + 1   3,-->>  print ('这是n1:%s'%n1)
print f1.next()           #n1, a1, b1 = 3, 2, 3  这是n1:3           3
print '干点别的-------4'    #接着yield b1 继续运行1，-->>a1, b1 = b1,a1+ b1  2,-->>n1 = n1 + 1   3,-->>  print ('这是n1:%s'%n1)
print f1.next()          #n1, a1, b1 = 4, 3, 5 这是n1:4            5
print '干点别的-------5'
# for i in f1:
#     print i