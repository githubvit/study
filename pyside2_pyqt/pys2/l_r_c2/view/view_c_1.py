from PySide2.QtWidgets import QApplication,QWidget,QPushButton,QComboBox,QCheckBox,QLabel
from PySide2.QtCore import Signal,Slot,QSize,QUrl,QObject
from PySide2.QtGui import QMovie,QDesktopServices

import os,sys


# 一 取得项目根目录加入系统目录
# print(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
# 把项目根目录加入环境变量 然后其它导入就有根了
sys.path.append(BASE_DIR)

# 1 导入从 Designer 设计师 转成的py文件中的  界面类  用于 多继承
from resource.ui.Ui_c_1 import Ui_Form

# 虚拟类 
# 定义和发射信号 掌管 按键后 显示屏le显示的内容
# 实现按键解析功能 
    # 按角色 、键值 逐一解析
# 衔接python的eval()函数，实现本界面的主体功能，完成计算功能
class CaUtil(QObject):
    # 管显示的信号
    show_content_signal=Signal(str)
    def __init__(self):
        super().__init__()
        self.ca_list=[]#每个item是[按键文本，按键角色]

    # '='按键的功能函数
    def calculate(self):
        # 建立表达式
        ex=''
        res=''
        # 如果最后一个item的按键角色是计算即'=',就计算
        if len(self.ca_list):
            for item in self.ca_list:
                text,role=item
                ex += text
            # 计算
            res=eval(ex)
            # 先清空
            self.ca_list=[]

            # 将结果放入计算列表
            item=[str(res),'num']
            self.ca_list.append(item)
        else:
            res='erro'
        return str(res)
        

    # 直接衔接 自定义按键CaBtn的 key_parse_signal信号 接收该信号的两个参数
    def parse_key(self,text,role):
        # 数字键 
        if role=='num':
            # 看计算列表的尾项
            # 如果是数字 就拼接或覆盖 计算列表 否则 就新增
            if len(self.ca_list):
                if self.ca_list[-1][-1]=='num':
                    if text=='.':
                        # 看列表有没有'.'，没有就加点
                        if '.' not in self.ca_list[-1][0]:
                            self.ca_list[-1][0]+=text
                            
                    else:
                        # 是0就覆盖不是0就拼接
                        if self.ca_list[-1][0]=='0':
                            self.ca_list[-1][0]=text 
                        else:
                            self.ca_list[-1][0]+=text

                    self.show_content_signal.emit(self.ca_list[-1][0])
                    return

            # 新增
            # 如果是 . 就改成 0.
            if text=='.':
                text='0.'
            item=[text,role]
            self.ca_list.append(item)
            self.show_content_signal.emit(self.ca_list[-1][0])
            return
                
        # 运算符 只添加到列表 不显示
        if role=='op':
            if len(self.ca_list):
                # 如果列表项 尾项是运算符 就覆盖 否则 就新增列表
                if self.ca_list[-1][-1]=='op':
                    self.ca_list[-1][0]=text
                    return
            
            item=[text,role]
            self.ca_list.append(item)
            return

        # AC键
        if role=='ac':
            # 清空计算列表
            self.ca_list=[]
            # 清空显示le
            self.show_content_signal.emit('0.0')
            return

        # '=' 
        if role=='ca':
            if len(self.ca_list):
                self.show_content_signal.emit(self.calculate())
            return

        # '+/-'
        if role=='zf':
            if self.ca_list[-1][-1]=='num':
                # 如果是数字就乘以-1
                self.ca_list[-1][0]=str(float(self.ca_list[-1][0])*-1)
                self.show_content_signal.emit(self.ca_list[-1][0])
                  
            return

        # '%'
        if role=='bf':
            if self.ca_list[-1][-1]=='num':
                # 如果是数字就乘以/100
                self.ca_list[-1][0]=str(float(self.ca_list[-1][0])/100)
                self.show_content_signal.emit(self.ca_list[-1][0])
            return
         


class C1Ui(QWidget,Ui_Form):
    
    def __init__(self):
        # 2 继承父类初始化
        super().__init__() 
      
        # 3 导入界面类setupUi函数，填入 self 参数作为父类。
        self.setupUi(self)

        # 虚拟工具类对象
        self.ca=CaUtil()

        self.ca.show_content_signal.connect(self.le_show)

        self.n0_btn.key_parse_signal.connect(self.ca.parse_key)
        self.n1_btn.key_parse_signal.connect(self.ca.parse_key)
        self.n2_btn.key_parse_signal.connect(self.ca.parse_key)
        self.n3_btn.key_parse_signal.connect(self.ca.parse_key)
        self.n4_btn.key_parse_signal.connect(self.ca.parse_key)
        self.n5_btn.key_parse_signal.connect(self.ca.parse_key)
        self.n6_btn.key_parse_signal.connect(self.ca.parse_key)
        self.n7_btn.key_parse_signal.connect(self.ca.parse_key)
        self.n8_btn.key_parse_signal.connect(self.ca.parse_key)
        self.n9_btn.key_parse_signal.connect(self.ca.parse_key)
        self.nd_btn.key_parse_signal.connect(self.ca.parse_key)
        self.o1_btn.key_parse_signal.connect(self.ca.parse_key)
        self.o2_btn.key_parse_signal.connect(self.ca.parse_key)
        self.o3_btn.key_parse_signal.connect(self.ca.parse_key)
        self.o4_btn.key_parse_signal.connect(self.ca.parse_key)
        self.ac_btn.key_parse_signal.connect(self.ca.parse_key)
        self.ca_btn.key_parse_signal.connect(self.ca.parse_key)
        self.zf_btn.key_parse_signal.connect(self.ca.parse_key)
        self.bf_btn.key_parse_signal.connect(self.ca.parse_key)


    def le_show(self,content):
        self.ca_le.setText(content)



if __name__ == "__main__":
    app=QApplication([])
    wd=C1Ui()
    wd.show()
    app.exec_()

