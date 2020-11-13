from PySide2.QtWidgets import QApplication,QWidget,QPushButton
from PySide2.QtCore import Signal,Qt


class CaBtn(QPushButton):
    filepath=r'D:\pyj\st\study\pyside2_pyqt\pys2\l_r_c2\ca_btn.css'
    # 自定义信号 
    key_parse_signal=Signal(str,str)
    def mousePressEvent(self,evt):
        super().mousePressEvent(evt)
        # 判断键值
        if evt.button()==Qt.MouseButton.LeftButton:
            # print(self.text(),self.property('role'))
            # 发射自定义信号 携带 按键文本 和 自定义的role属性值 两个参数
            self.key_parse_signal.emit(self.text(),self.property('role'))
        
        pass

    # 实现常规样式和动态样式的加载 
    def resizeEvent(self,evt):
        super().resizeEvent(evt)
        with open(self.filepath,'r') as f:
            # 常规样式
            # /* + - * / 这四个运算符有选中样式 明确当前选了哪个运算符 因为其他的按键一按就有结果，而运算符没有 */
            #  css文件中不能添加注释，一添加样式文件就失效，这是从样式文件中取出来的
            css1=f.read()
            # 动态样式
            css2='QPushButton {border-radius: %dpx;}'%(min(self.width(),self.height())/2)
            # 加载样式
            self.setStyleSheet(css1+css2)
        pass