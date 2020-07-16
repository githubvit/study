from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('对话框QDialog的学习')

        self.setup_ui()

    def setup_ui(self):
        # QDialog是对话窗口的基类
        # 对话窗口是顶级窗口，主要用于短期任务和与用户的简短通信。
        dlg=QDialog(self)
        self.dlg=dlg
        dlg.setWindowTitle('对话框标题')
        dlg.resize(300,50)

        # 1 三种打开方式 对应 三种对话框模式
        # dlg.exec_() #应用程序级 模态对话框 只打开一个窗口 即对话框 只有处理完该对话框 程序才能干别的 
        # dlg.open()  #窗口级 模态对话框 打开两个窗口 对话框为当前窗口，主窗口失去焦点，主窗口不能处理。
                        # 如果主窗口不是对话框的父控件，则 两个窗口无关联，可任意处理。
        # dlg.show()  #普通非模态对话框 打开两个窗口 两个窗口可切换 可单独处理。

        # 2 常用操作
        # 结合show方法将普通非模态对话框设置为模态对话
        # dlg.setModal(True) #一定要在show前设置，show后不行，达到窗口级 模态对话框
        # dlg.show()
        
        # 结合setWindowModality(Qt.WindowModal)也可以实现模态对话框
	        # Qt.WindowModal
	        # Qt.ApplicationModal
        # dlg.setWindowModality(Qt.ApplicationModal) # 必须在show前
        # dlg.show()

        # 是否显示尺寸调整控件 即使没有尺寸控件 也不影响尺寸调整
	        # setSizeGripEnabled(bool)
	        # isSizeGripEnabled() -> bool
        print(dlg.isSizeGripEnabled())#False
        dlg.setSizeGripEnabled(True)    

        # 3 按钮测试 弹出对话框
        btn=QPushButton(self)
        btn.setText('测试')
        btn.move(100,100)
        # btn.clicked.connect(lambda : dlg.exec_()) # 弹出对话框为当前窗口，主窗口失去焦点，主窗口不能处理。
        # btn.clicked.connect(lambda : dlg.open())  # 弹出对话框为当前窗口，主窗口失去焦点，主窗口不能处理。
        btn.clicked.connect(lambda : dlg.show())  # 打开两个窗口 两个窗口可切换 可单独处理。
        
        # 4 信号与槽
            # accepted、rejected、finished信号

        def accept_do():
            # 设置值
            self.dlg.setResult(1314) # 依然会向finished信号传递参数 1
            print ('accept',self.dlg.result())

        def reject_do():
            print ('reject')

        def done_do(val):
            print ('done',val)
       
        # 在对话框中添加按钮 激发对话框信号
        accept_btn=QPushButton(self.dlg)
        accept_btn.setText('accept')
        accept_btn.resize(50,30)
        accept_btn.move(10,10)
        # 激发 对话框 accepted信号
        accept_btn.clicked.connect(lambda :self.dlg.accept() ) # 会同时激发finished信号 即done信号 并传递 1
        # 设置 accepted槽 函数
        self.dlg.accepted.connect(accept_do)

        reject_btn=QPushButton(self.dlg)
        reject_btn.setText('reject')
        reject_btn.resize(50,30)
        reject_btn.move(60,10)
        # 激发 对话框 rejected信号
        reject_btn.clicked.connect(lambda :self.dlg.reject()) # 会同时激发finished信号 即done信号 并传递 0
        # 设置 rejected信号槽 函数
        self.dlg.rejected.connect(reject_do)

        done_btn=QPushButton(self.dlg)
        done_btn.setText('done')
        done_btn.resize(50,30)
        done_btn.move(110,10)

        # 点击 对话框 右上角 x 按钮 也会 激发done即finished信号 且 默认参数为0

        # 激发 对话框 done即finished信号 带整型参数 
        # 当参数设为0 会联动 rejected信号 即 = 按下 对话框的 右上角 x 按钮
        # 当参数设为1 会联动 accepted信号
        # 其余值不会联动信号。
        done_btn.clicked.connect(lambda : self.dlg.done(2))
        # 设置 done即finished槽 函数 
        self.dlg.finished.connect(done_do)

        # 5 对话框设置值
        # 设置 值 不同的按钮设置不同的值
        set_btn=QPushButton(self.dlg)
        set_btn.setText('set')
        set_btn.resize(50,30)
        set_btn.move(180,10)
        set_btn.clicked.connect(lambda : self.dlg.setResult(1314))
        # 对话框外
        set_btn1=QPushButton(self)
        set_btn1.setText('set1')
        set_btn1.resize(50,30)
        set_btn1.move(180,10)
        set_btn1.clicked.connect(lambda : self.dlg.setResult(1000))

        # 获取 值 默认是0
        get_btn=QPushButton(self.dlg)
        get_btn.setText('get')
        get_btn.resize(50,30)
        get_btn.move(230,10)
        get_btn.clicked.connect(lambda : print(self.dlg.result()))

        # 对话框外
        get_btn1=QPushButton(self)
        get_btn1.setText('get1')
        get_btn1.resize(50,30)
        get_btn1.move(230,10)
        get_btn1.clicked.connect(lambda : print(self.dlg.result()))
       

        pass

if __name__ == "__main__":
    app = QApplication([])
    wd=Window()
    wd.show()
    app.exec_()