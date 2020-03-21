# 浏览器自动化 selenium 

# http://www.python3.vip/doc/tutorial/selenium/01/

# selenium 是 实现 编写程序 通过浏览器驱动 操作 浏览器 完成 web自动化的框架 
# +--------------------+    +--------------------+     +---------------+                                                                                                                   
# |   自动化程序      发|--->|   浏览器驱动        |---> |               |                                                                                                  
# | selenium客户端库    |    | 由浏览器厂家提供    |     |     浏览器     |                                                                                           
# |                  收|<---|                    |<--- | edge、chrome等 |                                                                                                 
# +--------------------+    +--------------------+     +---------------+   
# 
# 1 打造 selenium 环境
#   安装 selenium ：  pip install selenium 
#   安装 浏览器：  安装chrome浏览器                                                                                    
#   下载 浏览器驱动： 根据 chrome浏览器版本 下载相应驱动

# 2 生成 webdriver 对象 ，操作该对象即可打开页面、选取节点、操作页面等一系列人为动作。
# 拿到列表页
import time
from selenium import webdriver
driver_path=r'D:\chromedriver.exe'


def index_search(url,search_el,search_btn_el,keyword):
    

    # 创建 WebDriver 对象，载入 下载解压好的 chrome浏览器驱动
    wd=webdriver.Chrome(driver_path)

    # 设置最大等待时长为 5秒
    wd.implicitly_wait(5)

    # 一 打开网页 用WebDriver 对象
    # 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
    wd.get(url)

    # 二 选取节点  用WebDriver 对象 选取 返回 WebElement对象 
    # 一般使用 css 选择器 选取搜索框'.nav-search-keyword'
    # 特殊的选择可以使用 xpath选择器  find_elements_by_xpath('xpath表达式')
    # 比如 次序选择 比 css简练  http://www.python3.vip/doc/tutorial/selenium/xpath_1/#按次序选择
    #  选择父节点 css没有       http://www.python3.vip/doc/tutorial/selenium/xpath_1/#选择父节点
    #  兄弟选择 可前可后        http://www.python3.vip/doc/tutorial/selenium/xpath_1/#选择父节点
    wel_search=wd.find_element_by_css_selector(search_el)

    # 获取网页html 通过属性选择器 获取该节点的整个html,如果要获取内部的html，则el.get_attribute('innerHTML'),由于该节点无内部节点，所以会输出空
    # print(el.get_attribute('outerHTML'))

    # 三 操作节点元素


    # 1 输入文本 在搜索框输入'小升初'并回车'\n'
    # wel_search.send_keys(f'{keyword}\n')
    #  清空 输入框
    wel_search.clear()
    #  
    # 2 获取文本 
    # 普通WebElement对象 比如 span、p、i、div等 获取网页文本，直接用el.text即可
    # 对于input 要用el.get_attribute('value')才能获取输入框内的值
    # print(wel_search.get_attribute('value'))

    # 3 点击click()
    #  如果在搜索框中不输入回车 就要点击搜索按钮。
    #  用wd获取搜索按钮
    wel_search_btn=wd.find_element_by_css_selector(search_btn_el)
    wel_search.send_keys(keyword)
    wel_search_btn.click()
    # print(wel_search.get_attribute('value'))

    # print('搜索页')
    # print('window_handles',wd.window_handles)

    # 4 更多操作 http://www.python3.vip/doc/tutorial/selenium/skills_2/#更多动作

    # 四 页面跳转 窗口切换 http://www.python3.vip/doc/tutorial/selenium/frame/#切换到新的窗口
    # 1 保存当前窗口的句柄 便于 跳回
    mainWindow=wd.current_window_handle
    # print('当前窗口',mainWindow)
    # 2 跳到搜索结果页 
    # WebDriver对象有window_handles 属性，这是一个列表对象， 里面包括了当前浏览器里面所有的窗口句柄。
    for handle in wd.window_handles:
        # print('for',handle)
        if handle == mainWindow:
            # print('1')
            continue
        # 先切换到搜索结果页面
        wd.switch_to.window(handle)
        # 如果 是 我们要的窗口 就 break
        # print(wd.title)
        if keyword in wd.title:
            break
    
    search_url=wd.current_url
    # print(search_url)
    # 3 跳回

    # 五 页面冻结 http://www.python3.vip/doc/tutorial/selenium/skills_2/#冻结界面
    # 有些元素甚至页面 需要鼠标放在上面才有，离开就消失，不利于进行页面分析。
    # 因此在 开发者工具栏 console 里面执行如下js代码

    # setTimeout(function(){debugger}, 5000) 便会在5秒后冻结页面，即使鼠标移开也不会消失，
    # 这样就捕捉元素，分析页面了。

    # 六 弹出对话框
    # 通知框    Alert
    #    获取提示信息 driver.switch_to.alert.text
    #    点击ok或确认 driver.switch_to.alert.accept()

    # 确认框    Confirm
    #    以上两点与Alert一致
    #    点击cancel或取消 driver.switch_to.alert.dismiss()


    # 输入确认框  Prompt
    #     以上三点一致
    #     在输入框中输入 driver.switch_to.alert.send_keys('输入的内容')

    # 退出 会关闭浏览器
    # wd.quit()

    return search_url


# if __name__ == "__main__":
#     # url='https://www.bilibili.com'
#     # search_el='.nav-search-keyword'
#     # search_btn_el='.bilifont bili-icon_dingdao_sousuo,.nav-search-submit'
#     # keyword='小升初'
    
#     url='https://www.ixigua.com'
#     search_el='.search-wrap input'
#     search_btn_el='.search-btn span' # 定位到span 搜索 文字 否则有时可以有时不行
#     keyword='小升初'

#     index_search(url,search_el,search_btn_el,keyword)