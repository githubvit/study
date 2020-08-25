# 
import time,datetime,random
from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey #键盘输入用
from appium.webdriver.common.touch_action import TouchAction


# 一 打开微信
desired_caps = {
  'platformName': 'Android', # 平台名称 被测手机是安卓
  'platformVersion': '6', # 平台版本 手机安卓版本
  'deviceName': 'gqs123', # 设备名，安卓手机可以随意填写
  'appPackage': 'com.tencent.mm', # 启动APP Package名称 打开bili应用
  'appActivity': '.ui.LauncherUI', # 启动Activity名称 启动的界面的名称 因为 安卓应用 可以有多个启动界面
  'unicodeKeyboard': True, # 安装unicodeKeyboard的输入法，便于输入中文，填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App           很重要 *****  否则每次都是刚刚安装打开的状态 数据都没有了
  'newCommandTimeout': 6000, # 客户端 命令的 超时时间
  'automationName' : 'UiAutomator2'  # 原来是第1代，现在第2代速度快一点。
  # 'app': r'd:\apk\bili.apk',
}
# 微信 cmp=com.tencent.mm/.ui.LauncherUI}
# 数据格式
re_list=[]
re_list_item={
    'day':None,
    'idx':None,
    'uuid':None,
    'num':None,
    'day_sum':None,
    'account_time':None,
    'record_time':None,
}
def re_item_dic(idx,uuid,num,day_sum,account_time):
    day_time=datetime.datetime.now()
    day=f'{day_time.year}-{day_time.month}-{day_time.day}'
    return {'day':day,'idx':idx,'uuid':uuid,'num':num,'day_sum':day_sum,'account_time':account_time,'record_time':time.time(),}

def open_wx():
    # 生成webdriver对象
    # 连接Appium Server，初始化自动化环境 
    # 'http://localhost:4723/wd/hub'是固定写法 连接Appium Server
    # desired_caps 是 连接的配置信息
    wd = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # 隐式等待
    # 设置缺省等待时间
    wd.implicitly_wait(20)

    # 二 操作页面元素
    # 1 检查 微信支付 是否有通知，有通知，就去点击打开
    pay_code='new UiSelector().resourceId("com.tencent.mm:id/bag").text("微信支付")'
    pay=wd.find_element_by_android_uiautomator(pay_code)
    time.sleep(2)
    # 2 微信支付 点击 到达微信支付页面
    pay.click()

    # 随机循环
    while True:
        time.sleep(random.randint(1,20))
        # 找到节点 即 获取 时间条 的父节点  该节点的最上面一行 
        time_line_parent=wd.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/ah"]/..')
        # 获取‘收款到账通知’
        account_notice_node=time_line_parent.find_elements_by_xpath('.//*[@resource-id="com.tencent.mm:id/as3"][@text="收款到账通知"]')
        # 如果是‘收款到账通知’节点
        if account_notice_node:
            # 取值
            # day,idx,uuid,num,day_sum,account_time
            # 汇总行 记录当天的第几笔账 当时到账总金额  是该节点中需要的最下面一行 只要在 则其余要的数据都会在
            idx_row=time_line_parent.find_elements_by_xpath('.//*[@resource-id="com.tencent.mm:id/aq3"][starts-with(@text,"今日第")]')
            # 有汇总行 有最下一行
            if idx_row:
                # 到账时间
                account_time=time_line_parent.find_element_by_xpath('.//*[@resource-id="com.tencent.mm:id/ah"]').get_attribute('text')
                # 该笔金额
                num=time_line_parent.find_element_by_xpath('.//*[@resource-id="com.tencent.mm:id/as_"]').get_attribute('text')
                # 备注
                uuid=time_line_parent.find_element_by_xpath('.//*[@resource-id="com.tencent.mm:id/aq3"][starts-with(@text,"uuid")]').get_attribute('text')
                # 取汇总行数据
                idx_text=idx_row[0].get_attribute('text')
                print(account_time,num,uuid,idx_text)
                # 第几笔账
                idx=int(idx_text.split('第')[1][0])
                # 当天当时的总金额
                day_sum=idx_text.split('￥')[1]
                
                # 数据节点
                data_dic=re_item_dic(idx,uuid,num,day_sum,account_time)
                # 加入数据列表
                re_list.append(data_dic)

                print(re_list)
                
            
       

        
    # 3 我的账单 点击 展开上拉菜单
    # aqu_code='new UiSelector().resourceId("com.tencent.mm:id/aqu").text("我的账单")'
    # aqu=wd.find_element_by_android_uiautomator(aqu_code).click()
    # time.sleep(2)
    # # 4 进入账单 点击 到达 账单页面
    # go_aqu_code='new UiSelector().text("进入账单").className("android.widget.TextView")'
    # go_aqu=wd.find_element_by_android_uiautomator(go_aqu_code).click()


open_wx()