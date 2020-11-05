from PySide2.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QFileDialog
from PySide2.QtCore import Signal,Slot

import os,sys



# 一 取得项目根目录加入系统目录
# print(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
# 把项目根目录加入环境变量 然后其它导入就有根了
sys.path.append(BASE_DIR)

# 二 显示ui框架 （2.1 2 3 即可显示ui 2.4 开始属于扩展 动作部分）
# 2.1 导入从 Designer 设计师 转成的py文件中的  界面类  用于 多继承
from resource.ui.Ui_m_key import Ui_Form

# 三 联结 主逻辑
# 3.1 导入主逻辑程序
import m_encrypter

class MKeyUi(QWidget,Ui_Form):
    
    def __init__(self,parent=None):
        # 2.2 继承父类初始化
        super().__init__(parent) 
      
        # 2.3 导入界面类setupUi函数，填入 self 参数作为父类。
        self.setupUi(self)
        # 隐藏提示标签
        self.tip_lb.setText('')
       

    # 2.4 信号 槽
    @Slot()
    def on_key_name_le_textChanged(self):
        # 隐藏提示标签
        self.tip_lb.setText('')
        print('name',self.key_name_le.text())
        self.mkey_btn.setEnabled(len(self.key_name_le.text().strip()))#让 制作密钥 按钮可用
        pass

    # 回车
    @Slot()
    def on_key_name_le_returnPressed(self):
        self.make_key()
    @Slot()
    def on_mkey_btn_clicked(self):
        self.make_key()

    # 打开密钥目录
    @Slot()
    def on_path_btn_clicked(self):
        # 获取目录
        key_dir=m_encrypter.smt_key_dir()
        print(f'打开密钥目录 {key_dir}')
        os.system(f'start {key_dir}')
    # 制作密钥   
    def make_key(self):
        # 取得密钥名称
        name=self.key_name_le.text()
        # 3.2 调用主逻辑 m_encrypter 的密钥文件生成函数
        v=m_encrypter.build_keyfile_by_name(name)
        print(v)
        # 清空
        self.key_name_le.setText('')
        if v==1:
            self.tip_lb.setText('密钥制作成功!')
            self.tip_lb.setStyleSheet('color:green;')
            self.tip_lb.show()

        elif v==2:
            self.tip_lb.setText('该密钥已存在,请换个名称')
            self.tip_lb.setStyleSheet('color:black;')
            self.tip_lb.show()
        else:
            self.tip_lb.setText('未知错误!!')
            self.tip_lb.setStyleSheet('color:red;')
            self.tip_lb.show()          


if __name__ == "__main__":
    
    app=QApplication([])
    wd=MKeyUi()
    wd.show()
    app.exec_()