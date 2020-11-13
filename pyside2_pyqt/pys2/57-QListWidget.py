
'''
扩展的列表控件 QListWidget 

是 QListView 的子类，添加了许多的api

不仅可以通过模型model添加数据，还可以直接添加数据

添加了信号：
    currentRowChanged(row:int) 行变化
    currentTextChanged(text)  文本变化
    currentItemChanged(当前条目newitme，以前条目olditem)) 条目变化

直接添加数据api：
    addItems(iterable)
    addItem(item)
    insertItems(row,iterable)
    insertItem(row,item)


'''

from PySide2.QtWidgets import QApplication, QWidget,  QListWidget, QVBoxLayout,QMessageBox
from PySide2.QtCore import  QStringListModel


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QListWidget的学习')
        self.resize(300,300)
        self.setup_ui()

    def setup_ui(self):
        # 1 定义QListWidget
        lw=QListWidget()
        self.lw=lw
        
        # 2 添加数据项
        lw.addItem('item1')
        lw.addItem('item2')
        lw.addItem('item3')
        lw.addItem('item4')
        lw.addItem('item5')

        # 4 布局
        # 采用布局就没有滚动条，可以看到全貌
        layout=QVBoxLayout(self)
        layout.addWidget(lw)

        # 5 点击事件
        lw.itemClicked.connect(self.showText)

    def showText(self,idx):
        QMessageBox.information(self,'QListWidget','您选择了'+self.lw.item(self.lw.row(idx)).text()) #item.row()可以获取行号，即是在lst中的索引


if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
    pass