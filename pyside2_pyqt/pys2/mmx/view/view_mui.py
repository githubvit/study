from PySide2.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QFileDialog
from PySide2.QtCore import Signal,Slot
from PySide2.QtGui import QIcon

import os,sys



# 一 取得项目根目录加入系统目录
# print(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
# 把项目根目录加入环境变量 然后其它导入就有根了
sys.path.append(BASE_DIR)

# 1 导入从 Designer 设计师 转成的py文件中的  界面类  用于 多继承
from resource.ui.Ui_mui import Ui_Form

class MuiUi(QWidget,Ui_Form):
    # 信号
    m_k_signal=Signal()     # 制作密钥 信号
    encrypt_signal=Signal() # 加密 信号
    decrypt_signal=Signal() # 解密 信号
    exit_signal=Signal()    # 退出 信号

    
    def __init__(self,parent=None):
        # 2 继承父类初始化
        super().__init__(parent) 
        
        # 3 导入界面类setupUi函数，填入 self 参数作为父类。
        self.setupUi(self)

        # 设置图标
        # 窗口 标题栏和在任务栏的图标
        self.setWindowIcon(QIcon(r'D:\pyj\st\study\pyside2_pyqt\pys2\mmx\6.ico'))
        # 任务栏的效果要打包之后，独立运行才可以看出来。
        # 开发阶段，用的是py解释器环境的值。看不出效果的。
        
        # 4 用信号和槽 发射自定义信号
        self.m_key_btn.clicked.connect(self.m_k_signal.emit)    
        self.encrypt_btn.clicked.connect(self.encrypt_signal.emit)    
        self.decrypt_btn.clicked.connect(self.decrypt_signal.emit)    
        self.exit_btn.clicked.connect(self.exit_signal.emit)    

if __name__ == "__main__":
    
    app=QApplication([])
    wd=MuiUi()
    wd.show()

    # 5 信号监测
    
    wd.m_k_signal.connect(lambda : print('制作密钥信号'))
    wd.encrypt_signal.connect(lambda : print('加密信号'))
    wd.decrypt_signal.connect(lambda : print('解密信号'))
    wd.exit_signal.connect(lambda : print('退出信号'))
    app.exec_()