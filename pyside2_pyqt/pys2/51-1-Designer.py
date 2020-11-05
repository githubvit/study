# MVC 开发方式
# M 与 数据库 打交道的部分 存取

# v 与 界面   打交道的部分 输入与输出

# C 联结 M与V 的控制部分 存取什么数据 与 输入与输出什么数据

# 为了在vscode界面直接用右击就可以用designer界面设计师工具打开ui文件，
# 要设置designer界面设计师的搜索路径，
    # 1 用快捷键 ‘ctrl+,’打开 vscode 搜索设置 界面
    # 2 输入'qt',
    # 3 找到 ‘Qt For Python > Path: Designer ’修改路径为designer所在路径
        # 	D:\pyj\st\venv\Lib\site-packages\PySide2\designer
        # 即可，注意去掉 '.exe' 后缀。


from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# from PyQt5.Qt import *

# 样式获取工具
from qt_css import get_stlye

# 1 调入从 Designer 设计师 转成的py文件中的  界面类

# from Ui_main import Ui_Form
from Ui_ctj import Ui_ctj

# 2 class 多继承 

# class Window(QWidget,Ui_Form):
class Window(QWidget,Ui_ctj):
    def __init__(self):
        super().__init__()
        # 3 导入界面类setupUi函数，填入self参数作为父类。
        self.setupUi(self)

    # 4 用slot装饰器添加槽函数
    @Slot()
    def on_pushButton_1_clicked(self):
        print('填充题库')

    @Slot()
    def on_pushButton_2_clicked(self):
        print('刷题')

    @Slot()
    def on_pushButton_3_clicked(self):
        print('制作试卷')

    @Slot()
    def on_pushButton_4_clicked(self):
        print('刷卷')
    
    # 5 解除父子关系保持位置的办法（比如外包控件Qwidget和里面的QPushButton）：
    
        # 先在界面上移出来，就不会有父子关系了。
    
        # 再选择原来的子控件，用属性选择器选择geometry属性，手动输入x和y到原来的位置，即可。
    
    # 6 当选中一个控件使用属性编辑器 编辑某个属性 时，要避免操作过程中选择了其他的控件。
    
    # 7 如果一个控件明明enable属性是打勾的，如果发现还是不可用，这时，有可能是其父控件的enable没打勾。

if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
    