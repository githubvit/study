from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
# from PyQt5.Qt import *
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('下拉菜单QComboBox的学习')
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        label.setText("社会我顺哥, 人狠话不多")
        label.move(100, 100)
        # 设置字体菜单下拉对象
        fcb = QFontComboBox(self)
        fcb.setEditable(False) # 默认是可编辑，改为不可编辑

        # 用按钮设置字体
        # btn=QPushButton(self)
        # btn.setText('设置字体')
        # btn.adjustSize()
        # btn.move(100,150)
        # btn.clicked.connect(lambda :label.setFont(fcb.currentFont()))

        
        
        # 字体变化  信号 设置字体
        fcb.currentFontChanged.connect(lambda font: label.setFont(font))
        

        
          



if __name__ == "__main__":
    from PySide2.QtWidgets import *
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()