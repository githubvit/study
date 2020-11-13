from PySide2.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QFileDialog
from PySide2.QtCore import Signal,Slot

import os,sys



# 一 取得项目根目录加入系统目录
# print(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
# 把项目根目录加入环境变量 然后其它导入就有根了
sys.path.append(BASE_DIR)

# 1 导入从 Designer 设计师 转成的py文件中的  界面类  用于 多继承
from resource.ui.Ui_decrypt import Ui_Form

# 三 联结 主逻辑
# 3.1 导入主逻辑程序
import m_encrypter

class DecryptUi(QWidget,Ui_Form):
    
    def __init__(self,parent=None):
        # 2 继承父类初始化
        super().__init__(parent) 
      
        # 3 导入界面类setupUi函数，填入 self 参数作为父类。
        self.setupUi(self)

        # 隐藏提示标签
        self.tip_lb.setText('')

        # self.prikey_le
        # self.prikey_btn
        # self.encrypt_file_btn
        # self.encrypt_file_le
        # self.decrypt_btn
        # self.tip_lb
        # self.path_btn

    # 关闭时 隐藏提示标签
    def closeEvent(self, *args, **kwargs):
        super().closeEvent( *args, **kwargs)
        # 隐藏提示标签
        self.tip_lb.setText('')
        # print('关闭解密文件窗口')

    def decrypt_file(self):
        encrypt_file=self.encrypt_file_le.text().strip()
        prikey_file=self.prikey_le.text().strip()
        # 判定key_path 是pem格式的密钥文件
        val=prikey_file.split('.')[-1]
        if self.file_judge(encrypt_file) and self.file_judge(prikey_file) and val=='pem':
            try:
                # 调用主逻辑的解密功能
                m_encrypter.decrypt_file(encrypt_file,prikey_file)

                self.tip_lb.setText('解密文件成功.')
                self.tip_lb.setStyleSheet('color:green;')
                self.tip_lb.show()
                # 清空
                self.encrypt_file_le.setText('')
                self.prikey_le.setText('')
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
    def on_encrypt_file_btn_clicked(self):
        # 隐藏提示标签
        self.tip_lb.setText('')
        # 获取加密文件夹
        encrypt_dir=m_encrypter.smt_encrypt_dir()
        # 选择要加密的文件
        file_name=QFileDialog.getOpenFileName(self, "选择要解密的文件", encrypt_dir, "All(*.*)", "All(*.*)")[0]
        self.encrypt_file_le.setText(file_name)
        


    @Slot()
    def on_prikey_btn_clicked(self):
        # 隐藏提示标签
        self.tip_lb.setText('')
        # 获取当前密钥目录
        key_dir=m_encrypter.smt_key_dir()
        # 选择要加密的私钥文件 .pem格式
        prikey_name=QFileDialog.getOpenFileName(self, "选择私钥文件", key_dir+"/pri", "密钥文件(*.pem)", "密钥文件(*.pem)")[0]
        
        self.prikey_le.setText(prikey_name)


    @Slot()
    def on_encrypt_file_le_textChanged(self):
        # 判定解密按钮是否可用
        val=len(self.encrypt_file_le.text().strip()) and len(self.prikey_le.text().strip())
        self.decrypt_btn.setEnabled(val)

    @Slot()
    def on_prikey_le_textChanged(self):
        # 判定解密按钮是否可用
        val=len(self.encrypt_file_le.text().strip()) and len(self.prikey_le.text().strip())
        self.decrypt_btn.setEnabled(val)
        

    # 给回车添加处理
    @Slot()
    def on_encrypt_file_le_editingFinished(self):
        # print('file完成')
        if len(self.encrypt_file_le.text().strip()) and len(self.prikey_le.text().strip()):
            self.decrypt_file()
        

    @Slot()
    def on_prikey_le_editingFinished(self):
        # print('key完成')
        if len(self.encrypt_file_le.text().strip()) and len(self.prikey_le.text().strip()):
            self.decrypt_file()
        

    # 加密
    @Slot()
    def on_decrypt_btn_clicked(self):
        self.decrypt_file()

    # 打开解密文件目录
    @Slot()
    def on_path_btn_clicked(self):
        # 获取目录
        decrypt_dir=m_encrypter.smt_decrypt_dir()
        print(f'打开解密文件目录 {decrypt_dir}')
        os.startfile(decrypt_dir)

if __name__ == "__main__":
    
    app=QApplication([])
    wd=DecryptUi()
    wd.show()
    app.exec_()