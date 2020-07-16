#获取样式
def get_stlye(filepath,obj):
    with open(filepath,'r',encoding='utf-8') as f:
        css_str=f.read() 
        # print(css_str)
        obj.setStyleSheet(css_str)
