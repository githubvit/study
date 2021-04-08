'''
QRCode
QRCode码是由日本于1994年9月研制的一-种矩阵二维码符号，
它具有一维条码及其它二 维条码所具有的信息容量大、可靠性高、
可表示汉字及图象多种文字信息、保密防伪性强等优点。

QR码符号共有40种规格,分别为版本1、版本....版本40
Version 1 是 21 x 21 的矩阵，Version 2 是 25 x 25 的矩阵，Version 3 是 29 的尺寸，
每增加一个 version，就会增加 4 的尺寸，公式是：(V-1)*4 + 21（V是版本号） 
最高 Version 40，(40-1)*4+21 = 177，所以最高是 177 x 177 的正方形。
其中最高版本40可容纳多达1850个大写字母或2710个数字或1108个字节，或500多个汉字，
比普通条码信息容量约高几十倍。由于其高密度编码，信息容量大，所以被广泛采用。

qrcode模块
是Github_上的一-个开源项目，提供了生成二维码的接口。
qrcode默认使用PIL库(即pillow)用于生成图像。
由于生成qrcode图片需要依赖Python的图像库，
所以需要先安装Python图像库PIL(Python Imaging Library)。

pip install qrcode

pillow
    用pillow的Image对象的open方法可以打开图像。
            # page_img=Image.open('snap.png')

    用pillow图片image的裁剪crop 取图
        #  crop_img=page_img.crop((left,top,right,bottom))

    用pillow图片Image逐点加载load()[x,y] 取得该点的rgb
        # 循环图片的宽和高，逐点取得rgb,每个点都是一个元组(r,g,b,255)，
         # for x in range(w): 
            # for y in range(h):
                #rgb1=img1.load()[x,y] #(r,g,b,255)
        # 两幅图片逐点取得rgb就可以比较。


'''

from PIL import Image
import qrcode
import sys,os

#找到目录
BASE_DIR=os.path.dirname(__file__) 

# 一 最简单的用法
# make 按照相关参数生成二维码
# show 将生成的二维码显示出来

def simple_qrcode():
    # qr=qrcode.make('https://www.baidu.com')
    # qr=qrcode.make(r'{"a":"清风明月"}')
    qr=qrcode.make({"a":"http://www.baidu.com"})

    qr.show()
# simple_qrcode()

# print(BASE_DIR) # BASE_DIR末尾是不带‘\’的

# 二 基本案例 生成普通二维码

def ordinary_qrcode():
    # 1 生成qrcode对象
        # 方法
            # qrcode.QRCode(
            #     version=1,
            #     error_ correction=qrcode.ERROR_ CORRECT_ _L, 
            #     box_ size=10,
            #     border=4,
            #     image_ factory=None,
            #     mask_ pattern=None
            # )
        # 参数： 
            # * error_ correction:控制二维码纠错级别，容错率。
                # * ERROR_ CORRECT_ _L:大约7%或者更少的错误会被更正。
                # 
                # * ERROR_ CORRECT_ _M:默认值，大约15%或者更少的错误会被更正。
                # 
                # * ERROR_ CORRECT_ Q:大约25%或者更少的错误会被更正。
                # 
                # * ERROR_ CORRECT_ H:大约30%或者更少的错误会被更正。

            # * box_ size: 控制二维码中每个格子的像素数，默认为10。
            # 
            # * border:控制二维码四周留白包含的格子数，默认为4。
            # 
            # * image_ factory: 选择生成图片的形式，默认为PIL图像。
            # 
            # * mask_ pattern: 选择生成图片的的掩模。

            

    qr=qrcode.QRCode(
        version=5, # 版本 版本越高 容量越大，最高版本 40 可容纳1850个大写字母或2710个数字或1108个字节，或500多个汉字。
        error_correction=qrcode.constants.ERROR_CORRECT_L, # 容错率 低
        box_size=10, # 每个格子的像素10
        border=4, # 空白边框占4格
    )

    # 2 添加数据
    # add_ _data(str,optimize=20):
        # 添加要转换的文字到data参数; 
        # 如果使用了optimize优化参数,数据将被拆分为多个块来进行优化，以找到一个长度至少为这个值的足够简洁的方式来生成二维码。
            # 设置为"0”以避免优化。
    qr.add_data('https://www.baidu.com')

    # 3 生成二维码
    # make(fit=True):
        # 当fit参数为真或者没有给出version参数时， 将会调用best_ fit方法来找到适合数据的最小尺寸。
        # 取值为 None （默认）或者使用fit=True参数（默认）时，二维码会自动调整大小。
    # qr.make(fit=True)
    qr.make()

    
    # 4 将二维码转为图像 并 保存图像
    # make_ image(ill color=None, back_ color=None,image_ factory=None):
        # 创建二维码的图像并返回，默认为PIL图像。
    img = qr.make_image()

    filepath= BASE_DIR+'\ordinaryqrcode.png' #注意 在BASE_DIR后 加‘\’路径符号，
    img.save(filepath)

    # 5 显示 图像
    img.show()

# ordinary_qrcode()

# 三 生成带有图片的二维码
# 在二维码中间镶上小图片
def img_qrcode():
    # 1. 建立对象
    qr=qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # 2. 添加数据
    qr.add_data('https://www.baidu.com')
    # 3. 生成二维码
    qr.make(fit=True)

    # 4. 转为图像 并 保存图像
    img=qr.make_image()

    img = img.convert("RGBA")               # 彩色，不然是黑白 *****

    filepath=BASE_DIR+'\imgqrcode.png'
    img.save(filepath)


    # 5. 添加中心icon

    # 5.1 获取icon 用PIL的Image的open方法
    icon=Image.open(r'D:\pyj\st\study\pyside2_pyqt\pys2\xxx.png')
    # icon=Image.open(r'D:\pyj\st\study\pyside2_pyqt\pys2\rose.png')
    
    # print(icon.size) #(512, 512) 太大

    # 5.2 调整icon大小
    # 获取图片的宽、高
    img_w,img_h=img.size
    # 获取icon的宽、高
    icon_w,icon_h=icon.size

    # 图片img中心位置参数设置
    factor=4 #设置4格center
    center_w=int(img_w/factor) #转为像素
    center_h=int(img_h/factor)

    # 如果icon原来的宽、高大于要中心位置的宽高 就 调整icon宽、高 
    if icon_w > center_w:
        icon_w=center_w
    if icon_h > center_h:
        icon_h=center_h
    # 重设icon的尺寸
    icon=icon.resize((icon_w,icon_h),Image.ANTIALIAS)

    # 5.3 计算icon在img图片的坐标
    # 得到icon的x,y坐标，居中显示
    w=int((img_w-icon_w)/2)
    h=int((img_h-icon_h)/2)

    icon=icon.convert('RGBA')           # ***** 对黑白图片采取中心透明方式，img.paste(icon,(w,h),icon)，没有就报错bad transparency mask

    # 5.4 黏贴到计算的位置
    # img.paste(icon,(w,h),mask=None) #中心黑块
    img.paste(icon,(w,h),icon) # 中心透明，没有黑块背景
    

    # 6 显示 二维码图片
    img.show()


# img_qrcode()

# 四 生成带有二维码的图片
# 在一张图片的某个地方贴上二维码

def qrcode_img():
    # 1 获取图片
    img=Image.open(r'D:\pyj\st\study\pyside2_pyqt\pys2\rose.png')
    # img=Image.open(r'D:\pyj\st\study\pyside2_pyqt\pys2\xxx.png')

    # 2 获取二维码图片
    # qr=qrcode.QRCode(box_size=3) # 一个格子三像素
    qr=qrcode.QRCode(box_size=2) # 一个格子两像素 小了很多 可以调整大小
    qr.add_data('http://www.baidu.com')
    qr.make()
    qr_img=qr.make_image()

    # 3 获取图片和二维码图片的宽高
    img_w,img_h=img.size
    qr_img_w,qr_img_h=qr_img.size

    # 4 在图片上黏贴二维码图片
    # img.paste(qr_img)                         # 左上(0,0)
    # img.paste(qr_img,(img_w-qr_img_w,0))        # 右上
    # img.paste(qr_img,(img_w-qr_img_w,img_h-qr_img_h)) # 右下 
    img.paste(qr_img,(0,img_h-qr_img_h))            # 左下 

    # 5 展示图片
    img.show()

# qrcode_img()








