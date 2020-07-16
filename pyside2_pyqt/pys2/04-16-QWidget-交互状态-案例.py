# 三个子控件
# 标签、文本框、登录按钮
# 默认隐藏标签，登录按钮不可用
# 文本框有内容，则登录按钮可用
# 点击登录或在文本框回车 当文本是“DC”则标签内容为登录成功，否则，显示登录失败
# 
from PySide2.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('交互状态案例')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        # 标签、文本框、登录按钮
        self.lb=QLabel(self)
        self.lb.setText('标签')
        self.lb.move(50,50)
        self.le=QLineEdit(self)
        self.le.setPlaceholderText('文本框')
        self.le.move(50,100)
        self.btn=QPushButton(self)
        self.btn.setText('登录')
        self.btn.move(50,150)
        # 默认隐藏标签，登录按钮不可用
        self.lb.setVisible(False)
        self.btn.setEnabled(False)
        # 文本框有内容，则登录按钮可用
        # 文本框文本变化信号textChanged
        self.le.textChanged.connect(self.tc_cao)
        # 当文本是“DC”则标签内容为登录成功，否则，显示登录失败
        self.btn.clicked.connect(self.btn_cao)
        #文本框回车信号 editingFinished和returnPressed
        # self.le.editingFinished.connect(self.btn_cao)
        self.le.returnPressed.connect(self.btn_cao)
    
    def tc_cao(self,text):
        print(text)
        # 文本框有内容，则登录按钮可用
        # if len(text.strip()):
        #     self.btn.setEnabled(True)
        # else:
        #     self.btn.setEnabled(False)
        # 优化上述代码
        self.btn.setEnabled(len(text.strip()))

    def btn_cao(self):
        # 获取文本
        text=self.le.text()
        # 设置文本
        # if text=='DC':
        #     self.lb.setText('登录成功')
        # else:
        #     self.lb.setText('登录失败')
        # 上述代码优化
        tip_text='登录成功' if text=='DC' else '登录失败'
        self.lb.setText(tip_text)

        # 设置可见
        self.lb.setVisible(True)

if __name__ == "__main__":

    app=QApplication([])   
    wd=Window()
    wd.show()
    app.exec_()