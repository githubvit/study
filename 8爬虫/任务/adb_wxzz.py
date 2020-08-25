import time,datetime
import os
from pyzbar import pyzbar
from PIL import Image
from PIL import ImageGrab #截屏
import uuid

'''
wxzz:微信转账
1 开始 页面：微信 首页
点击 我                    [907,1785][983,1861]

2 进入 管理 页面
点击 支付                   [997,564][1080,715]

3 进入 支付 页面
点击 收付款                 [212,437][350,499]

4 进入收付款 页面        #捕捉不到该页面 报EOF错误
滑动 到最下
点击 向银行卡或手机号转账    

5 进入请选择转账方式 页面
点击 向手机号转账               [216,763][932,974]

6 进入 请填写对方手机号 页面
填写 手机号
确定按钮变色（可点击）
点击 确定

7 进入 转账给  页面
填写 转账金额
点击 添加转账说明

8 弹出 添加转账说明 模态框
填写 转账说明
点击 确定


9 返回 转账给 页面
点击 转账

10 进入 完成 页面
点击 完成

11 进入 微信 页面

完成循环


'''

# def wxzz(price,time_code):
def wxzz(p_num,price,time_code,pwd):
    print('点击 我') #[907,1785][983,1861]
    os.popen('adb shell input tap 941 1832')

    # 一 进入 管理 页面
    time.sleep(1)
    print('点击 支付') #[997,564][1080,715]
    os.popen('adb shell input tap 1022 640')


    # 二 进入支付 页面
    time.sleep(1)
    print('点击 收付款') #[212,437][350,499]
    os.popen('adb shell input tap 282 467')
    
    # 三 进入 收付款 页面 #捕捉不到该页面 报EOF错误
    time.sleep(2)
    print('滑动 到最下') # 盲采
    os.popen('adb shell input swipe 313 820 321 513 ')
    time.sleep(2)
    print('点击 向银行卡或手机号转账') # 以通讯录按钮为参考点 [367,1785][443,1861]
    os.popen('adb shell input tap 543 1786')

    # 四 进入请选择转账方式 页面
    time.sleep(1) 
    print('点击 向手机号转账') # [216,763][932,974]
    os.popen('adb shell input tap 516 773')
    
    # 五 进入 请填写对方手机号 页面
    time.sleep(1) 
    print('填写 手机号')
    os.popen(f'adb shell input text {p_num}')
    time.sleep(1) 
    # 确定按钮变色（可点击）
    print('点击 确定') #[291,1553][788,1661]
    os.popen('adb shell input tap 551 1608')

    # 六 进入 转账给  页面
    time.sleep(2)
    print('填写 转账金额')
    os.popen(f'adb shell input text {price}')
    time.sleep(1)
    print('点击 添加转账说明') #[86,882][314,926]
    os.popen('adb shell input tap 201 904')

    # 七 弹出 添加转账说明 模态框
    time.sleep(1)
    print('填写 转账说明')
    os.popen(f'adb shell input text {time_code}')
    time.sleep(1)
    print('点击 确定') #[541,1093][972,1244]
    os.popen('adb shell input tap 756 1163')



    # 八 返回 转账给 页面
    
    time.sleep(1)
    # 必须点击金额输入框 才能出现转账按钮
    print('点击 金额输入框')#[161,665][962,805]
    os.popen('adb shell input tap 951 725')
    time.sleep(2)
    print('点击 转账') # 大 [815,1464][1058,1898] 小 [772,1464][1015,1898]
    os.popen('adb shell input tap 911 1679')

    # 九 进入 请输入支付密码模态框
    time.sleep(3)
    print('填写 密码')
    os.popen(f'adb shell input text {pwd[0]}')
    time.sleep(1)
    os.popen(f'adb shell input text {pwd[1]}')
    time.sleep(1)
    os.popen(f'adb shell input text {pwd[2]}')
    time.sleep(1)
    os.popen(f'adb shell input text {pwd[3]}')
    time.sleep(1)
    os.popen(f'adb shell input text {pwd[4]}')
    time.sleep(1)
    os.popen(f'adb shell input text {pwd[5]}')

    # 十 进入 完成 页面
    time.sleep(2)
    print('点击 完成') #[291,1559][788,1667]
    os.popen('adb shell input tap 535 1609')


    # 进入 微信 页面
    # 完成循环
    pass

if __name__ == "__main__":
    s_t=time.time()

    p_num='13507983627'
    price=0.01

    time1=datetime.datetime.now()
    y=str(time1.year)
    m=str(time1.month)
    d=str(time1.day)
    h=str(time1.hour)
    mt=str(time1.minute)
    time_code=''.join((y,m,d,h,mt))#年月日小时分钟
    
    pwd='710102'

    wxzz(p_num,price,time_code,pwd)

    d_t=time.time()-s_t

    print(f'转账共耗时:{d_t:.2f}秒')#共耗时:27.11
    pass
