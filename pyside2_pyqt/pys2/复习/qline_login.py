from PySide2.QtWidgets import QApplication,QWidget,QPushButton,QLineEdit,QLabel,QAction,QCompleter
from PySide2.QtGui import QIcon

# 账号验证工具类
class AccountTool:
    account_errol=1
    pwd_errol=2
    success_info=3
    @staticmethod
    def check_login(account,pwd):
        if account!='bq':
            return AccountTool.account_errol
        if pwd!='123go':
            return AccountTool.pwd_errol
        return AccountTool.success_info

# 登录框类
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('复习QlineEdit_登录')
        self.resize(500,500)
        self.setMinimumSize(400,400)
        self.setMaximumSize(800,800)
        self.setup_ui()

    def setup_ui(self):
        # 两个输入框 一个登录按钮
        self.account_le=QLineEdit(self)
        self.account_le.setPlaceholderText('请输入用户名')
        self.pwd_le=QLineEdit(self)
        self.pwd_le.setPlaceholderText('请输入密码')
        self.pwd_le.setEchoMode(QLineEdit.Password)
        self.login_btn=QPushButton(self)
        self.login_btn.setText('登录')

        
        # 三个提示标签
        self.account_tip=QLabel(self)
        self.pwd_tip=QLabel(self)
        self.success_tip=QLabel(self)

        # 设置登录按钮不可用，提示标签字体设置，设置标签不可见
        self.login_btn.setEnabled(False)
        for lb in self.findChildren(QLabel):
            lb.setStyleSheet("color:red")
            lb.setVisible(False)
        
        self.success_tip.setStyleSheet("color:green") # 将成功提示标签字体改为绿色

        # 设置密码框的清楚按钮
        self.pwd_le.setClearButtonEnabled(True)

        # 给密码框设置 状态ACtion 用来显示密码的明文或密文
        # 定义action
        self.pwd_state_action=QAction(self.pwd_le)
        self.pwd_state_action.setIcon(QIcon('pyside2_pyqt\pys2\close.png')) 
        self.pwd_state_action.triggered.connect(self.pwd_state_change) # 定义 动作
        # 给密码框添加action
        self.pwd_le.addAction(self.pwd_state_action,QLineEdit.TrailingPosition)

        # 定义 各个控件 动作
        self.account_le.textChanged.connect(self.login_btn_isEndable)
        self.pwd_le.textChanged.connect(self.login_btn_isEndable)
        self.account_le.textEdited.connect(self.clear_tips)
        self.pwd_le.textEdited.connect(self.clear_tips)
        self.login_btn.clicked.connect(self.login)

    # 各个控件的大小和定位
    def resizeEvent(self, evt):
        # 定义基础变量
        margin_x=150
        margin_y=50
        margin_tip=10
        widget_w=self.width()-2*margin_x
        widget_h=40

        # 两个输入框和按钮的大小
        self.account_le.resize(widget_w,widget_h)
        self.pwd_le.resize(widget_w,widget_h)
        self.login_btn.resize(widget_w,widget_h)

        # 两个输入框和按钮定位
        self.account_le.move(margin_x,self.height()/4)
        self.pwd_le.move(margin_x,self.account_le.y()+widget_h+margin_y)
        self.login_btn.move(margin_x,self.pwd_le.y()+widget_h+margin_y)

        # 三个提示标签的定位
        self.account_tip.move(margin_x,self.account_le.y()+widget_h+margin_tip)
        self.pwd_tip.move(margin_x,self.pwd_le.y()+widget_h+margin_tip)
        self.success_tip.move(margin_x,self.login_btn.y()+widget_h+margin_tip)


        return super().resizeEvent(evt) 

    # 密码框 密文 明文 切换   
    def pwd_state_change(self):            
        if self.pwd_le.echoMode()==QLineEdit.Password:
            self.pwd_le.setEchoMode(QLineEdit.Normal)
            self.pwd_state_action.setIcon(QIcon('pyside2_pyqt\pys2\open.png'))
        else: 
            self.pwd_le.setEchoMode(QLineEdit.Password)
            self.pwd_state_action.setIcon(QIcon('pyside2_pyqt\pys2\close.png'))   
        pass

    # 输入框的变化 引起 登录按钮的可用与否
    def login_btn_isEndable(self):
        self.login_btn.setEnabled( len(self.account_le.text().strip()) and len(self.pwd_le.text().strip()))
        pass 

    # 输入框的编辑 去除 老的提示
    def clear_tips(self):
        for lb in self.findChildren(QLabel):
            lb.setText('')
            lb.setVisible(False)
        pass

    # 登录
    def login(self):
        # 获取 用户名和密码
        account=self.account_le.text()
        pwd=self.pwd_le.text()
        # 设置标签 可见
        for lb in self.findChildren(QLabel):
            lb.setVisible(True)
        # 获取验证结果
        login_state=AccountTool.check_login(account,pwd)
        # 根据验证结果，展示标签内容
        if login_state==AccountTool.account_errol:
            self.account_tip.setText('用户名错误')
            self.account_tip.adjustSize()
        if login_state==AccountTool.pwd_errol:
            self.pwd_tip.setText('密码错误')
            self.pwd_tip.adjustSize()
        if login_state==AccountTool.success_info:
            self.success_tip.setText('登录成功。。。')
            self.success_tip.adjustSize()
            
        pass


if __name__=="__main__":
    app=QApplication([])
    wd=LoginWindow()
    wd.show()
    app.exec_()
    pass
