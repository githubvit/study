from PySide2.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QFileDialog
from PySide2.QtCore import Signal,Slot

import os,sys



# 一 取得项目根目录加入系统目录
# print(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
# 把项目根目录加入环境变量 然后其它导入就有根了
sys.path.append(BASE_DIR)

# 1 导入从 Designer 设计师 转成的py文件中的  界面类  用于 多继承
from resource.ui.Ui_encrypt import Ui_Form

# 三 联结 主逻辑
# 3.1 导入主逻辑程序
import m_encrypter

class EncryptUi(QWidget,Ui_Form):
    
    def __init__(self,parent=None):
        # 3 继承父类初始化
        super().__init__(parent) 
      
        # 4 导入界面类setupUi函数，填入 self 参数作为父类。
        self.setupUi(self)

        # 隐藏提示标签
        self.tip_lb.setText('')
        
    
    # 调用主逻辑 程序 加密文件
    def encrypt_file(self):
        # 获取并判定文件路径和密钥路径的存在
        file_path=self.file_le.text().strip()
        key_path=self.key_le.text().strip()
        # 判定key_path 是pem格式的密钥文件
        val=key_path.split('.')[-1]
        if self.file_judge(file_path) and self.file_judge(key_path) and val=='pem':
            try:
                m_encrypter.encrypt_file(file_path,key_path)

                self.tip_lb.setText('加密文件成功.')
                self.tip_lb.setStyleSheet('color:green;')
                self.tip_lb.show()
                # 清空
                self.file_le.setText('')
                self.key_le.setText('')
            except Exception as e:
                self.tip_lb.setText('奇怪的文件名！')
                self.tip_lb.setStyleSheet('color:red;')
                self.tip_lb.show()

            
        else:
            self.tip_lb.setText('路径或密钥格式错误！')
            self.tip_lb.setStyleSheet('color:red;')
            self.tip_lb.show()
                        
    # 文件判定
    def file_judge(self,file_name):
        # 是否是文件
        v1=os.path.isfile(file_name)
        # 是否存在
        v2=os.path.exists(file_name)
        v=v1 and v2
        return v
            

    @Slot()
    def on_file_btn_clicked(self):
        # 隐藏提示标签
        self.tip_lb.setText('')
        # 选择解密文件夹
        decrypt_dir=m_encrypter.smt_decrypt_dir()
        # 选择要加密的文件
        file_path=QFileDialog.getOpenFileName(self, "选择要加密的文件", decrypt_dir, "All(*.*)", "All(*.*)")[0]
        self.file_le.setText(file_path)
        


    @Slot()
    def on_key_btn_clicked(self):
        # 隐藏提示标签
        self.tip_lb.setText('')
        # 获取当前公钥目录
        key_dir=m_encrypter.smt_key_dir()
        # 选择要加密的私钥文件 .pem格式
        key_path=QFileDialog.getOpenFileName(self, "选择公钥文件", key_dir+'/pub', "密钥文件(*.pem)", "密钥文件(*.pem)")[0]
        self.key_le.setText(key_path)


    @Slot()
    def on_file_le_textChanged(self):
        # 判定加密按钮是否可用
        val=len(self.file_le.text().strip()) and len(self.key_le.text().strip())
        self.encrypt_btn.setEnabled(val)

    @Slot()
    def on_key_le_textChanged(self):
        # 判定加密按钮是否可用
        val=len(self.file_le.text().strip()) and len(self.key_le.text().strip())
        self.encrypt_btn.setEnabled(val)
        

    # 给回车添加处理
    @Slot()
    def on_file_le_editingFinished(self):
        # print('file完成')
        if len(self.file_le.text().strip()) and len(self.key_le.text().strip()):
            self.encrypt_file()
        

    @Slot()
    def on_key_le_editingFinished(self):
        # print('key完成')
        if len(self.file_le.text().strip()) and len(self.key_le.text().strip()):
            self.encrypt_file()
        

    # 加密
    @Slot()
    def on_encrypt_btn_clicked(self):
        self.encrypt_file()

    # 打开加密文件目录
    @Slot()
    def on_path_btn_clicked(self):
        # 获取目录
        encrypt_dir=m_encrypter.smt_encrypt_dir()
        print(f'打开加密文件目录 {encrypt_dir}')
        os.startfile(encrypt_dir)
       

if __name__ == "__main__":
    
    app=QApplication([])
    wd=EncryptUi()
    wd.show()
    app.exec_()