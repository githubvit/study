密码箱 

功能：
    制作密钥
        公钥和私钥
    加密    
        选择要加密的文件 
        选择用于加密的公钥
    解密
        选择要解密的文件 
        选择用于解密的私钥

    退出
        即关闭界面
        也退出系统

场景：
    一般常驻于系统托盘 右击弹出菜单 左击弹出界面
    点退出键 退出系统
    有快捷键唤醒


系统托盘图标
右键菜单
左键界面 

结构：
    加密解密 主逻辑 文件 m_encrypter.py
        1 构建基本结构目录和设定文件存储位置
        2 制作密钥、加密、解密三大核心功能的实现

    主文件 main.py
        # 1 设置窗口关闭 并不退出程序  
        # 默认是True  就会导致关闭界面时退出程序。
        app.setQuitOnLastWindowClosed(False)   # *******  很重要 对于系统托盘应用    ***********

    系统托盘文件 encrypter.py 
        向外发射各种右键信号 通过主文件main 打开相应 view 文件

    主界面 view 文件
        三个按钮链接 三个功能view文件

    制作密钥 view 文件
        链接 到 主逻辑文件的 制作密钥 特定功能
    加密 view 文件
        链接 到 主逻辑文件的 加密 特定功能
    解密 view 文件
        链接 到 主逻辑文件的 解密 特定功能

打包：
    问题：
        开始的打包采用了 依据配置文件打包的方案 分成两部：
            1 先生成配置文件 (一个exe -F 没有console -w小写)
                pyi-makespec -F main.py -w 在当前目录下得到 main.spec

                修改了配置文件，添加了py 和 icon 图片的位置。

            2 根据修改的配置文件 打包
                pyinstaller -F main.spec -w

        产生了 退出时 报 'Failed to execute script encrypter_icon' 即 系统图标文件退出时产生了错误。 
            
            当时给系统图标文件  encrypter_icon.py 
            
                设置 发射退出信号 时 添加 删除图标命令  或 隐藏图标命令等等都没有解决错误。    
            
            接着给app外包了一层，设立了定时器响应事件，等图标删除后，再退出。
            
            解决，尽管解决了，但是如鲠在喉，别扭。

        最终的解决方案如下：
             
             用最简单的打包方式如下，即可，
             
             不用什么依据配置打包，直接一步就解决问题，也不要修改，什么都没动。
            

            
        
    解决：    
        直接在虚拟环境下用：
            pyinstaller -F main.py -w 
                -F 打包成一个.exe文件
                main.py 是入口文件
                -w (w小写)表示没有dos命令,即 = --noconsole

           ' (venv) D:\pyj\st\study\pyside2_pyqt\pys2\mmx>pyinstaller -F main.py -w '

        结果：ok

            什么都没动，没有出现任何问题，退出正常。
    



    

