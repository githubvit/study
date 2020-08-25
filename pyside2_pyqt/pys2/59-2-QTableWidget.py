
'''
扩展的表格控件 QTableWidget 

放置控件 setCellWidget

'''
from PySide2.QtWidgets import QApplication, QWidget, QTableWidget, QPushButton,\
    QVBoxLayout,QTableWidgetItem,QAbstractItemView,QComboBox
from PySide2.QtCore import *



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QTableWidget的学习-2')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):

        # 1 定义
        tw=QTableWidget()

        # 2 设置行和列
        tw.setRowCount(4)
        tw.setColumnCount(3)

        # 3 设置表头
        tw.setHorizontalHeaderLabels(['姓名','性别','体重(kg)'])

        # 4 添加数据、控件
        # 添加文本数据用：QTableWidgetItem(i) tw.setItem(行,列,QTableWidgetItem(i))
        item1=QTableWidgetItem('小米')
        tw.setItem(0,0,item1)

        # 添加控件用：setCellWidget(行，列，Qwidget（）)

        # 添加下拉列表
        combox=QComboBox()
        # 添加表项
        combox.addItems(['男','女'])
        combox.setStyleSheet('margin:3px')
        tw.setCellWidget(0,1,combox)
        
        # 添加按钮
        btn=QPushButton('修改')
        btn.setCheckable(True)
        btn.setChecked(True)
        btn.setStyleSheet('margin:3px')
        tw.setCellWidget(0,2,btn)
        
    

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