from PIL import Image
from PIL import ImageGrab #截屏

# 1 截取电脑屏幕
def one():
    im = ImageGrab.grab((360,410,360+255,410+255))# 参数是个元组(左上x,左上y,右上x,右上y),是个矩形框。
    # im = ImageGrab.grab() # 参数如果为空，则截取整个屏幕
    name='13asfda'
    im.save(f'C:\\Users\\69598\\Desktop\\wxqr\\{name}.png')#用f就要用转义符
    # im.save(r'C:\Users\69598\Desktop\wxqr\%s.png'%name)
# one()

# 2 图片处理 获取特定坐标点的像素
def two():
    # img=Image.open(r'D:\pyj\st\study\8爬虫\任务\test.png')
    # img=Image.open(r'C:\Users\69598\Desktop\uix\db\dump_1109333730231979582.png')
    img=Image.open(r'C:\Users\69598\Desktop\uix\db\dump_1472681437498865820.png')
    # print(img.size)
    # 特定坐标点(x,y)
    coordinate_points=[(89,226),
    (412,226),(440,226),(468,226),(490,229),(515,228),(523,226),(558,238),(573,226),(603,226),
    (342,280),(355,280),(389,280),
    (101,328+24),(101,403+24),(101,454+28),(101,590+28),
    (101,765),(494,765),(537,774),(552,766),(574,768),(591,769),
    (101,885+24),
    (458,1001+24),(458+19,1001+24),(458+19+19,1001+24),
    (101,1244+24),
    (412,226+1042),(440,226+1042),(468,226+1042),(490,229+1042),(515,228+1042),(523,226+1042),(558,238+1042),(573,226+1042),(603,226+1042),
    (342,280+1042),(355,280+1042),(389,280+1042),
    (101,1370+24),(101,1445+24),(101,1660),
    ]
    pixel=[]
    for i,v in enumerate(coordinate_points):
        print(i,img.load()[v][:3])
        pixel.append(img.load()[v][:3])#只取前 3 位 rgb
    # print(pixel)
two()