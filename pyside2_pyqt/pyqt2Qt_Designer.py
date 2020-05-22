# 用QT界面生成器 Qt Designer （QT 设计师 ），拖拖拽拽就可以直观的创建出程序大体的界面。

# 怎么运行这个工具呢？

# Windows下，运行在Python安装目录下 Lib\site-packages\PySide2\designer.exe 这个可执行文件

# QT 设计师 位置：D:\pyj\st\venv\Lib\site-packages\PySide2

# 对界面控件进行布局，白月黑羽的经验是 按照如下步骤操作

    # 先不使用任何Layout，把所有控件 按位置 摆放在界面上
    
    # 然后先从 最内层开始 进行控件的 Layout 设定
    
    # 逐步拓展到外层 进行控件的 Layout设定
    
    # 最后调整 layout中控件的大小比例， 优先使用 Layout的 layoutStrentch 属性来控制