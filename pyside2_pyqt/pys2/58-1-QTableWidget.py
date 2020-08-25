
'''
扩展的表格控件 QTableWidget 

是 QTableView 的子类，添加了许多的api

每一个Cell（单元格）是一个QTableWidgetItem

不仅可以通过模型model添加数据，还可以直接添加数据

'''
from PySide2.QtWidgets import QApplication, QWidget, QTableWidget, QVBoxLayout,QTableWidgetItem,QAbstractItemView
from PySide2.QtCore import *



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QTableWidget的学习')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):

        # 1 定义
        tw=QTableWidget()

        # 2 设置行和列
        tw.setRowCount(4)
        tw.setColumnCount(3)

        # 3 设置表头
        tw.setHorizontalHeaderLabels(['id','姓名','年龄'])
        # tw.setVerticalHeaderLabels(['a','b','c'])

        # 4 添加数据
        data=[
            ('10','雷神','2800'),
            ('20','美国队长','200'),
            ('30','黑寡妇','3200'),
            ('40','钢铁侠','1800'),
        ]
        for idx,item in enumerate(data):
            idn,name,age=[QTableWidgetItem(i) for i in item]
            tw.setItem(idx,0,idn)   #第idx行第一列
            tw.setItem(idx,1,name)  #第idx行第二列
            tw.setItem(idx,2,age)   #第idx行第三列
    
        # 5 禁止编辑、整行选择
        tw.setEditTriggers(QAbstractItemView.NoEditTriggers)
        tw.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 6 列和行尺寸自适应内容
        tw.resizeRowsToContents()
        tw.resizeColumnsToContents()

        # 7 关闭表头
        tw.horizontalHeader().setVisible(False) #关闭水平表头
        tw.verticalHeader().setVisible(False) #关闭竖直表头

        # 8 隐藏表格线条
        tw.setShowGrid(False)
    

        # 布局
        # 采用布局就没有滚动条，可以看到全貌
        layout=QVBoxLayout(self)
        layout.addWidget(tw)
        
        pass
    pass

if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
    pass