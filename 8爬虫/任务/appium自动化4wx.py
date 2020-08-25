# 该款机器人 由于 频繁操作 被识别为机器人 不让刷新数据
import time,random
from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey #键盘输入用
from appium.webdriver.common.touch_action import TouchAction


# 一 打开微信
desired_caps = {
  'platformName': 'Android', # 平台名称 被测手机是安卓
  'platformVersion': '6', # 平台版本 手机安卓版本
  'deviceName': 'agq123', # 设备名，安卓手机可以随意填写
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

# 生成webdriver对象
# 连接Appium Server，初始化自动化环境 
# 'http://localhost:4723/wd/hub'是固定写法 连接Appium Server
# desired_caps 是 连接的配置信息
wd = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 隐式等待
# 设置缺省等待时间
wd.implicitly_wait(20)

# 1  点击 我 到达 管理中心
# ui automator viewer 与 appium不能同时运行
# me_code='new UiSelector().resourceId("com.tencent.mm:id/ta")'
# me=wd.find_elements_by_android_uiautomator(me_code).click()

# 二 操作页面元素
# 2 微信支付 点击 到达微信支付页面
pay_code='new UiSelector().resourceId("com.tencent.mm:id/bag").text("微信支付")'
pay=wd.find_element_by_android_uiautomator(pay_code).click()



# 建立列表
data_list=[]
cnt=0
# 三 页面监听 注意 频繁操作会被封 因此每5秒下拉就不会刷新
# 循环监听，每5秒 下拉 刷新，对比新旧数据，
while True:
  cnt+=1
  start_time=time.time()
  time.sleep(2)
  # 在微信支付页面
  # 3 我的账单 点击 展开上拉菜单
  aqu_code='new UiSelector().resourceId("com.tencent.mm:id/aqu").text("我的账单")'
  aqu=wd.find_element_by_android_uiautomator(aqu_code).click()
  time.sleep(2)
  # 4 进入账单 点击 到达 账单页面
  go_aqu_code='new UiSelector().text("进入账单").className("android.widget.TextView")'
  go_aqu=wd.find_element_by_android_uiautomator(go_aqu_code).click()
  t1=random.randint(20,50)
  # 5.1 随机等待10秒以下 获取数据列表
  time.sleep(t1) # 考虑协程 提高pc效率 切换到另一个微信的操作 比如 客服 等。。。
  # 获取列表页节点
  list_node=wd.find_elements_by_xpath('//*[@resource-id="fastlist"]/*[position()>1]')
  # print(list_node)
  # 取数据
  # 要在某个元素内部使用xpath选择元素， 需要 在xpath表达式最前面加个点 。
  for item in list_node:
     # 5.2 循环该页数据 
  
 
    user_num_node=item.find_elements_by_xpath('.//*[starts-with(@text,"二维码收款-来自")]')
    time_data_node=item.find_elements_by_xpath('.//*[contains(@text,"月")][contains(@text,"日")]')
    if user_num_node:
      user_num_text=user_num_node[0].get_attribute('name')
      time_data_text=time_data_node[0].get_attribute('name')
      print('---------------------------------------------------------------------------')
      
      # 如果有新数据 
      if (user_num_text,time_data_text) not in data_list:
        print(user_num_text,time_data_text)
      
        # 取出新数据，存储到列表。
        data_list.append((user_num_text,time_data_text))
        # 5.3 点击该行，进入账单详情页

        # 6 取详情页数据
        # 6.1 取出备注 

        # 6.2 返回账单页面 继续监听
        # 用 手机操作 的 发送键到设备 的 返回键 返回到 账单列表页
        # wd.press_keycode(4)  # 返回键
      

  # print(data_list)
  t2=random.randint(2,5)
  time.sleep(t2)

  # 下拉刷新 按下 向下移动 抬起
  
  # 这一段下拉并不能刷新，原因可能在于：微信识别出这是机器人，因此没有刷新数据。
  # parent_node=wd.find_element_by_android_uiautomator('new UiSelector().resourceId("fastlist")')
  # p_la=parent_node.location
  # p_sz=parent_node.size

  # s_x=p_la['x']+(p_sz['width']/2)
  # s_y=p_la['y']+10
  # e_x=s_x
  # e_y=s_y+(p_sz['height']*2/3)
  # # t_action=TouchAction(wd).press(list_node[0]).move_to(list_node[1]).release().perform()
  # wd.swipe(s_x,s_y,e_x,e_y,duration=800)

  # 改用 返回 上一页 在进入的步骤 看数据是否刷新
  wd.press_keycode(4)
  end_time=time.time()
  print(f'第{cnt}次循环共耗时{end_time-start_time}')

  t3=random.randint(50,100)
  time.sleep(t3)
  print(f'在微信支付页面共呆了{t3}秒')



# 用input让程序停在这儿，然后按任意键退出
input('**** Press to quit..')
wd.quit()


# 二 微信json
# 将配置desired_caps转为json格式(双引号""和逗号','):
{
  "platformName": "Android",
  "platformVersion": "6",
  "deviceName": "xxx",
  "appPackage": "com.tencent.mm",
  "appActivity": ".ui.LauncherUI",
  "unicodeKeyboard": true,
  "resetKeyboard": true,
  "noReset": true,
  "newCommandTimeout": 6000,
  "automationName": "UiAutomator2"
}

# 点击appium server 的inspect放大镜图标，代替应用程序客户端，启动微信。
# 用这个 可以 代替 uiautomatorviewer来捕捉节点元素。

