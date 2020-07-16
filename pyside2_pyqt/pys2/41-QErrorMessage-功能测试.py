from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('错误消息对话框QErrorMessage的学习')
        self.setup_ui()


    def setup_ui(self):
        err=QErrorMessage(self)
        # 错误消息对话框
        # 界面
        # i 图标、信息框、checkBox（下次再一次显示 复选框）、ok按钮
        # 默认弹出模式是非模态 设置为模态 setModal(True) 一定要放在show前才能生效
        err.setModal(True)
        # 弹出 消息 否则无效果
        err.showMessage('请注意：错误消息err1')
        err.showMessage('请注意：错误消息err1') # 取消checkbox 重复消息不显示，不重复的依然显示
        err.showMessage('请注意：错误消息err2')
        err.showMessage('请注意：错误消息err1') # 不显示

        # 消息默认可选中 可复制 不可编辑。
        
        
        pass

if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    # 静态方法展示级别信息： 该对话框为非模态，要放在wd.show()后面去展示，不然会被挡住
    # 如果无终端 显示调试、警告、错误等日志信息，可以用该对话框显示
    # QErrorMessage.qtHandler()
    # qDebug('xxx')
    # qWarning('xx1')
    app.exec_()