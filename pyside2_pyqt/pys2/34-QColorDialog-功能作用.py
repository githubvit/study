from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('颜色对话框QColorDialog的学习')
        self.setup_ui()

    def setup_ui(self):
        # 用静态方法设置自定义颜色和标准颜色
        # 要在颜色对话框定义前设置
        QColorDialog.setCustomColor(3, QColor(100,200,50))
        # QColorDialog.setStandardColor(2, QColor(255, 0, 0))
        # cd = QColorDialog(QColor(100, 200, 150), self)
        
        cd=QColorDialog(self)
        print(cd.customCount()) # 获取可自定义颜色的总数 16 


        btn=QPushButton(self)
        self.btn=btn
        btn.setText('弹出颜色对话框')
        btn.move(10,10)
        # 一 用不同的弹出方式 获取颜色
        # 1 show() 非模态对话框 可用colorSelected信号 获取颜色
        # btn.clicked.connect(lambda:cd.show())
        # 当对话框的ok按下 就发射colorSelected信号
        # cd.colorSelected.connect(lambda col: self.change_background_color(col))

        # 2 open() 模态对话框 对pyqt5 open(槽函数)
        def get_color():
            print('获取颜色')
            self.change_background_color(cd.selectedColor())
        # btn.clicked.connect(lambda:cd.open(get_color))

        # 3 exec_() 程序级模态对话框可用返回的值是1还是0来获取颜色
        def e_color():
            result=cd.exec_()
            if result:
                get_color()
                self.change_background_color(cd.selectedColor())
        # btn.clicked.connect(e_color)

        # 二 用静态方法 获取颜色
        def static_getColor():
            col=QColorDialog.getColor() # isok
            # col=QColorDialog.getColor(self) # isno 报错 wrong argument types

            # col=QColorDialog.getColor(QColor(10, 20, 100), self, "选择颜色") #isok
            
            # cr=str(col.red())
            # cg=str(col.green())
            # cb=str(col.blue())
            # self.change_background_color(cr,cg,cb)
            
            # print(cr,cg,cb)

            self.change_background_color(col)

        # btn.clicked.connect(static_getColor)

        # 三 实时配置
        # 选项控制
        # cd.setOption(QColorDialog.NoButtons) #设定无 确定和取消按钮
        # cd.setOptions(QColorDialog.NoButtons| QColorDialog.ShowAlphaChannel) #多项设定用options 
        # QColorDialog.ShowAlphaChannel 允许用户选择颜色的alpha分量。
        # QColorDialog.DontUseNativeDialog 使用Qt的标准颜色对话框而不是操作系统原生颜色对话框。
        # 弹出
        # btn.clicked.connect(lambda:cd.show())
        # 使用 currentColorChanged 信号
        # cd.currentColorChanged.connect(lambda col: self.change_background_color(col))


        # 四 改变按钮文字颜色案例
        btn.clicked.connect(self.change_btnText)

    # 改变背景颜色  
    def change_background_color(self,col):
        # self.setStyleSheet(f'background-color:rgb({r},{g},{b})')#这样设置影响子控件，不可用。

        # 真正设置窗口背景，是用QPalette 调色板对象
        # 设置调色板对象
        plt=QPalette()
        # 为调色板对象设置 角色 颜色 （角色，颜色）
        plt.setColor(QPalette.Background,col)
        # 将 调色板对象 应用于 主窗口 
        self.setPalette(plt)
        
        pass

    # 改变按钮文字颜色
    def change_btnText(self):
        cd1=QColorDialog(self)
        cd1.show()
        def btn_text_color(col):
            # 设置 调色板 对象
            plt=QPalette()
            # 为调色板对象设置 角色 颜色 （角色，颜色）
            plt.setColor(QPalette.ButtonText,col)
            # 将调色板对象应用于按钮
            self.btn.setPalette(plt)

        # 用 colorSelected 改变
        # cd1.colorSelected.connect(btn_text_color)
        
        # 用 currentColorChanged 实时改变
        cd1.setOption(QColorDialog.NoButtons) # 实时改变 就不要按钮了
        cd1.currentColorChanged.connect(btn_text_color)

        
  
if __name__ == "__main__":
    app = QApplication([])
    wd=Window()
    wd.show()
    app.exec_()