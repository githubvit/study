#  简介
# 一 Python图形界面开发的几种方案
# Tkinter

基于Tk的Python库，这是Python官方采用的标准库，优点是作为Python标准库、稳定、发布程序较小，缺点是控件相对较少。

# wxPython

基于wxWidgets的Python库，优点是控件比较丰富，缺点是稳定性相对差点、文档少、用户少。

# PySide2、PyQt5

基于Qt 的Python库，优点是控件比较丰富、跨平台体验好、文档完善、用户多。

缺点是 库比较大，发布出来的程序比较大。


# 二  方案选择

白月黑羽的建议是，如果大家要开发小工具，界面比较简单，可以采用Tkinter。

如果是发布功能比较多的正式产品，采用 基于Qt的PySide2、PyQt5。

本教程介绍的就是于Qt的PySide2、PyQt5 开发Python程序的图形界面。


# 三 安装 pyside2

安装包已经包含了qt的库和qt的界面设计开发工具

使用豆瓣源下载安装：

pip install pyside2 -i https://pypi.douban.com/simple/
建议：如果你的程序要发布给客户使用，建议使用32位的Python解释器，这样打包发布的exe程序可以兼容32位的Windows
注意：

Qt 官方网站声明了： Windows上 Python 3.8.0 调用 Qt 5.14 ， 会有问题。

有类似下面这样的导入错误

ImportError: Dll load failed while importing shiboken2: 找不到指定的程序
所以， 就是不能用 Python 3.8.0 ，请使用3.8.1或者以后的版本， Python 3.7 也可以。