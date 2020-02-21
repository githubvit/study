#1、打印九九乘法表

'''
1*1=1                #layer=1 运算次数1
2*1=2 2*2=4          #layer=2 运算次数2
3*1=3 3*2=6 3*3=9
...
9*1
'''
# for layer in range(1,10):
#     # print('第%d层' %layer)
#     for j in range(1,layer+1):
#         print('%s*%s=%s ' %(layer,j,layer*j),end='')
#     print()




#2、打印金字塔
'''
                 #max_layer=5
    *            #current_layer=1,space=4,star=1
   ***           #current_layer=2,space=3,star=3
  *****          #current_layer=3,space=2,star=5
 *******         #current_layer=4,space=1,star=7
*********        #current_layer=5,space=0,star=9

space=max_layer - current_layer
star=2*current_layer-1
'''


max_layer=50
for current_layer in range(1,max_layer+1):
    # print(current_layer)
    # 打印空格
    for i in range(max_layer - current_layer):
        print(' ',end='')

    # 打印星号
    for j in range(2*current_layer-1):
        print('*',end='')

    print()
