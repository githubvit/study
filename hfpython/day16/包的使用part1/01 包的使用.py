import aaa #
'''
1 产生一个包的名称空间
2 执行包下的__init__.py文件，将产生的名字存放于包的名称空间中
3 在当前执行文件中拿到一个名字aaa，该名字指向包的名称空间
'''



# print(aaa.x) #aaa.x 就是问__init__.py要一个名字x
# print(aaa.y)

# print(aaa.m1) #aaa.m1 就是问aaa.__init__.py要一个名字m1
# aaa.m1.f1()


# print(aaa.xxx)
print(aaa.bbb.zzz)
