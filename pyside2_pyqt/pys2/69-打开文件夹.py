# 启动一个单独的窗口 start
# 打开文件夹实际用的就是命令行
from PySide2.QtWidgets import QApplication,QWidget,QPushButton
import os



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300,100)
        self.setWindowTitle('文件对话框QFileDialog的学习')
        self.setup_ui()

    def setup_ui(self):
        btn=QPushButton(self)
        btn.setText('打开')
        btn.move(50,50)

        btn.clicked.connect(self.open_dir)

    def open_dir(self):
        # os.startfile('d:/')  #打开 D盘 ok
        # os.system('explorer')#打开 资源管理器 快速访问选项
        # os.system('start .') #打开 当前目录

        # os.system('start d:\\')   #打开 D盘 ok
        # os.system('start d:')     #打开 D盘 ok
        os.system('start d:/')      #打开 D盘 ok
        
        

if __name__ == "__main__":
    pass
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()

