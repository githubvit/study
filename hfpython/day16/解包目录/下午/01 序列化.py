# 序列化：内存中的数据结构----》转成一种中间格式（字符串）----》存到文件中
# dic={'name':'egon','age':18}
#
# with open('db.txt','w',encoding='utf-8') as f:
#     f.write(str(dic))


#反序列化：文件----》读取中间格式（字符串）------》eval转成内存中数据结构
# with open('db.txt','r',encoding='utf-8') as f:
#     data=f.read()
#     dic=eval(data)
#     print(dic,type(dic))

# l=[1,True,None,False]
# x=str(l) # "[1,True,None,False]"
# import json
# x="[null,true,false,1]"
#
# res=json.loads(x)
#
# print(res,type(res))


#序列化反序列化--------------------》json.dumps,json.loads
# import json
# # 序列化：内存中的数据结构----》转成一种中间格式（字符串）----》存到文件中
# dic={'name':'egon','age':18}
#
# res=json.dumps(dic) # json格式全都是双引号
# # print(res,type(res))
#
# with open('db.json','wb') as f:
#     f.write(res.encode('utf-8'))


#反序列化：文件----》读取中间格式（字符串）------》eval转成内存中数据结构
# with open('db.json','r',encoding='utf-8') as f:
#     data=f.read()
#     dic=json.loads(data)
#     print(dic,type(dic),dic['name'])


# 验证json格式全都为双引号
# with open('db.txt','r',encoding='utf-8') as f:
#     data=f.read()
#     dic=json.loads(data)
#     print(dic,type(dic),dic['name'])



#序列化反序列化--------------------》json.dump,json.load
import json
# dic={'name':'egon','age':18}
#
# with open('db1.json','wt',encoding='utf-8') as f:
#     json.dump(dic,f)

# with open('db1.json','rt',encoding='utf-8') as f:
#     dic=json.load(f)
#     print(dic['name'])



#=-==============================pickle序列化
import pickle
#序列化
# s={1,2,3,4,}
# res=pickle.dumps(s)
# print(res,type(res))
#
# with open('db.pkl','wb') as f:
#     f.write(res)

#反序列化
# with open('db.pkl','rb') as f:
#     data=f.read()
#     # print(data)
#     s=pickle.loads(data)
#     print(s,type(s))


#dump与load
import pickle
# s={1,2,3}
# with open('db1.pkl','wb') as f:
#     pickle.dump(s,f)

with open('db1.pkl','rb') as f:
    s=pickle.load(f)
    print(s,type(s))

