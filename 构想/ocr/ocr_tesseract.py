from PIL import Image
import pytesseract as pyt

path=r'D:\pyj\st\study\8爬虫\任务\test.png'
img=Image.open(path)
#二值化图像传入图像和阈值
'''
图像二值化（ Image Binarization）就是将图像上的像素点的灰度值设置为0或255，
也就是将整个图像呈现出明显的黑白效果的过程。

在数字图像处理中，二值图像占有非常重要的地位，图像的二值化使图像中数据量大为减少，
从而能凸显出目标的轮廓。

阈值: 自定义灰度界限，大于这个值为黑色，小于这个值为白色

'''
def erzhihua(image,threshold):
    # 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
    image=image.convert('L')
    table=[]
    for i in range(256):
      if i < threshold:
        table.append(0)
      else:
        table.append(1)
    return image.point(table,'1')
 
image=erzhihua(img,127)
image.show()
t=pyt.image_to_string(image,lang='chi_sim+eng')
print(t)