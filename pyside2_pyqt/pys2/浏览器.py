import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self,parent = None):
        super().__init__(parent)
        # self.setGeometry(QApplication.desktop().screenGeometry())
        self.resize(900,600)
        self.showMaximized()
        self.setWindowTitle("Browser")
        self.setFont(QFont("宋体",18))
        self.tool_bar=self.addToolBar("toolbar")
        self.back_action = self.tool_bar.addAction("退后")
        self.forward_action = self.tool_bar.addAction("向前")
        self.reload_action = self.tool_bar.addAction("重载")
        self.main_action = self.tool_bar.addAction("主页")
        self.line_edit = QLineEdit(self)
        self.line_edit.setMaximumWidth(500)
        self.line_edit.setFixedHeight(32)
        self.tool_bar.addWidget(self.line_edit)


        self.view = View(self)
        self.line_edit.setText(self.view.url().toString())
        self.setCentralWidget(self.view)

        self.back_action.triggered.connect(self.view.back)
        self.forward_action.triggered.connect(self.view.forward)
        self.reload_action.triggered.connect(self.view.reload)
        self.main_action.triggered.connect(lambda :self.view.load("https://www.hao123.com"))
        self.view.urlChanged.connect(lambda url:self.line_edit.setText(url.toString()))
        self.line_edit.editingFinished.connect(lambda :self.view.load(self.line_edit.text()))
        self.progress_bar = QProgressBar(self)
        status_label = QLabel("网页加载状态：",self)
        self.statusBar().addWidget(status_label)
        self.statusBar().addWidget(self.progress_bar)

        self.view.loadStarted.connect(lambda :(self.progress_bar.show(),
                                      status_label.setText("网页加载状态：")))
        self.view.loadProgress.connect(lambda n:self.progress_bar.setValue(n))
        self.view.loadFinished.connect(lambda :(self.progress_bar.hide(),
                                                status_label.setText("网页加载状态：完毕！")))



class View(QWebEngineView):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.load(QUrl("https://www.baidu.com"))
        self.setWindowTitle("New Page")
        self.show()

    # 简单重载了下createWindow函数，实现鼠标点击链接在新窗口打开
    def createWindow(self,type):
        self.newView = View()
        self.newView.resize(900,600)
        return self.newView



if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

