'''
QTreeView的基本用法:
   
Model

QDirModel  QFileSystemModel 显示目录树结构model

QModelIndex对象相对模型提供索引，
    包含着在模型中定位数据的所有信息，
    每个索引都通过给定的行、列以及父索引组成，
    可以使用 row(), column(),和parent()获得。
    每个顶层模型项都由一个不含父索引的QModelIndex组成，
    此时调用parent()函数返回的就是不正确的。

    要获取数据模型（这里也就是树形结构）中某项的QModelIndex索引对象，
    可以调用index()方法，就能获得相应的行、列、父对象。

    注意的是：模型索引应该立即被使用然后被丢弃，
    你不应该依赖索引在调用相关函数更改结构或删除项目后还能保持正确。

'''
from PySide2.QtWidgets import QApplication, QWidget, QTreeView,QTreeWidget,QPushButton,QLineEdit,\
    QHBoxLayout,QVBoxLayout,QTableWidgetItem,QAbstractItemView,QComboBox,QTreeWidgetItem,QDirModel,QFileSystemModel
from PySide2.QtCore import *
from PySide2.QtGui import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QTreeView的学习')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        # 1 定义目录树model
        # dir_model=QDirModel() #不设置，默认显示整个电脑的根目录 列出所有盘符
        dir_model=QFileSystemModel()
        self.dir_model=dir_model
          
        # 2 定义view
        tree=QTreeView()
        self.tree=tree
        
        # 3 关联view和model
        tree.setModel(dir_model)

        # 4 显示目录树结构

        # 4.1 设置 model 根目录路径 model.setRootPath(path)
        # 4.2 设置 treeview  根节点索引 treeview.setRootIndex(model.index(path))
        # model的根目录和tree的根索引必须保持一致

        # 显示根目录树结构
        # dir_model.setRootPath('')             #   空 即是设置为根目录
        # tree.setRootIndex(dir_model.index(''))

        # 显示其余目录树结构
        # dir_path=r'D:\\pyj\\st\study\\pyside2_pyqt\\pys2\\'
        dir_path=r'D:\pyj\st\study\pyside2_pyqt\pys2' # 这样写与上面相同 省事
        dir_model.setRootPath(dir_path)
        # 这步是最重要的 没有这一步 怎么设置都是 显示根目录
        # 这一步的顺序也是很重要的，一定要放在view关联model之后，
        tree.setRootIndex(dir_model.index(dir_path))
        
        # 5 布局
        # 采用布局就没有滚动条，可以看到全貌
        layout=QVBoxLayout(self)
        layout.addWidget(tree)

        # 6 信号 
        # 双击信号，会传递点击的QModelIndex对象
        # 通过QModelIndex对象，可以获取文件路径、文件名、文件信息等等，
        # 还可以获取当前对象的行号、列号以及父对象的QModelIndex
        tree.doubleClicked.connect(self.get_path)

    def get_path(self,index_model):
        # path=self.dir_model.filePath(index_model)
        name=self.dir_model.fileName(index_model) # 对于中文支持有时行有时不行
        info=self.dir_model.fileInfo(index_model) #判断是文件夹还是文件
        print(name,info.isFile())
        print(index_model.row(),index_model.column(),index_model.parent())
        # 03-1-QObject-API_pysd2.py True
        # 4 0 <PySide2.QtCore.QModelIndex(0,0,0x1aed3e11170,QFileSystemModel(0x1aed3e3d820)) at 0x000001AED41CD508>
        # 02-pys2程序基本结构.py True
        # 3 0 <PySide2.QtCore.QModelIndex(0,0,0x1aed3e11170,QFileSystemModel(0x1aed3e3d820)) at 0x000001AED41CD508>
        
        # 02-pys2程序基本结构.py True
        # 3 0 <PySide2.QtCore.QModelIndex(0,0,0x13327ec0760,QFileSystemModel(0x13327c58c70)) at 0x000001332820E488>
        # 03-1-QObject-API_pysd2.py True
        # 4 0 <PySide2.QtCore.QModelIndex(0,0,0x13327ec0760,QFileSystemModel(0x13327c58c70)) at 0x000001332820E488>
        


if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()
    pass