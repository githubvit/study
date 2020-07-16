from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
# from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('旋钮表盘QDial的学习')
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        label.move(100, 100)
        label.setText("社会我顺哥, 人狠话不多")

        dia = QDial(self)
        dia.setRange(0, 200)
        # 用旋钮刻度的值来实时改变标签字体的大小
        def test(val):
            label.setStyleSheet("font-size: {}px;".format(val))
            label.adjustSize()
        dia.valueChanged.connect(test)

        dia.setNotchesVisible(True)#显示刻度
        dia.setPageStep(5)

        dia.setWrapping(True) #设置循环
        dia.setNotchTarget(10) #设置每格刻度的数值
        

if __name__ == "__main__":
    from PySide2.QtWidgets import *
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()