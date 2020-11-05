from PySide2.QtWidgets import QApplication
import sys,os

# 找到项目根目录
BASE_DIR=os.path.dirname(__file__) # 取得父目录，即项目根目录

# 把项目根目录加入环境变量 然后其它导入就有根了
sys.path.append(BASE_DIR)

# 系统托盘图标文件
from encrypter_icon import SIcon
# 引入view
from view.view_mui import MuiUi
from view.view_m_key import MKeyUi
from view.view_decrypt import DecryptUi
from view.view_encrypt import EncryptUi

class App(QApplication):
    def __init__(self,*args):
        super().__init__(*args)
        # 1 设置窗口关闭 并不退出程序  
        # 默认是True  就会导致关闭界面时退出程序。
        self.setQuitOnLastWindowClosed(False)   # *******  很重要 对于系统托盘应用    ***********
       
        # 2 系统托盘图标
        self.sicon=SIcon()
        self.sicon.setToolTip('加解密')
        # 3 初始化 各个界面
        self.main_ui=MuiUi()             #主界面
        self.mkey=MKeyUi()               #制作密钥界面
        self.encrypt_file=EncryptUi()    #加密界面
        self.decrypt_file=DecryptUi()    #解密界面
        # 4 打开系统图标
        self.sicon.show()
        

        # 5 信号 与 槽(完成界面打开和退出动作)

        # 系统图标 信号
        self.sicon.main_ui_signal.connect(self.main_ui.show)          # 左键 主界面信号
        self.sicon.m_k_signal.connect(self.mkey.show)                 # 右键 制作密钥信号
        self.sicon.encrypt_signal.connect(self.encrypt_file.show)     # 右键 加密信号
        self.sicon.decrypt_signal.connect(self.decrypt_file.show)     # 右键 解密信号
        self.sicon.exit_signal.connect(self.quit)                     # 右键 退出信号 

        # 主界面 信号 
        self.main_ui.m_k_signal.connect(self.mkey.show )
        self.main_ui.encrypt_signal.connect(self.encrypt_file.show)
        self.main_ui.decrypt_signal.connect(self.decrypt_file.show)
        self.main_ui.exit_signal.connect(self.quit)


if __name__ == "__main__":    
   
    app=App([])
   
    app.exec_()
