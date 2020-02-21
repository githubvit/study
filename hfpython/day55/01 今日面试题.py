"""
生成如下列表：
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 3, 6, 9, 12]]
"""


# 方式一

list1 = []
for i in range(4):
    tmp = []
    for j in range(5):
        tmp.append(j * i)
    list1.append(tmp)

print(list1)


# 方式二
ret = [[i * j  for j in range(5)] for i in range(4)]
print(ret)
