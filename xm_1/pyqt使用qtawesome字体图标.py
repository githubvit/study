# 使用 第三方库 qtawesome 实现使用前端流行的 字体图标 Font Awesome, Elusive Icons or Material Design Icons. 字体图标 
# 源码和用法  国内镜像页面 https://gitee.com/mirrors/qtawesome      *****
# https://github.com/spyder-ide/qtawesome

from PySide2.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QLayout
from PySide2.QtCore import Slot,QSize
from PySide2.QtGui import QIcon
import qtawesome as qta #引入图标



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('第三方字体图标的学习')
        self.setGeometry(1000,400,500,500)
        self.setupUi()
        

    def changeIcon(self):
        # 给图标绑定标志 切换图标
        if self.btn1_icon_flag:
            self.btn1.setIcon(self.icon)
            self.btn1_icon_flag=0
        else:
            self.btn1.setIcon(self.icon1)
            self.btn1_icon_flag=1
        
    def setupUi(self):

        btn1=QPushButton(self)
        self.btn1=btn1
        btn1.setGeometry(100,50,100,30)
        # icon1=qta.icon('fa.music')# 音乐图标 默认比例为1 黑色
        icon=qta.icon('fa.music',scale_factor=1,color='orange')#音乐图标
        self.icon=icon
        icon1=qta.icon('fa.music',scale_factor=1,color='blue')#音乐图标
        self.icon1=icon1
        # icon1=qta.icon('fa.window-close-o')# 原来复制下来的名称 fa-window-close-o 所以 就是 fa.+后面的名称 即可
        # icon1=qta.icon('fa.tint')# 原来复制下来的名称 fa-tint 所以 就是 fa.+后面的名称 即可
        # print(icon1)

        # 给图标绑定标志 切换图标
        # 比如icon==0 icon1==1
        btn1.setIcon(icon1)
        self.btn1_icon_flag=1
        btn1.clicked.connect(self.changeIcon)
       
        
        # 使用ttf字体方式
        btn2=QPushButton(self)
        btn2.setText('\uf101')
        btn2.setGeometry(100,100,100,30)
        btn2.setFont(qta.font('fa', 20))
        # icon2=qta.icon('fa.close')
        # btn2.setIcon(icon2)

        btn3=QPushButton(self,)
        btn3.setText('禁止拍照')
        btn3.setGeometry(100,150,100,30)
        # 两个图标叠加 相机+禁止=禁止拍照
        icon3=qta.icon('fa5s.camera', 'fa5s.ban',
                      options=[{'scale_factor': 0.5,
                                'active': 'fa5s.balance-scale'},
                               {'color': 'red'}])
        btn3.setIcon(icon3)
        btn3.setIconSize(QSize(32,32))


if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
