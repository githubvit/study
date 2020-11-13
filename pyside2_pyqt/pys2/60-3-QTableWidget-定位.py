'''
扩展的表格控件 QTableWidget 
快速定位
1 数据的定位：findItems 返回一个列表
2 如果找到，快速定位到所在行：setSliderPosition(row)

'''
from PySide2.QtWidgets import QApplication, QWidget, QTableWidget, QPushButton,QLineEdit,\
    QHBoxLayout,QVBoxLayout,QTableWidgetItem,QAbstractItemView,QComboBox
from PySide2.QtCore import *
from PySide2.QtGui import *



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QTableWidget的学习-3')
        self.resize(500,500)

        self.previous_list=[]
        self.itemlist=[]
        self.setup_ui()


    def setup_ui(self):
        le=QLineEdit()
        self.le=le
        btn=QPushButton('查找下一个')
        btn.resize(100,30)
        h_layout=QHBoxLayout()
        h_layout.addWidget(le)
        h_layout.addWidget(btn)

        # 1 定义
        tw=QTableWidget()
        self.tw=tw

        # 2 设置行和列
        tw.setRowCount(40)
        tw.setColumnCount(4)

        # 3 添加数据
        for i in range(40):
            for j in range(4):
                item=QTableWidgetItem(f'{i,j}')
                tw.setItem(i,j,item)


        # 4 查找和定位
        # 4.1 先看输入框有没有变化
        # self.ischange=False
        # def find_change():
        #     self.ischange=True
        #     print('textchange',self.ischange,le.isModified())
        # le.textChanged.connect(find_change)
        # 4.2 
        
        le.editingFinished.connect(self.find_list)


        btn.clicked.connect(self.search_go)
        # 精确查找
        # tag='13'
        # taglist=tw.findItems(tag,Qt.MatchExactly)

        # if len(taglist):
        #     for item in taglist:
        #         item.setBackground(QBrush(qcolor(0,255,0)))
        #         item.setForeground(QBrush(qcolor(255,0,0)))
        #         row=item.row()
                

        # 布局
        # 采用布局就没有滚动条，可以看到全貌
        layout=QVBoxLayout(self)
        layout.addLayout(h_layout)
        layout.addWidget(tw)
        
        pass
    def find_list(self):
        # 1 获取 le的值
        value=self.le.text().strip()
        # 2 查找
        if len(value):
            # 获取列表
            itemlist=self.tw.findItems(value,Qt.MatchExactly) #精确查找模式 全匹配
            # itemlist=self.tw.findItems(value,Qt.MatchStartsWith) #查找模式 以...开头
            # itemlist=self.tw.findItems(value,Qt.MatchExactly) #查找模式 以...结尾
            # itemlist=self.tw.findItems(value,Qt.MatchContains) #查找模式 包含
            self.itemlist=itemlist
            # 设置样式
            if len(itemlist):
                # 恢复上次查询列表样式
                for oitemtupe in self.previous_list:
                    oitem,background_obj,foreground_obj=oitemtupe
                    oitem.setBackground(background_obj)
                    oitem.setForeground(foreground_obj)
                # 清空上次查询列表 
                self.previous_list=[]
                # 设置本次查询列表样式
                for item in itemlist:
                    # 加入 上次查询列表 获取原来样式 item,item背景、item前景
                    self.previous_list.append((item,item.background(),item.foreground()))
                    # 设置新样式
                    item.setBackground(QBrush(QColor(0,255,255)))
                    item.setForeground(QBrush(QColor(255,0,0)))
                    print(itemlist)
                    

    def search_go(self):
        # 定位
        if len(self.itemlist):
            # 取出item 
            item=self.itemlist.pop()
            # 获取行号
            row=item.row()
            # 用垂直滚动条 定位到指定的行
            self.tw.verticalScrollBar().setSliderPosition(row)
        else:
            print('没有')


    pass

if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
    pass