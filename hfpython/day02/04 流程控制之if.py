# sex='female'
# age=20
# is_beutiful=True
#
# if sex == 'female' and age > 18 and age < 26 and is_beutiful:
#     print('表白....')


# sex='female'
# age=20
# is_beutiful=True
#
# if sex == 'female' and age > 18 and age < 26 and is_beutiful:
#     print('表白....')
# else:
#     print('阿姨好')


#
# age_of_oldboy=18
# inp_age=input('your age: ')
# inp_age=int(inp_age)
# if inp_age > age_of_oldboy:
#     print('猜大了')
# elif inp_age < age_of_oldboy:
#     print('猜小了')
# else:
#     print('猜对了')

# username='egon'
# password='123'
#
# inp_name=input('name>>: ')
# inp_pwd=input('password>>: ')
#
# if inp_name ==  username and inp_pwd == password:
#     print('login successfull')
# else:
#     print('user or password not vaild')





# sex='female'
# age=20
# is_beutiful=True
# is_successful=False
#
# if sex == 'female' and age > 18 and age < 26 and is_beutiful:
#     print('表白....')
#     if is_successful:
#         print('在一起')
#     else:
#         print('对不起,我也不喜欢你,我逗你玩呢...')
# else:
#     print('阿姨好')



'''
如果：成绩>=90，那么：优秀
如果成绩>=80且<90,那么：良好
如果成绩>=70且<80,那么：普通
其他情况：很差
'''
score=89
if score >= 90:
    print('优秀')
elif score >= 80:
    print('良好')
elif score >= 70:
    print('普通')
else:
    print('很差')