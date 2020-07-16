from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# from PyQt5.Qt import *

# 界面 ：按钮1 按钮2 文本框 

# 点击按钮1，弹出打开文件对话框，选择文件，
# 点击ok,在文本框展示选中文件并编辑，
# 点击按钮2，弹出保存文件对话框，输入文件名，保存。
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('文件对话框QFileDialog-案例的学习')
        self.file_path=''  #初始为空
        self.setup_ui()

    def setup_ui(self):
        open_btn=QPushButton(self)
        open_btn.setText('打开文件对话框')
        open_btn.adjustSize()
        open_btn.move(50,50)   
        open_btn.clicked.connect(self.get_path)
       

        save_btn=QPushButton(self)
        save_btn.setText('保存文件对话框')
        save_btn.adjustSize()
        save_btn.move(250,50)
        save_btn.clicked.connect(self.save_file)

        self.edit_text=QTextEdit(self)
        self.edit_text.setPlaceholderText('打开并编辑')
        self.edit_text.resize(400,250)
        self.edit_text.move(50,100)

         

    # 打开文本
    def get_path(self):
        # 获取要打开的文本路径和名称
        path=QFileDialog.getOpenFileName(self, "", "./", "All(*.*);;Images(*.png *.jpg);;Python文件(*.py);;文本文件(*.txt)", "文本文件(*.txt)")[0]
        if len(path.strip()):
            # 读取文本
            with open(path,'r',encoding="utf-8") as file:
                str=file.read()
                # 在文本框展示
                self.edit_text.setText(str)
        
    # 保存文本
    def save_file(self):
        # 获取文本框文本
        str=self.edit_text.toPlainText()
        # 获取要保存的文件路径和文件名
        path=QFileDialog.getSaveFileName(self, "", "./", "All(*.*);;Images(*.png *.jpg);;Python文件(*.py);;文本文件(*.txt)", "文本文件(*.txt)")[0]
        if len(path.strip()):
            # 将文本框的文本，写入输入的文件
            with open(path,'w',encoding="utf-8") as file:
                file.write(str)

if __name__ == "__main__":
    app = QApplication([])
    wd=Window()
    wd.show()
    app.exec_()