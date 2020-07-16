from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('简单对话框QInputDialog的学习')
        self.setup_ui()

    def setup_ui(self):
        btn=QPushButton(self)
        btn.setText('弹出简单对话框')
        btn.move(50,50)
        # 简单对话框可以快速的实现 前面学过的 步长调节器spinbox、下拉菜单框combox、文本输入框等
        
        def InputDialog_handle():
            # 一  静态方法 快速 方便
            # 用静态方法 方便 快捷 打开 不用生成文件对话框对象  弹出模式为 模态级别 ，即阻塞。
            # self即是父控件也是父对象，父对象是站在内存管理的角度，即父对象销毁，子对象也被销毁。
            # 在控件的角度，说的是受到了父控件的约束。

            # 整型步长调节器
            # getInt(QWidget, str, str, value: int = 0, min: int = -2147483647, max: int = 2147483647, step: int = 1, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) -> Tuple[int, bool]
            # (父控件,'标题','标签',值=默认0,最小=-2147483647,最大=默认2147483647,步长=默认1)
            # result=QInputDialog.getInt(self,'标题','标签')  # (156, True) 点取消 输出(0, False)
            # result=QInputDialog.getInt(self,'标题','标签',888,step=8) 
            
            # 浮点型步长调节器
            # getDouble(QWidget, str, str, value: float = 0, min: float = -2147483647, max: float = 2147483647, decimals: int = 1, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) -> Tuple[float, bool]
            # (父控件,'标题','标签',值=默认0,最小=-2147483647,最大=默认2147483647,小数位数=默认1)
            # result=QInputDialog.getDouble(self,'标题','标签',888.88,decimals=2) # (894.88, True)
                # getDouble(QWidget, str, str, float, float, float, int, Union[Qt.WindowFlags, Qt.WindowType], float) -> Tuple[float, bool]
            
            # 单行文本输入框
            # getText(QWidget, str, str, echo: QLineEdit.EchoMode = QLineEdit.Normal, text: str = '', flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags(), inputMethodHints: Union[Qt.InputMethodHints, Qt.InputMethodHint] = Qt.ImhNone) -> Tuple[str, bool]
            # (父控件,'标题','标签',单行文本框QLineEdit输出模式（ 默认 普通模式）, '输入框文本'默认空，窗口类型，外观)
            # result=QInputDialog.getText(self,'标题','标签',text='abc') # ('abc', True)  点取消 ('', False)
            # result=QInputDialog.getText(self,'标题','标签',echo= QLineEdit.Password) # 密文形式输出 ('123456', True) 点取消 ('', False)
            
            # 多行文本输入框
            # getMultiLineText(QWidget, str, str, text: str = '', flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags(), inputMethodHints: Union[Qt.InputMethodHints, Qt.InputMethodHint] = Qt.ImhNone) -> Tuple[str, bool]
            # (父控件,'标题','标签', '输入框文本'默认空，窗口类型，外观)
            # result=QInputDialog.getMultiLineText(self,'标题','标签')#('嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻', True)

            #  下拉列表框
            # getItem(QWidget, str, str, Iterable[str], current: int = 0, editable: bool = True, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags(), inputMethodHints: Union[Qt.InputMethodHints, Qt.InputMethodHint] = Qt.ImhNone) -> Tuple[str, bool]
            # (父控件,'标题','标签',可迭代对象，当前索引 默认0，可否编辑 默认可以，窗口类型，外观)
            # result=QInputDialog.getItem(self,'标题','标签',['abc','123','xxx'],1)
            # 按回车不增加条目 输出('123333', True)
            # 点取消 输出 (默认选项，False) ('123', False)
            # print(result)


            # 二 一步步构造 实现
            ipt=QInputDialog(self)
            
            # 通过输入模式（文本、整型、浮点）,实现spinbox、combox、LineText、MultiLineText
                # QInputDialog.TextInput
                # QInputDialog.IntInput
                # QInputDialog.DoubleInput
            # 1 单行文本框
            ipt.setInputMode(QInputDialog.TextInput)
            # 可以设定默认的文本及输出模式（普通和密文）
            # ipt.setTextValue('默认')
            # ipt.setTextEchoMode(QLineEdit.Password)
            

            # 2 整型步长调节
            # ipt.setInputMode(QInputDialog.IntInput)
            # 可以设定最大（默认99）最小（默认0）或设范围，设定步长（默认1）和设定默认值(默认0)
            # ipt.setIntMaximum(999)
            # ipt.setIntMinimum(-999)
            # ipt.setIntRange(-111,111)
            # ipt.setIntValue(66)
            # ipt.setIntStep(10)#这是小步长，大步长即翻页是小步长*10
            


            # 3 浮点步长调节
            # ipt.setInputMode(QInputDialog.DoubleInput)
            # 默认范围（0.00 99.99） 默认值0.00 默认setp=1 比整型多了个小数位数
            # ipt.setDoubleStep(0.02)
            # ipt.setDoubleDecimals(3) #位数

            # 4 下拉列表
            # 是在文本输入模式的基础上，通过添加列表项目实现。默认不可编辑，信号响应文本变化和文本选中信号。
            # ipt.setInputMode(QInputDialog.TextInput)
            # ipt.setComboBoxItems(['dab','中','123'])
            # ipt.setComboBoxEditable(True) # 设为可编辑
            # 通过设置使用QListView而不是QComboBox来显示使用setComboBoxItems（）设置的项目。
            # ipt.setOption(QInputDialog.UseListViewForComboBoxItems)
            
            # 5 多行文本
            # 是在文本输入模式的基础上，通过选项控制设置使用纯文本编辑器实现多行文本输入。
            ipt.setInputMode(QInputDialog.TextInput)
            ipt.setOption(QInputDialog.UsePlainTextEditForTextInput)
            # 设置多行文本默认值
            ipt.setTextValue('\n'.join(['abc','流浪吧','在风雨交加的时候']))


            # 界面文本设置
            ipt.setWindowTitle('标题')
            ipt.setLabelText('标签')
            ipt.setOkButtonText('确认')
            ipt.setCancelButtonText('取消')

            # 选项控制
            # 设置选项 不显示'ok'和'cancel'按钮
            ipt.setOption(QInputDialog.NoButtons)#会叠加前面的已设置的选项
            # ipt.setOptions(QInputDialog.UsePlainTextEditForTextInput|QInputDialog.NoButtons)#pyside2没有optons

            # 弹出
            ipt.show()
            # ipt.open()
            # ipt.exec_()

            # 信号 点ok或回车 发射选中
	            # intValueChanged(int value)
	            # intValueSelected(int value)
	            # doubleValueChanged(double value)
	            # doubleValueSelected(double value)
	            # textValueChanged(text_str)
	            # textValueSelected(text_str)
            
            ipt.textValueChanged.connect(lambda str: print('文本变化',str))
            # 文本变化 1
            # 文本变化 12
            # 文本变化 123
            # 文本变化 1234
            # 文本变化 12345

            ipt.textValueSelected.connect(lambda str: print('选中文本',str))
            # 选中文本 12345
        
            # ipt.intValueChanged.connect(lambda val: print('int变化',val)) 
            # ipt.intValueSelected.connect(lambda val: print('int选中',val))

            # ipt.doubleValueChanged.connect(lambda val: print('double变化',val))
            # ipt.doubleValueSelected.connect(lambda val: print('double选中',val))
            pass
        btn.clicked.connect(InputDialog_handle) 
        
           
        pass
if __name__ == "__main__":
    app = QApplication([])
    wd=Window()
    wd.show()
    app.exec_()