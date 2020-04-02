# 
from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey

# 一 获取包名和启动界面名
#  1 手机上打开西瓜
#  2 pc上命令行输入
    # C:\Users\69598>adb shell dumpsys activity recents | find "intent={"
#  3 查找第一行 找到cmp=包名/启动界面名称
    # intent={act=android.intent.action.MAIN cat=[android.intent.category.LAUNCHER] flg=0x10200000 cmp=com.ss.android.article.video/.activity.SplashActivity}
    # cmp=com.ss.android.article.video/.activity.SplashActivity
desired_caps = {
  'platformName': 'Android', # 平台名称 被测手机是安卓
  'platformVersion': '6', # 平台版本 手机安卓版本
  'deviceName': 'xxx', # 设备名，安卓手机可以随意填写
  'appPackage': 'com.ss.android.article.video', # 启动APP Package名称 打开bili应用
  'appActivity': '.activity.SplashActivity', # 启动Activity名称 启动的界面的名称 因为 安卓应用 可以有多个启动界面
  'unicodeKeyboard': True, # 安装unicodeKeyboard的输入法，便于输入中文，填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App           很重要 *****  否则每次都是刚刚安装打开的状态 数据都没有了
  'newCommandTimeout': 6000, # 客户端 命令的 超时时间
  'automationName' : 'UiAutomator2' 
  # 'app': r'd:\apk\bili.apk',
}

# 生成webdriver对象
# 连接Appium Server，初始化自动化环境 
# 'http://localhost:4723/wd/hub'是固定写法 连接Appium Server
# desired_caps 是 连接的配置信息
wd = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 隐式等待
# 设置缺省等待时间
wd.implicitly_wait(5)

# 二 从appium server获取 要拷贝的json
{
"platformName":"Android",
"platformVersion":"6",
"deviceName":"xxx",
"appPackage":"com.ss.android.article.video",
"appActivity":".activity.SplashActivity",
"unicodeKeyboard":true,
"resetKeyboard":true,
"noReset":true,
"newCommandTimeout":6000,
"automationName":"UiAutomator2"
}