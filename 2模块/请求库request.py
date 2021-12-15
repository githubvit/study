import requests

# 参加白月黑羽 自动化测试 中 requests库和session http://www.python3.vip/tut/auto/apitest/03/

# request 是用来 发送http请求的，构建 http请求 就是 ，而http请求 由 请求方法 请求url 请求头 请求体组成。
# 因此，构建 http请求 就是 用request 构建 http请求的各个部分 发出请求 得到 Requests库里面定义的Response类的实例对象 response

# 一 构建请求
#1 构建简单请求
    # 响应response=request.请求方法('请求url')， 请求方法:get\post\put\delete。。。

#2 构建 含url请求参数的 请求 , 关键字params
    # 发生在get请求方法，post和其他请求方法没有url参数
    # 响应response=request.get('请求url？url参数部分k1=v1&k2=v2&...')， 
        # url参数直接写在url中，？号之后接url参数，参数之间用&隔开。
    # 响应response=request.请求方法('请求url',params=字典类参数名)， 请求方法:get\post\put\delete
        # url参数也可以不直接写在url中，而是事先用字典定义（urlarg={'k1':'v1','k2':'v2',...}）后，用params关键字传递给request的请求方法
            # response=request.get('请求url',params=urlarg)
            # request的get方法会把params参数字典转换为 urlencoded 格式(k1=v1&k2=v2&...) 放入请求url中 构造为 '请求url？url参数部分k1=v1&k2=v2&...'的get含参请求 


#3 构建 请求头headers， 关键字headers
    # 响应response=request.请求方法('请求url'，headers=请求头字典名)， 
        # h1={'user-agent': 'my-app/0.0.1',  'auth-type': 'jwt-token'}
        # response=request.请求方法('请求url',headers=h1)

#4 构建 请求消息体, 关键字 data
    # 请求消息体 的 请求方法为post，
    # 请求消息体文本可以采用多种格式，比如xml字符串\json\urlencoded等,
    # 如果是字符串格式，里面有中文要注意在传参时进行编码，
    # 否则，字符串格式文本默认的编码是latin-1编码，不能识别中文，因此，有中文就要data=消息体文本名.encode('urf8')
    # 如果是 字典格式，data会将其转换为urlencoded格式放入消息体
    # 如果是 json格式，就不要使用data关键字，request库直接提供json关键字 方便使用
        

# 抓包工具Fiddler
    # 启动后 就是系统代理 监听在 127.0.0.1:8888

    # 要生成根证书 以便拦截https 打开Fiddler 按如下步骤操作：

'''
    1 Click Tools > Options > HTTPS.

    2 Click the Decrypt HTTPS Traffic box.

    3 弹出如下警告，点击是。
            To intercept HTTPS traffic, Fiddler generates a unique root certificate.

            You may configure Windows to trust this root certificate to suppress
            security warnings. This is generally safe.

            Click 'Yes' to reconfigure Windows' Trusted CA list.
            Click 'No' if this is all geek to you.

            为了拦截HTTPS流量，Fiddler生成一个唯一的根证书。

            您可以将Windows配置为信任此根证书以禁止

            安全警告。这通常是安全的。

            单击“是”重新配置Windows的受信任CA列表。

            如果这对你来说都是极客，请单击“否”。
'''

    # 点击 Filters  
        #  根据目标主机地址 过滤 HTTP消息
            # 在 HOSTS  选择 show only the following hosts
            # 在下面的输入框中 输入地址(可以使用通配符，多个地址用分号隔开),输入完成后 点击 Changes not yet saved 生效.
        #  根据URL中包含的关键字 过滤
            # 在Request Headers 区域 选择 show only if URL contains ，并在右边的输入框中输入关键字。

    # 点击Inspectors 上下都选Raw 以便查看原始的请求和响应信息。
    
# 设置代理
proxies = {
  'http': 'http://127.0.0.1:8888',
  'https': 'https://127.0.0.1:8888',
}

# 通过代理 连接 就可以用fiddler抓包工具 抓包
# 获取返回的对象
# r = requests.get('http://mirrors.sohu.com/', proxies=proxies)

# 构建请求头
r_hds={
    'user-agent': 'my-app/0.0.1', 
    'auth-type': 'jwt-token'
}

# 构建请求消息体 xml 格式
# r_msg = '''
# <?xml version="1.0" encoding="UTF-8"?>
# <WorkReport>
#     <Overall>良好</Overall>
#     <Progress>30%</Progress>
#     <Problems>暂无</Problems>
# </WorkReport>
# '''
# r = requests.post("http://httpbin.org/post",
#                     headers=r_hds,
#                     data=r_msg.encode('utf8'),
#                     proxies=proxies)

# 构建请求消息体  urlencoded 格式
# 用字典构造消息体 
# r_msg={'key1': 'value1', 'key2': 'value2'}

# r = requests.post("http://httpbin.org/post",
                    # headers=r_hds,
                    # data=r_msg,
                    # proxies=proxies) 
# fiddler  抓包后 请求头中 出现 
    # 连接类型 Content-Type: application/x-www-form-urlencoded
    # 发现请求消息体 key1=value1&key2=value2 这就是urlencoded 格式


# 构建请求消息体 json 格式

import json

# 用 json格式(严格要求：字符串要用双引号""，最后一个元素结尾不能加逗号,) 定义消息
# 实际上用单引号也可以，最后一个元素加了逗号，也可以，因为request的json关键字会按json格式对其进行修改。
r_msg={
    'Overall':"良好",
    "Progress":"30%",
    "Problems":[
        {
            "No" : 1,
            "desc": "问题1...."
        },
        {
            "No" : 2,
            "desc": "问题2...."
        },
    ]
}

# r = requests.post("http://httpbin.org/post", data=json.dumps(r_msg),proxies=proxies)#请求头 没有 Content-Type 中文会被处理成Unicode
# r = requests.post("http://httpbin.org/post", data=json.dumps(r_msg,ensure_ascii=False).encode('utf8'),proxies=proxies)#显示中文：添加 ensure_ascii=False dumps就不会处理非ASCII码， 就不会处理中文，那么就会使用requests的默认编码Latin-1，就会报错，因此要用encode('utf8')
# 或 用 requests库中 json关键字
# r = requests.post("http://httpbin.org/post", json=r_msg,proxies=proxies)#请求头 出现 Content-Type: application/json 中文会被处理成Unicode
# r = requests.post("http://httpbin.org/post", data=r_msg,proxies=proxies)#如果不用json处理 data就会把r_msg当成字典 转成urlencoded 格式 出现 Content-Type: application/x-www-form-urlencoded


# 解析返回值 用文本方式查看
# print(r.text)
# print(r.json())

# 二 检查HTTP响应
# r = requests.get("http://www.python3.vip/")
# 1 检查http响应码  status_code

# print(r.status_code)

# 2 检查http响应头 headers

# print(r.headers) #字典

# 3 检查http响应消息体 content字节码 text文本 json()等

# 指定编码格式
# 否则requests会猜测是什么格式，然后按格式解码 往往是错的

# 1、
# print(r.text) # 中文 出现乱码 <h5 class="modal-title">å¼ç¨</h5>
# print(r.encoding) # 认为格式为 ISO-8859-1 显然是错的

# 2、
# r.encoding='utf8' # 指定编码 
# print(r.text) # 这样 text就会按指定编码解码 中文 显示正常 <h5 class="modal-title">引用</h5> 

# 3、
# 获取bytes对象 即字节串，用content,
# print(r.content) #b'<!DOCTYPE html>\r\n<html lang="zh">\r\n\...'

# 4、
# 用指定格式对字节串解码
# print(r.content.decode('utf8'))

# 5.
# 如果确定返回的消息体应为json格式 就用loads将字节码反序列化为json格式
# r=requests.post('http://httpbin.org/post',json={'1':1,'2':2,'3':'zf-字符','4':[1,2,3]})
# obj=json.loads(r.content.decode('utf8'))
# print(obj)
# print(type(obj)) #  <class 'dict'>
# print(obj['json']['3'])


# 因为 json 返回的太常见，所以 Response对象直接有r.json()方法打开 取代 json.loads(r.content.decode('utf8'))

# obj=r.json()
# print(obj)
# print(obj['json'])

# 云函数 api
# r=requests.get('http://service-otp4h4fi-1303002520.hk.apigw.tencentcs.com/')
# 列表页
# r=requests.get('http://service-otp4h4fi-1303002520.hk.apigw.tencentcs.com/test_list')
# 详情页
# r=requests.get('http://service-otp4h4fi-1303002520.hk.apigw.tencentcs.com/test_list/2')

# 三 session机制
# 对于有session要求的可以使用requests.Session()类的实例，用这个实例发请求，实现请求要求的session会话机制
# http://www.python3.vip/tut/auto/apitest/03/#session机制
s=requests.Session()
# 当然没有session要求的也可以用这个发请求
r=s.get('http://service-otp4h4fi-1303002520.hk.apigw.tencentcs.com/test_list/2')
obj=r.json()
print(obj)






