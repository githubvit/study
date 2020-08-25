
'''
显示列表数据 QListView

MVC：Model Viewer Controller

需要创建QListView实例和一个数据源（Model）,然后将两者关联。

这样定义，将model数据和vie前端视图的耦合度降低。
'''

from PySide2.QtWidgets import QApplication, QWidget,  QListView, QVBoxLayout,QMessageBox
from PySide2.QtCore import  QStringListModel



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QListView的学习')
        self.resize(300,300)
        self.setup_ui()

    def setup_ui(self):
        # 1 数据表 model
        # 定义数据源 字符串列表
        md=QStringListModel()
        # 添加数据 设置列表项
        lst=['列表项1','列表项2','列表项3']
        self.lst=lst
        md.setStringList(lst)
   
        # 2 定义view
        # lv=QListView(self)
        lv=QListView()
        
        # 3 关联 view和model
        lv.setModel(md)

        # 4 布局
        # 采用布局就没有滚动条，可以看到全貌
        layout=QVBoxLayout(self)
        layout.addWidget(lv)

        # 5 点击事件
        lv.clicked.connect(self.showText)

    def showText(self,item):
        QMessageBox.information(self,'QListView','您选择了'+self.lst[item.row()]) #item.rw()可以获取行号，即是在lst中的索引



        
        pass
    pass

if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
    pass