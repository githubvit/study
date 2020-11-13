from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# from PyQt5.Qt import QPushButton,pyqtSignal

import sys,os

#定位css文件
css_dir=os.path.dirname(__file__)
css_path='%s\calculate_btn.css'%css_dir

class CalculateBtn(QPushButton):
    
    # 自定义信号 发射键值和角色

    # keypressed_signal=pyqtSignal(str,str) #pyqt5
    keypressed_signal=Signal(str,str)

    # 动作：当按下时  发射自定义信号
    def mousePressEvent(self,evt):
        super().mousePressEvent(evt)
        # 发射信号
        self.keypressed_signal.emit(self.text(),self.property('role'))
        
    # 监测尺寸变化 
    def resizeEvent(self,evt):
        super().resizeEvent(evt)
        with open(css_path,'r',encoding='utf-8') as f:
            # 常规样式获取
            str1=f.read()
            # 动态样式 取长宽中较小的一半为半径
            str2='''
                QPushButton {
                    border-radius:%dpx;
                }
            '''%(min(self.width(),self.height())/2)
            # 添加常规样式和动态样式
            self.setStyleSheet(str1+str2)


        