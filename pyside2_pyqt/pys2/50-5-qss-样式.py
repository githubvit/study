from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# from PyQt5.Qt import *

# 样式获取工具
from qt_css import get_stlye



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('QSS控件样式4-样式')
        self.setup_ui()

    def setup_ui(self):
        btn1=QPushButton('按钮1')
        cbx=QCheckBox('复选框')
        rdt=QRadioButton('单选框')
        h_layout=QHBoxLayout()
        h_layout.addWidget(btn1)
        h_layout.addWidget(cbx)
        h_layout.addWidget(rdt)

        le=QLineEdit()
        # le.setEchoMode(QLineEdit.Password)
        # le.setReadOnly(True)

        lte=QTextEdit()

        cmx=QComboBox()
        cmx.addItems(['123','456','abc'])
        cmx.setEditable(True)

        slider=QSlider()
        # 设为水平
        slider.setOrientation(Qt.Horizontal)

        bar=QProgressBar()
        bar.setValue(50)

        v_layout=QVBoxLayout(self)
        v_layout.addLayout(h_layout)
        v_layout.addWidget(le)
        v_layout.addWidget(lte)
        v_layout.addWidget(cmx)
        v_layout.addWidget(slider)
        v_layout.addWidget(bar)
  


        pass
if __name__ == "__main__":
    
    app=QApplication([])
    wd=Window()
    wd.show()
    # 用样式文件设置样式
    # 选择器[:伪状态]{
            # 声明
        # } 
    filepath=r'D:\pyj\st\study\pyside2_pyqt\pys2\test3.css'
    get_stlye(filepath,app)

    # 加载第三方暗黑样式 仅对pyqt5有效 对pyside2无效
    # import qdarkgraystyle
    # app.setStyleSheet(qdarkgraystyle.load_stylesheet_pyqt5())
    app.exec_()