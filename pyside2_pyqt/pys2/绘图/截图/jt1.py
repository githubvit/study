from PyQt5 import QtCore, QtWidgets,QtGui
'''
一 下面两行是PyQt 截屏的关键代码：

    screen= QtWidgets.QApplication.primaryScreen()#PyQt5
    screen.grabWindow(QtWidgets.QApplication.desktop().winId())#PyQt5

二 python 封装的Windows系统的api接口

    import win32gui

    python对Win32 SDK中的 GUI绘图 API函数 的封装
    windows 用户界面接口

    win32gui 可以指定获取的窗口，即使窗口被遮挡。需注意的是，窗口最小化时无法获取截图。
    首先需要获取窗口的句柄。

    hwnd = win32gui.FindWindow(None, 'C:Windowssystem32cmd.exe') #查找 title 为 'C:Windowssystem32cmd.exe' 的窗口

    有了title 'C:Windowssystem32cmd.exe' 就可以进行截图了

    安装 pip install pywin32

    就可以使用如下 接口

    win32api、win32gui、win32con一般对窗口进行操作都是会用到的

'''

class Screenshot(QtWidgets.QWidget):
    def __init__(self):
        super(Screenshot, self).__init__()
        self.screenshotLabel = QtWidgets.QLabel()
        self.screenshotLabel.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                QtWidgets.QSizePolicy.Expanding)
        self.screenshotLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.screenshotLabel.setMinimumSize(240, 160)
        self.createOptionsGroupBox()
        self.createButtonsLayout()
        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addWidget(self.screenshotLabel) #标签
        mainLayout.addWidget(self.optionsGroupBox) #选项
        mainLayout.addLayout(self.buttonsLayout) #按钮
        self.setLayout(mainLayout)
        self.shootScreen()
        self.delaySpinBox.setValue(0) #延迟多少秒后截屏
        self.setWindowTitle("Screenshot")
        self.resize(300, 200)
        
    def resizeEvent(self, event):
        scaledSize = self.originalPixmap.size()
        scaledSize.scale(self.screenshotLabel.size(), QtCore.Qt.KeepAspectRatio)
        if not self.screenshotLabel.pixmap() or scaledSize != self.screenshotLabel.pixmap().size():
            self.updateScreenshotLabel()
            
    def newScreenshot(self):
        if self.hideThisWindowCheckBox.isChecked():
            self.hide()
        self.newScreenshotButton.setDisabled(True)
        QtCore.QTimer.singleShot(self.delaySpinBox.value() * 1000,
                self.shootScreen)
                
    def saveScreenshot(self):
        format = 'png'
        initialPath = QtCore.QDir.currentPath() + "/untitled." + format
        fileName,filetype = QtWidgets.QFileDialog.getSaveFileName(self, "Save As",
                initialPath,
                "%s Files (*.%s);;All Files (*)" % (format.upper(), format))
        if fileName:
            self.originalPixmap.save(fileName, format)
            print("file saved as  %s" % fileName)
    # 截屏   
    def shootScreen(self):
        if self.delaySpinBox.value() != 0:
            QtWidgets.qApp.beep()
        # Garbage collect any existing image first.
        self.originalPixmap = None
        #self.originalPixmap = QtGui.QPixmap.grabWindow(QtWidgets.QApplication.desktop().winId())#PyQt4
       
        screen= QtWidgets.QApplication.primaryScreen()  #PyQt5 获取屏幕
        self.originalPixmap = screen.grabWindow(QtWidgets.QApplication.desktop().winId()) #PyQt5 截屏
        # 将截屏设置给标签
        self.updateScreenshotLabel()
        self.newScreenshotButton.setDisabled(False)
        if self.hideThisWindowCheckBox.isChecked():
            self.show()
            
    def updateCheckBox(self):
        if self.delaySpinBox.value() == 0:
            self.hideThisWindowCheckBox.setDisabled(True)
        else:
            self.hideThisWindowCheckBox.setDisabled(False)
    # 选项  
    def createOptionsGroupBox(self):
        self.optionsGroupBox = QtWidgets.QGroupBox("Options")
        self.delaySpinBox = QtWidgets.QSpinBox()
        self.delaySpinBox.setSuffix(" s")
        self.delaySpinBox.setMaximum(60)
        self.delaySpinBox.valueChanged.connect(self.updateCheckBox)
        self.delaySpinBoxLabel = QtWidgets.QLabel("Screenshot Delay:")
        self.hideThisWindowCheckBox = QtWidgets.QCheckBox("Hide This Window")
        optionsGroupBoxLayout = QtWidgets.QGridLayout()
        optionsGroupBoxLayout.addWidget(self.delaySpinBoxLabel, 0, 0)
        optionsGroupBoxLayout.addWidget(self.delaySpinBox, 0, 1)
        optionsGroupBoxLayout.addWidget(self.hideThisWindowCheckBox, 1, 0, 1, 2)
        self.optionsGroupBox.setLayout(optionsGroupBoxLayout)
    # 按钮    
    def createButtonsLayout(self):
        self.newScreenshotButton = self.createButton("New Screenshot",
                self.newScreenshot)
        self.saveScreenshotButton = self.createButton("Save Screenshot",
                self.saveScreenshot)
        self.quitScreenshotButton = self.createButton("Quit", self.close)
        self.buttonsLayout = QtWidgets.QHBoxLayout()
        self.buttonsLayout.addStretch()
        self.buttonsLayout.addWidget(self.newScreenshotButton)  #新截屏
        self.buttonsLayout.addWidget(self.saveScreenshotButton) #保存截屏
        self.buttonsLayout.addWidget(self.quitScreenshotButton) #退出
    def createButton(self, text, member):
        button = QtWidgets.QPushButton(text)
        button.clicked.connect(member)
        return button

    # 设置标签的图片为截屏 并按比例更新标签图片的大小 
    def updateScreenshotLabel(self):
        self.screenshotLabel.setPixmap(self.originalPixmap.scaled(
                self.screenshotLabel.size(), QtCore.Qt.KeepAspectRatio,
                QtCore.Qt.SmoothTransformation))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    screenshot = Screenshot()
    screenshot.show()
    sys.exit(app.exec_())
