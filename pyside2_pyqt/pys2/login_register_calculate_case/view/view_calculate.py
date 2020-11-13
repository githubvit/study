from PySide2.QtWidgets import QApplication,QWidget
from PySide2.QtCore import QObject,Signal,Slot,Qt


# from PyQt5.Qt import *

# 1 调入从 Designer 设计师 转成的py文件中的  界面类

# from Ui_main import Ui_Form
from Ui_calculate import Ui_Form


# 定义工具类 处理计算业务 虚拟object类

#  让其继承QObject  
# 就可以 自定义信号和发射信号 
# 可以和 其他控件很好的配合
class Calculator(QObject):
    # 自定义信号
    # show_content_signal=pyqtSignal(str)#pyqt5
    show_content_signal=Signal(str)
    def __init__(self,parent=None):
        super().__init__(parent)
        # 要计算的列表
        self.calculate_models=[] # 就是 计算器 显示屏le 计算前的内容

    # 计算
    def calculate(self):
        # 列表不为空且最后角色是运算符 就取出来
        if len(self.calculate_models)>0 and self.calculate_models[-1]['role']=='operator':
            self.calculate_models.pop(-1)

        # 取出title的值拼接成表达式
        exprice=''
        for i in self.calculate_models:
            exprice += i['title']

        # 执行表达式 取得结果
        res=eval(exprice)
        print(exprice,'=',res)
        return str(res)


    # 解析 按钮
    def parse_key(self,calculate_dic):
        # 先解析接收的的数字和角色
        # print(calculate_dic)

        # 先处理两个特殊键 清空 Ac 和 计算 =
        if calculate_dic['role']=='clear':
            print('清空')
            # 清空列表
            self.calculate_models=[]
            print(self.calculate_models)
            self.show_content_signal.emit('0.0')
            return None

        # 当点击了'='号 就调用计算功能，并发射结果
        if calculate_dic['role']=='calculate':
            # 列表为空 就不理
            if not len(self.calculate_models):
                return None
            print('计算')
            #发射信号
            self.show_content_signal.emit(self.calculate())
            return None

        # 剩下的角色就是 数字num 和 运算符operator 要加入计算列表

        # 当列表为空时，先加入的必须是数字角色
        if len(self.calculate_models)==0:
            if calculate_dic['role']=='num':
                if calculate_dic['title'] in ('%','+/-'):
                    return None
                # 处理是开头‘.’ 改成'0.'
                if calculate_dic['title']=='.':
                    calculate_dic['title']='0.'
                
                self.calculate_models.append(calculate_dic)
                print(self.calculate_models)
                self.show_content_signal.emit(self.calculate_models[-1]['title'])
            return None

        # 处理 % 和 +/- 键
        if calculate_dic['title'] in ('%','+/-'):
            # 如果列表最后不是数字就退出
            if self.calculate_models[-1]['role'] != 'num':
                return None
            # 除以100
            if calculate_dic['title']=='%':
                self.calculate_models[-1]['title']=str(float(self.calculate_models[-1]['title']) /100)
            # 添加-号
            if calculate_dic['title']=='+/-':
                self.calculate_models[-1]['title']=str(float(self.calculate_models[-1]['title']) *-1)
            print(self.calculate_models)
            # 数字角色就激发title 运算符就激发self.calculate()
            self.show_content_signal.emit(self.calculate_models[-1]['title'])
            return None

        # 如果列表中的最后的角色==加入的角色
        # 1 如果是num ,如果title 不是 0 就拼接title，title是0就覆盖
        # 2 如果是operator 就覆盖
        if self.calculate_models[-1]['role']==calculate_dic['role']:
            if calculate_dic['role']=='num': #拼接
                # 前面有‘.’继续输入‘.’ 
                if calculate_dic['title']=='.' and self.calculate_models[-1]['title'].__contains__('.'):
                    # 扔出去
                    return None
                # 处理非0开头
                if self.calculate_models[-1]['title']!='0':
                    self.calculate_models[-1]['title']+=calculate_dic['title']
                else:
                    # 开头是0 后面是小数点 拼接
                    if calculate_dic['title']=='.':
                        self.calculate_models[-1]['title']+=calculate_dic['title']
                    else:
                        #覆盖
                        self.calculate_models[-1]['title']=calculate_dic['title']

                self.show_content_signal.emit(self.calculate_models[-1]['title'])
            else: #覆盖
                self.calculate_models[-1]['title']=calculate_dic['title']
                self.show_content_signal.emit(self.calculate())
        
        else:
            
            if calculate_dic['role']=='num':
                self.show_content_signal.emit(calculate_dic['title'])
            else:
                self.show_content_signal.emit(self.calculate())
            # 处理是开头‘.’ 改成'0.'
            if calculate_dic['title']=='.':
                calculate_dic['title']='0.'
            self.calculate_models.append(calculate_dic)

        print(self.calculate_models)



# 2 class 多继承 

class CalculateUi(QWidget,Ui_Form):
    # 自定义信号
    
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)    
        # 解决背景图片没有了的问题 这里没有背景图片
        # self.setAttribute(Qt.WA_StyledBackground,True)
        # 3 导入界面类setupUi函数，填入self参数作为父类。
        self.setupUi(self)
        
        # 计算器 引入定义的工具类 处理计算业务
        self.calculator=Calculator(self)

        # 链接信号 显示计算内容 
        self.calculator.show_content_signal.connect(self.show_content) # 捕捉 虚拟类的 显示内容信号 调用该信号参数(传递的内容） 展示显示屏内容

        
        # 这样写不管是pyqt5还是pyside2，都可以。
        self.ac_btn.keypressed_signal.connect(self.get_key)
        self.zero_btn.keypressed_signal.connect(self.get_key)
        self.point_btn.keypressed_signal.connect(self.get_key)
        self.percent_btn.keypressed_signal.connect(self.get_key)
        self.plus_minus_btn.keypressed_signal.connect(self.get_key)

        self.n1_btn.keypressed_signal.connect(self.get_key)
        self.n2_btn.keypressed_signal.connect(self.get_key)
        self.n3_btn.keypressed_signal.connect(self.get_key)
        self.n4_btn.keypressed_signal.connect(self.get_key)
        self.n5_btn.keypressed_signal.connect(self.get_key)
        self.n6_btn.keypressed_signal.connect(self.get_key)
        self.n7_btn.keypressed_signal.connect(self.get_key)
        self.n8_btn.keypressed_signal.connect(self.get_key)
        self.n9_btn.keypressed_signal.connect(self.get_key)

        self.add_btn.keypressed_signal.connect(self.get_key)
        self.sub_btn.keypressed_signal.connect(self.get_key)
        self.multiplication_btn.keypressed_signal.connect(self.get_key)
        self.division_btn.keypressed_signal.connect(self.get_key)
        self.equal_btn.keypressed_signal.connect(self.get_key)
    
    # 显示计算内容 
    # 是 虚拟计算工具类Calculator对象 即self.calculator 的 自定义信号显示内容show_content_signal 的槽函数，
    # 接收该信号的一个参数 
    # 用其参数展示计算器显示屏self.lineEdit
    def show_content(self,content):
        self.lineEdit.setText(content)

    # 获取键值和角色
    # 是 本自定义按钮类CalculateBtn对象 即self 的 自定义信号keypressed_signal 的槽函数
    # 接收该信号的两个参数
    def get_key(self,key_value,role):
        calculate_dic={'title':key_value,'role':role}
        self.calculator.parse_key(calculate_dic) # 调用虚拟类对象self.calculator的按钮解析功能

       
    # 4 用slot装饰器添加槽函数
  

if __name__ == "__main__":
    app=QApplication([])
    wd=CalculateUi()
    # 监测自定义信号
   
    wd.show()
    app.exec_()