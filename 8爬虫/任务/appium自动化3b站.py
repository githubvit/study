# 同上例，可以不断上滑，更新列表，打印title。

from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey # 键盘输入
import time
desired_caps = {
  'platformName': 'Android', # 平台名称 被测手机是安卓
  'platformVersion': '6', # 平台版本 手机安卓版本
  'deviceName': 'xxx', # 设备名，安卓手机可以随意填写
  'appPackage': 'tv.danmaku.bili', # 启动APP Package名称 打开bili应用
  'appActivity': '.ui.splash.SplashActivity', # 启动Activity名称 启动的界面的名称 因为 安卓应用 可以有多个启动界面
  'unicodeKeyboard': True, # 安装unicodeKeyboard的输入法，便于输入中文，填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App           很重要 *****  否则每次都是刚刚安装打开的状态 数据都没有了
  'newCommandTimeout': 6000, # 客户端 命令连接的 超时时间
  'automationName' : 'UiAutomator2' 
  # 'app': r'd:\apk\bili.apk',
}

# 生成webdriver对象，用http协议连接Appium Server，初始化自动化环境 
# 'http://localhost:4723/wd/hub'是固定写法 连接Appium Server 是Appium Server服务监听的地址和端口
# desired_caps 是 连接的配置信息
wd = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# webdriver对象带上desired_caps信息用http协议连接appium服务器。

# 隐式等待
# 设置缺省等待时间
wd.implicitly_wait(5)


# bili启动 界面通知
# 如果有`青少年保护`界面，点击`我知道了` 用find_elements，没有不会报错，所以下面iknow是列表。
# iknow = wd.find_elements_by_
# id("text3")
# 用find_elements_by_android_uiautomator直接获取元素 不用 appserver 翻译
iknow = wd.find_elements_by_android_uiautomator('new UiSelector().resourceId("tv.danmaku.bili:id/text3")')
if iknow:
    iknow[0].click()

# 在搜索框点击 到达搜索页
# 根据id定位搜索位置框，点击
# wd.find_element_by_id("expand_search").click()
# 直接法中resourceId必须写全名
wd.find_element_by_android_uiautomator(
    'new UiSelector().resourceId("tv.danmaku.bili:id/expand_search")'
).click()


# 在搜索页的搜索框中输入关键字 并 回车
# 根据id定位搜索输入框，点击
# sbox = wd.find_element_by_id('search_src_text')
# 根据 元素的content-desc 内容描述 定位 by_accessibility_id
# sbox = wd.find_element_by_accessibility_id('搜索查询')
# 用直接获取的api 是 description
sbox = wd.find_element_by_android_uiautomator('new UiSelector().description("搜索查询")')
sbox.send_keys('白月黑羽')
# 输入回车键，确定搜索
wd.press_keycode(AndroidKey.ENTER)

# 进入搜索结果页
# 
# 1 获取节点的大小和坐标
ls_code='new UiSelector().resourceId("tv.danmaku.bili:id/pager")'
ls_node=wd.find_element_by_android_uiautomator(ls_code)
# print(ls_node.location)
# {'x': 0, 'y': 318}
# print(ls_node.size)
# {'height': 1602, 'width': 1080}
# 2 建立所有元素.text列表 和 初始上滑计数器 
all_ls=[]
swipe_n=len(all_ls) # 用 所有元素列表的元素个数来计算
s_x=ls_node.location['x']+10
s_y=ls_node.size['height']-10
e_x=s_x
e_y=s_y-ls_node.size['height']/2
print('滑动的坐标',s_x,s_y,e_x,e_y)
# 3 循环上滑 获取元素 加入 所有元素列表
while True:
    time.sleep(1) # 等待元素加载完毕

    swipe_1=len(all_ls) # 节点循环前 所有元素列表长度

    # 获取当前页节点中的元素列表
    eles = wd.find_elements_by_android_uiautomator('new UiSelector().resourceId("tv.danmaku.bili:id/title")')
    # 循环当前页节点列表 
        # 如果该节点不在所有元素列表中就放入列表 并打印title
    for ele in eles:
        if ele.text not in all_ls: #不能用 ele not in all_ls这个判断，
            all_ls.append(ele.text)
            # 打印标题 
            print('------------------------------------')
            print(ele.text)
    swipe_2=len(all_ls) # 节点循环后 所有元素列表长度

    # print('循环前前元素列表个数',swipe_1)
    # print('循环后前元素列表个数',swipe_2)
    if swipe_1==swipe_2:
        print(f'当前已取完所有元素{swipe_2}，退出上滑')
        break

    # 上滑 尽量减少惯性
    wd.swipe(s_x,s_y,e_x,e_y,duration=2000) #这个可以抓全 38个
    # wd.drag_and_drop(eles[-1],eles[-3]) #这个只能抓到 18个 20个 就是抓不全
 

# 用input让程序停在这儿，然后按任意键退出
input('**** Press to quit..')
wd.quit()




# 一 滑动有三种
# 1 swipe   滑动 有惯性
# 从一个位置滑动到另一个位置
# driver.swipe(start_x,start_y,end_x,end_y,duration=None) #duration 滑动持续时间 即滑动快慢
# 上滑

# wd.swipe(100,1600,100,600)

# 上滑会有误差 duration 越长 惯性越小。

# 2 scroll  滚动 惯性大
# 从一个元素滚动到另一个元素，直到页面自动停止.
# driver.scroll(开始的元素origin_el，结束的元素destination_el，duration=None) 、
# wd.scroll()


# 3 drag and drop  拖拽 无惯性 没有时间参数
# 从一个元素滑动到另一个元素，第二个元素替代第一个元素屏幕上的位置。
# driver.drag_and_drop(开始的元素origin_el，结束的元素destination_el)
# wd.drag_and_drop()

# 二 TouchAction 高级手势 
# from appium.webdriver.common.touch_action import TouchAction

# 可以实现一些针对手势的操作，比如滑动、长按、拖动等。
# 我们可以将这些基本手势组合成一个相对复杂的手势，完成解锁手机或应用软件的方式。

# 比如滑动屏幕：可以分解为 按下 移动 抬起 三个基本手势


# 使用步骤
    # 1 创建TouchAction对象
    # 2 通过对象调用手势
    # 3 通过perform()执行动作  ******

# 类似于 selenium 的 ActionChains

# 基本手势
# 1 轻敲 
    # TouchAction(driver).tap(el或x,y,count=1).perform()
    # tap的参数是
        # 要点击的el元素(el)
        # 或位置坐标(x=123,y=456)。 坐标必须用指定参数，不能（123,456）
        # count代表点击次数，比如单击、双击、三击、...。


# 2 按下
    # TouchAction(driver).press(el或x,y).perform()
    # press的参数是
        # 要点击的el元素(el)
        # 或位置坐标(x=123,y=456)。 坐标必须用指定参数，不能（123,456）
        

# 3 抬起
    # TouchAction(driver).press(el或x,y).release().perform()
    # 按下和抬起的组合可以完成tap轻敲。

    # TouchAction(driver).press(x=650,y=650).perform()
    # time.sleep(2)
    # TouchAction(driver).press(x=650,y=650).release().perform() #先按下接着释放 模拟点击

# 4 等待
    # TouchAction(driver).wait(ms=0).perform() 
    # wait参数是毫秒
    # TouchAction(driver).press(x=650,y=650).wait(2000).release().perform() #先按下 等待2秒 接着释放 模拟长按

# 5 长按
    # TouchAction(driver).long_press(el或x,y,duration=1000).perform()
    # long_press的参数是
        # 要点击的el元素(el)
        # 或位置坐标(x=123,y=456)。 坐标必须用指定参数，不能（123,456）
        # duration表示按住的时间 单位毫秒。
    # TouchAction(driver).long_press(x=650,y=650,duration=2000).perform() # 和 4 等待 中的示例一样

# 6 移动
    # TouchAction(driver).move_to(el或x,y).perform()
    # move_to的参数是
        # 要点击的el元素(el)
        # 或位置坐标(x=123,y=456)。 坐标必须用指定参数，不能（123,456）

# 移动端的每个页面都是有名称的，有些页面不用一步步点进去，可以让启动页面直接就是你要的页面。
        
# 三 手机操作
# 1 获取手机分辨率
# driver.get_window_size()
# print('分辨率',wd.get_window_size()) 
# print('矩形rect',wd.get_window_rect())
# 分辨率 {'width': 1080, 'height': 1920}
# 矩形rect {'width': 1080, 'height': 1920, 'x': 0, 'y': 0}

# 2 获取手机截图
# filename=r'D:\pyj\st\study\8爬虫\任务\test.png'
# img=wd.get_screenshot_as_file(filename)

# 3 获取和设置网络状态
# print('网络类型',wd.network_connection) # 网络类型 6,返回数字 ，按下面数字 网络类型对照表 就可以看出是什么网络
# 获取当前手机网络类型:有(0 None)(1 Airplone Mode)(2 Wifi only)(4 Data only)(6 All network on)
# None 表示无网络 
# Airplone Mode 表示飞行模式 
# Wifi only 表示打开wifi 
# Data only 表示打开流量  
# All network on 表示WiFi和data都开着

# 设置网络类型
# wd.set_network_connection(connection_type=1) #设置网络类型为 Airplone Mode 飞行模式 

# 4 发送键到设备（拨号键、音量键、返回键、home键。。。）
# driver.press_keycode(keycode,metastate=None)
# wd.press_keycode(24) # 音量+
# wd.press_keycode(25) # 音量-
# wd.press_keycode(4)  # 返回键
# wd.press_keycode(3)  # Home键
# wd.press_keycode(5)  # 拨号键
# wd.press_keycode(6)  # 挂机键
# wd.press_keycode(27) # 拍照键
# wd.press_keycode(82) # 菜单键
# wd.press_keycode(26) # 电源键
# wd.press_keycode(66) # 回车键
# wd.press_keycode(111) # Esc键

# 按键对应的编码，可以在百度搜索关键字"android keycode"
# 如 Android KEYCODE键值对应大全  https://blog.csdn.net/midux/article/details/80064054
# 如 Android下添加新的自定义键值和按键处理流程 https://blog.csdn.net/tkwxty/article/details/43338921

# 5 操作手机通知栏
    # driver.open_notifications() # 打开手机通知栏
    # 关闭通知栏 向上滑动 或 按返回键
    # driver.press_keycode(4) #用返回键 关闭通知栏
# wd.open_notifications() # 拉下手机通知栏
# time.sleep(5)
# wd.press_keycode(4) # 关闭通知栏

