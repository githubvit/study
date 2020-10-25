# 生成base64编码的.pem格式密钥文件
# （从<class 'rsa.key.PublicKey'> -> pkcsl -> pem -> .pem文件）
import rsa

# 先生成一对密钥，然后保存.pem格式文件，当然也可以直接使用
(pubkey, privkey) = rsa.newkeys(512)


pub=b''
pub += pubkey.save_pkcs1() #这一步很重要 这是密钥的pkcs1格式，里面记载了密钥的信息（比如密钥的n），再转成bytes类型。
pubmark='-----BEGIN RSA PUBLIC KEY-----' # 密钥开始的标记 
pub1=rsa.pem.save_pem(pub,pubmark) # 转成base64编码的pem格式信息
with open('public.pem', 'wb') as pubfile:
    pubfile.write(pub1) #存成pem密钥文件

pri=b''
pri += privkey.save_pkcs1()
primark='-----BEGIN RSA PRIVATE KEY-----'
pri1=rsa.pem.save_pem(pri,primark)
with open('private.pem', 'wb') as prifile:
    prifile.write(pri1)
