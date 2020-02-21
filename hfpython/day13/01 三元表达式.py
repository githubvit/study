
def max2(x,y):
    if x > y:
        return x
    else:
        return y

res=max2(10,11)
print(res)

x=12
y=11

#三元表达式仅应用于：
#1、条件成立返回 一个值
#2、条件不成立返回 一个值
# res=x if x > y else y
# print(res)


def max2(x,y):
    return x if x > y else y

print(max2(10,11))