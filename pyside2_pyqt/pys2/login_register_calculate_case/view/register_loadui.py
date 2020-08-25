
# ui不转成py，使用loader(uifile)

import os,sys
from PySide2.QtWidgets import QWidget,QApplication,QMessageBox,QFrame
from PySide2.QtCore import Signal,Slot,Qt,QSequentialAnimationGroup,QPropertyAnimation,QAbstractAnimation

from PySide2.QtUiTools import QUiLoader

ui_dir=os.path.dirname(os.path.dirname(__file__))
ui_path='%s/resouse/ui/register.ui'%ui_dir




if __name__ == "__main__":
    
    # 程序实例化
    app = QApplication([])
    # 界面类实例化
    # wd=RegisterUI
    # 界面类主窗口的展示 ***
    RegisterUI=QUiLoader().load(ui_path)
    RegisterUI.show()
    # 启动程序
    app.exec_()
