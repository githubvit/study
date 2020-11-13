from PySide2.QtWidgets import QApplication
import os,sys

# 将项目加入系统路径
BASE_DIR=os.path.dirname(__file__)
sys.path.append(BASE_DIR)
# 引入界面
from view.view_c_1 import C1Ui
from view.view_l_1 import L1Ui
from view.view_r_1 import R1Ui

class App(QApplication):
    def __init__(self,*args):
        super().__init__(*args)

        # 初始化各个界面
        self.l_1=L1Ui()
        self.r_1=R1Ui()
        self.c_1=C1Ui()

        # 显示主界面 登录界面
        self.l_1.show()

        # 各个界面 信号 与 槽(完成界面打开和退出动作)

        self.l_1.l_register_signal.connect(self.open_register)
        self.l_1.login_signal.connect(self.open_caui)

        self.r_1.registerExit_signal.connect(self.exit_register)
        self.r_1.registerSignal.connect(lambda u,p: print(f'注册的用户名{u},密码{p}'))

    def open_register(self):
        self.r_1.show()
        self.l_1.hide()

    def open_caui(self,u,p):
        print(f'open_caui用户名{u},密码{p}')
        self.c_1.show()
        self.l_1.hide()

    def exit_register(self):
        self.l_1.show()
        self.r_1.hide()

if __name__ == "__main__":
    app=App([])
    app.exec_()

