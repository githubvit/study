

def eat(name):
    print('%s ready to eat' %name)
    food_list=[]
    while True:
        food=yield food_list # food='骨头'
        food_list.append(food) #food_list=['泔水','骨头']
        print('%s start to eat %s' %(name,food))


dog1=eat('alex')

#1、必须初始化一次，让函数停在yield的位置
res0=dog1.__next__()
print(res0)

#2、接下来的事，就是喂狗
#send有两方面的功能
#1、给yield传值
#2、同__next__的功能
res1=dog1.send('泔水')
print(res1)
res2=dog1.send('骨头')
print(res2)
res3=dog1.send('shit')
print(res3)
