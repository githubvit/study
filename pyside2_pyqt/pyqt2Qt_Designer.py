# 用QT界面生成器 Qt Designer （QT 设计师 ），拖拖拽拽就可以直观的创建出程序大体的界面。

# 1 怎么运行 Qt Designer 这个工具呢？

    # Windows下，运行在Python安装目录下 Lib\site-packages\PySide2\designer.exe 这个可执行文件

    # QT 设计师 位置：D:\pyj\st\venv\Lib\site-packages\PySide2
    # QT 设计师 的 .ui文件和资源文件 .rcc 转换成py文件的工具在：
        # pyqt5用的命令行转换工具
            # D:\pyj\st\venv\Scripts\pyuic5.exe 
                # pyuic5 要转的ui文件名（全路径） -o 转成的py文件名（全路径）-x 
                # 加-x表示可以带 
                # -if __name__ == "__main__":
                #     pass
                # 可执行 
            # D:\pyj\st\venv\Scripts\pyrcc5.exe
                # pyrcc5.exe 要转换的qrc资源文件 -o 转成的py文件 
                # 注意 资源文件转成的该资源py文件名要和ui转成的py文件中引用该资源的名称保持一致。
                # 资源转成的py文件数据部分都是二进制。

            # 要使转换的py文件完整，还要补全槽函数。

        # pyside2该目录下有rcc.exe和uic.exe两个执行文件：
            # D:\pyj\st\venv\Scripts\pyside2-rcc.exe 
            # D:\pyj\st\venv\Scripts\pyside2-uic.exe

    

    # py直接使用ui文件
        # from PyQt5.uic import loadUi
        # loadUi('main.ui',父控件)

# 1.1 在vscode中将QT 设计师 的 .ui文件和资源文件 .rcc 转换成py文件                 *****
    # 在vscode安装pyqt扩展,搜索一下就可以找到了，很简单;
    # 在ui界面文件或qrc资源文件上 右击 选择 PySide2:Compile Form to Python        *****
    # 弹出成功提示条，就会在同目录下生成'ui_原u界面或资源文件名.py'的python文件。

# 1.2 Qt Designer操作控件

    # 预览 Ctrl+r
    # 标签小伙伴 单击标签 选择 菜单Edit  选择 编辑伙伴  按住鼠标从标签指向伙伴控件。
    # 信号与槽 
        # 选中发射信号的控件
        # 选择 菜单Edit  选择 编辑信号/槽
        # 按住鼠标从发射控件指向响应控件
        # 就会弹出 发射控件的信号栏 和 响应控件的功能函数栏 选择相应的信号和函数 点击ok即可
            # 如果是自定义的信号，在信号栏下点击edit，输入自定义的信号名，就可选择了。
            # 如果是自定义的槽函数，在右侧功能函数下点击edit，输入自定义的函数名，就可选择了。
        # 一个发射控件可以对应多个响应控件 所以 可以继续按住鼠标指向响应控件 完成设定
        # 按ESC 退出
        
        # 删除一个信号与槽 
        # 选中发射控件 选择 编辑信号/槽 展示出该发射控件的信号/槽链条
        # 选中要删除的发射和响应链条 按键盘上的删除键即可

    # 修改样式
        # 选中要添加样式的控件
        # 右击 选择 改变样式表 弹出编辑样式表
        # 在文本框中写入样式 点击apply就可看到效果

    # 添加资源
        # 右下角的 资源浏览器 如没有看到 就点击 视图菜单 选择 资源浏览器。
            # 选择 编辑资源 按钮（笔） 弹出 编辑资源 对话框 
                # 选择 新建资源文件 左下角新建图片按钮 弹出 新建资源文件 对话框
                    # 选择要保存的目录 和 输入 资源文件名 就建立了 .qrc资源文件。
                # 刚建立的qrc资源文件就出现在左侧文本框。
                # 右侧选择 + 按钮 在右侧文本框添加前缀  前缀是用来区分资源文件类别的作用，比如前缀为背景和前景。
                # 再选择 添加文件 按钮，打开添加文件对话框，选择一个或多个图片或别的资源文件。
                # 选择的资源就出现在该前缀的树下。
                # 点击ok按钮，就完成了一次资源的添加。

            # 一个app 可以添加多个资源文件，要注意的是，不同资源文件下的相同前缀会合并。

    # 使用自定义控件类——类的提升
        # 在设计师 使用该自定义类的基类 创建 控件
        # 右击控件 选择 提升为... 菜单  弹出 提升的窗口部件 对话框
        # 在 填写提升的类名称 填写 自定义的类名
        # 在 头文件 填写 自定义类的文件名 不要有文件的后缀名
            # 这就实现将ui文件转成py文件时 有一行代码是： from 自定义类的文件名  import 自定义类
            # 这就要求 从ui转成的py文件 必须能找到 自定义类的文件。
        # 点击 添加 按钮，会把类名和文件名添加到上方的栏目中，点击 - 按钮，就类和文件名。
        # 点击 提升按钮 就完成提升  但是在ui预览看不到效果。
        # 要将该ui转成py，再执行，就可以看到效果，因为转成py时，自定义类已被成功引入。







    


# 2 对界面控件进行布局，白月黑羽的经验是 按照如下步骤操作

    # 先不使用任何Layout，把所有控件 按位置 摆放在界面上
    
    # 然后先从 最内层开始 进行控件的 Layout 设定
    
    # 逐步拓展到外层 进行控件的 Layout设定
    
    # 最后调整 layout中控件的大小比例， 优先使用 Layout的 layoutStrentch 属性来控制

# 3 打包发布 pyinstaller
    # 把 解释器、Python 代码 和 依赖的库 制作到一个目录中，我们只需要双击其中的 可执行程序，就可以运行我们的Python程序了。

    # 其中 PyInstaller 是目前比较常用的一款。
        # 安装 pip install pyinstaller

    # PyInstaller 支持 Python 2.7 和 Python 3.3 以后的版本。

    # 支持在 Windows, Mac OS X, and Linux 系统上打包出 可执行程序，但不能交叉编译（在windwos编译Linux或反过来）。

    # 其官方网站在这里： http://www.pyinstaller.org

    # 命令行程序打包
        # pyinstaller 要打包的程序xx.py  --noconsole  --hidden-import PySide2.QtXml PySide2.QtCore.Qt.WA_StyledBackground
        # 静态文件考入 main.ui

        # 报缺少qt插件错误：
            # 我们找到路径：D:\pyj\st\venv\Lib\site-packages\PySide2\plugins
            # 在此文件夹下找到platforms文件夹，然后拷贝整个文件夹，覆盖dist目录下 \pyqt2Qt_Designer\PySide2\plugins目录中的同名目录
            # D:\pyj\st\study\pyside2_pyqt\dist\pyqt2Qt_Designer\PySide2\plugins
    
    # 打包好的程序，就是dist目录下的 程序名文件目录，打开该目录，双击 目录下的同名exe文件 程序名.exe,即可运行。

    # dist目录下的程序文件目录可以压缩成zip文件，到处运行。

    # 打包过程中形成的build目录等文件，在打包完成后可以删除。
     
# from PySide2.QtWidgets import QApplication,QMessageBox
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile

class Stats():
    def __init__(self):
        # 打开文件 动态加载ui定义
        # qfile_stats=QFile('main.ui')
        # qfile_stats.open(QFile.ReadOnly)
        # qfile_stats.close()
        
        # self.ui=QUiLoader().load(qfile_stats)

        # 不用上面这个QFile也可以，直接用QUiLoader打开
        self.ui=QUiLoader().load('main.ui')

        # 连接 动作 signal connect slot
        self.ui.tonji.clicked.connect(self.handleCalc)

    # slot
    def handleCalc(self):
        # 取得薪资的结果 多行文本
        info = self.ui.xinzi.toPlainText()
        # print(type(info)) #<class 'str'>
        # 薪资20000 以上 和 以下 的人员名单
        salary_above_20k = ''
        salary_below_20k = ''
        for line in info.splitlines(): # 把info字符串 按行切割 info.splitlines()
            if not line.strip(): #如果是空行 就直接跳过
                # print(1)
                continue
            parts = line.split(' ') #把每行的字符串 按空格切割
            # 利用列表生成式及三元判断 去掉列表中的空字符串内容
            parts = [p for p in parts if p]
            # print(parts) #['薛蝌', '4460', '25']
            # 取出姓名 工资 年龄
            name,salary,age = parts
            # 数字字符串转换成int，比较大小
            if int(salary) >= 20000: # 注意换行 '\n'
                salary_above_20k += name + '\n'
            else:
                salary_below_20k += name + '\n'
        # 消息窗口控件.about(父控件，本消息窗口名称，消息体)
        QMessageBox.about(self.ui,
                    '统计结果',
                    f'''薪资20000 以上的有：\n{salary_above_20k}
                    \n薪资20000 以下的有：\n{salary_below_20k}'''
                    )

if __name__ == "__main__":
    
    # 程序实例化
    app = QApplication([])
    # 界面类实例化
    stats = Stats()
    # 界面类主窗口的展示 ***
    stats.ui.show()
    # 启动程序
    app.exec_()
    