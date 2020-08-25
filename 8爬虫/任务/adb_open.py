import time
import os
from pyzbar import pyzbar
from PIL import Image
from PIL import ImageGrab #截屏
import uuid

'''
非常稳定
前期准备：
1 用人工方式操作->获取流程，
    1.1 在二维码收款页面 
        1.1.1 点击 设置金额

    1.2 进入设置页面
        1.2.1 输入 金额 price
        1.2.2 点击 备注

    1.3 进入 备注页 模态框
        1.3.1 输入 备注信息 uuid
        1.3.2 点击 确定

    1.4 回到设置页面
        1.4.1 点击 设置页面 确定

    1.5 进入 有二维码收款码结果 的 二维码收款页面 
        1.5.1 用pillow截图获取结果
        1.5.2 保存到指定位置
        1.5.3 点击 清除金额  回到1.1  至此 走完一个循环

2 用uiautomatorviewer工具->获取 操作 坐标点（在AndroidSdk目录下 的 tools\bin 目录中uiautomatorviewer.bat即automator机器人）
    2.1 将手机页面人工设置在初始页面：二维码收款页面   
           
    2.2 打开 uiautomatorviewer工具：抓取初始页面

    2.3 开始 按流程 操作 ：在操作前，记录每步流程中要操作元素的坐标位置 

3 根据流程和记录的坐标，编写脚本。

4 合理执行脚本。
    比如 循环多少次
    给定参数等，达到预期。

'''

# 关于automator机器人 uiautomatorviewer.bat
#     双击这个bat打开程序。
#     启动后有四个按钮
#     第一个按钮 打开已保存的布局
#     第四个按钮 点击保存，将存储两个文件，一个是图片文件，一个是.uix文件（XML布局结构）
#     第二按钮（Device Screenshoot uiautomator dump）截屏 布局区呈现完整布局
#     第三按钮（Device Screenshoot with Compressed Hierarchy uiautomator dump –compressed）截屏 布局区呈现压缩后的布局 
#     第二第三个按钮的区别在于，第二按钮把全部布局呈现出来，而第三按钮只呈现有用的控件布局。
#     比如某一 Frame存在，但只有装饰功能，那么点击第三按钮时，可能不被呈现。

def get_qr(price,uuid,i):
    print(f'当前是第{i}个')
    # print(f"当前uuid:{uuid}" )

    # 一 在二维码收款页面 点击设置金额
    # print('点击设置金额') # 该点坐标 [306,1082][458,1134]
    os.popen('adb shell input tap 370 1100')

    # 二 进入设置页面
    time.sleep(1)
    # 1 输入金额price #手机输入法 要设为 Unicode IME，一般 scrcpy会自动设置，如果没有自动设置就手动改即可。
    # print(f"设置金额{price}")
    # 只有一个输入框
    os.popen(f'adb shell input text {price}')
    # 要停一下 不然0.01有可能会被输入到备注栏
    # print('输入完金额要停一下，避免把金额输入到备注栏')
    time.sleep(1)

    # 2 点击备注
    # print('点击备注')#该点坐标 [122,591][332,632]
    os.popen('adb shell input tap 220 610')

    time.sleep(1)
    # 三 进入备注页 模态框
    # 1 键入备注信息
    # print('键入备注信息')
    os.popen(f"adb shell input text {uuid}" )
    time.sleep(1)

    # 2 点击确定 坐标[541,1093][972,1244]
    # print('点击备注模态框确定')
    os.popen('adb shell input tap 750 1160')

    # 四 回到设置页面
    time.sleep(1)
    # 1 再此点击 设置页面 确定
    # print('再此点击设置页面确定') # [122,713][958,843] [122,713][958,843]
    os.popen("adb shell input tap 591 772")

    time.sleep(2)
    # 五 进入 二维码收款码 页面
    # 1 获取结果截图
    # 用pillow截图获取结果 电脑屏幕坐标 左上（425,305) 右下 (680,560)
    # print('截图')
    im=ImageGrab.grab((220,415,220+255,415+255))#每次使用，都要量一下这里的尺寸。因为是截scrcpy投屏到pc的图。

    # 2 保存到指定位置
    # print('保存')
    im.save(f'C:\\Users\\69598\\Desktop\\wxqr\\{uuid}.png')
    time.sleep(1)

    # 3 点击清除金额 回到 初始页面
    # print("点击清除金额") #[306,1275][458,1327]
    os.popen("adb shell input tap 388 1291")
    time.sleep(1)
    
if __name__ == '__main__':
    s_time=time.time()
    for i in range(1,10):
        # 生成uuid
        uid=str(uuid.uuid4())
        # 去掉uuid中的'-'号
        suid='uuid'+''.join(uid.split('-'))
        # 生成二维码
        get_qr(0.01,suid,i) #生成的二维码要用pyzbar读取信息，再用qrcode 把 信息 重新生成二维码 这样可以精简大小。未精简前一个有20kB多一点。
    e_time=time.time()
    h_time=e_time-s_time
    print(f'共耗时{h_time:.2f}秒,每个耗时{h_time/9:.2f}',)
