from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('纯文本编辑器QPlainTextEdit的学习')
        self.setup_ui()
    def setup_ui(self):
        # 快捷键录制 可以捕捉键盘输入的快捷键
        kse = QKeySequenceEdit(self)

        # ks = QKeySequence("Ctrl+C") # 使用字符组合生成组合键对象
        # ks = QKeySequence(QKeySequence.Copy) # 使用标准组合键生成组合键对象 
        ks = QKeySequence(Qt.CTRL + Qt.Key_C, Qt.CTRL + Qt.Key_A)
        # 录制组合键对象
        kse.setKeySequence(ks)
        # 清除录制
        # kse.clear()

        # 信号
        btn = QPushButton(self)
        btn.move(100, 100)
        btn.setText("测试按钮")
        btn.clicked.connect(lambda :print(kse.keySequence().toString(), kse.keySequence().count()))#组合键及个数

        kse.editingFinished.connect(lambda :print("结束编辑"))#改变 停顿1秒后 会自动结束 
        kse.keySequenceChanged.connect(lambda key_val:print("键位序列发生改变", key_val.toString()))#读出当前按下的键
        pass
if __name__ == "__main__":
    from PySide2.QtWidgets import *
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()