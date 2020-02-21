#函数递归：函数的递归调用,即在函数调用的过程中，又直接或间接地调用了函数本身
# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(10000)
# print(sys.getrecursionlimit())


# 直接调用
# def foo():
#     print('from foo')
#     foo()
#
# foo()

# 间接调用
# def bar():
#     print('from bar')
#     foo()
#
# def foo():
#     print('from foo')
#     bar()
#
# foo()

# 递归分为两个阶段
#1、回溯:
    # 注意：一定要在满足某种条件结束回溯，否则的无限递归
#2、递推

# 总结：
#1、递归一定要有一个明确地结束条件
#2、没进入下一次递归，问题的规模都应该减少
#3、在python中没有尾递归优化

#例 递推年龄
# age(5)=age(4)+2
# age(4)=age(3)+2
# age(3)=age(2)+2
# age(2)=age(1)+2
# age(1)=18
# 递推式如下：
# age(n)=age(n-1)+2 # n > 1
# age(n)=18            #n=1
#

def age(n):
    print(n)
    if n == 1: # 结束递归条件
        return 18
    return age(n-1)+2 #age(4)+2

print(age(5))


#例 嵌套列表的打印
items=[1,[2,[3,[4,[5,[6,[7,[8,[9,[10,]]]]]]]]]]
def tell(l):
    for item in l:
        if type(item) is not list: #明确的跳出递归条件
            print(item)
        else:
            tell(item)

tell(items)











