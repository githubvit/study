from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
# 自定义展示
class MyDoubleSB(QDoubleSpinBox):
    def textFromValue(self, p_float):
        print("xxxxx", p_float)
        return str(p_float) + "*" + str(p_float)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('浮点型调节QDoubleSpinBox的学习')
        self.setup_ui()

    def setup_ui(self):
        # dsb = QDoubleSpinBox(self)
        dsb = MyDoubleSB(self)
        dsb.move(100, 100)
        dsb.resize(100, 30)
        # 默认最大最小值，步长1.00
        # 0.00 - 99.99

        # 设置最大最小值
        # dsb.setMaximum(88.88)
        # dsb.setMinimum(22.22)
        # 设置步长 
        dsb.setSingleStep(0.02)
        # 设置循环
        # dsb.setWrapping(True)
        # 设置前后缀
        dsb.setPrefix("$")
        dsb.setSuffix("%")
        # 设置范围
        # dsb.setRange(1.0, 2.0)
        # dsb.setSingleStep(0.5)
        # dsb.setSuffix("倍速")
        # dsb.setSpecialValueText("正常")
        # dsb.setWrapping(True)
        # 设置小数位数
        # dsb.setDecimals(1)

        # 设置和获取数值
        test_btn = QPushButton(self)
        test_btn.move(300, 300)
        test_btn.setText("测试按钮")
        # test_btn.clicked.connect(lambda :dsb.setValue(-166.66))
        test_btn.clicked.connect(lambda :print(type(dsb.value()), dsb.value()))
        # test_btn.clicked.connect(lambda :print(type(dsb.cleanText()), dsb.cleanText()))#不包括任何前缀，后缀或前导或尾随空格 value的str
        # test_btn.clicked.connect(lambda :print(type(dsb.text()), dsb.text()))
        # test_btn.clicked.connect(lambda :print(type(dsb.lineEdit().text()), dsb.lineEdit().text()))

        # dsb.valueChanged.connect(lambda val: print(val, type(val)))
        dsb.valueChanged[str].connect(lambda val: print(val, type(val)))

if __name__ == "__main__":
    from PySide2.QtWidgets import *
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()