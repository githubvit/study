from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import os
# from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('文件对话框QFileDialog的学习')
        self.setup_ui()

    def setup_ui(self):
        btn=QPushButton(self)
        btn.setText('弹出文件对话框')
        btn.move(50,50)
        # 用静态方法 方便 快捷 打开 不用生成文件对话框对象  弹出模式为 模态级别 ，即阻塞。
        def FileDialog_handle():

            # 静态方法 快速 方便

            # result = QFileDialog.getOpenFileName(self, "", "./", "All(*.*);;Images(*.png *.jpg);;Python文件(*.py)", "Python文件(*.py)")
            # 打开一个文件(父控件，文件对话框标题，打开的路径，过滤菜单，选中的过滤菜单项) 输出是 （路径字符串，过滤项）
            # 当  文件对话框标题 为空 则显示标题为 “打开”   
            # 输出
                # 点击打开 输出 ('D:/pyj/st/study/1 内置函数.py', 'Python文件(*.py)') 或 ('D:/pyj/st/study/snap.png', 'Images(*.png *.jpg)')
                # 点击取消 输出 ('', 'Python文件(*.py)')

            # 过滤字符串格式   项目名称1(*.jpg *.png);;项目名称2(*.py)
            
            # result = QFileDialog.getOpenFileNames(self, "选择一批py文件", "./", "All(*.*);;Images(*.png *.jpg);;Python文件(*.py)", "Python文件(*.py)")
            # 打开一批文件（父控件，文件对话框标题，打开的路径，过滤菜单，选中的过滤菜单项）   输出是 （路径列表和过滤项） 
            # 输出 
                # (['D:/pyj/st/study/PEP8规范.py'], 'Python文件(*.py)')
            
            # result = QFileDialog.getOpenFileUrl(self, "选择一个py文件", QUrl("./"), "All(*.*);;Images(*.png *.jpg);;Python文件(*.py)", "Python文件(*.py)")
            # 打开一个文件资源（父控件，文件对话框标题，打开的路径，过滤菜单，选中的过滤菜单项）输出是 （资源url对象 fileurl:///,过滤项）
            # 与getOpenFileName效果是一样的，差别在于输出的一个是路径字符串，一个是路径url对象。
                # getOpenFileUrls(parent: QWidget = None, caption: str = '', directory: str = '', filter: str = '', initialFilter: str = '', options: Union[QFileDialog.Options, QFileDialog.Option] = 0, supportedSchemes: Iterable[str] = []) -> Tuple[List[QUrl], str]

            # result = QFileDialog.getSaveFileName(self, "保存一个py文件", "./", "All(*.*);;Images(*.png *.jpg);;Python文件(*.py)", "Python文件(*.py)")
            # 保存一个文件 -> Tuple[str, str]
                # getSaveFileUrl(parent: QWidget = None, caption: str = '', directory: str = '', filter: str = '', initialFilter: str = '', options: Union[QFileDialog.Options, QFileDialog.Option] = 0, supportedSchemes: Iterable[str] = []) -> Tuple[QUrl, str]
            # 输出
                # 输入文件名1312 点击保存 输出 ('D:/pyj/st/study/1312.py', 'Python文件(*.py)')

            # 获取文件夹

            result = QFileDialog.getExistingDirectory(self, "打开一个文件夹", "./")
            # 打开文件夹（父控件，文件对话框标题，打开的路径） -> str
            # 选定文件夹后 点击 选择文件夹 输出 D:/pyj/st/study/ctj

            # result = QFileDialog.getExistingDirectoryUrl(self, "打开一个文件夹", QUrl("./"))
            # 打开文件夹 同上 -> QUrl
            # 选择文件夹 输出
                # QWindowsNativeFileDialogBase::shellItem : Unhandled scheme:  ""
                # PySide2.QtCore.QUrl('file:///D:/pyj/st/study/8????/????')
            
                # QWindowsNativeFileDialogBase::shellItem : Unhandled scheme:  ""
                # PySide2.QtCore.QUrl('file:///D:/pyj/st/study/ATM/log')

            print(result)
            pass
        btn.clicked.connect(FileDialog_handle)    
if __name__ == "__main__":
    app = QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
    