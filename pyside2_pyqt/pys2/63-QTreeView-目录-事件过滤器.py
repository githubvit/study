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
from PySide2.QtWidgets import QApplication, QWidget, QTreeView,QPushButton,QLineEdit,QToolTip,\
    QHBoxLayout,QVBoxLayout,QTableWidgetItem,QAbstractItemView,QComboBox,QDirModel,QFileSystemModel,\
    QToolTip
from PySide2.QtCore import *
from PySide2.QtGui import *

# 知识点
# 一 了解QFileSystemModel 这个模型类
# 1 视图、模型 获取 QindexModel的方式 ： 比如 视图.indexAt(pos) 通过位置可以获取 QindexModel等等。
# 2 QFileSystemModel 通过 QindexModel 参数 可以 获取很多信息，文件名、路径、大小 等等 。
# 3 QFileSystemModel 的过滤  文件过滤即可，可以方便的搜索文件。
# 4 QFileSystemModel 的展开和递归加载完成信号 directoryLoaded ，以及获取正确的行数等。
# 二 过滤事件的用法 
# 1 两步  安装和过滤 
# 2 解决了设置提示信息的问题 ToolTip

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QTreeView的学习')
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        # 1 定义目录树model
        # dir_model=QDirModel() #不设置，默认显示整个电脑的根目录 列出所有盘符
        dir_model=QFileSystemModel()#主要用这个模型 而不是上面的QDirModel 单独的线程
        # QFileSystemModel 采用单独的线程获取目录文件结构，而 QDirModel 不使用单独的线程。
        # 使用单独的线程就不会阻碍主线程，所以推荐使用 QFileSystemModel。
        
        # QFileSystemModel 提供的接口函数，可以创建目录、删除目录、重命名目录，
            # 可以获得文件名称、目录名称、文件大小等参数，还可以获得文件的详细信息。
       
       
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
        dir_path=r'D:\pyj\st\study\pyside2_pyqt\pys2' # 这样写与上面相同  '\'通用分隔符 不管是Linux或win
        dir_model.setRootPath(dir_path) # 
        # dir_model.setRootPath((QDir.rootPath())) # 这样写也可以
        
        
        # 过滤
        # 被过滤的文件会变成灰色
        dir_model.setNameFilterDisables(False) # 被过滤掉的灰色文件不显示 
        # dir_model.setNameFilters(['*.py']) # 表示只显示py文件
        # dir_model.setNameFilters(['m*']) # 表示只显示以m开头的文件、文件夹
        dir_model.setNameFilters(['*l*']) # 表示只显示包含l的文件、文件夹
        
        # dir_model.setNameFilters(['*鼠标*']) # 中文过滤 没有问题
        # 注：setNameFilters参数只接受列表。
        
        # 默认只过滤文件不过滤文件夹 
        # 如果过滤文件夹 就会导致过滤搜索不完整 在子文件夹中的文件不会被搜索到。 因此一般不用设置。
            # dir_model.setFilter(QDir.Dirs)  # 只显示过滤后的文件夹 
            # dir_model.setFilter(QDir.Files)  # 只显示过滤后的文件
            # dir_model.setFilter(QDir.Dirs|QDir.Files)  # 显示过滤后的文件夹 与 文件
            # QDir中的Filter枚举变量见下面
            # QDir类及其用法总结 https://www.cnblogs.com/aiguona/p/10298226.html

        parentIndex=dir_model.index(dir_path)
        print('类和方法',type(parentIndex),dir(parentIndex))
        print('flags',parentIndex.flags())

        def directoryLoaded_info():
            tree.expandAll()
            
            print('总行数',dir_model.rowCount(parentIndex)) #这时才能获取正确的行数
            
            print('每次递归flags',parentIndex.flags())

        # setRootIndex 指定视图目录索引
        # 这步是最重要的 没有这一步 怎么设置都是 显示根目录
        # 这一步的顺序也是很重要的，一定要放在view关联model之后，
        tree.setRootIndex(dir_model.index(dir_path)) # 把 模型dir_model的根节点 Qindex_model 设置为 视图的根节点Qindex_model 

        
      
        # 隐藏列
        # tree.setColumnHidden(1,True) # size 列
        # tree.setColumnHidden(2,True) # type 列
        # tree.setColumnHidden(3,True) # Date Modified 即 Modifiedtime 列

        # 关闭列头
        # tree.setHeaderHidden(True) 
        # r_index=tree.rootIndex()
        # print(r_index.data())

        # QFileSystemModel 信号 directoryLoaded 目录递归加载完成
        # 展开全部 节点
        # tree.expandAll() # 这样运行无用
        # 解决以QFileSystemModel为模型对QTreeView执行expandAll()操作不起作用的问题
            # 要解决这个问题，我们首先需要明白一个问题，那就是QFileSystemModel这个Qt自带的标准控件比较特殊，
            # 目前我所知道的特殊之处有两个，一个是我们无法直接修改它的表头为中文，我们只能通过国际化的方式将表头文字进行翻译，但是也很别扭。
            # 另一个就是当前要讲的问题，直接展开QTreeView对象的所有节点是无效的，
            # 因为为了效率，QFileSystemModel在目录递归加载完成之前，执行expandAll()是无效的，
            # 为此，我们利用QFileSystemModel的信号directoryLoaded(const QString &)来实现，
            # 当QFileSystemModel递归加载完成之后，
            # 调用QTreeView的expandAll()方法，经过测试，该方法是有效的.
        # dir_model.directoryLoaded.connect(lambda:print('目录加载完毕'))
        # dir_model.directoryLoaded.connect(tree.expandAll)
        dir_model.directoryLoaded.connect(directoryLoaded_info)



        
        
        

        # 设置提示 这是个难点                                   ***** 
        # 要用事件过滤来设置                                难点1
            # 这就牵扯到事件过滤器的用法
           
            # 你要对哪个控件的什么事件进行操作
            # 用哪个控件的过滤器过滤，一般肯定是用self的过滤器,因为在这里能重写的事件过滤函数就是self的。
            
            # 两步 
            #  一 安装事件过滤器
            # 哪个控件.installEventFilter(用哪个控件的过滤器 self)

            # 二 重写事件过滤函数 eventFilter 两个参数 即控件和事件
            # def eventFilter(self,watcher,evt):
                # 进行控件和事件判断
                # if watcher==self.tree and evt.type()==QEvent.ToolTip:
                    # ...
                    # todosth
                    # ...

                # 继承原过滤器
                # return super().eventFilter(watcher,evt)

        # 要用 indexAt(pos) 获取 index_model               难点2
        # 要用 QToolTip.showText(pos,text) 显示提示         难点3
        

        # 安装事件过滤器
        self.tree.installEventFilter(self)
      
        
        
        
        # 5 布局
        # 采用布局就没有滚动条，可以看到全貌
        layout=QVBoxLayout(self)
        layout.addWidget(tree)

        # 6 信号 
        # 双击信号，会传递点击的QModelIndex对象
        # 通过QModelIndex对象，可以获取 
            # 文件路径filePath、文件名fileName、
            # 文件类型type(返回描述节点类型的文字，如硬盘符是 "Drive"，文件夹是 "FileFolder"，
                # 文件则用具体的后缀描述，如 "txtFile"、"exe File"、"pdfFile"等。)、
            # 文件大小size(如果节点是文件，返回文件大小的字节数：如果节点是文件夹，返回 0。)、
            # 判断节点是不是一个目录isDir、
        # 等等，
        # 还可以获取当前对象的行号、列号以及父对象的QModelIndex
        tree.doubleClicked.connect(self.get_path)
        tree.clicked.connect(self.select_changed)

    #  事件过滤器   
    def eventFilter(self,watcher,evt):
        if watcher==self.tree and evt.type()==QEvent.ToolTip:
            # 注意：
            # 如果显示列头，就要在位置上减去列头高度，不然显示的提示就不是当前行的名称
            # 获取列头高度
            h=self.tree.header().height()
            x=evt.pos().x()
            y=evt.pos().y()-h #减去列头高度 只有这样才能获取当前行的index_model
            pos=QPoint(x,y)
            file_name=self.dir_model.fileName(self.tree.indexAt(pos)) # indexAt(pos)  根据位置 返回 QindexModel ********** 
            # 不显示列表，就不要减，直接用evt.pos() 即可。
            # file_name=self.dir_model.fileName(self.tree.indexAt(evt.pos()))
            if file_name:
                # 要用全局位置 才能获得正确的显示位置
                QToolTip.showText(evt.globalPos(),file_name)

        return super().eventFilter(watcher,evt)
                

    def select_changed(self,v):
        print('选择变化',v)
    
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