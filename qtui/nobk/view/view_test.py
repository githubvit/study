from PySide2.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QSizeGrip
from PySide2.QtCore import Signal,Slot,Qt
from PySide2.QtGui import QIcon

import os,sys



# 一 取得项目根目录加入系统目录
# print(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
# 把项目根目录加入环境变量 然后其它导入就有根了
sys.path.append(BASE_DIR)

# 二 显示ui框架 （2.1 2 3 即可显示ui 2.4 开始属于扩展 动作部分）
# 2.1 导入从 Designer 设计师 转成的py文件中的  界面类  用于 多继承
from resource.ui.Ui_test import Ui_Form

# 三 联结 主逻辑
# 3.1 导入主逻辑程序



class TestUi(QWidget,Ui_Form):
    
    def __init__(self):
        # 2.2 继承父类初始化
        super().__init__()

        self.setupUi(self)
        # self.setMouseTracking(True) #有可视子控件遮挡时，无效。
        # 自定义鼠标跟踪
        self.mouseTracking_set(True)
        
    def mouseMoveEvent(self,evt):
        print(evt.pos())
    
    # 解决可视化控件遮挡 鼠标跟踪
    def mouseTracking_set(self,bool):
        # 鼠标跟踪 不是一设置就有效果的，如果有多级遮挡，就必须一级一级来设置，才能有效。
        self.setMouseTracking(bool)
        # 为了避免被子控件遮挡导致的问题，需要把所有可视子控件都设置 鼠标跟踪
        for item in self.findChildren(QWidget): #采用这种方式 避免下面这样一个一个设置
            # print(item)
            item.setMouseTracking(bool)
        # self.cnt_wgt.setMouseTracking(True)
        # self.left_wgt.setMouseTracking(True)
        # self.right_wgt.setMouseTracking(True)
        # self.list_wgt.setMouseTracking(True)
         
        # self.btl_wgt.setMouseTracking(True)
        
if __name__ == "__main__":
    
    app=QApplication([])
    wd=TestUi()
    wd.show()
    app.exec_()