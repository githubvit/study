import base64
import rsa
from rsa import common
import sys,os

# 取得当前目录
print(__file__)
# 取得当前文件名
print(__file__.split('/')[-1])
# 取得当前文件名 不含扩展名
print(__file__.split('/')[-1].split('.')[0])
# 取得当前目录名
print(os.path.dirname(__file__))
rpath=os.path.dirname(__file__)
# 生成目录结构
    # 公钥文件目录
    # 私钥文件目录
    # 已加密文件目录
    # 已解密文件目录
def make_key_pubpath():
    pubpath=rpath+'\\key\\pub' # 注意路径符号的写法与__file__相反，所以要避免转义 *****
    os.makedirs(pubpath)
    # pass
def make_key_pripath():
    pripath=rpath+'\\key\\pri'
    os.makedirs(pripath)
    # pass
def make_encrypt_file_path():
    encrypt_file_path=rpath+'\\encrypt_file'
    os.mkdir(encrypt_file_path)
    # pass
def make_decrypt_file_path():
    decrypt_file_path=rpath+'\\decrypt_file'
    os.mkdir(decrypt_file_path)
    # pass    

# 根据填写的名称 生成相应的公钥和私钥.pem密钥文件
def build_keyfile_by_name(name):
    # 先生成一对密钥，然后保存.pem格式文件，当然也可以直接使用
    (pubkey, privkey) = rsa.newkeys(512)
    # 再生成放密钥的目录 在当前目录下建立keyfile目录

    pub=b''
    pub += pubkey.save_pkcs1() #这一步很重要 这是密钥的pkcs1格式，里面记载了密钥的信息（比如密钥的n），再转成bytes类型。
    pubmark='-----BEGIN RSA PUBLIC KEY-----' # 密钥开始的标记 
    pub_pem=rsa.pem.save_pem(pub,pubmark) # 转成base64编码的pem格式信息
    # 判断路径是否存在
    pubpath=rpath+'\\key\\pub'
    pubpath_isExists=os.path.exists(pubpath)
    if not pubpath_isExists:
        make_key_pubpath()
    pubfile=pubpath+'\\'+name+'_public.pem'
    with open(pubfile, 'wb') as f:
        f.write(pub_pem) #存成pem密钥文件

    pri=b''
    pri += privkey.save_pkcs1()
    primark='-----BEGIN RSA PRIVATE KEY-----'
    pri_pem=rsa.pem.save_pem(pri,primark)
    # 判断路径是否存在
    pripath=rpath+'\\key\\pri'
    pripath_isExists=os.path.exists(pripath)
    if not pripath_isExists:
        make_key_pripath()
    prifile=pripath+'\\'+name+'_private.pem'
    with open(prifile, 'wb') as f:
        f.write(pri_pem)
    

# 根据要加密的文件 生成密钥文件
def build_keyfile_by_filepath(filepath):
    # 1 取得要加密的文件 路径+文件名
        # 从文件取得文件名
    filename=filepath.split('\\')[-1] # 注意路径符号的写法与__file__相反，所以要避免转义 *****
    # print(filename)
    # 2 生成密钥文件
    filename2=filepath.split('\\')[-1].split('.')[0] # 不含扩展名的文件名
    # print(filename2)
    build_keyfile_by_name(filename2)

# 使用.pem密钥文件进行 加密/解密/ 签名/验签
class RsaCrypt():

    # 初始化key
    def __init__(self,company_pub_file,company_pri_file):

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
        blocksize = common.byte_size(rsa_key.n)
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

# 单独的加密类
class RsaEncrypt():
    def __init__(self,company_pub_file):
        # 从私钥文件取得私钥
        if company_pub_file:
            with open(company_pub_file,'rb') as pub_key_file:
                pub_key_pem=pub_key_file.read()
            pubmark='-----BEGIN RSA PUBLIC KEY-----'                # 密钥开始标记
            public_key_pkcsl =rsa.pem.load_pem(pub_key_pem,pubmark) # 获取pkcsl格式的密钥
            self.company_public_key=rsa.PublicKey.load_pkcs1(public_key_pkcsl) # 获取包含密钥信息的密钥
        pass

    # 成功实现 获取 大文件加解密 切割用 的 数据长度 
    def get_max_length(self, rsa_key):
        """加密内容过长时 需要分段加密 换算每一段的长度.
            :param rsa_key: 钥匙.
            :param encrypt: 是否是加密.
        """
        blocksize = common.byte_size(rsa_key.n) # 计算密钥长度:common.byte_size(rsa_key.n)
        reserve_size = 11  # 预留位为11 
        maxlength = blocksize - reserve_size # 加密消息的最大长度=密钥长度-预留位(解密没有预留位)
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


# 单独的解密类
class RsaDecrypt():
    def __init__(self,company_pri_file):
        # 从私钥文件取得私钥
        if company_pri_file:
            with open(company_pri_file,'rb') as pri_key_file:
                pri_key_pem=pri_key_file.read()
                # print(pri_key)
            primark='-----BEGIN RSA PRIVATE KEY-----'
            private_key_pkcsl =rsa.pem.load_pem(pri_key_pem,primark)
            self.company_private_key = rsa.PrivateKey.load_pkcs1(private_key_pkcsl) #已经转成了rsa库密钥的私钥类 可以用来解密和签名
        pass
    # 取得消息的 切割长度
    def get_max_length(self,rsa_key):
        """加密内容过长时 需要分段加密 换算每一段的长度.
            :param rsa_key: 钥匙.
            :param encrypt: 是否是加密.
        """
        blocksize = common.byte_size(rsa_key.n) # 计算密钥长度
        maxlength = blocksize #每次解密的长度需要小于密钥的长度
        return maxlength

    def decrypt_by_private_key(self,message):
        """使用私钥解密.
            :param message: 需要加密的内容.
            解密之后的内容直接是字符串，不需要在进行转义
        """
        decrypt_result = b""

        max_length = self.get_max_length(self.company_private_key)

        decrypt_message = base64.b64decode(message)#进行base64解码
        try:
            while decrypt_message:
                input = decrypt_message[:max_length]
                decrypt_message = decrypt_message[max_length:]
                out = rsa.decrypt(input, self.company_private_key)
                decrypt_result += out
            return decrypt_result
        except Exception as e:# 如果解密过程中出现了错误比如私钥不对 等 就会产生异常导致解密失败错误
            print('解密失败',e)
            return f'解密失败 {e}'.encode('utf-8')

        
         
# 使用 密钥文件函数build_rsa_keyfile() 和 RsaCrypt对象 对 文件 进行加密/解密
# 参数：要加密的文件
# 输出：加密完的文件 相应的公钥和私钥

# 加密文件1 
# 用 指定公钥 对 指定文件 加密
def encrypt_file(filepath,pub_key_file):

    # 1 用公钥文件 生成 加密对象RsaEncrypt(pub_key_file)

    rsa_encrypt_obj=RsaEncrypt(pub_key_file)

    # 2 用加密对象 对 文件 加密

    # 2.1 读取要加密文件的bytes格式内容
    with open(filepath,'rb') as f:
        message=f.read()
    # 2.2 用 加密对象 加密 读取的消息 取得 加密结果
    res_encrypt=rsa_encrypt_obj.encrypt_by_public_key(message)

    # 3 将加密结果 写入 指定加密文件

    # 3.1 从文件取得文件名
    filename=filepath.split('\\')[-1] # 注意路径符号的写法与__file__'/'相反，所以要避免转义 *****
    encrypt_filename='encrypt_'+filename
    # 3.2 判断路径是否存在 
    encrypt_file_path=rpath+'\\encrypt_file'
    encrypt_file_path_isExists=os.path.exists(encrypt_file_path)
    if not encrypt_file_path_isExists: # 不存在 就调用 该目录生成函数 生成该目录
        make_encrypt_file_path()
    # 3.3 写入
    with open(encrypt_file_path+'\\'+encrypt_filename,'wb') as encrypt_file:
        encrypt_file.write(res_encrypt)


    pass

# 加密文件2
def file_encrypt(filepath):

    # 1 取得要加密的文件 路径+文件名
        # 从文件取得文件名
    filename=filepath.split('\\')[-1] # 注意路径符号的写法与__file__相反，所以要避免转义 *****
    print(filename)
    
    filename2=filepath.split('\\')[-1].split('.')[0] # 不含扩展名的文件名
    print(filename2)
    # 2 利用密钥文件生成RsaCrypt对象rsa_obj
    pubfile=rpath+'\\key\\pub\\'+filename2+'_public.pem'
    key_isexist=os.path.exists(pubfile)

    # 2.1 密钥文件不存在就生成密钥文件
    if not key_isexist:
        build_rsa_keyfile(filename2)
    
    # 3 调用 加密文件1
    encrypt_file(filepath,pubfile)
   
    
# 解密1 
# 用 指定私钥 对 指定加密文件 解密
def decrypt_file(encryptfile,prikey_file):

    # 1 用 私钥文件 实例化 解密对象

    decrypt_obj=RsaDecrypt(prikey_file)

    # 2 用 解密对象 解密 指定加密文件 

    # 2.1 读出已加密文件的bytes内容
    with open(encryptfile,'rb') as f:
        message=f.read()
    # 2.2 取得解密对象解密结果
    res_decrypt=decrypt_obj.decrypt_by_private_key(message)
    
    # 3 将 解密结果 写入 指定解密文件

    # 3.1 取得文件名
    filename=encryptfile.split('\\')[-1].split('encrypt_')[-1]
    decrypt_filename='decrypt_'+filename
    # 3.2 判断指定目录是否存在
    decrypt_file_path=rpath+'\\decrypt_file'
    decrypt_file_path_isExists=os.path.exists(decrypt_file_path)
    if not decrypt_file_path_isExists:
        make_decrypt_file_path() # 不存在 就生成该指定目录
    # 3.3 将 解密结果 写入
    with open(decrypt_file_path+'\\'+decrypt_filename,'wb') as f:
        f.write(res_decrypt) 

# 解密2 
# 只放入已加密文件 
def file_decrypt(encrypt_file):
    
    # 1 取得文件名
    filename=encrypt_file.split('\\')[-1].split('encrypt_')[-1]
    # 2 解密文件是否存在
    # 解密文件路径
    decrypt_file_arg=rpath+'\\decrypt_file'+'\\decrypt_'+filename
    decrypt_file_isexists=os.path.exists(decrypt_file_arg)
    if decrypt_file_isexists:
        print('解密文件已存在，退出。')
        return 
    # 3 根据文件名取得私钥文件
    filename2=filename.split('.')[0] # 不含扩展名的文件名
    prikey_file=rpath+'\\key\\pri\\'+filename2+'_private.pem'

    # 4 解密文件
    if os.path.exists(prikey_file):
        # 调用解密1
        decrypt_file(encrypt_file,prikey_file)
        print('解密已完成，退出。')
        pass
    else:
        print('没有密钥文件，无法解密，退出。')
        
    pass



if __name__ == "__main__":
    # 功能1 生成密钥文件
    # 生成指定名称name的密钥文件
        # 这里的密钥文件,都是指经过base64转码的.pem格式的密钥文件。
        # 放在指定的目录下：公钥目录 key/pub 和 私钥目录 key/pri 
        # 以指定格式文件名命名： 
            # 公钥文件相应文件名 name+'_public.pem'
            # 私钥文件相应文件名 name+'_private.pem'
    # name='道'
    # build_keyfile_by_name(name)


    

    # 生成指定文件的密钥文件 
        # 放在指定的目录下：公钥目录 key/pub 和 私钥目录 key/pri 
        # 以指定格式文件名命名： 这里的filename 指不含扩展名的文件名称 比如 道德经
            # 公钥文件相应文件名 filename+'_public.pem'
            # 私钥文件相应文件名 filename+'_private.pem'
    # filepath=r'D:\pyj\st\study\道德经.txt'
    # build_keyfile_by_filepath(filepath)


    # 功能2：加密
        # 生成的加密文件会放在指定的目录'/encrypt_file'下
        # 以指定的格式命名：'encrypt_'+filename 命名 （这里的filename指包含扩展名的文件名称 比如 道德经.txt）
    # 加密1
        #用指定密钥对指定文件加密
    # filepath=r'D:\pyj\st\study\道德经.txt'
    # pub_key_file=r'D:\pyj\st\study\2模块\key\pub\道德经_public.pem'
    # encrypt_file(filepath,pub_key_file)
    
    # 加密2
        # 如果在指定目录有相应密钥文件，就会使用相应密钥文件加密
        # 否则，会生成相应密钥文件，再加密
    # filepath=r'D:\pyj\st\study\道德经.txt'  
    # file_encrypt(filepath)

    # 功能4：解密
        # 生成的解密文件会放在指定的目录'/decrypt_file'下
        # 以指定的格式命名：'decrypt_'+filename 命名 （这里的filename指包含扩展名的文件名称 比如 道德经.txt）

    # 解密1 需要指定私钥文件的解密
    # encrypt_file=r'D:\pyj\st\study\2模块\encrypt_file\encrypt_道德经.txt'
    # prikey_file=r'D:\pyj\st\study\2模块\key\pri\道德经_private.pem'
    # decrypt_file(encrypt_file,prikey_file)

    # 解密2 根据要解密的文件名自动寻找私钥文件的解密
    # 如果 解密文件已存在，退出。
    # encrypt_file=r'D:\pyj\st\study\2模块\encrypt_file\encrypt_道德经.txt'
    # file_decrypt(encrypt_file)
