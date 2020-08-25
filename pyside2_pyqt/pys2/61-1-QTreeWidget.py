'''
树控件(QTreeWidget)的基本用法:
    节点组成。
    可添加多列。

1 节点创建方法
2 添加文本、图标、复选框
3 隐藏表头
4 设置打开时 全部展开   
5 信号 

'''
from PySide2.QtWidgets import QApplication, QWidget, QTreeView,QTreeWidget, QPushButton,QLineEdit,\
    QHBoxLayout,QVBoxLayout,QTableWidgetItem,QAbstractItemView,QComboBox,QTreeWidgetItem
from PySide2.QtCore import *
from PySide2.QtGui import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QTreeWidget的学习')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):

        # 定义
        tree=QTreeWidget()
        self.tree=tree
      
        # 一 逐点添加方法
        # 指定列数
        # tree.setColumnCount(2)
        # 指定列标签 否则就是1,2
        # tree.setHeaderLabels(['key','value'])
        # # 添加节点
        # root=QTreeWidgetItem(tree)
        # root.setText(0,'根节点')    #添加文本
        # root.setIcon(0,QIcon(r'pyside2_pyqt\pys2\xxx.png')) #添加图标
        # # 设置第1列的列宽为120
        # tree.setColumnWidth(0,120)
        # # 添加子节点 child1
        # child1=QTreeWidgetItem(root)
        # child1.setText(0,'子节点1')
        # child1.setText(1,'子节点1的值')
        # child1.setIcon(0,QIcon(r'D:\pyj\st\study\pyside2_pyqt\pyqt_ln\pyqt5-master\src\table_tree\images\bao3.png'))
        # # 添加子节点 child2
        # child2=QTreeWidgetItem(root)
        # child2.setText(0,'子节点2')
        # child2.setText(1,'子节点2的值')
        # # 给child2子节点 在0列 添加 选中状态 复选框 
        # child2.setCheckState(0,Qt.Checked)  # 添加复选框

        # # 添加child2的子节点
        # child2_1=QTreeWidgetItem(child2)
        # child2_1.setText(0,'child2的子节点2-1')
        # child2_1.setText(1,'child2-1的值')

       
        
        # 二 连续递归添加
        # 指定列数和列名
        tree.setColumnCount(2)
        tree.setHeaderLabels(['节点名称','节点描述'])
        dic={
            '根节点':{
                'cnt':None,
                'node':{
                    '子节点1':{
                        'cnt':'子节点1的描述',
                        'node':None,
                    },
                    '子节点2':{
                        'cnt':None,
                        'node':{
                            '子节点2-1':{
                                'cnt':'子节点2-1的描述',
                                'node':None,
                             }
                        }
                    }
                }
            }  
        }
        # 定义添加节点函数
        def add_node(dic,node):
            if isinstance(dic,dict):
                for key,val in dic.items():
                    print(key,val)
                    # 定义 item 属于node节点
                    item=QTreeWidgetItem(node)
                    # 定义 0列 节点名称
                    item.setText(0,key) 
                    # 定义 1列  节点描述
                    item.setText(1,val['cnt'])
                    # 递归
                    add_node(val['node'],item)
                            
        add_node(dic,tree)

        #  打开时 默认是关闭的 现在要求 全部展开
        tree.expandAll()
        # 隐藏标头
        # tree.setHeaderHidden(True)
        # 布局
        layout=QVBoxLayout(self)
        layout.addWidget(tree)

        # 信号
        tree.clicked.connect(self.show_colum_text)
    def show_colum_text(self,index):
        print('当前行：',index.row(),'当前列',index.column())
        print('0列文本：',self.tree.currentItem().text(0),'1列文本：',self.tree.currentItem().text(1))
        
        pass
    pass

if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
    pass