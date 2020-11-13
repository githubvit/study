from PySide2.QtWidgets import QApplication,QWidget,QPushButton,QComboBox,QCheckBox,QLabel
from PySide2.QtCore import Signal,Slot,QSize,QUrl
from PySide2.QtGui import QMovie,QDesktopServices

import os,sys



# 一 取得项目根目录加入系统目录
# print(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
# 把项目根目录加入环境变量 然后其它导入就有根了
sys.path.append(BASE_DIR)

# 1 导入从 Designer 设计师 转成的py文件中的  界面类  用于 多继承
from resource.ui.Ui_l_1 import Ui_Form

class L1Ui(QWidget,Ui_Form):
    # 立即注册信号
    l_register_signal=Signal()
    # 登录信号(u,p)
    login_signal=Signal([str,str])
    def __init__(self):
        # 2 继承父类初始化
        super().__init__() 
      
        # 3 导入界面类setupUi函数，填入 self 参数作为父类。
        self.setupUi(self)

        # 4 添加动图
        # 使用qrc中的gif图像生成qmovie对象。注意写法(设计师designer 里面 ':/资源浏览器中的该资源的索引路径')
        movie=QMovie(':/l_1/resource/img/login_bg.gif')
        # 设定动图大小自动适应标签
        self.an_lb.setScaledContents(True)
        # movie.setScaledSize(QSize(500,250))
        # 将movie对象设置给动图标签
        self.an_lb.setMovie(movie)
        # 启动movie
        movie.start()
        
    # 5 让登录按钮变得可用
    def login_enable(self):
        val=len(self.user_cmbx.currentText().strip()) and len(self.pw_le.text().strip())
        self.lg_btn.setEnabled(val)

    # 监测用户输入和密码输入
    @Slot(str)
    def on_user_cmbx_editTextChanged(self,v):
        
        print(f'用户下拉框{v}高亮')
        self.login_enable()
    @Slot()
    def on_pw_le_textChanged(self):
        print('密码输入框变化')
        self.login_enable()    

    # 6 登录 向外发射登录信号 传递u和p
    @Slot()
    def on_lg_btn_clicked(self):
        self.login_emit()
    def login_emit(self):
        print('登录 用户名 密码')
        self.login_signal.emit(self.user_cmbx.currentText().strip(),self.pw_le.text().strip())

    # 7 立即注册 按钮 向外发射注册信号
    @Slot()
    def on_r_btn_clicked(self):
        print('立即注册')
        self.l_register_signal.emit()

    # 8 链接按钮 用桌面浏览器打开外部链接
    def open_url(self):
        link='https://www.baidu.com'
        QDesktopServices.openUrl(QUrl(link))
    
    @Slot()
    def on_url_btn_clicked(self):
        print('链接按钮')
        self.open_url()

    # 9 记住密码 checkbox
    @Slot(bool)
    def on_rp_cbx_toggled(self,v):
        print(f'记住密码{v}')
        # 如果v是False且自动登录是True，则将自动登录也置为False
        if (not v) and self.alg_cbx.isChecked():
            self.alg_cbx.setChecked(False)

    # 10 自动登录
    @Slot(bool)
    def on_alg_cbx_toggled(self,v):
        print(f'自动登录{v}')
        # 如果v是True且记住密码是False，则将记住密码也置为True
        if v and (not self.rp_cbx.isChecked()):
            self.rp_cbx.setChecked(True)


if __name__ == "__main__":
    app=QApplication([])
    wd=L1Ui()
    wd.show()
    # 监测自定义向外发射的信号
    wd.login_signal.connect(lambda u,p: print(f'收到login_signal登录信号，传递用户名{u}和密码{p}'))
    wd.l_register_signal.connect(lambda : print(f'收到l_register_signal打开立即注册界面信号'))
    app.exec_()