from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
# from PyQt5.Qt import *

# 两级联动下拉菜单，最后输出数据编码
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('两级联动下拉菜单')
        # 省市字典
        self.city_dic = {
            "北京": {
                "东城": "001",
                "西城": "002",
                "朝阳": "003",
                "丰台": "004"
            },
            "上海": {
                "黄埔": "005",
                "徐汇": "006",
                "长宁": "007",
                "静安": "008",
                "松江": "009"
            },
            "广东": {
                "广州": "010",
                "深圳": "011",
                "湛江": "012",
                "佛山": "013"
            }
        }
        self.setup_ui()

    def setup_ui(self):
        # 1 两个下拉菜单
        self.pro_cbx=QComboBox(self)
        self.pro_cbx.resize(100,25)
        self.pro_cbx.move(50,50)
        self.city_cbx=QComboBox(self)
        self.city_cbx.resize(100,25)
        self.city_cbx.move(200,50)

        # 2 响应省级下拉菜单信号 注意信号要在增加条目前设置 这样就可以抓住早的信号
        self.pro_cbx.currentTextChanged.connect(self.city_changed)

        # 3 响应市级下拉菜单信号 输出编码
        # 输出索引，当没有索引（即clear时），输出 -1
        # self.city_cbx.currentTextChanged.connect(lambda : print(self.city_cbx.currentIndex()))
        # 输出编码，当clear时，输出None，
        self.city_cbx.currentTextChanged.connect(lambda : print(self.city_cbx.itemData(self.city_cbx.currentIndex())))
        
        # 4 给省级下拉框增加条目
        self.pro_cbx.addItems(self.city_dic.keys())

        pass

    def city_changed(self,val):
        # print(val)
        # 获取省级下的城市
        citys=self.city_dic[val]
        # print(citys)
        # 设置二级菜单
        # 先清空 
        # 为了避免市级下拉菜单输出None 在clear时，先暂时屏蔽
        self.city_cbx.blockSignals(True)
        self.city_cbx.clear()
        # 恢复信号
        self.city_cbx.blockSignals(False)
        # 再添加
        for key,val in citys.items():
            self.city_cbx.addItem(key,val)
        
        pass

if __name__ == "__main__":
    from PySide2.QtWidgets import *
    app=QApplication([])
    wd=Window()
    wd.show()
    app.exec_()