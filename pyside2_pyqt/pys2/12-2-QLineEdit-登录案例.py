from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

# 定义账号工具类
class AccountTool:
    ACCOUNT_ERROR=1
    PWD_ERROR=2
    SUCCESS=3
    @staticmethod 
    def check_login(account,pwd): #检查账号密码
        if account != 'bq':
            return AccountTool.ACCOUNT_ERROR
        if pwd != '123go':
            return AccountTool.PWD_ERROR
        return AccountTool.SUCCESS    

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QLineEdit案例-登录')
        self.resize(500,500)
        self.setMinimumSize(400,400)#限定最小尺寸
        self.setMaximumSize(800,800)#限定最大尺寸
        self.setup_ui()

    def setup_ui(self):
        # 三个控件
        # 账号
        self.account=QLineEdit(self)
        self.account.setPlaceholderText('请输入用户名')
        # 密码
        self.pwd=QLineEdit(self)
        self.pwd.setPlaceholderText('请输入密码')
        self.pwd.setEchoMode(QLineEdit.Password) #设置为密文
        # 登录按钮
        self.login_btn=QPushButton(self)
        self.login_btn.setText('登录')
        

        # 两个提示标签 
        self.account_tip=QLabel(self)
        # self.account_tip.setText('用户名提示')
        self.pwd_tip=QLabel(self)
        # self.pwd_tip.setText('密码提示')
        # 设置标签提示字体为红色
        for lb in self.findChildren(QLabel):
            lb.setStyleSheet('color:red')

        # 成功登录提示标签
        self.success_tip=QLabel(self)
        # 设置该提示标签字体为绿色
        self.success_tip.setStyleSheet('color:green')

        # 默认隐藏标签 登录按钮不可用
        self.login_btn.setEnabled(False)    
        self.account_tip.setVisible(False)
        self.pwd_tip.setVisible(False)
        self.success_tip.setVisible(False)

        
        # 监测输入框文本内容变化事件 textChanged
        self.account.textChanged.connect(self.account_textchange)
        # self.pwd.textChanged.connect(self.pwd_change)

        # 监测账号输入框文本编辑事件 textEdited
        self.account.textEdited.connect(self.account_pwd_textedit)

        # 监测密码输入框文本编辑事件 textEdited 清除标签原有提示
        self.pwd.textEdited.connect(self.account_pwd_textedit)

        # 监测登录按钮
        self.login_btn.clicked.connect(self.login) 

        # 给密码框设置清空按钮
        self.pwd.setClearButtonEnabled(True)

        # 给密码框设置输出模式 明文密文状态切换图片
        # addAction(QAction, QLineEdit.ActionPosition)
	        # QLineEdit.ActionPosition
		        # QLineEdit.LeadingPosition
			        # 搁前面
		        # QLineEdit.TrailingPosition
			        # 搁后面
        # addAction(QIcon, QLineEdit.ActionPosition) -> QAction
        # 定义action对象
        self.pwd_action=QAction(self.pwd)
        self.pwd_action.setIcon(QIcon(r'pyside2_pyqt\pys2\close.png'))
        self.pwd_action.triggered.connect(self.pwdstate_change)
        # 添加action  设置位置 
        # self.pwd.addAction(self.pwd_action,QLineEdit.LeadingPosition) 
        self.pwd.addAction(self.pwd_action,QLineEdit.TrailingPosition)

        # 给账号输入框设置自动补全
        # 设置completer完成器对象
        account_completer=QCompleter(['Sz','bq','boqi','wangzha'],self.account)
        self.account.setCompleter(account_completer)

        # 输入限制
            # 内容长度限制
                # 获取输入长度 maxLength() 
                # 设置限制输入的长度 setMaxLength(int)

            # 只读限制
                # setReadOnly(bool)
                # isReadOnly()
            # 规则验证
                # 设置验证器 setValidator(QValidator)
                # 掩码验证   setInputMask(mask_str)
	
            # 判断输入文本是否通过验证 hasAcceptableInput()
        

    def account_textchange(self):
        # 如果账号输入框有内容 则登录按钮可用 反之 不可用
        self.login_btn.setEnabled(len(self.account.text().strip()))
        
    def account_pwd_textedit(self):    
        # 清除原有的提示
        for lb in self.findChildren(QLabel):
            lb.setText('')

    # 密码框 状态切换行为 的slot函数
    def pwdstate_change(self):
        if self.pwd.echoMode() == QLineEdit.Password:#密文
            # 切换输出模式
            # self.pwd.setEchoMode(QLineEdit.PasswordEchoOnEdit)#编辑时明文, 结束后密文
            self.pwd.setEchoMode(QLineEdit.Normal)#普通
            # 更换图片
            self.pwd_action.setIcon(QIcon(r'pyside2_pyqt\pys2\open.png'))
        else:
            self.pwd.setEchoMode(QLineEdit.Password)
            self.pwd_action.setIcon(QIcon(r'pyside2_pyqt\pys2\close.png'))

    def login(self):
        print('点击了登录')
        # 置三个标签可见
        # 无提示时是不可见的
        self.account_tip.setVisible(True)
        self.pwd_tip.setVisible(True) 
        self.success_tip.setVisible(True)
        # 获取用户名和密码
        account=self.account.text()
        pwd=self.pwd.text()
        # 交给验证类，根据验证类返回的监测结果 采取相应动作
        login_state=AccountTool.check_login(account,pwd)
        # 账号错误
        if login_state == AccountTool.ACCOUNT_ERROR:
            # 展示提示
            self.account_tip.setText('用户名错误！')
            # self.account_tip.adjustSize()
            # 清空账号和密码输入框
            self.account.setText('')
            self.pwd.setText('')
            # 账号输入框获取焦点
            self.account.setFocus()
            return None
        # 密码错误
        if login_state == AccountTool.PWD_ERROR:
            # 展示提示
            self.pwd_tip.setText('密码错误！')
            self.pwd_tip.adjustSize()
            # 清空密码输入框
            self.pwd.setText('')
            # 密码输入框获取焦点
            self.pwd.setFocus()
            return None
        # 展示成功登录提示
        self.success_tip.setText('登录成功，即将跳转。。')
        self.success_tip.adjustSize()
    
    def resizeEvent(self,evt):
        # 控件宽高 自适应窗口
        margin_x=150
        margin_y=50
        margin_tip=10
        widget_x=self.width()-2*margin_x
        widget_y=40

        self.account.resize(widget_x,widget_y)
        self.pwd.resize(widget_x,widget_y)
        self.login_btn.resize(widget_x,widget_y)

        # 控件位置
        self.account.move(margin_x,self.height()/4)
        self.pwd.move(margin_x,self.account.y()+widget_y+margin_y)
        self.login_btn.move(margin_x,self.pwd.y()+widget_y+margin_y)

        # 标签位置
        self.account_tip.move(self.account.x(),self.account.y()+widget_y+margin_tip)
        self.pwd_tip.move(self.pwd.x(),self.pwd.y()+widget_y+margin_tip)
        self.success_tip.move(self.login_btn.x(),self.login_btn.y()+widget_y+margin_tip)

        # 标签宽度
        # adjustSize必须在有内容后设置，内容长度是变化的，因此在这里设置是无效的，反而会影响内容的显示
        # self.account_tip.adjustSize()
        # self.pwd_tip.adjustSize()
        # self.success_tip.adjustSize()

        

if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()