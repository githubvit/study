from PIL import Image
import pyzbar.pyzbar as pyzbar

# 获取 二维码 图片
img_path=r'C:\Users\69598\Desktop\wxzf1.png'
img=Image.open(img_path)

# 用pyzbar 读取 二维码 获取二维码解析信息
bars=pyzbar.decode(img)
print(bars)
# 因为一张图片，可能是一张二维码，可能图片里有多张二维码
# 可以识别一张照片上的多个二维码，若识别效果不好可相应的调节亮度、锐利化、对比度还有灰度。实际测试中一般增加对比度和灰度化后识别效果会更好。

#img = ImageEnhance.Brightness(img).enhance(2.0)#增加亮度

#img = ImageEnhance.Sharpness(img).enhance(17.0)#锐利化

#img = ImageEnhance.Contrast(img).enhance(4.0)#增加对比度

#img = img.convert('L')#灰度化

for bar in bars:
    bar_data=bar.data.decode('utf-8')
    print(bar_data)
    bar_rect=bar.rect#二维码在图片中的像素坐标位置
    print(bar_rect)
