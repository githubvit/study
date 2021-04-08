from PySide2.QtWidgets import *
from PySide2.QtGui import *
# from PyQt5.Qt import *

app = QApplication([])

# 1 设定顶层窗口类型和外观 无边框
window = QWidget()          #创建控件时就设定了窗口的类型为 QWidget类型
# 设定顶层窗口外观样式setWindowFlags(外观样式)
window.setWindowFlags(Qt.FramelessWindowHint) #无边框外观

'''
参考 c++ 窗口类型和外观
    窗口类型和 Qt::WindowFlags

     1 Qt::Widget               //是一个窗口或部件，有父窗口就是部件，没有就是窗口
     2 Qt::Window               //是一个窗口，有窗口边框和标题
     3 Qt::Dialog               //是一个对话框窗口
     4 Qt::Sheet                //是一个窗口或部件Macintosh表单
     5 Qt::Drawer               //是一个窗口或部件Macintosh抽屉，去掉窗口左上角的图标
     6 Qt::Popup                //是一个弹出式顶层窗口
     7 Qt::Tool                 //是一个工具窗口
     8 Qt::ToolTip              //是一个提示窗口，没有标题栏和窗口边框
     9 Qt::SplashScreen         //是一个欢迎窗口，是QSplashScreen构造函数的默认值
     10 Qt::Desktop              //是一个桌面窗口或部件
     11 Qt::SubWindow            //是一个子窗口

    窗口外观风格
    //为窗口添加一些功能，窗口属性

    1 Qt::CustomizeWindowHint          //关闭默认窗口标题提示
    2 Qt::WindowTitleHint              //为窗口修饰一个标题栏
    3 Qt::WindowSystemMenuHint         //为窗口修饰一个窗口菜单系统
    4 Qt::WindowMinimizeButtonHint     //为窗口添加最小化按钮
    5 Qt::WindowMaximizeButtonHint     //为窗口添加最大化按钮
    6 Qt::WindowMinMaxButtonsHint      //为窗口添加最大化和最小化按钮
    7 Qt::WindowCloseButtonHint			//窗口只有一个关闭按钮
    8 Qt::WindowContextHelpButtonHint
    9 Qt::MacWindowToolBarButtonHint
    10 Qt::WindowFullscreenButtonHint
    11 Qt::BypassGraphicsProxyWidget
    12 Qt::WindowShadeButtonHint
    13 Qt::WindowStaysOnTopHint	       //总在最上面的窗口,置前
    14 Qt::WindowStaysOnBottomHint
    15 Qt::WindowOkButtonHint
    16 Qt::WindowCancelButtonHint
    17 Qt::WindowTransparentForInput

    示例：

    this->setWindowFlags(windowFlags() | Qt::WindowStaysOnTopHint);
    1
    如果想去掉某个属性就直接加~就可以了。
    示例：

    setWindowFlags(windowFlags()& ~Qt::WindowMaximizeButtonHint);//去掉最大化按钮
'''
window.setWindowTitle("顶层窗口")
window.resize(500, 500)

# 2 设定窗口半透明
# window.setWindowOpacity(0.8)

# 3 设定关闭
btn=QPushButton(window)
btn.setText('关闭')
btn.move(200,200)
btn.clicked.connect(window.close)



window.show()

app.exec_()
