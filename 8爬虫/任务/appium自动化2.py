# 使用 Appium 自动化的打开 B站 应用，搜索 白月黑羽 发布的教程视频，并且打印视频标题的示例。

from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey

desired_caps = {
  'platformName': 'Android', # 平台名称 被测手机是安卓
  'platformVersion': '6', # 平台版本 手机安卓版本
  'deviceName': 'xxx', # 设备名，安卓手机可以随意填写
  'appPackage': 'tv.danmaku.bili', # 启动APP Package名称 打开bili应用
  'appActivity': '.ui.splash.SplashActivity', # 启动Activity名称 启动的界面的名称 因为 安卓应用 可以有多个启动界面
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


# bili启动 界面通知
# 如果有`青少年保护`界面，点击`我知道了`
iknow = wd.find_elements_by_id("text3")
if iknow:
    iknow.click()

# 在搜索框点击 到达搜索页
# 根据id定位搜索位置框，点击
wd.find_element_by_id("expand_search").click()

# 在搜索页的搜索框中输入关键字 并 回车
# 根据id定位搜索输入框，点击
sbox = wd.find_element_by_id('search_src_text')
sbox.send_keys('白月黑羽')
# 输入回车键，确定搜索
wd.press_keycode(AndroidKey.ENTER)

# 在后台打印 视频标题
# 选择（定位）所有视频标题
eles = wd.find_elements_by_id("title")

for ele in eles:
    # 打印标题
    print(ele.text)

# 用input让程序停在这儿，然后按任意键退出
input('**** Press to quit..')
wd.quit()

# 1 先要在电脑启动 Appium server 
    # 双击桌面的Appium 图标 点击 start Appium Server 得到如下：
    # [Appium] Appium REST http interface listener started on 0.0.0.0:4723
    # 说明 Appium server 已准备好。

    # 执行程序时 会在 手机 上 新建 一个Appium Settings 的图标。

    # Appium Server上的反应
    # [HTTP] --> POST /wd/hub/session
    # [HTTP] {"capabilities":
    # {"firstMatch":[
        # {"platformName":"Android",
        # "appium:platformVersion":"6",
        # "appium:deviceName":"xxx",
        # "appium:appPackage":"tv.danmaku.bili",
        # "appium:appActivity":".ui.splash.SplashActivity",
        # "appium:unicodeKeyboard":true,
        # "appium:resetKeyboard":true,
        # "appium:noReset":true,
        # "appium:newCommandTimeout":6000,
        # "appium:automationName":"UiAutomator2"}
    # ]},
    # "desiredCapabilities":{
        # "platformName":"Android",
        # "platformVersion":"6",
        # "deviceName":"xxx",
        # "appPackage":"tv.danmaku.bili",
        # "appActivity":".ui.splash.SplashActivity",
        # "unicodeKeyboard":true,
        # "resetKeyboard":true,
        # "noReset":true,
        # "newCommandTimeout":6000,
        # "automationName":"UiAutomator2"}}

    # [Appium] Appium v1.15.1 creating new AndroidUiautomator2Driver (v1.37.2) session
    # [BaseDriver] W3C capabilities and MJSONWP desired capabilities were provided
    # [BaseDriver] Creating session with W3C capabilities: {
    # [BaseDriver]   "alwaysMatch": {
    # [BaseDriver]     "platformName": "Android",
    # [BaseDriver]     "appium:platformVersion": "6",
    # [BaseDriver]     "appium:deviceName": "xxx",
    # [BaseDriver]     "appium:appPackage": "tv.danmaku.bili",
    # [BaseDriver]     "appium:appActivity": ".ui.splash.SplashActivity",
    # [BaseDriver]     "appium:unicodeKeyboard": true,
    # [BaseDriver]     "appium:resetKeyboard": true,
    # [BaseDriver]     "appium:noReset": true,
    # [BaseDriver]     "appium:newCommandTimeout": 6000,
    # [BaseDriver]     "appium:automationName": "UiAutomator2"
    # [BaseDriver]   },
    # [BaseDriver]   "firstMatch": [
    # [BaseDriver]     {}
    # [BaseDriver]   ]
    # [BaseDriver] }
    # [BaseDriver] Session created with session id: 2d9f3c56-87dd-4c5f-86e5-7401c71b8925
    # [UiAutomator2] Starting 'tv.danmaku.bili' directly on the device

# 2 如何查看要打开的应用程序的(package名称)包名和启动的界面名称？
    # "appPackage":"tv.danmaku.bili",
    # "appActivity":".ui.splash.SplashActivity",
    # 有两个方法
    # 方法一 dumpsys activity recents 返回最近的活动 命令 
        # 1 在手机上打开要测试的app 比如 哔哩哔哩
        # 2 紧接着在电脑上输入 adb shell dumpsys activity recents | find "intent={"
            # 得到的反馈：取第一条
            # C:\Users\69598>adb shell dumpsys activity recents | find "intent={"
            # intent={act=android.intent.action.MAIN cat=[android.intent.category.LAUNCHER] flg=0x10200000 cmp=tv.danmaku.bili/.ui.splash.SplashActivity}
            # intent={act=android.intent.action.MAIN cat=[android.intent.category.HOME] flg=0x10000000 cmp=com.zui.launcher/.Launcher}
            # intent={act=android.intent.action.MAIN cat=[android.intent.category.LAUNCHER] flg=0x10a00000 cmp=io.appium.settings/.Settings}
            # 。。。
            # 取第一个就是，找到 cmp=tv.danmaku.bili/.ui.splash.SplashActivity，前面是包名package名称 ，后面是 启动界面 名称。
    # 方法二 如果有安装包，就用Android SDK中的aapt命令 'aapt.exe dump badging 安装包路径' 来获取包名和启动界面名称
        # 包名：
            # 命令行中。。。\androidsdk\build-tools\29.0.3\aapt.exe dump badging 安装包路径 | find "package: name="
        # 启动界面：
            # 把find "package: name=" 改成 find "launchable-activity" 即可。
            
# 3 定位元素
    # Appium是基于Selenium的，所以 和 Selenium 代码 定位元素的 基本规则相同：
        # find_element_by_XXX 方法，返回符合条件的第一个元素，找不到抛出异常
        # find_elements_by_XXX 方法，返回符合条件的所有元素的列表，找不到返回空列表
        # 通过 WebDriver 对象调用这样的方法，查找范围是整个界面
        # 通过 WebElement 对象调用这样的方法，查找范围是该节点的子节点

    # 不同于 selenium web自动化 这里的 find_element_by_id 并不一定唯一。
    
# 4 界面元素查看工具
    # Selenium Web 自动化的时候，要找到元素，
        # 我们是通过按F12 打开浏览器的 开发者工具栏来查看元素的特性，根据这些特性（属性和位置），来定位元素
    # Appium 移动端 常用的查看工具有两种： 
        # Android Sdk包中的 uiautomatorviewer：automator机器人
            # 它在SDK目录目录 的 tools\bin 目录中
            # 双击打开，点击 uiautomatorviewer dump 得到 当前手机的界面
            # 移动鼠标 ，会有虚线红框变化，右侧属性列表会变化，是自由态。
            # 点击选中，红框变实线。此时，再移动鼠标，右侧属性列表不会变化。是固定态。
            # 再次点击选中的界面元素，就释放了固定状态，回到了自由态。
            # 右上是类似html 节点树
            # 右下侧属性列表：Node Detail 节点详情
                # index:2   当前父节点中的第2个子节点
                # text      当前元素的文本 空
                # redource-id:tv.danmaku.bili:id/expand_search  这是find_element_by_id选择的id。
                # class:android.widget.TextView 当前标签的类型TextView，类似于web中的标签名
                # package:tv.danmaku.bili  当前元素所属包名
                # content-desc 当前元素的内容描述 空
                # checkable:false 是可选择吗 不可选择
                # checked：false 是被选中吗 不
                # clickable:true 是可点击吗 可以
                # enable:true 是可用吗 是
                # focusable:false 是可输入聚焦的吗 不
                # focused:false 输入聚焦了吗 不
                # scrollable:false 是可以滚动的吗 不
                # long-clickable:false 有常按状态吗 没
                # password:false 是加密的吗 不
                # selected:false 是选中的吗 不
                # bounds:[192,99][642,189] 边界 元素在界面的矩形范围 [左上] [右下]

            # 常用的属性选择是index、text、redource-id、class，还有bounds。
       
        # Appium server 中的 Appium Inspector：
            # 打开Appium server
            # 运行自动化应用程序，
            # 在Appium server界面复制"desiredCapabilities"中的配置，放在vscode中。
                # 该配置就是 代码当中的配置项，只不过是转为了json格式，便于下面应用。
            # 关闭应用程序。

            # 点击 App server 中右边的搜索图标 放大镜。
            # 在右下角的JSON Representation中，点击编辑按钮 笔。
            # 把复制的"desiredCapabilities"黏贴到该json中，并点击保存。
            # 这时右边应该会展示出多行与json中一致的配置项表格。
            # 点击右下角的start session开始会话按钮。
            # 点击隔壁的save as 可以把当前配置保存下来。下次从save capabilities sets按钮直接调用即可。

            # appium server会在手机中打开哔哩app。
            # 并把手机打开的界面传输到app server中，同时打开html和属性列表，打开了调式窗口，
            # 属性列表和 上面uiautomatorviewer是一样的。
            
            # 特点：
                # 展开html,可以看到节点树上有id,这就比 uiautomatorviewer节点树要直观。
                    # 可以看到id之间的关系，比较容易选择。
                # 最大的优势，在于有节点搜索功能 search for element 放大镜。
                    # 可以输入id或其他属性 看到找到的节点的数量，并可以点击看是不是要找的。
                # 手机页面变化，只用点击刷新按钮即可。
            