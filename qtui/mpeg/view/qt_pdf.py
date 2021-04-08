from PySide2.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QFileDialog,QHBoxLayout,QVBoxLayout,\
QMessageBox,QFileSystemModel,QToolTip,QTreeView,QScrollArea,QTextEdit,QSlider,QShortcut
from PySide2.QtCore import Signal,Slot,QEvent,QDir,QModelIndex,Qt
from PySide2.QtGui import QPixmap,QImage,QKeySequence

import os,sys

import fitz # pymupdf

# 知识点
# 1 QScrollArea的用法
    # QScrollArea实际是个窗框，在外面，里面还要有内容区，里面的内容如果小于窗口，自然不会有滚动条。
    # 因此，该控件的用法，定义完QScrollArea，还要定义内容区。
    # QScrollArea定义完了，就不用管了。
    # 主要工作都在内容区：放置控件，设置布局等，如果最后内容区大于窗口，就自然会出现滚动条。

# 2 内容区的缩放：
    # 依赖label的resize和内容区widget的resize，同步缩放实现。
    # 要点在于要事先存储好要用的原始数据，比如：label的objectName和原始的宽高等，以备resize时要用到。
    # 这里是定义了专门的列表来存储这些原始数据
    # 实际上更好的方式是用控件的Property属性来存储原始的宽高。 在 view_bfq2.py的缩放中就是用了这种方式。
# 3 快捷键qshortcut用法：一定要搭配QKeySequence

    

class PdfWd(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1000,500)
        self.setWindowTitle('PDF测试')

        # QScrollArea的用法
        self.pdf_area1=QScrollArea() # 窗口
        self.pdf_cnt_wgt=QWidget()   # 内容
        
        
        self.pdf_area1.setWidget(self.pdf_cnt_wgt) # 给窗口设置内容

        # 缩放用滑动条
        self.zoom_slider=QSlider()
        self.zoom_slider.setOrientation(Qt.Horizontal) #设置为水平，默认是垂直
        self.zoom_slider.setRange(50,150)
        self.zoom_slider.setValue(100) # 初始值为1

        # self.zoom_slider.valueChanged.connect(lambda v: print(v))    
        self.zoom_slider.valueChanged.connect(self.label_resize)    # 缩放

        cnt_layout=QVBoxLayout(self)
        cnt_layout.addWidget(self.pdf_area1)
        cnt_layout.addWidget(self.zoom_slider)

        # 放大用的原始尺寸
        self.lab_list=[]
        self.lab_wh=[]
        self.cnt_page_wh=None
        
        # 定义放大快捷键
        self.minus_shortcut=QShortcut(QKeySequence('Ctrl+-'),self.pdf_cnt_wgt) # 快捷键 父对象
        self.minus_shortcut.activated.connect(self.zoom_out)
        self.plus_shortcut=QShortcut(QKeySequence('Ctrl+='),self.pdf_cnt_wgt) # 快捷键 父对象
        self.plus_shortcut.activated.connect(self.zoom_in)

        # 加载pdf
        self.pdf_load()

        

    def pdf_load(self):
        self.pdf_file=r'F:\OneDrive - 中国加油！武汉加油！\02初中\数学\初中数学朱韬\人教版 初中数学\第01讲 有理数初步（一）.pdf'
        # self.pdf_file=r'D:\pyj\st\study\del_img.pdf'
        # 取得 pdf 对象 doc
        self.doc=fitz.open(self.pdf_file)
        # 循环该对象 并定义标签加载 该对象
        self.v_layout=QVBoxLayout(self.pdf_cnt_wgt)
        # 定义一个容器 空文件
        self.page_img='page.png'
        # 放大1.333333倍
        zn=1.333333
        zoom_x=zn
        zoom_y=zn
        self.mtx=fitz.Matrix(zoom_x,zoom_y).preRotate(0)
        for i,page in enumerate(self.doc):
            # 转为图形
            pix=page.getPixmap(matrix=self.mtx,alpha=False)
            # print(dir(pix))
            # 放入容器 即保存
            pix.writePNG(self.page_img)

            # 不使用容器 官方提供的方法 转 qimg
            # 该法无效 也不报错 自动就退出 
            # fmt=QImage.Format_RGBA8888 if pix.alpha else QImage.Format_RGB888
            # qtimg=QImage(pix.samples,pix.width,pix.height,pix.stride,fmt)
            # print(qtimg)
            

            # 定义label
            lab=QLabel()
            # print('pdf页的宽和高',pix.w,pix.h)
            # lab.resize(pix.w,pix.h)
            # lab.setText(f'第{i}页')

            # 加载图形

            # 定义尺寸
            sn=self.zoom_slider.value()*0.01#缩放比
            w=pix.w*sn #原始宽
            h=pix.h*sn #原始高

            # 命名
            lab.setObjectName(f'lab{i}')
            # 加入lab列表 以备 缩放尺寸用
            self.lab_list.append(lab.objectName()) # 名称列表
            self.lab_wh.append((w,h))              # 和 名称对应的原始尺寸列表

            # print(w,h,lab.objectName())
            # 用QPixmap的scaled缩放功能
            lab.setPixmap(QPixmap(self.page_img).scaled(w,h,Qt.KeepAspectRatio))#Qt.KeepAspectRatio 保持宽高比
            
            # lab.setScaledContents(True)
            self.v_layout.addWidget(lab)

        # print(lab.width(),lab.height())  # 640 480 这个值是错的, 实际尺寸应该是w和h 1123,794, 所以不能取这个数据, 取上面的w,h.

        self.pdf_cnt_wgt.adjustSize()   # 在布局和控件弄完后，一定要用adjustSize                *****
        # self.pdf_cnt_wgt.resize(1000,2000)# 这个会造成空隙过大，不如上面，不推荐。
        # print('内容区的大小',self.pdf_cnt_wgt.width(),self.pdf_cnt_wgt.height())  # 这个数据和后面取得数据是一致的，可用
        self.cnt_page_wh=(self.pdf_cnt_wgt.width(),self.pdf_cnt_wgt.height()) # 内容区缩放用
    
    def label_resize(self,v):
        # print(v)
        # 取出要缩放的label
        for item in self.findChildren(QLabel):
            # 在 lab 列表中查询 并 找到原始 w,h
            if item.objectName() in self.lab_list:
                index=self.lab_list.index(item.objectName())
                w,h=self.lab_wh[index]
                # print(w,h)
                # 缩放
                item.resize(w*v*0.01,h*v*0.01)
                item.setScaledContents(True) # 设定 图片大小适合label 很重要 不然 图片不会缩放 *****
        

        # 同步缩放 放置label的 内容区      
        # print('内容区的大小',self.pdf_cnt_wgt.width(),self.pdf_cnt_wgt.height())                                                                            
        self.pdf_cnt_wgt.resize(self.cnt_page_wh[0]*v*0.01,self.cnt_page_wh[1]*v*0.01) # *****
   
        pass
    # 通过 快捷键 改变滑动条的值，从而实现缩放
    def zoom_in(self):
        # print('zoom in')
        value=self.zoom_slider.value()+10
        self.zoom_slider.setValue(value)
        pass

    def zoom_out(self):
        # print('zoom out')
        value=self.zoom_slider.value()-10
        self.zoom_slider.setValue(value)
        pass
if __name__ == "__main__":
    app=QApplication([])
    wd=PdfWd()
   
    # wd.pdf_load(pdf_file)
    wd.show()
    app.exec_()