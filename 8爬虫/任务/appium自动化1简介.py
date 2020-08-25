#  移动端自动化 http://www.python3.vip/doc/tutorial/appium/01/

#  一 appium 简介
#  appium是模仿 selenium web自动化而 打造的 移动端 自动化 框架。
#  类似于 selenium web自动化框架
# +--------------------+    +--------------------+     +---------------+                                                                                                                   
# |   自动化程序      发|--->|   浏览器驱动        |---> |               |                                                                                                  
# | selenium客户端库    |    | 由浏览器厂家提供    |     |     浏览器     |                                                                                           
# |                  收|<---|                    |<--- | edge、chrome等 |                                                                                                 
# +--------------------+    +--------------------+     +---------------+   

#  appium 建立了 移动客户端自动化框架
# +--------------------+    +--------------------+     +---------------+                                                                                                                   
# |   自动化程序      发|--->|   android SDK      |---> |               |                                                                                                  
# | appium客户端库      |    | appium server      |     |  手机、平板    |                                                                                           
# |                  收|<---|   (iOS)XCUITest    |<--- |  等移动客户端  |                                                                                                 
# +--------------------+    +--------------------+     +---------------+  
#  1. 自动化程序
#   使用appium 客户端库 发出自动化指令给手机 。
# 
#  2. Appium Server
#   Appium Server 是 Appium 组织开发的程序，它负责管理手机自动化环境，
#   并且转发 自动化程序的控制指令 给 手机，并且转发 手机给 自动化程序的响应消息。
#   appium 客户端库 和 Appium Server 之间 通过http协议通信。

#   Appium Server会在手机上安装 代理 appium setting
#   自动化程序是通过pc上的Appium Server与手机上的代理appium setting之间的交互，来控制手机的。
#   Appium Server与代理appium setting之间是通过自动化框架来实现自动化控制的。
#   如果测试的是苹果手机，用的是苹果的 XCUITest 框架 （IOS9.3版本以后）
#   如果测试的是安卓手机，用的是安卓的 UIAutomator 框架 (Android4.2以后)
#   这些自动化框架提供了在手机设备上运行的库，可以让程序调用这些库，
#   像人一样自动化操控设备和APP，比如：点击、滑动，模拟各种按键消息等。

#  3. 移动客户端
#   包括所有 苹果、安卓的移动设备，比如：手机、平板、智能手表等。
#   为什么能 接收并且处理自动化指令呢？
#   因为，Appium Server 会在手机上 安装一个 自动化代理程序， 
#   代理程序会等待自动化指令，并且执行自动化指令。
#   其中，自动化代理控制，使用的什么库来实现自动化的呢？
#   如果测试的是苹果手机， 用的是苹果的 XCUITest 框架 （IOS9.3版本以后）
#   如果测试的是安卓手机，用的是安卓的 UIAutomator 框架 (Android4.2以后)
#   这些自动化框架提供了在手机设备上运行的库，可以让程序调用这些库，
#   像人一样自动化操控设备和APP，比如：点击、滑动，模拟各种按键消息等。

# 二 环境搭建：
# 1 安装基于python的 appium客户端 ： 
    # pip install appium-python-client
# 2 安装appium server 
    # Appium Server 是用 nodejs 运行的，基于js开发出来的。
    # Appium组织为了方便大家安装使用，制作了一个可执行程序 Appium Desktop，
    # 把 nodejs 运行环境、Appium Server 和一些工具 打包在里面了，只需要简单的下载安装就可以了。
    # Appium Desktop官方下载： https://github.com/appium/appium-desktop/releases/latest

# 3 安装 Android SDK ：本例主要讲解 安卓APP的自动化，必须要安装安卓SDK，安装在d盘根目录下D:\androidsdk。
    # 3.1 安装 JDK(java 编译器)
        # 安卓SDK需要 java 环境。
        # 安装 java : jdk-8u211-windows-x64.exe
        # 设置Java环境变量：JAVA_HOME 指定 值 为 jdk安装目录

    # 3.2 安装 Android SDK 
        # 安装  androidsdk.zip 解压即可。
        # 设置 Android SDK环境变量：ANDROID_HOME 设置值为sdk包解压目录
        # 把 Android SDK 中 adb 所在目录 。。\androidsdk\platform-tools 添加 到系统环境变量 path中。

# 4 在 cmd 命令行中 输入 adb 命令，看是否成功返回。    
    # 如果手机已经用usb连上电脑，输入 设备查看命令 adb devices -l
    # C:\Users\69598>adb devices -l
    # List of devices attached
    # 4ee7dd3f               device product:z2_row model:ZUK_Z2121 device:z2_row transport_id:2
    # 说明环境的安装和设置都已经做好了

# 三 scrcpy 投屏软件
# 用usb线连接手机
    # 在你运行程序的电脑上 用 USB线 连接上 你的安卓手机
    # 进入 手机设置 -> 关于手机 ，不断点击 版本号 菜单（7次以上），
    # 退出到上级菜单，在开发者模式中，启动USB调试

# 安装
    # 软件：scrcpy-win64-v1.12.1.zip https://github.com/Genymobile/scrcpy/releases
    # 下载解压，将解压目录添加到path环境变量。
# 启动
    # 1 先要把手机开发者模式打开，在开发者模式中要设置允许usb调式模式，一般连接手机客户端都早已经设好。
    # 2 手机用usb连接电脑。
    # 3 命令行中 输入 adb usb
        # C:\Users\69598>adb usb
        # 返回如下：
        # restarting in USB mode


    # 4 输入 scrcpy 则 手机屏幕成功在电脑中出现
        # C:\Users\69598>scrcpy
        # 返回如下：
        # INFO: scrcpy 1.12.1 <https://github.com/Genymobile/scrcpy>
        # D:\scrcpy\scrcpy-win64-v1.12.1\scrcpy-server: 1 file pushed. 1.3 MB/s (26202 bytes in 0.020s)
        # INFO: Initial texture: 1080x1920

# 使用
    # 命令
        # 关闭手机屏幕	    scrcpy -S
        # 限制画面分辨率	scrcpy -m 1024 (比如限制为 1024)
        # 修改视频码率	    scrcpy -b 4M (默认 8Mbps，改成 4Mbps)
        # 裁剪画面	        scrcpy -c 1224:1440:0:0
            # 表示分辨率 1224x1440 并且偏移坐标为 (0,0)
        # 多设备切换	    scrcpy -s 设备ID (使用 adb devices 命令查看设备ID)
        # 窗口置顶	        scrcpy -T
        # 显示触摸点击	    scrcpy -t
            # 在演示或录制教程时，可在画面上对应显示出点击动作
        # 全屏显示	        scrcpy -f
        # 文件传输默认路径	scrcpy --push-target /你的/目录
            # 将文件拖放到 scrcpy 可以传输文件，此命令指定默认保存目录
        # 只读模式(仅显示不控制)    scrcpy -n
        # 屏幕录像	               scrcpy -r 视频文件名.mp4 或 .mkv
        # 屏幕录像 (禁用电脑显示)	scrcpy -Nr 文件名.mkv
        # 设置窗口标题	    scrcpy --window-title '异次元好棒！'
        # 同步传输声音	可借助 USBaudio 这个开源项目实现，但仅支持 Linux 系统

    # 快捷键
        # 看到 Scrcpy 的投屏窗口和手机画面了，你可以直接用鼠标进行操作，它同时也有很多键盘快捷键可以使用。
        # 切换全屏模式	                Ctrl+F
        # 将窗口调整为1：1（完美像素）	 Ctrl+G
        # 调整窗口大小以删除黑色边框	Ctrl+X | 双击黑色背景
        # 设备 HOME 键	Ctrl+H | 鼠标中键
        # 设备 BACK 键	Ctrl+B | 鼠标右键
        # 设备 任务管理 键 (切换APP)	Ctrl+S
        # 设备 菜单 键	Ctrl+M
        # 设备音量+键	Ctrl+↑
        # 设备音量-键	Ctrl+↓
        # 设备电源键	Ctrl+P
        # 点亮手机屏幕	鼠标右键
        # 复制内容到设备	Ctrl+V
        # 启用/禁用 FPS 计数器（stdout）	Ctrl+i
        # 安装APK	将 apk 文件拖入投屏
        # 传输文件到设备	将文件拖入投屏（非apk）