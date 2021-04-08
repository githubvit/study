from PySide2.QtWidgets import QApplication,QWidget,QMainWindow,QVBoxLayout,QDockWidget
from PySide2.QtCore import Signal,Slot,QEvent,Qt
from PySide2.QtGui import QKeySequence

import os,sys

# 一 取得项目根目录加入系统目录
# print(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
# 把项目根目录加入环境变量 然后其它导入就有根了
sys.path.append(BASE_DIR)

from resource.ui.Ui_short_screen import Ui_MainWindow

class ShortScreenUi(QMainWindow,Ui_MainWindow):
     def __init__(self,parent=None):
        # 继承父类初始化
        super().__init__(parent) 
      
        # 导入界面类setupUi函数，填入 self 参数作为父类。
        self.setupUi(self)


if __name__ == "__main__":
    
    app=QApplication([])
    wd=ShortScreenUi()
    wd.show()
    app.exec_()