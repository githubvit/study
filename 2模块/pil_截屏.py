from PIL import Image
from PIL import ImageGrab #截屏

im = ImageGrab.grab((360,410,360+255,410+255))# 参数是个元组(左上x,左上y,右上x,右上y),是个矩形框。
# im = ImageGrab.grab() # 参数如果为空，则截取整个屏幕
name='13asfda'
im.save(f'C:\\Users\\69598\\Desktop\\wxqr\\{name}.png')#用f就要用转义符
# im.save(r'C:\Users\69598\Desktop\wxqr\%s.png'%name)