
'''
用表格QTableView控件显示数据

MVC：Model Viewer Controller

需要创建QTableView实例和一个数据源（Model）,然后将两者关联。

这样定义，将model数据和vie前端视图的耦合度降低。
'''

from PySide2.QtWidgets import QApplication, QWidget, QTableView, QListView, QVBoxLayout
from PySide2.QtCore import  QStringListModel
from PySide2.QtGui import QStandardItemModel,QStandardItem


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QTableView的学习')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        # 1 数据表 model
        # 定义数据表 4行3列
        md=QStandardItemModel(4,3)
        # 设置字段
        md.setHorizontalHeaderLabels(['id','姓名','年龄'])
        # 添加数据
        data=[
            ('10','雷神','2800'),
            ('20','美国队长','200'),
            ('30','黑寡妇','3200'),
            ('40','钢铁侠','1800'),
        ]
        for idx,item in enumerate(data):
            idn,name,age=[QStandardItem(i) for i in item]
            md.setItem(idx,0,idn)   #第idx行第一列
            md.setItem(idx,1,name)  #第idx行第二列
            md.setItem(idx,2,age)   #第idx行第三列
        
        # 老方法：
        # item11=QStandardItem('10')      
        # item12=QStandardItem('雷神')    
        # item13=QStandardItem('2800')      
        # md.setItem(0,0,item11) #第一行第一列
        # md.setItem(0,1,item12) #第一行第二列
        # md.setItem(0,2,item13) #第一行第三列

        # 2 定义view
        # tv=QTableView(self)
        tv=QTableView()
        
        # 3 关联 view和model
        tv.setModel(md)

        # 4 布局
        # 采用布局就没有滚动条，可以看到全貌
        layout=QVBoxLayout(self)
        layout.addWidget(tv)
        
        pass
    pass

if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
    pass