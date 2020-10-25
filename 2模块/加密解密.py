'''
非对称加密算法：

文件加密需要公开密钥（publickey）和私有密钥（privatekey）。
接收方在发送消息前需要事先生成公钥和私钥，然后将公钥发送给发送方。
发送放收到公钥后，将待发送数据用公钥加密，发送给接收方。
接收到收到数据后，用私钥解密。

在这个过程中，公钥负责加密，私钥负责解密，数据在传输过程中即使被截获，攻击者由于没有私钥，因此也无法破解。
非对称加密算法的加解密速度低于对称加密算法，但是安全性更高。
非对称加密算法：RSA、DSA、ECC等算法


RSA加密
    公钥加密算法，一种非对称密码算法

    公钥加密，私钥解密

3个参数：

    sa_n， rsa_e，message

    sa_n, rsa_e 用于生成公钥

    message： 需要加密的消息

安装 pip install rsa  -i http://pypi.douban.com/simple/  报错

pip install rsa -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com 成功

数字签名
签名使用privkey，验证使用pubkey。刚好和加密相反。

(pubkey, privkey) = rsa.newkeys(512)
message = 'Go left at the blue tree'
# 签名
signature = rsa.sign(message, privkey, 'SHA-1')
# 验证
rsa.verify(message, signature, pubkey)

'''

import rsa
# from rsa.bigfile import *
'''
4.0的主要变化
版本3.4是3.x范围内的最后一个版本。版本4.0删除了以下模块，因为它们不安全：

rsa._version133
rsa._version200
rsa.bigfile
rsa.varblock
这些模块在3.4版中被标记为已弃用。

此外，在4.0中，I / O函数经过简化，可以在所有支持的Python版本上使用字节。

4.0版本不再支持Python 2.6和3.3。
'''
from binascii import b2a_hex,a2b_hex #16进制转换


# 定义一个加密类 
class RsaCrypt():
    # 初始化取得 公钥 和 私钥
    def __init__(self,pubkey,prikey):
        self.pubkey=pubkey
        self.prikey=prikey

    # 加密
    def encrypt(self,text):
        # 用rsade的encrypt函数加密，参数为：需加密的文本,加密用的公钥。
        cipher_text=rsa.encrypt(text.encode('utf-8'),self.pubkey)
        # 因为rsa加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        return b2a_hex(cipher_text)

    # 解密
    def decrypt(self,text):
        decrypt_text=rsa.decrypt(a2b_hex(text),self.prikey)
        return decrypt_text

    # 加密大型文件 把要加密的作为input_file，加密完的作为output_file
    def encrypt_file(self,input_file,output_file):
        with open(input_file,'rb') as infile,open(output_file,'wb') as outfile:
            rsa.bigfile.encrypt_bigfile(infile,outfile,self.pubkey)

    # 解密大型文件 把要解密的作为input_file，解密完的作为output_file 与上面刚好相反
    def decrypt_file(self,input_file,output_file):
        with open(input_file,'rb') as infile,open(output_file,'wb') as outfile:
            rsa.bigfile.decrypt_bigfile(infile,outfile,self.prikey)

    # 签名
    def sign(self,msg):
        sign_msg=rsa.sign(msg.encode('utf-8'),self.prikey,'SHA-1')
        return sign_msg

    # 验证
    def verify(self,msg,sign_msg):
        res=rsa.verify(msg.encode('utf-8'),sign_msg,self.pubkey)
        return res

    # 签名文件 用私钥加密后得到签名后的文件
    def sign_file(self,file):
        with open(file,'rb') as f:
            signature = rsa.sign(f, self.prikey, 'SHA-1')
        return signature
    
    # 验证文件签名 (用未签名的原文和签名后的文件加上公钥，得出是否是与公钥对应的私钥加密的结果)
    def verify_file(self,file,signature):
        with open(file,'rb') as f:  
            res=rsa.verify(f,signature,self.pubkey)
        return res



if __name__ == "__main__":
    # 用rsa的newkeys函数生成一对公钥和私钥
    pubkey,prikey=rsa.newkeys(512) #64、128无效，加密最低只能用256，512、1024可以用  签名最低要用512 否则报错
    print('---公钥---')
    print(pubkey)
    print('---私钥---')
    print(prikey)
    # 生成加密对象
    rs_obj=RsaCrypt(pubkey,prikey)
    # 定义要加密的文本
    # text='hello world'
    # text='你好 世界'
    
    # 用加密对象加密
    # encrypt_text=rs_obj.encrypt(text)
    # print('----加密后的文本----')
    # print(encrypt_text)

    # 用加密对象解密
    # decrypt_text=rs_obj.decrypt(encrypt_text)
    # print('----解密后的文本----')
    # print(decrypt_text.decode('utf-8'))

    # 加密文件
  

    input_file=r'D:\pyj\st\study\test1.txt'
    output_file=r'D:\pyj\st\study\test1_encrypt.txt'
    rs_obj.encrypt_file(input_file,output_file)
    # 解密文件


    # 签名
    # print('-------签名------------')
    # # 定义要签名的消息
    # msg='hello'
    # mse='hello1'
    # # 用加密对象签名
    # sign_msg=rs_obj.sign(msg)
    # print(sign_msg)
    # # 用加密对象验证签名
    # try:
    #     # 验证成功 会返回加密的算法SHA-1
    #     print(rs_obj.verify(msg,sign_msg))

    # except Exception as e:
    #     # 验证失败 
    #     print(e)

    # 用加密对象签名文件
    # sign_file=rs_obj.sign_file(r'D:\pyj\st\study\道德经.txt')
    # print(sign_file)

    # # 用加密对象验证签名文件
    # print('-------验证签名------------')
    # print(rs_obj.verify_file(r'D:\pyj\st\study\道德经.txt',sign_msg))
    # 加密软件
        # 以功能为主体 
            # 加密
            # 解密
            # 签名
            # 验证签名

            # 加密/解密
            # 签名/验证