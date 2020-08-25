import time
from selenium import webdriver
driver_path=r'D:\chromedriver\chrome_84\chromedriver.exe'
# ifram嵌套网页选择
def one():
    wd=webdriver.Chrome(driver_path)
    url='http://cdn1.python3.vip/files/selenium/sample2.html'
    wd.implicitly_wait(5)
    wd.get(url)
    
    # wels=wd.find_elements_by_css_selector('.plant')
    
    # for wel in wels:
        # print(wel.get_attribute('outerHTML')) # 什么都没有打印出来 原因就在于这个节点是嵌套页面里的节点 页面里面还有页面 要进到里面这个页面去选择

    # 1 获取嵌套页面iframe的节点
    wframe=wd.find_element_by_css_selector('#frame1')
    print(wframe)
    # 2 把wd切换到该节点
    wd.switch_to.frame(wframe)
    time.sleep(5)
    # 3 用切换后的wd选择元素
    # wels=wd.find_elements_by_css_selector('.plant')
    wels=wd.find_elements_by_css_selector('.animal')
    for wel in wels:
        print('---------------------------------------')
        print(wel.get_attribute('outerHTML'))

    # 4 将wd切换回父节点.
    # wd.switch_to.parent_frame()
    # 4 将wd切回外层
    wd.switch_to.default_content()
    # 5 操作外层按钮
    wbtn=wd.find_element_by_css_selector('#outerbutton')
    print(wbtn.text)#wbtn.text
    wd.quit()
# one()

# select类选择

def two():
    
    # 导入Select类
    from selenium.webdriver.support.ui import Select
    wd=webdriver.Chrome(driver_path)
    url='http://cdn1.python3.vip/files/selenium/test2.html'
    wd.implicitly_wait(5)
    wd.get(url)
    # 1 单选
    # 创建Select对象于单选框父节点
    select=Select(wd.find_element_by_css_selector('#ss_single'))
    # 选择'小雷老师'
    select.select_by_visible_text('小雷老师')

    # 2 多选
    select=Select(wd.find_element_by_css_selector('#ss_multi'))

    # 取消所有
    select.deselect_all()       #*****

    
    # 选择小雷老师 和 小凯老师
    select.select_by_visible_text("小雷老师")
    select.select_by_visible_text("小凯老师")

    time.sleep(5)
two()
