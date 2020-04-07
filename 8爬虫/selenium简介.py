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
def one():
    # url='https://www.bilibili.com'
    # search_el='.nav-search-keyword'
    # search_btn_el='.bilifont bili-icon_dingdao_sousuo,.nav-search-submit'
    # keyword='小升初'

    # url='https://www.ixigua.com'
    # search_el='.search-wrap input'
    # search_btn_el='.search-btn span' # 定位到span 搜索 文字 否则有时可以有时不行
    # keyword='小升初'

    url="https://www.ixigua.com/search/%E5%B0%8F%E5%8D%87%E5%88%9D/?logTag=oBQJEV45pQzISSgkG_KKQ&keyword=%E5%B0%8F%E5%8D%87%E5%88%9D"  

    # 创建 WebDriver 对象，载入 chrome浏览器驱动
    wd=webdriver.Chrome(driver_path)
    # s=wd.start_session
    # 隐式等待
    # 设置最大等待时长为 5秒
    wd.implicitly_wait(5)

    # 一 打开网页 用WebDriver 对象
    # 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
    # print("session:",s)
    wd.get(url)


    # 二 选取节点  用WebDriver 对象 选取 返回 WebElement对象 
    # 一般使用 css 选择器 选取搜索框'.nav-search-keyword'
    # 特殊的选择可以使用 xpath选择器  find_elements_by_xpath('xpath表达式')
    # 比如 次序选择 比 css简练  http://www.python3.vip/doc/tutorial/selenium/xpath_1/#按次序选择
    #  选择父节点 css没有       http://www.python3.vip/doc/tutorial/selenium/xpath_1/#选择父节点
    #  兄弟选择 可前可后        http://www.python3.vip/doc/tutorial/selenium/xpath_1/#选择父节点
    # wel_search=wd.find_element_by_css_selector(search_el)

    # 获取网页html 通过属性选择器 获取该节点的整个html,如果要获取内部的html，则el.get_attribute('innerHTML'),由于该节点无内部节点，所以会输出空
    # print(el.get_attribute('outerHTML'))

    # 三 操作节点元素


    # 1 输入文本 在搜索框输入'小升初'并回车'\n'
    # wel_search.send_keys(f'{keyword}\n')
    #  清空 输入框
    # wel_search.clear()
    #  
    # 2 获取文本 
    # 普通WebElement对象 比如 span、p、i、div等 获取网页文本，直接用el.text即可
    # 对于input 要用el.get_attribute('value')才能获取输入框内的值
    # print(wel_search.get_attribute('value'))

    # 3 点击click()
    #  如果在搜索框中不输入回车 就要点击搜索按钮。
    #  用wd获取搜索按钮
    # wel_search_btn=wd.find_element_by_css_selector(search_btn_el)
    # wel_search.send_keys(keyword)
    # wel_search_btn.click()
    # print(wel_search_btn.get_attribute('outerHTML'))

    # print('搜索页')
    # print('window_handles',wd.window_handles)

    # 4 更多操作 http://www.python3.vip/doc/tutorial/selenium/skills_2/#更多动作

    # 四 页面跳转 窗口切换 http://www.python3.vip/doc/tutorial/selenium/frame/#切换到新的窗口
    # 1 保存当前窗口的句柄 便于 跳回
    # mainWindow=wd.current_window_handle
    # print('当前窗口',mainWindow)
    # 2 跳到搜索结果页 
    # WebDriver对象有window_handles 属性，这是一个列表对象， 里面包括了当前浏览器里面所有的窗口句柄。
    # for handle in wd.window_handles:
    #     print('for',handle)
    #     if handle == mainWindow:
    #         print('1')
    #         continue
    #     # 先切换到搜索结果页面
    #     wd.switch_to.window(handle)
    #     # 如果 是 我们要的窗口 就 break
    #     # print(wd.title)
    #     if keyword in wd.title:
    #         break

    # search_url=wd.current_url
    # print("session:",wd.session_id)
    # print(search_url)
    # 3 跳回


    # 退出 会关闭浏览器
    # wd.quit()




# 五 页面冻结 http://www.python3.vip/doc/tutorial/selenium/skills_2/#冻结界面
    # 有些元素甚至页面 需要鼠标放在上面才有，离开就消失，不利于进行页面分析。
    # 因此在 开发者工具栏 console 里面执行如下js代码

    # setTimeout(function(){debugger}, 5000) 便会在5秒后冻结页面，即使鼠标移开也不会消失，

    # 5秒后 页面出现 paused in debugger界面，页面暂停了。
    # 这样就可捕捉元素，分析页面了。

    # 在paused in debugger界面点击 跳出，页面就恢复了。

# 六 捕捉弹出对话框
    # 通知框    Alert
    #    获取提示信息 driver.switch_to.alert.text
    #    点击ok或确认 driver.switch_to.alert.accept()

    # 确认框    Confirm
    #    以上两点与Alert一致
    #    点击cancel或取消 driver.switch_to.alert.dismiss()


    # 输入确认框  Prompt
    #     以上三点一致
    #     在输入框中输入 driver.switch_to.alert.send_keys('输入的内容')

# 七 执行js 打开选项卡
def open_window():
    #选项卡管理：切换选项卡，有js的方式windows.open,有windows快捷键：ctrl+t等，最通用的就是js的方式

    browser=webdriver.Chrome(driver_path)
    # 隐式等待
    # 设置最大等待时长为 5秒
    browser.implicitly_wait(5)
    # 打开网页
    browser.get('https://www.baidu.com')

    # 执行js代码 打开新选项卡
    browser.execute_script('window.open()')

    print(browser.window_handles) #获取所有的选项卡
    
    # 切换到新选项卡
    browser.switch_to.window(browser.window_handles[-1])
    browser.get('https://www.taobao.com')
    time.sleep(5)
    
    # 返回到原来的选项卡
    browser.switch_to.window(browser.window_handles[0])
    time.sleep(5)
    
    # 打开新页面
    browser.get('https://www.bilibili.com')
    time.sleep(5)
    
    # 后退到原来的页面
    browser.back()
    time.sleep(5)
    
    
    # 关闭浏览器
    browser.close()

# open_window()

# 八 xpath 选择

def xpath_sl():
    driver = webdriver.Chrome(driver_path)
    driver.get('https://doc.scrapy.org/en/latest/_static/selectors-sample1.html')
    driver.implicitly_wait(3) #使用隐式等待
    try:
        # find_element_by_xpath
        #//与/
        # driver.find_element_by_xpath('//body/a')  # 开头的//代表从整篇文档中寻找,body之后的/代表body的儿子，这一行找不到就会报错了

        driver.find_element_by_xpath('//body//a')  # 开头的//代表从整篇文档中寻找,body之后的//代表body的子子孙孙
        driver.find_element_by_css_selector('body a')

        #取第n个
        res1=driver.find_elements_by_xpath('//body//a[1]') #取第一个a标签 是[1]不是[0]
        print(res1[0].text)

        #按照属性查找,下述三者查找效果一样
        res1=driver.find_element_by_xpath('//a[5]') #找到第5个a标签
        res2=driver.find_element_by_xpath('//a[@href="image5.html"]')#找到属性href="image5.html"的a标签
        res3=driver.find_element_by_xpath('//a[contains(@href,"image5")]') #模糊查找 找到包含href属性，有"image5"字样的a标签
        print('==>', res1.text)
        print('==>',res2.text)
        print('==>',res3.text)


        #其他
        res1=driver.find_element_by_xpath('/html/body/div/a')
        print(res1.text)

        res2=driver.find_element_by_xpath('//a[img/@src="image3_thumb.jpg"]') #找到子标签img的src属性为image3_thumb.jpg的a标签
        print(res2.tag_name,res2.text)
        print(res2.id)
        # 获取标签的右上角坐标
        print(res2.location)
        # 获取标签的宽和高
        print(res2.size)

        # res3 = driver.find_element_by_xpath("//input[@name='continue'][@type='button']") #查看属性name为continue且属性type为button的input标签
        # res4 = driver.find_elements_by_xpath("//*[@name='continue'][@type='button']") #查看属性name为continue且属性type为button的所有标签

        # print(res3.tag_name,res3.text)
        # print(res4[0].tag_name,res4[0].text)
        time.sleep(5)

    except Exception as e:
        print(e)

    finally:
        driver.close()

# xpath_sl()
# 结果
    # Name: My image 1
    # ==> Name: My image 5
    # ==> Name: My image 5
    # ==> Name: My image 5
    # Name: My image 1
    # a Name: My image 3
    # 576ae867-ce46-4cac-a161-10fc2bc94c49
    # {'x': 8, 'y': 50}
    # {'height': 42, 'width': 165}


# 九 页面高级操作
    # 1 移动页面元素 
    # actionchains是selenium里面专门处理鼠标相关的操作 
    # 使用click() 方法可以模拟鼠标单击操作,
    # 但是鼠标操作还包括:右击、双击、悬停、鼠标拖动等复杂功能就可以使用actionchains对象。


from selenium.webdriver import ActionChains
# 分析人移动鼠标的过程 产生移动轨迹
def make_track(distancex):
    # 轨迹点
    track_list=[]
    # 匀加速和快接近就匀急减速

    # 初始速度
    v=0
    # 间隔时间
    t=0.23
    # 减速点
    deceleration_point=distancex*4/5

    # 初始距离
    cs=0
    while cs<distancex:
        if cs<deceleration_point:
            # 匀加速
            a=2.5
        else:
            # 匀减速
            a=-4

        # 记录移动距离
        s=v*t+0.5*a*(t**2)  
        # 把当前移动距离加入轨迹列表
        track_list.append(round(s)) 
        # 更新当前移动总距离
        cs=cs+s
        # 更新当前速度
        v=v+a*t

    return track_list

# 按移动轨迹移动滑块 通过验证
def move_slid(wd,slider,track_list):
    
    # 获取 滑块
    slider=wd.find_element_by_css_selector(slider)
    # 按住滑块
    ActionChains(wd).click_and_hold(slider).perform()
    # 按轨迹移动
    for x in track_list:
        # print(x)
        ActionChains(wd).move_by_offset(xoffset=x,yoffset=0).perform()

    # else:
    #     # 先移过去一点，再移回来，更像人的移动
    #     mouse.move_by_offset(xoffset=2.5,yoffset=0).perform()
    #     mouse.move_by_offset(xoffset=-2.5,yoffset=0).perform()
    # 释放
    time.sleep(0.5) #0.5秒后释放鼠标
    ActionChains(wd).release().perform()

def move_el():
    
    driver = webdriver.Chrome(driver_path)
    driver.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
    
    driver.implicitly_wait(3)  # 使用隐式等待

    try:
        # 切换到子页面
        driver.switch_to.frame('iframeResult') ##切换到iframeResult

        # 找到要操作的元素
        
        sourse=driver.find_element_by_id('draggable')
        target=driver.find_element_by_id('droppable')
        # 获取鼠标移动距离
        distance=target.location['x']-sourse.location['x']

        # 模仿人移动 产生轨迹
        track_list=make_track(distance)
        print(f'轨迹：{track_list}，{sum(track_list)},距离：{distance}')

        # 按轨迹 移动 滑块
        move_slid(driver,'#draggable',track_list)

        #方式一：基于同一个动作链串行执行
        # actions=ActionChains(driver) #拿到动作链对象
        # actions.drag_and_drop(sourse,target) #把动作放到动作链中，准备串行执行
        # actions.perform()

        #方式二：不同的动作链，每次移动的位移都不同
        # 用 ActionChains(driver)对象，按住鼠标左键不放
        # ActionChains(driver).click_and_hold(sourse).perform()
        
        # track=0
        # while track < distance:
        #     # 用 ActionChains(driver)对象，按住鼠标左键不放并沿x，移动鼠标，每次2像素。
        #     ActionChains(driver).move_by_offset(xoffset=2,yoffset=0).perform()
        #     track+=2
        # for track in track_list:
            # ActionChains(driver).move_by_offset(xoffset=track,yoffset=0).perform()
        # else:
            # ActionChains(driver).move_by_offset(xoffset=3,yoffset=0).perform()
            # ActionChains(driver).move_by_offset(xoffset=-3,yoffset=0).perform()
        
        #  用 ActionChains(driver)对象，释放鼠标。这里会弹出对话框，结束。
        
        # ActionChains(driver).release().perform()
        
        

        time.sleep(3)

        # 点击确定 
        driver.switch_to.alert.accept()

        time.sleep(1)

        #切回父页面
        driver.switch_to.parent_frame() 
        # 执行js 弹出 对话框
        driver.execute_script('alert("关闭浏览器")')
        time.sleep(3)
         # 再次点击确定 
        driver.switch_to.alert.accept()

    except Exception as e:
        print(e)
    finally:
        driver.close()

move_el()