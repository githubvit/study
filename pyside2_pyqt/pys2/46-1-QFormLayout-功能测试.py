from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('布局管理QFormLayout的学习')
        self.setup_ui()


    def setup_ui(self):
        # 表单布局（两列多行布局）
        # 以填写表单为主的布局，比如登录、注册、收货地址等。
        # 以行为单元的布局，可以当作每行有两列，
        # 左边是标签列-角色为labelRole，右边是控件列-角色为FieldRole,
        # 跨两列的角色为 SpanningRole 占据整行，比如就是1个提交按钮

        # 子控件
        name_label=QLabel('姓名(&name)')
        name_widget=QLineEdit()
        name_label.setBuddy(name_widget) #设置小伙伴的快捷方式

        age_label=QLabel('年龄(&age)')
        age_widget=QSpinBox()
        age_label.setBuddy(age_widget)

        # 用布局方式来添加性别复选框
        sex_label=QLabel('性别')
        sex_male=QRadioButton('男')
        sex_female=QRadioButton('女')
        # 添加一个盒式布局对象
        sex_layout=QBoxLayout(QBoxLayout.LeftToRight)
        sex_layout.addWidget(sex_label)
        sex_layout.addWidget(sex_male)
        sex_layout.addWidget(sex_female)

        address_lt=QLineEdit()
        address_lt.setObjectName('adr')
        address_lt.setPlaceholderText('请输入地址')

        submit_btn=QPushButton('提交')



        # 定义布局对象
        f_layout=QFormLayout()

        # 设置布局
        self.setLayout(f_layout)

        # 1 添加行 
        # addrow有多种参数形式（widget,widget）、（widget）、（layout）或(str,widget)、（str,layout）
        f_layout.addRow(name_label,name_widget) #添加两个控件（标签控件，输入控件）
        f_layout.addRow(sex_layout) #添加布局 占据一行
        f_layout.addRow(age_label,age_widget) #添加两个控件（标签控件，输入控件）
        f_layout.addRow('地址(a&ddress)',address_lt)#可以用str方式&d直接添加快捷方式（str,widget）,不用设置小伙伴
        f_layout.addRow(submit_btn) #添加按钮 占据一行

        #2  插入行
        # 插入一个爱好行 在性别选择下一行
        hobby_music=QCheckBox('音乐')
        hobby_basketball=QCheckBox('篮球')
        hobby_read=QCheckBox('阅读')

        hobby_layout=QHBoxLayout()
        hobby_layout.addWidget(hobby_music)
        hobby_layout.addWidget(hobby_basketball)
        hobby_layout.addWidget(hobby_read)

        # f_layout.insertRow(-1,'爱好',hobby_layout)#当插入的行号不存在，就会添加在最后一行
        f_layout.insertRow(2,'爱好',hobby_layout)#（index_int,label_text,widget or layout）
        # 插入行与添加行完全一致，就是多了一个索引行号index_int

        # 3 获取位置参数
        print(f_layout.getWidgetPosition(name_label)) 
        #(0, PySide2.QtWidgets.QFormLayout.ItemRole.LabelRole)
        # 得到的结果是一个元组，第一个0 表示在第0行，第二个 表示 角色 当前是labelRole，也表示在第一列
        print(f_layout.getWidgetPosition(name_widget))
        #(0, PySide2.QtWidgets.QFormLayout.ItemRole.FieldRole)
        # 表示在0行，角色是FieldRole，第二列
        print(f_layout.getWidgetPosition(submit_btn))
        # (5, PySide2.QtWidgets.QFormLayout.ItemRole.SpanningRole)
        # 表示在5行，角色为SpanningRole，表示占据整行。
        
        # 查看布局的位置参数
        print(f_layout.getLayoutPosition(sex_layout))
        # (1, PySide2.QtWidgets.QFormLayout.ItemRole.SpanningRole)
        # 在1行，角色为SpanningRole，表示占据整行
        print(f_layout.getLayoutPosition(hobby_layout))
        # (2, PySide2.QtWidgets.QFormLayout.ItemRole.FieldRole)
        # 在2行，角色为FieldRole，表示在第2列。

        # 4 设置行
        # 根据行号盒角色，设置相关控件或布局，如果有必要会延长布局。
        # 如果单元格已经被占用，则不会设置成功。
        # 在行号为6处，设置控件
        test_lb=QLabel('测试')
        test_le=QLineEdit()
        f_layout.setWidget(6,QFormLayout.ItemRole.LabelRole,test_lb)#(行号，角色，控件)
        f_layout.setWidget(6,QFormLayout.ItemRole.FieldRole,test_le)#(行号，角色，控件)
        # 继续在行号为6处，设置控件
        test_lb1=QLabel('测试1')
        test_le1=QLineEdit()
        # f_layout.setWidget(6,QFormLayout.ItemRole.LabelRole,test_lb1) # 在最后一行 出现 测试1
        # f_layout.setWidget(6,QFormLayout.ItemRole.FieldRole,test_le1) # 乱了
        # 设置失败
        
        # 在行号为7处，设置布局
        test2_layout=QHBoxLayout()
        test_lb2=QLabel('测试2')
        test_le2=QLineEdit()
        test_lb3=QLabel('测试3')
        test_le3=QLineEdit()
        test2_layout.addWidget(test_lb2)
        test2_layout.addWidget(test_le2)
        test2_layout.addWidget(test_lb3)
        test2_layout.addWidget(test_le3)
        f_layout.setLayout(7,QFormLayout.ItemRole.SpanningRole,test2_layout)#(行号，角色，布局)
        # 继续在行号为7处，设置控件
        # f_layout.setWidget(7,QFormLayout.ItemRole.LabelRole,test_lb1) # 有用 
        # f_layout.setWidget(7,QFormLayout.ItemRole.FieldRole,test_le1) # 乱了
        # 说明对于占据整行的角色SpanningRole，可以在其右侧设置标签 ，其余不行。

        # 5 移除行
        # 看看是不是被销毁了
        test_lb2.destroyed.connect(lambda:print('行号7被删除了，行中的元素被销毁了'))
        # f_layout.removeRow(7) # 移除行号为7的行 行号7的所有元素都被销毁了
        # f_layout.removeRow(test_lb)#移除该控件所在行
        # f_layout.removeRow(test2_layout)#移除该布局所在行
        # 用子布局下的控件作为参数无效
        # f_layout.removeRow(test_lb2) #无效
        # f_layout.removeWidget(test_lb2) #无效 
    
        # f_layout.takeRow(7) #pyqt5 有用，pyside2无效 第一步是脱开布局 元素并没有被删除 下一步要隐藏或删除脱开的元素。
        # takeRow(7)命令多余，如果要删除直接用removeRow，不删除，直接隐藏其中元素即可。
        # test_lb2.hide()
        # test_le2.hide()
        # test_lb3.hide()
        # test_le3.hide()   
        # 
        # 6 取出布局中的元素
        # 查看元素  子布局只能算1个item元素
        # 元素的索引值与其添加或插入或设置的顺序相关
        # print(f_layout.getItemPosition(0)) #(0, PySide2.QtWidgets.QFormLayout.ItemRole.LabelRole)
        # print(f_layout.getItemPosition(1)) #(0, PySide2.QtWidgets.QFormLayout.ItemRole.FieldRole)
        # print(f_layout.getItemPosition(2)) #(1, PySide2.QtWidgets.QFormLayout.ItemRole.SpanningRole)
        # print(f_layout.getItemPosition(3)) #(3, PySide2.QtWidgets.QFormLayout.ItemRole.LabelRole)
        # print(f_layout.getItemPosition(4)) #(3, PySide2.QtWidgets.QFormLayout.ItemRole.FieldRole)
        # print(f_layout.getItemPosition(5)) #(4, PySide2.QtWidgets.QFormLayout.ItemRole.LabelRole)
        # print(f_layout.getItemPosition(6)) #(4, PySide2.QtWidgets.QFormLayout.ItemRole.FieldRole)
        # print(f_layout.getItemPosition(7)) #(5, PySide2.QtWidgets.QFormLayout.ItemRole.SpanningRole)
        # print(f_layout.getItemPosition(8)) #(2, PySide2.QtWidgets.QFormLayout.ItemRole.LabelRole)
        # print(f_layout.getItemPosition(9)) #(2, PySide2.QtWidgets.QFormLayout.ItemRole.FieldRole)
        # print(f_layout.getItemPosition(10)) #(6, PySide2.QtWidgets.QFormLayout.ItemRole.LabelRole)
        # print(f_layout.getItemPosition(11)) #(6, PySide2.QtWidgets.QFormLayout.ItemRole.FieldRole)

        # 没有元素的时候，出现-1
        # print(f_layout.getItemPosition(12)) #(-1, PySide2.QtWidgets.QFormLayout.ItemRole(-1346412048))
        
        # 取出元素 taketakeAt(int) 
        # 取出0号元素 姓名标签被取出 布局中0行左侧空白。
        # 姓名标签出现在最后一行。
        # print(f_layout.takeAt(0)) #<PySide2.QtWidgets.QWidgetItem object at 0x0000013209259DC8>
        # print(f_layout.takeAt(0).widget()) #<PySide2.QtWidgets.QLabel(0x1410ac2b200) at 0x000001410A1F2548>
        # 隐藏取出的标签 最后一行没有出现姓名标签
        # f_layout.takeAt(0).widget().hide() #隐藏后 
        
        
        # 7 修改标签
        # 通过取FieldRole角色 修改该角色的标签文本
        # print(f_layout.labelForField(name_widget)) #<PySide2.QtWidgets.QLabel(0x1c3dbf8ae20) at 0x000001C3DB551908>
        # 修改地址标签
        print(f_layout.labelForField(address_lt)) #<PySide2.QtWidgets.QLabel(0x25578f6a580) at 0x000002557A315208>
        print(f_layout.children()) 
        #[<PySide2.QtWidgets.QBoxLayout(0x24cf24f39f0) at 0x0000024CF2FFED08>, 
        # <PySide2.QtWidgets.QHBoxLayout(0x24cf24f3c20) at 0x0000024CF2FFEEC8>, 
        # <PySide2.QtWidgets.QHBoxLayout(0x24cf24f3cc0) at 0x0000024CF3005048>]
        
        # f_layout.labelForField(address_lt).setText('a&ddress_地址') #改动字段address_lt的标签label的文本
        self.findChild(QLineEdit,'adr').setText('地址_地址')#改动name='adr',type=QLineEdit的控件的文本
        

        # 8 设定标签列和控件列 换行排列 策略 
       
        # 默认策略  QFormLayout.DontWrapRows 是标签和控件左右排列，不能换行，压缩至最小后就不能压缩了。
        # 策略1 压缩到当一行排不下 就换行 
        # f_layout.setRowWrapPolicy(QFormLayout.WrapLongRows)#
        # 策略2 标签和控件上下排列
        # f_layout.setRowWrapPolicy(QFormLayout.WrapAllRows) #
        
        # 9 对齐方式 和 间距
        # 9.1 整个表单的对齐方式
        # 默认布局对象的对齐方式是左上
        # print(f_layout.formAlignment()==Qt.AlignLeft | Qt.AlignTop)#True
        # 设置布局对象的对齐方式 为 右下
        # f_layout.setFormAlignment(Qt.AlignRight | Qt.AlignBottom)

        # 9.2 表单中标签的对齐方式
        # 默认是左对齐
        # 改为右对齐
        # f_layout.setLabelAlignment(Qt.AlignRight)

        # 9.3 间距
        # 水平最小间距
        # f_layout.setHorizontalSpacing(50)
        # 垂直最小间距
        # f_layout.setVerticalSpacing(50)

        # 10 字段列 增长策略
        # 默认 是 随着窗口拉伸而拉伸 
        # f_layout.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)#大小固定 既不拉伸也不压缩
        # f_layout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)#输入框变、整行角色变，其余不变。
        # f_layout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)#这是默认的
        

        pass
if __name__ == "__main__":
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()