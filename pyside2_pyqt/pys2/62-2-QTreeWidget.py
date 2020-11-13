'''
树控件(QTreeWidget)的基本用法:
   
1 增删改


'''
from PySide2.QtWidgets import QApplication, QWidget, QTreeView,QTreeWidget,QPushButton,QLineEdit,\
    QHBoxLayout,QVBoxLayout,QTableWidgetItem,QAbstractItemView,QComboBox,QTreeWidgetItem,QMessageBox
from PySide2.QtCore import *
from PySide2.QtGui import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QTreeWidget的学习2')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        # 输入节点名称和描述
        node_le=QLineEdit()
        node_le.setPlaceholderText('请输入节点名称')
        self.node_le=node_le
        cnt_le=QLineEdit()
        cnt_le.setPlaceholderText('请输入节点描述')
        self.cnt_le=cnt_le
        # 来一波按钮
        addbtn=QPushButton('增')
        updatebtn=QPushButton('更新')
        deletebtn=QPushButton('删')
        h_layout=QHBoxLayout()
        h_layout.addWidget(node_le)
        h_layout.addWidget(cnt_le)
        h_layout.addWidget(addbtn)
        h_layout.addWidget(updatebtn)
        h_layout.addWidget(deletebtn)

        addbtn.clicked.connect(self.addnode)
        updatebtn.clicked.connect(self.updatenode)
        deletebtn.clicked.connect(self.deletenode)

        # 定义
        tree=QTreeWidget()
        self.tree=tree
      
        tree.setColumnCount(2)
        tree.setHeaderLabels(['节点名称','节点描述'])
        # dic={
            # 节点名称：{
                # 节点描述：xxx,
                # 节点：{
                    # 节点描述：xxx,
                    # 节点：{
                        # ...
                    # }
                # }
                # ...
                # ...
            # }
        # }
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
        # 定义初始数据添加节点函数
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
        # 采用布局就没有滚动条，可以看到全貌
        layout=QVBoxLayout(self)
        layout.addLayout(h_layout)
        layout.addWidget(tree)

        # 信号
        tree.clicked.connect(self.show_colum_text)
        
        

    def show_colum_text(self,index):
        print('当前行：',index.row(),'当前列',index.column())
        print('0列文本：',self.tree.currentItem().text(0),'1列文本：',self.tree.currentItem().text(1))
        
        pass

    def addnode(self):
        print('添加节点')
        # 获取当前节点 作为 父节点
        parent_item=self.tree.currentItem()
        node_name=self.node_le.text().strip()
        node_cnt=self.cnt_le.text().strip()
        if not parent_item:
            print('节点选中不能为空')
            return

        if len(node_name) :
            # 在当前父节点下 添加节点
            item=QTreeWidgetItem(parent_item)
            item.setText(0,node_name)
            if len(node_cnt):
                item.setText(1,node_cnt)
        else:
            print('节点名称输入不能为空')
            return
            
    def updatenode(self):
        print('更新节点')
        # 获取当前节点
        item=self.tree.currentItem()
        node_name=self.node_le.text().strip()
        node_cnt=self.cnt_le.text().strip()
        if not item:
            print('节点选中不能为空')
            return
        if len(node_name) :
            # 修改当前节点
            item.setText(0,node_name)
            if len(node_cnt):
                item.setText(1,node_cnt)
        else:
            print('节点名称输入不能为空')
            return
        pass
    def deletenode(self):
        print('删除节点')
        '''
        如何删除根节点
        注意不可见的RootItem是根节点的父节点，这就保证可以删除根节点

        '''
        root_parent=self.tree.invisibleRootItem()

        #选中了多个item
        for item in self.tree.selectedItems():
            # 获取父节点，用父节点的removeChild(item)删除该节点
            # 当根节点的item.parent()不存在，就会用root_parent来删除，否则无法删除根
            # (item.parent() or root_parent).removeChild(item)
            try:
                # 一般情况下是不允许删除根节点的
                item.parent().removeChild(item)
            except Exception as e:
                QMessageBox.about(self,'产生异常',e.__str__())

if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
    pass