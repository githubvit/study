#_*_coding:utf-8_*_
'''
生成用户登陆数据：输入用户id和密码，就会生成一个以用户id为文档名的json格式的md5文档。
1，用json的序列化
2，每个用户一个json文档
3，用户的id就是md5文档名，id.json.
4，用户名和密码均不能为空
5，不能创建同名用户
'''
import json,os,hashlib
while True:
    user_id=raw_input('your_id>>:')
    user_password = raw_input('password>>:')
    # 4，用户名和密码均不能为空
    # 5，不能创建同名用户
    if os.path.isfile('accounts/'+user_id+'.json') or not ( user_id and user_password ):
        print'用户已存在或用户名、密码为空'
        ch=raw_input('check "b" to break or other to continue>>:')
        if ch=='b':
            break
        else:
            continue
    else:
        # 生成用户登陆数据：输入用户id和密码，就会生成一个以用户id为文档名的json文档。
        # 1，用json的序列化
        # 2，每个用户一个json文档
        # 3，用户的id就是md5文档名，id.json.
        authen_user_dic = {
            'id': user_id,
            'password': user_password
        }
        with open('accounts/' + str(authen_user_dic['id']) + '.text', 'w')as f:
            print json.dumps(authen_user_dic)
            json.dump(authen_user_dic, f)  # 等于f.write(json.dumps(authen_user_dic))

        m=hashlib.md5()
        m.update(user_password.decode('utf-8').decode('utf-8'))
        authen_user_md5 = {
            'id': user_id,
            'password': m.hexdigest()
        }
        with open('accounts/'+str(authen_user_md5['id'])+'.json','w')as f:
            print json.dumps(authen_user_md5)
            json.dump(authen_user_md5,f)#等于f.write(json.dumps(authen_user_dic))
        break