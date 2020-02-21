#-*- coding:utf8 -*-

import  random
# 随机浮点数
print random.random() #生成0到1之间的随机浮点数。
print random.uniform(1,10)#生成1到10之间的随机浮点数。
# 随机整数
print random.randint(1,7) #生成1到7之间的随机整数（包含1和7）[1,7]
print random.randrange(7)#生成0到7之间的随机整数（包含0，不包含7）[1,7）
print random.randrange(0,101,2)#随机选取0到100间的偶数
# 随机序列
print random.choice((1,'a',66))#从一个序列中随机找一个值
print random.choice('hello')#从一个序列中随机找一个值
print random.sample('hello',2)#从一个序列中随机取两个值，组成列表

# 洗牌
items=[1,2,3,4,5,6,7]
print  items
random.shuffle(items)
print  items
# 1,[2, 6, 3, 7, 1, 4, 5]
#2,[1, 7, 2, 4, 3, 6, 5]
#3,[5, 1, 2, 3, 4, 6, 7]