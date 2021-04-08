from PySide2.QtWidgets import QApplication,QWidget,QFileSystemModel,QToolTip
from PySide2.QtCore import Signal,Slot,QEvent,Qt,QDir,QPoint
from PySide2.QtGui import QKeySequence

import os,sys

# 一 取得项目根目录加入系统目录
# print(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
# 把项目根目录加入环境变量 然后其它导入就有根了
sys.path.append(BASE_DIR)

# 1 导入从 Designer 设计师 转成的py文件中的  界面类  用于 多继承
from resource.ui.Ui_file_explorer import Ui_Form

# 三 联结 主逻辑
# 3.1 导入主逻辑程序
# from core.split_music import split_music

class FileExplorerUi(QWidget,Ui_Form):
    
    def __init__(self,file_folder,parent=None):
        # 3 继承父类初始化
        super().__init__(parent) 
        self.file_folder=file_folder # 文件夹
        # 4 导入界面类setupUi函数，填入 self 参数作为父类。
        self.setupUi(self)

        # 建立资源索引
        self.bulid_index()

        # 搜索框
        self.sch_le.textChanged.connect(self.bulid_index) # 重新加载一遍目录 实现搜索

        # 给 视图 安装 事件过滤器 用事件过滤实现 提示 功能
        self.lst_trv.installEventFilter(self)
        


    # 建立索引
    def bulid_index(self):
        # 建模型
        # 设置model
        self.fe_model=QFileSystemModel()
        # 关联View
        self.lst_trv.setModel(self.fe_model)

        # 设置model根目录
        self.fe_model.setRootPath(self.file_folder)
        # 设置view根索引 为 model的根路径索引 必须保持一致 这样 view和model的QindexModel相等。
        self.lst_trv.setRootIndex(self.fe_model.index(self.file_folder))
        
        # 关闭列头
        self.lst_trv.setHeaderHidden(True)
        # 隐藏列
        self.lst_trv.setColumnHidden(1,True) # size 列
        self.lst_trv.setColumnHidden(2,True) # type 列
        self.lst_trv.setColumnHidden(3,True) # Date Modified 即 Modifiedtime 列

        # 文件搜索设置
        self.fe_model.setNameFilterDisables(False) # 被过滤掉的灰色文件不显示
        sch_text=self.sch_le.text().strip()
        if sch_text:
            self.fe_model.setNameFilters([f'*{sch_text}*']) # 中文过滤 没有问题
            # 注：setNameFilters参数只接受列表。
            # 展开全部过滤搜索结果
            self.fe_model.directoryLoaded.connect(self.lst_trv.expandAll)

    # 重写过滤事件函数 用过滤器实现 提示 功能
    def eventFilter(self,watcher,evt):
        if watcher==self.lst_trv and evt.type()==QEvent.ToolTip:
            # 捕捉所在位置的qindexmodel 
            # 注意：
            # 如果显示列头，就要在位置上减去列头高度，不然显示的提示就不是当前行的名称
            # 获取列头高度
            # h=self.lst_trv.header().height()
            # x=evt.pos().x()
            # y=evt.pos().y()-h #减去列头高度 只有这样才能获取当前行的index_model
            # pos=QPoint(x,y)
            # qindex=self.lst_trv.indexAt(pos) 
            
            # 无列头 捕捉所在位置的qindexmodel 
            qindex=self.lst_trv.indexAt(evt.pos()) # 因为关闭了列头，所以可以直接用evt.pos(),不然高度要减去列头高度
            # 用model 获取 该 qindexmodel 的 filename
            filename=self.fe_model.fileName(qindex)
            if filename:
                # 用 QToolTip 的静态方法 显示 提示 位置参数要用事件的全局位置参数
                QToolTip.showText(evt.globalPos(),filename)

        return super().eventFilter(watcher,evt)



if __name__ == "__main__":
    app=QApplication([])
    file_folder=r'F:\OneDrive - 中国加油！武汉加油！\02初中\数学\初中数学朱韬\人教版 初中数学'
    wd=FileExplorerUi(file_folder)
    wd.show()
    app.exec_()