from PySide2.QtWidgets import QApplication,QWidget
from PySide2.QtCore import QUrl,QSize,Signal,Slot,Qt,QSequentialAnimationGroup,QPropertyAnimation,QAbstractAnimation,QPoint,QEasingCurve
from PySide2.QtGui import QDesktopServices,QMovie
# from PyQt5.Qt import *

# 1 调入从 Designer 设计师 转成的py文件中的  界面类

# from Ui_main import Ui_Form
from Ui_login import Ui_Form

# 2 class 多继承 

class LoginUi(QWidget,Ui_Form):
    # 自定义信号
    # go_register_signal=pyqtSignal() #立即注册信号
    # login_signal=pyqtSignal(str,str) #登录信号
    go_register_signal=Signal() #立即注册信号
    login_signal=Signal(str,str) #登录信号
    
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)    
        # 解决背景图片没有了的问题 这里没有背景图片
        # self.setAttribute(Qt.WA_StyledBackground,True)
        # 3 导入界面类setupUi函数，填入self参数作为父类。
        self.setupUi(self)

        # 导入gif
        # 使用qrc中的gif图像生成qmovie对象。注意写法
        movie=QMovie(':/login/images/login_bg.gif')
        movie.setScaledSize(QSize(600,160))
        # 将movie对象设置给标签
        self.animation_lb.setMovie(movie)
        # 启动movie
        movie.start()

        # 4  信号与槽

        # 登录按钮是否可用
        self.username_cmbx.currentTextChanged.connect(self.login_btn_enabled)
        self.pwd_le.textChanged.connect(self.login_btn_enabled)

        # 点击注册按钮 激发 去注册信号
        self.register_btn.clicked.connect(self.emit_register_signal)

        # 点击登录按钮 激发 登录信号
        self.login_btn.clicked.connect(self.emit_login_signal)

        # 点击图片按钮 打开网址
        self.url_btn.clicked.connect(self.openUrl)

        # 勾选自动登录 就同时勾选记住密码
        self.auto_login_cbx.clicked.connect(self.checked_rememberpwd)

        # 取消记住密码 就同时取消自动登录
        self.remember_cbx.clicked.connect(self.unchecked_auto_login)

    # 4 槽函数 用slot装饰器添加
    
    def emit_register_signal(self):
        # print('立即注册')
        # 激发注册信号
        self.go_register_signal.emit()

    def emit_login_signal(self):
        # print('安全登录')
        # 激发登录信号 传递用户名和密码
        self.login_signal.emit(self.username_cmbx.currentText(),self.pwd_le.text())

    def openUrl(self):
        # print('打开百度')
        # 打开超链接
        link='http://www.baidu.com'
        QDesktopServices.openUrl(QUrl(link))
   
    # 登录按钮可用与否
    def login_btn_enabled(self):
        name=self.username_cmbx.currentText().strip()
        pwd=self.pwd_le.text().strip()
        if len(name)>0 and len(pwd):
            self.login_btn.setEnabled(True)
        else:
            self.login_btn.setEnabled(False)

    
    # 自动登录和记住密码的逻辑
    # 1 选择了 自动登录 则自动选择 记住密码
    def checked_rememberpwd(self,val):
        if val:
            self.remember_cbx.setChecked(True)

    # 2 取消了 记住密码 则自动取消 自动登录
    def unchecked_auto_login(self,val):
        if not val:
            self.auto_login_cbx.setChecked(False)

    # 登录错误抖动动画api 给外部调用
    def error_login_animation(self):
        # 创建动画对象 目标是整个登录的下半部布局
        animation=QPropertyAnimation(self.login_bottom,b'pos',self)
        # 左右抖动 用关键帧
        animation.setKeyValueAt(0,self.login_bottom.pos())
        animation.setKeyValueAt(0.25,self.login_bottom.pos()+QPoint(20,0)) # QPoint重载了运算，可以分别相加。
        animation.setKeyValueAt(0.5,self.login_bottom.pos())
        animation.setKeyValueAt(0.75,self.login_bottom.pos()+QPoint(-20,0))
        animation.setKeyValueAt(1,self.login_bottom.pos())
        # 设定时长
        animation.setDuration(1000)
        # 设定动画曲线 弹簧
        animation.setEasingCurve(QEasingCurve.OutBounce)
        # 开始 不保留动画
        animation.start(QAbstractAnimation.DeleteWhenStopped)
        
        pass


      


if __name__ == "__main__":
    app=QApplication([])
    wd=LoginUi()
    # 监测自定义信号
    wd.go_register_signal.connect(lambda : print('收到go_register_signal'))
    wd.login_signal.connect(lambda u,p:print('收到login_signal',u,p))
    wd.show()
    app.exec_()