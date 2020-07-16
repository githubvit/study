from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('错误消息对话框QErrorMessage的学习')
        self.setup_ui()


    def setup_ui(self):
        # 用于通知用户或请求用户的提问和接收应答一个模态对话框
        msgbox=QMessageBox(self)
        # msgbox=QMessageBox(图标,'窗口标题','主题',标准按钮1|标准按钮2,self) #多个按钮必须用按位或|
        # msgbox=QMessageBox(QMessageBox.Icon.Question,'警告提示','<h3>文档内容已经被修改</h3>',QMessageBox.Ok|QMessageBox.Cancel,self)
        
        # 标准图标
        # msgbox.setIcon(QMessageBox.Icon.Critical)         # err
        # msgbox.setIcon(QMessageBox.Icon.Information)      # info
        # msgbox.setIcon(QMessageBox.Icon.Warning)            # warning
        msgbox.setIcon(QMessageBox.Icon.Question)           # help Question
        # msgbox.setIcon(QMessageBox.Icon.NoIcon)           # 无图标
        # 自定义图标
        # pmp=QPixmap(r'pyside2_pyqt\pys2\xxx.png')
        # pmp=pmp.scaled(60,60)
        # msgbox.setIconPixmap(pmp)

        # 对话框标题
        msgbox.setWindowTitle('警告提示')

        # 主题标签文本
        msgbox.setText('<h3>文档内容已经被修改</h3>')
        # 提示文本
        msgbox.setInformativeText('<h5>是否要在关闭前保存？</h5>')
        # 复选框
        msgbox.setCheckBox(QCheckBox('下一次再打开',msgbox))
        # 详细文本 不能展示富文本 默认隐藏 点击Show Details按钮 可以看到
        msgbox.setDetailedText(
            '''<h3>点击Show Details才能看到本详细内容，
                点击Hide Details就能隐藏本详细内容。
            </h3>'''
            ) 
# 
        # 添加按钮
        # 如果不添加，默认会有ok和Show Details..按钮
        
        # 添加标准按钮 QMessageBox.StandardButton 和角色默认捆绑好的按钮
        # msgbox.addButton(标准按钮)
        # msgbox.setStandardButtons(标准按钮1|标准按钮2|标准按钮3) #设置多个标准按钮

        # 添加自定义按钮  会输出QPushButton对象
        # msgbox.addButton('按钮名称',按钮角色) -> QPushButton
        btn1=msgbox.addButton('确定',QMessageBox.AcceptRole)
        btn2=msgbox.addButton('取消',QMessageBox.RejectRole)

        # 移除按钮
        # msgbox.removeButton(btn1)

        # 设置默认按钮 这样回车就可以点击该按钮
        # msgbox.setDefaultButton(btn1)
        
        # 关联退出按钮 
        msgbox.setEscapeButton(btn2) # 按ESC 就等于点击了btn2按钮
        # print(btn2) # <PySide2.QtWidgets.QPushButton(0x27818918190) at 0x0000027818CC9488>

        # 获取按钮角色
        # print(msgbox.buttonRole(btn2)) # PySide2.QtWidgets.QMessageBox.ButtonRole.RejectRole
        
        # 信号 buttonClicked 会传递点击的按钮 

        # msgbox.buttonClicked.connect(lambda btn: print(btn)) #按ESC 输出 <PySide2.QtWidgets.QPushButton(0x27818918190) at 0x0000027818CC9488>

        def get_btnrole(btn):
            if msgbox.buttonRole(btn2) == msgbox.buttonRole(btn):
                print('按ESC和点击了取消就是点击了btn2')
            # print(msgbox.buttonRole(btn)) #PySide2.QtWidgets.QMessageBox.ButtonRole.RejectRole
            pass

        msgbox.buttonClicked.connect(get_btnrole) #按ESC 输出 <PySide2.QtWidgets.QPushButton(0x27818918190) at 0x0000027818CC9488>

        # 文本交互  只对主题有效
        #可以用鼠标选中 也可以用键盘选中 还可以编辑
        # msgbox.setTextInteractionFlags(Qt.TextSelectableByMouse|Qt.TextSelectableByKeyboard|Qt.TextEditable)
        # 文本格式 设置主题文本格式为普通文本
        # msgbox.setTextFormat(Qt.PlainText)#这时主题显示html代码
        
        
        msgbox.open()

        # 按钮角色： 不同的角色代表不同的意思
        # QMessageBox.ButtonRole
        	# InvalidRole
        		# 该按钮无效。
        	# AcceptRole
        		# 单击该按钮将使对话框被接受（例如，确定）。
        	# RejectRole
        		# 单击该按钮会导致拒绝对话框（例如取消）。
        	# DestructiveRole
        		# 单击该按钮会导致破坏性更改（例如，对于Discarding Changes）并关闭对话框。
        	# ActionRole
        		# 单击该按钮将导致更改对话框中的元素。
        	# HelpRole
        		# 可以单击该按钮以请求帮助。
        	# YesRole
        		# 按钮是一个“是”的按钮。
        	# NoRole
        		# 按钮是一个“无”按钮。
        	# ApplyRole
        		# 该按钮应用当前更改。
        	# ResetRole
        		# 该按钮将对话框的字段重置为默认值。

        # 标准按钮
        # QMessageBox.StandardButton
        	# QMessageBox.Ok
        		# 使用AcceptRole定义的“确定”按钮。
        	# QMessageBox.Open
        		# 使用AcceptRole定义的“打开”按钮。
        	# QMessageBox.Save
        		# 使用AcceptRole定义的“保存”按钮。
        	# QMessageBox.Cancel
        		# 使用RejectRole定义的“取消”按钮。
        	# QMessageBox.Close
        		# 使用RejectRole定义的“关闭”按钮。
        	# QMessageBox.Discard	
        		# “丢弃”或“不保存”按钮，具体取决于使用DestructiveRole定义的平台。
        	# QMessageBox.Apply
        		# 使用ApplyRole定义的“应用”按钮。
        	# QMessageBox.Reset
        		# 使用ResetRole定义的“重置”按钮。
        	# QMessageBox.RestoreDefaults
        		# 使用ResetRole定义的“恢复默认值”按钮。
        	# QMessageBox.Help
        		# 使用HelpRole定义的“帮助”按钮。
        	# QMessageBox.SaveAll
        		# 使用AcceptRole定义的“全部保存”按钮。
        	# QMessageBox.Yes
        		# 使用YesRole定义的“是”按钮。
        	# QMessageBox.YesToAll
        		# 使用YesRole定义的“Yes to All”按钮。
        	# QMessageBox.No
        		# 使用NoRole定义的“否”按钮。
        	# QMessageBox.NoToAll
        		# 使用NoRole定义的“No to All”按钮。
        	# QMessageBox.Abort
        		# 使用RejectRole定义的“Abort”按钮。
        	# QMessageBox.Retry
        		# 使用AcceptRole定义的“重试”按钮。
        	# QMessageBox.Ignore
        		# 使用AcceptRole定义的“忽略”按钮。
        	# QMessageBox.NoButton
        		# 无效按钮。

        pass

if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    # 静态方法 快速展示 模态 返回按钮
    # QMessageBox.about(wd,'标题','关于xxx') 
    # QMessageBox.aboutQt(wd,'标题') #关于Qt
    # QMessageBox.critical(wd,'错误','xxx',QMessageBox.Ok|QMessageBox.Cancel,QMessageBox.Ok) # 错误提示  默认按钮 ok
    # QMessageBox.information(wd,'信息','xxx',QMessageBox.Ok|QMessageBox.Cancel) # 信息提示
    # QMessageBox.question(wd,'问题','xxx',QMessageBox.Ok|QMessageBox.Cancel) # 问题提示
    # QMessageBox.warning(wd,'警告','xxx',QMessageBox.Ok|QMessageBox.Cancel) # 问题提示
    app.exec_()