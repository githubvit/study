#while:条件循环
# import time
# # time.sleep(10)
# # print('===>1')
# count=1
# while count < 3:
#     print('=====>',count)
#     time.sleep(0.1)


# count=1
# while count <= 3:
#     print('=====>',count)
#     count+=1


#break:跳出本层循环
# age_of_oldboy=18
# while 1:
#     inp_age=input('your age: ')
#     inp_age=int(inp_age)
#     if inp_age > age_of_oldboy:
#         print('猜大了')
#     elif inp_age < age_of_oldboy:
#         print('猜小了')
#     else:
#         print('猜对了')
#         break

# age_of_oldboy=18
# count=0
# while count < 3:
#     inp_age=input('your age: ')
#     inp_age=int(inp_age)
#     if inp_age > age_of_oldboy:
#         print('猜大了')
#     elif inp_age < age_of_oldboy:
#         print('猜小了')
#     else:
#         print('猜对了')
#         break
#     count+=1
#     print('猜的次数',count)


# age_of_oldboy=18
# count=0
# while True:
#     if count == 3:
#         print('try too many times')
#         break
#     inp_age=input('your age: ')
#     inp_age=int(inp_age)
#     if inp_age > age_of_oldboy:
#         print('猜大了')
#     elif inp_age < age_of_oldboy:
#         print('猜小了')
#     else:
#         print('猜对了')
#         break
#     count+=1
#     print('猜的次数',count)




#continue:跳过本次循环,进入下一次循环
# count=1
# while count < 5: #3
#     if count == 3:
#         count += 1
#         continue
#     print(count)
#     count+=1

# while True:
#     print('=========>')
#     continue
#     print('=========>')
#     print('=========>')
#     print('=========>')



username='egon'
password='123'

# while True:
#     inp_name=input('name>>: ')
#     inp_pwd=input('password>>: ')
#
#     if inp_name ==  username and inp_pwd == password:
#         print('login successfull')
#         while True:
#             cmd=input('cmd>>>: ')
#             if cmd == 'quit':
#                 break
#             print('%s 命令正在执行...' %cmd)
#         break
#     else:
#         print('user or password not vaild')
#     # print('====>')


tag=True
while tag:
    inp_name=input('name>>: ')
    inp_pwd=input('password>>: ')

    if inp_name ==  username and inp_pwd == password:
        print('login successfull')
        while tag:
            cmd=input('cmd>>>: ')
            if cmd == 'quit':
                tag=False
                continue
                # break
            print('%s 命令正在执行...' %cmd)
    else:
        print('user or password not vaild')
    # print('====>')

#for


