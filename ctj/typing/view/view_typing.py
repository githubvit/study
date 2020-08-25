from PySide2.QtWidgets import QApplication,QWidget,QFrame
from PySide2.QtCore import Signal,Slot,Qt


# 1 调入从 Designer 设计师 转成的py文件中的  界面类

from Ui_typing import Ui_Form

# 2 class 多继承 

class TypingUi(QWidget,Ui_Form):
    # 自定义信号
   
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs) # 这里必须有parent，不能是parent=None，否则闪退。
     
        # 3 导入界面类setupUi函数，填入self参数作为父类。
        self.setupUi(self)
        
        # 4 信号与槽

    # 4 用slot装饰器添加槽函数
  
    

if __name__ == "__main__":
    app=QApplication([])
    wd=TypingUi()

    # 监测自定义信号
    
    wd.show()
    app.exec_()