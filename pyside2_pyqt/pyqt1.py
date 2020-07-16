# 案例
# 现在我们要开发一个程序，让用户输入一段文本包含：员工姓名、薪资、年龄。

# 格式如下：

# 薛蟠     4560 25
# 薛蝌     4460 25
# 薛宝钗   35776 23
# 薛宝琴   14346 18
# 王夫人   43360 45
# 王熙凤   24460 25
# 王子腾   55660 45
# 王仁     15034 65
# 尤二姐   5324 24
# 贾芹     5663 25
# 贾兰     13443 35
# 贾芸     4522 25
# 尤三姐   5905 22
# 贾珍     54603 35
# 该程序可以把薪资在 2万 以上、以下的人员名单分别打印出来。


from PySide2.QtWidgets import QApplication,QMainWindow,QPushButton,QPlainTextEdit,QMessageBox
# 一 初始化
# QtWidgets 是pyside2负责控件（Widgets）的部分
# QApplication 提供了整个图形界面程序的底层管理功能，比如：
    # 初始化、程序入口参数的处理，用户事件（对界面的点击、输入、拖拽）分发给各个对应的控件，等等…
    # 既然QApplication要做如此重要的初始化操作，所以，我们必须在任何界面控件对象创建前，先要创建它。

# 二 图形界面
    # QMainWindow、QPlainTextEdit、QPushButton 是3个控件类，分别对应界面的主窗口、文本框、按钮
        # 他们都是控件基类对象QWidget的子类。
    # 在 Qt 系统中，控件（widget）是 层层嵌套 的，除了最顶层的控件，其他的控件都有父控件。


    # 控件对象的 move 方法决定了这个控件显示的位置，单位是像素。
    # 控件对象的 resize 方法决定了这个控件显示的大小。

# 三 界面动作处理 (signal 和 slot)
    # 在 Qt 系统中， 当界面上一个控件被操作时，比如 被点击、被输入文本、被鼠标拖拽等， 
    # 就会发出 信号 ，英文叫 signal 。就是表明一个事件（比如被点击、被输入文本）发生了。
    # 我们可以预先在代码中指定 处理这个 signal 的函数，这个处理 signal 的函数 叫做 slot 。

# 四 常用控件查阅 http://www.python3.vip/tut/py/gui/qt_05/
def one():
    # 实例化应用程序
    # app=QApplication([]) #例中有空列表参数
    app=QApplication()

    # 实例化主窗口（）
    window=QMainWindow()
    # 主窗口大小 
    window.resize(500,400)
    # 主窗口出现的起始位置
    window.move(2000,600)
    # 主窗口标题栏
    window.setWindowTitle('薪资统计')

    # 实例化文本编辑器窗口-多行纯文本框(父控件对象是主窗口)
    textEdit=QPlainTextEdit(window)
    textEdit.setPlaceholderText("请输入薪资表")
    # 文本编辑器窗口位置（距离主窗口左边的距离，距离主窗口上边的距离）
    textEdit.move(10,25)
    # 文本编辑器窗口大小（宽，高）
    textEdit.resize(300,350)

    # 实例化按钮(名称，父控件对象是主窗口)
    button=QPushButton('统计',window)
    # 按钮的位置（距离主窗口左边的距离，距离主窗口上边的距离）
    button.move(360,100)
    # button.resize(60,30) #不写这行就会以默认的大小显示出来
    # print(button.size())# PySide2.QtCore.QSize(100, 30) 默认大小 是宽100，高30

    
    # slot
    def handleCalc():
        print('统计按钮被点击了')
    # 点击按钮signal connect slot
    button.clicked.connect(handleCalc)


    


    # 放在主窗口的控件，要能全部显示在界面上， 必须加上下面这行代码
    window.show()

    # 进入QApplication的事件处理循环，接收用户的输入事件（），并且分配给相应的对象去处理。
    app.exec_()

# one()

# 五 封装到类中

# 在开发中，一般每个窗体被封装成类，多个类的组合就是多个窗体的组合，可以形成复杂的较大的系统性的图形界面。

class Stats():
    def __init__(self):
        # 界面
        self.window = QMainWindow()
        self.window.resize(500, 400)
        self.window.move(300, 300)
        self.window.setWindowTitle('薪资统计')

        self.textEdit = QPlainTextEdit(self.window)
        self.textEdit.setPlaceholderText("请输入薪资表")
        self.textEdit.move(10, 25)
        self.textEdit.resize(300, 350)

        self.button = QPushButton('统计', self.window)
        self.button.move(380, 80)

        # 界面动作 signal connect slot
        self.button.clicked.connect(self.handleCalc)

    # slot函数
    # 实现统计按钮功能：把薪资在 2万 以上、以下的人员名单分别打印出来。
    def handleCalc(self):
        # 取得 文本编辑器控件self.textEdit的输入结果 需要查阅每个控件的功能函数，比如取得文本编辑控件的结果：toPlainText()
        info = self.textEdit.toPlainText()
        # print(type(info)) #<class 'str'>
        # 薪资20000 以上 和 以下 的人员名单
        salary_above_20k = ''
        salary_below_20k = ''
        for line in info.splitlines(): # 把info字符串 按行切割 info.splitlines()
            if not line.strip(): #如果是空行 就直接跳过
                # print(1)
                continue
            parts = line.split(' ') #把每行的字符串 按空格切割
            # 利用列表生成式及三元判断 去掉列表中的空字符串内容
            parts = [p for p in parts if p]
            # print(parts) #['薛蝌', '4460', '25']
            # 取出姓名 工资 年龄
            name,salary,age = parts
            if int(salary) >= 20000: # 注意换行 '\n'
                salary_above_20k += name + '\n'
            else:
                salary_below_20k += name + '\n'
        # 消息窗口控件.about(父控件，本消息窗口名称，消息体)
        QMessageBox.about(self.window,
                    '统计结果',
                    f'''薪资20000 以上的有：\n{salary_above_20k}
                    \n薪资20000 以下的有：\n{salary_below_20k}'''
                    )
# 程序实例化
app = QApplication([])

# 界面类实例化
stats = Stats()
# 秀出界面 显示窗口 没有show() 就不显示 界面类主窗口的展示 ***
stats.window.show()

# 启动程序 进入死循环 阻塞 直到按x 退出阻塞
app.exec_()

# 只有关闭界面后才会执行下一行代码
print('阻塞了')