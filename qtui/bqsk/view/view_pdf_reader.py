from PySide2.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QShortcut
from PySide2.QtCore import Slot,QEvent,Qt
from PySide2.QtGui import QKeySequence

import os,sys

import fitz 

# 一 取得项目根目录加入系统目录
# print(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
# 把项目根目录加入环境变量 然后其它导入就有根了
sys.path.append(BASE_DIR)

# 1 导入从 Designer 设计师 转成的py文件中的  界面类  用于 多继承
from resource.ui.Ui_pdf_reader import Ui_Form

# 三 联结 主逻辑
# 3.1 导入主逻辑程序
# from core.split_music import split_music

class PdfReaderUi(QWidget,Ui_Form):
    
    def __init__(self,pdf_file,parent=None):
        # 3 继承父类初始化
        super().__init__(parent) 

        self.pdf_file=pdf_file
        
        # 4 导入界面类setupUi函数，填入 self 参数作为父类。
        self.setupUi(self)
        # self.setProperty('path',pdf_file) # 设置 path 属性 
        # 外框
        # self.pdf_sca
        # 内容
        # self.pdf_wgt


        # 加载pdf
        self.pdf_load()

        # 用快捷键 进行缩放
        # 注意 ： 一定要把designer定义的QSCrollArea 中 的属性 widgetTesizable 默认的勾 取消
        # self.pdf_sca.setWidgetResizable(False)
        # 定义缩放快捷键
        self.minus_shortcut=QShortcut(QKeySequence('Ctrl+-'),self) # 快捷键 父对象 缩小
        self.minus_shortcut.activated.connect(self.zoom_out)
        self.plus_shortcut=QShortcut(QKeySequence('Ctrl+='),self)  # 放大
        self.plus_shortcut.activated.connect(self.zoom_in)
        self.reset_shortcut=QShortcut(QKeySequence('Ctrl+z'),self) # 复位100% 
        self.reset_shortcut.activated.connect(self.zoom_0)


    # 加载pdf
    def pdf_load(self):
        # 取得 pdf 对象 doc
        doc=fitz.open(self.pdf_file)
        # 给内容区设置一个布局
        v_layout=QVBoxLayout(self.pdf_wgt)

        # 定义一个容器 空文件
        page_img='page.png'

        # 设置转换格式
        # 把pdf转为图形pix放大1.333333倍 
        zn=1.333333
        z_x=zn
        z_y=zn
        mtx=fitz.Matrix(z_x,z_y).preRotate(0) # 转换下，y放大1.333333倍，角度不变
        # 循环pdf对象 并定义标签加载 该对象
        for i,page in enumerate(doc):
            # 转为图形
            pix=page.getPixmap(matrix=mtx,alpha=False)
            # print(dir(pix))
            # 放入容器 即保存
            pix.writePNG(page_img)

            # 定义label
            lab=QLabel()
            # 放入图片
            lab.setPixmap(page_img)

            # 添加每一页的名字和宽高属性  用于缩放
            lab.setObjectName(f'lab{i}')
            lab.setProperty('w',pix.w)
            lab.setProperty('h',pix.h)

            # 放入布局
            v_layout.addWidget(lab)

        self.pdf_wgt.adjustSize() # 保证内容区合适大小                 ******
        # 添加内容区控件的名字和宽高属性 用于缩放
        self.pdf_wgt.setObjectName('cnt_wgt')
        self.pdf_wgt.setProperty('w',self.pdf_wgt.width())
        self.pdf_wgt.setProperty('h',self.pdf_wgt.height())
 
     # 放大
    def zoom_in(self):

        # 取 lab
        for lab in self.findChildren(QLabel):
            # 用添加的宽高属性 缩放
            w=lab.width()+lab.property('w')*0.1
            h=lab.height()+lab.property('h')*0.1
            if w/lab.property('w') >1.5:
                w=lab.property('w')*1.5
                h=lab.property('h')*1.5
            # print(w,h)
            lab.resize(w,h)
            lab.setScaledContents(True) # 设定 图片大小适合label 
        # 取 内容区域
        cnt_wgt=self.findChild(QWidget,'cnt_wgt')
        # print(cnt_wgt.property('w'),cnt_wgt.property('h'))
        # 同步缩放内容区域
        cnt_wgt_w=cnt_wgt.width()+cnt_wgt.property('w')*0.1
        cnt_wgt_h=cnt_wgt.height()+cnt_wgt.property('h')*0.1
        if cnt_wgt_w/cnt_wgt.property('w') > 1.5:
            cnt_wgt_w=cnt_wgt.property('w')*1.5
            cnt_wgt_h=cnt_wgt.property('h')*1.5
        
        cnt_wgt.resize(cnt_wgt_w,cnt_wgt_h)
            
        # print('zoom in')

    # 缩小
    def zoom_out(self):
  
        # 取 lab
        for lab in self.findChildren(QLabel):
            # 用添加的宽高属性 缩放
            w=lab.width()-lab.property('w')*0.1
            h=lab.height()-lab.property('h')*0.1
            if w/lab.property('w') <0.5:
                w=lab.property('w')*0.5
                h=lab.property('h')*0.5
            # print(w,h)
            lab.resize(w,h)
            lab.setScaledContents(True) # 设定 图片大小适合label 
        # 取 内容区域
        cnt_wgt=self.findChild(QWidget,'cnt_wgt')
        # print(cnt_wgt.property('w'),cnt_wgt.property('h'))
        # 同步缩放内容区域
        cnt_wgt_w=cnt_wgt.width()-cnt_wgt.property('w')*0.1
        cnt_wgt_h=cnt_wgt.height()-cnt_wgt.property('h')*0.1
        if cnt_wgt_w/cnt_wgt.property('w') < 0.5:
            cnt_wgt_w=cnt_wgt.property('w')*0.5
            cnt_wgt_h=cnt_wgt.property('h')*0.5
        
        cnt_wgt.resize(cnt_wgt_w,cnt_wgt_h)
        # print('zoom out')

    # 重置为100%
    def zoom_0(self):
        # 取 lab
        for lab in self.findChildren(QLabel):
            w=lab.property('w')
            h=lab.property('h')
            # print(w,h)
            lab.resize(w,h)
            lab.setScaledContents(True) # 设定 图片大小适合label 
        # 取 内容区域
        cnt_wgt=self.findChild(QWidget,'cnt_wgt')
        # print(cnt_wgt.property('w'),cnt_wgt.property('h'))
        cnt_wgt.resize(cnt_wgt.property('w'),cnt_wgt.property('h'))
        # print('zoom_0')
        

if __name__ == "__main__":
    app=QApplication([])
    pdf_file=r'F:\OneDrive - 中国加油！武汉加油！\02初中\数学\初中数学朱韬\人教版 初中数学\第01讲 有理数初步（一）.pdf'
    wd=PdfReaderUi(pdf_file)
    wd.show()
    app.exec_()