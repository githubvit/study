import base64
import rsa
from rsa import common
'''
知识基础

    加密是为了保证传输内容隐私，签名是为了保证消息真实性。

    服务器存私钥，客户端存公钥。（服务器和客户端关系可以考虑为 1:N）

    客户端往服务器传输内容，更多考虑是隐私性，所以公钥签名、私钥解密。

    服务器往客户端传输内容，更多考虑真实性，所以私钥签名，公钥验签。

    消息的摘要生的算法常用的是MD5或者SHA1，消息内容不一样，生成的摘要信息一定不一样。

    真实性的考虑一方面是内容由私钥拥有者发出，另一方面内容在传输过程中没有改变过，所以签名的对象是传输信息生成的消息摘要（摘要内容短，签名也会快些）。

    每次加密的长度需要小于密钥长度-特殊位（128位公钥，最长可加密128-11=117位明文）。

    每次解密的长度需要小于密钥的长度（128位私钥解密，解密密文长度需要小于等于128位）。

    如果加解密内容过长，就需要分段加密、解密。

    PEM格式的密钥为base64位文本格式。

'''


# 使用 rsa库进行RSA签名和加解密
class RsaUtil(object):
    # 使用 密钥.py 生成的base64转码的.pem密钥文件
    PUBLIC_KEY_PATH = r'D:\pyj\st\study\public.pem'  # 公钥
    PRIVATE_KEY_PATH = r'D:\pyj\st\study\private.pem'  # 私钥

    # 初始化key
    def __init__(self,
                 company_pub_file=PUBLIC_KEY_PATH,
                 company_pri_file=PRIVATE_KEY_PATH):

        if company_pub_file:
            # （从 .pem文件 -> pem -> pkcsl -><class 'rsa.key.PublicKey'>公钥）
            with open(company_pub_file,'rb') as pub_key_file:
                pub_key_pem=pub_key_file.read()                     # 获取pem格式的密钥
                # print(pub_key_pem)
                
            pubmark='-----BEGIN RSA PUBLIC KEY-----'                # 密钥开始标记
            public_key_pkcsl =rsa.pem.load_pem(pub_key_pem,pubmark) # 获取pkcsl格式的密钥
            self.company_public_key=rsa.PublicKey.load_pkcs1(public_key_pkcsl) # 获取包含密钥信息的密钥
        
            # print(type(self.company_public_key)) # <class 'rsa.key.PublicKey'> 已经转成了rsa库密钥的公钥类 可以用来加密和验签
                
        if company_pri_file:
            with open(company_pri_file,'rb') as pri_key_file:
                pri_key_pem=pri_key_file.read()
                # print(pri_key)
            primark='-----BEGIN RSA PRIVATE KEY-----'
            private_key_pkcsl =rsa.pem.load_pem(pri_key_pem,primark)
            self.company_private_key = rsa.PrivateKey.load_pkcs1(private_key_pkcsl) #已经转成了rsa库密钥的私钥类 可以用来解密和签名

    # 成功实现 获取 大文件加解密 切割用 的 数据长度 
    def get_max_length(self, rsa_key, encrypt=True):
        """加密内容过长时 需要分段加密 换算每一段的长度.
            :param rsa_key: 钥匙.
            :param encrypt: 是否是加密.
        """
        blocksize = common.byte_size(rsa_key.n) #每次加密的长度需要小于密钥长度-特殊位（128位公钥，最长可加密128-11=117位明文）。
        reserve_size = 11  # 预留位为11
        if not encrypt:  # 解密时不需要考虑预留位 decrypt_by_private_key(self, message)
            reserve_size = 0
        maxlength = blocksize - reserve_size
        return maxlength

    # 加密 公钥
    def encrypt_by_public_key(self, message):
        """使用公钥加密.
            :param message: 需要加密的内容.
            加密之后需要对接过进行base64转码
        """
        encrypt_result = b''
        max_length = self.get_max_length(self.company_public_key) # 获取消息切割长度
        while message:
            input = message[:max_length]
            message = message[max_length:]
            out = rsa.encrypt(input, self.company_public_key)
            encrypt_result += out
        encrypt_result = base64.b64encode(encrypt_result) #对结果进行base64编码
        return encrypt_result

    # 解密 私钥
    def decrypt_by_private_key(self, message):
        """使用私钥解密.
            :param message: 需要加密的内容.
            解密之后的内容直接是字符串，不需要在进行转义
        """
        decrypt_result = b""

        max_length = self.get_max_length(self.company_private_key, False) # 获取消息切割长度 记住要有False参数

        decrypt_message = base64.b64decode(message)
        while decrypt_message:
            input = decrypt_message[:max_length]
            decrypt_message = decrypt_message[max_length:]
            out = rsa.decrypt(input, self.company_private_key)
            decrypt_result += out
        return decrypt_result

    # 签名 私钥 base64转码
    def sign_by_private_key(self, data_bytes):
        """私钥签名.
            :param data: 需要签名的内容.
            使用SHA-1 方法进行签名（也可以使用MD5）
            签名之后，需要转义后输出
        """
        signature = rsa.sign(data_bytes, priv_key=self.company_private_key, hash_method='SHA-1')
        return base64.b64encode(signature)
        
    # 验签  原文 密文 公钥 
    def verify_by_public_key(self, message_bytes, signature):
        """公钥验签.
            :param message: 验签的内容.
            :param signature: 对验签内容签名的值（签名之后，会进行b64encode转码，所以验签前也需转码）.
        """
        signature = base64.b64decode(signature)

        try:
            rsa.verify(message_bytes, signature, self.company_public_key) 
            print('验证成功')
            return True
        except Exception as e:
           print('验证失败',e)
           return False
         
        # 
# 一 消息加密
# message = '你好 world'
# message1 = '你好1 world'
# # message = 'hell world'
# print("明文内容：>>> ")
# print(message)
# rsaUtil = RsaUtil()
# encrypy_result = rsaUtil.encrypt_by_public_key(message.encode('utf-8')) #必须是 bytes字节
# print("加密结果：>>> ")
# print(encrypy_result)
# decrypt_result = rsaUtil.decrypt_by_private_key(encrypy_result)
# print("解密结果：>>> ")
# print(decrypt_result.decode('utf-8'))
# sign = rsaUtil.sign_by_private_key(message.encode('utf-8'))
# print("签名结果：>>> ")
# print(sign)
# print("验签结果：>>> ")
# print(rsaUtil.verify_by_public_key(message.encode('utf-8'), sign))

# 二 成功对大文件进行加密和解密
# with open(r'D:\pyj\st\study\道德经.txt','r',encoding='utf-8') as f:
    # message=f.read()#读的时候一定要告诉文件的编码模式为encoding='utf-8'，否则就会按当前的环境（比如cmd的gbk编码）加载，会报错
# 
# rsaUtil = RsaUtil()
# encrypy_result = rsaUtil.encrypt_by_public_key(message.encode('utf-8'))
# print("加密结果：>>> ")
# print(encrypy_result)
# decrypt_result = rsaUtil.decrypt_by_private_key(encrypy_result)
# print("解密结果：>>> ")
# print(decrypt_result.decode('utf-8'))
# sign = rsaUtil.sign_by_private_key(message.encode('utf-8'))
# print("签名结果：>>> ")
# print(sign)
# print("验签结果：>>> ")
# print(rsaUtil.verify_by_public_key(message.encode('utf-8'), sign))

# 三 一般性文件的加密和解密，就是使用字节 ‘rb’ 方式
with open(r'D:\pyj\st\study\道德经.txt','rb') as f:
    message=f.read() # rb 读出来就是字节了，因此这里的message就是bytes，不用去编码了。
    
rsaUtil = RsaUtil()
encrypy_result = rsaUtil.encrypt_by_public_key(message)
print("加密结果：>>> ")
print(encrypy_result)
decrypt_result = rsaUtil.decrypt_by_private_key(encrypy_result)
print("解密结果：>>> ")
print(decrypt_result.decode('utf-8'))
sign = rsaUtil.sign_by_private_key(message)
print("签名结果：>>> ")
print(sign)
print("验签结果：>>> ")
print(rsaUtil.verify_by_public_key(message, sign))

'''
知识点：
    rsa计算密钥长度的方式是 common.byte_size(rsa_key.n)
    rsa加密：rsa.encrypt(message, pub_key)
    rsa解密：rsa.decrypt(crypto, priv_key)
    rsa签名：rsa.sign(message, priv_key, hash)
    rsa验签：rsa.verify(message, signature, pub_key)
    rsa默认没有私钥加密，公钥解密的方法（加解密传入错误的key会报错，如果想实现私钥加密，公钥解密可以自行模拟底层代码实现）
    签名只能用私钥（用到私钥的n值，公钥没有n值，n、d、e具体什么意思请百度RSA算法原理）
    rsa加载公钥和私钥的方法不同
    rsa私钥签名时，需要传入的是不是具体的摘要信息（字符串），而是签名信息的hash对象（对象）
    不同版本的rsa验签成功之后返回结果不一样，有的是True，有的是返回生成摘要算法名：如sha1

结果：
    明文内容：>>> 
    你好 world
    加密结果：>>>
    b'OAFJbpVcwmS310aPR3purnp+gHXA4FJTQBnU9lyyINAXY/AOT7fvI6QhjFDv6HgiHuuMDI9QI+gU4J0qPNLeFQ=='
    解密结果：>>>
    你好 world
    签名结果：>>>
    b'QUXjrjHBgmYmSO/zlueWfCzsToEbX3QecBU+KpLdarp1QA2oeD3/cemuMWp/pKD+888O3+n2E612L3/LtqsBlg=='
    验签结果：>>>
    SHA-1

'''