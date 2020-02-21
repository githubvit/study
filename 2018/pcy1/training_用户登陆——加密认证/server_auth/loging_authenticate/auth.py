#_*_coding:utf-8_*_
'''
用户认证模块
读配置文档数据库
获取比对秘钥结果
'''
import key_ch,os

from conf import setting
def authenticate(userdic,user_id_list):
    # 从配置文件setting中读入数据库的路径
    db_path = '%s/%s' % (setting.DATABASE['path'],setting.DATABASE['name'])
    # 在数据库中查找用户id是否存在（以数据库中是否有该用户id的json文档做依据）
    userfile='%s/%s.json'%(db_path,userdic['user_id'].encode('utf-8'))
    if os.path.isfile(userfile):#判断是否是文件，就要做两件事1，是否存在2，是否是文件
        # 获取比对秘钥结果
        key_res= key_ch.check_key(userdic['user_password'].encode('utf-8'), userfile)
        if key_res:
            auth_res='登陆成功'
            user_id_list['user_id'].append(userdic['user_id'].encode('utf-8'))
        else:
            auth_res='密码错误'
    else:
        auth_res='用户不存在'
    print auth_res
    return auth_res