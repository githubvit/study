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
# driver_path=r'D:\chromedriver\chrome_84\chromedriver.exe'     #chrome浏览器驱动
driver_path=r'D:\EdgeDriver\edgedriver_win64\msedgedriver.exe'  #Edge浏览器驱动
def one():
    url='https://www.bilibili.com'
    search_el='input.nav-search-keyword'
    # 手工定位要使用的元素 
        # 1 按F12（或在页面右击 检查、审查元素等） 打开开发者页面 

        # 2 点击 Elements 标签后， 同时按 Ctrl 键 和 F 键， 就会出现 元素搜索框(Find by string,selector,or XPath)       *****

        # 3 可以在里面输入任何 CSS Selector 表达式 ，如果能选择到元素， 右边就会显示出类似 '2 of 3' 这样的内容。
            # of 后面的数字表示这样的表达式 总共选择到几个元素
            # of 前面的数字表示当前黄色高亮显示的是 其中第几个元素

        # 4 css选择 
            # 练习网址 http://cdn1.python3.vip/files/selenium/sample1.html
            # 4.1 后代选择 
                # 直接用'>' '#layer1>div'; 
                # 间接用' '空格 '#layer1 span'

            # 4.2 属性选择 
                # 用方括号'[]'  '[href]' 选择有href属性的元素;
                # '[href="http://www.miitbeian.gov.cn"]' 选择属性href的值为"http://www.miitbeian.gov.cn"的元素
                #  属性值 包含用'*=' 某个值 '[href*='miitbeian']'
                #  属性值 开头用'^=' 某个值 '[href^='http']'
                #  属性值 结尾用'$=' 某个值 '[href$='com']'

            # 4.3 叠加选择
                # 无空格  'div.plant'   注意不能有空格 否则变成后代选择. 

            # 4.4 和选 +
                # 用','  '.plant,.animal'选择plant和animal 

            # 4.5 子节点次序选择 :
                # 练习网址 http://cdn1.python3.vip/files/selenium/sample1b.html
                # 父元素空格:nth-child(父元素的第几个子节点)
                    # '#t1 :nth-child(2)' id为t1的节点下的第二个子节点 选择了唐诗的第一个作者.
                # 选择器叠加次序选择
                    # 'span:nth-child(2)' 选择是第二个子节点是span的子节点  选择了唐诗和宋词的第一个作者.

                # 倒数选择 :nth-last-child(1) 倒数第一
                    # 'p:nth-last-child(1)' 选择了最后一个子节点 选择了最后一首唐诗和宋词
                    # #t2 :nth-last-child(2) 选择了id为t2的子节点中的倒数第二个子节点 选择了倒数第二首宋词

                # 类型选择 
                    # span:nth-of-type(1)  父节点中 选择类型是span的子节点中的第一个 选择了唐诗宋词的第一个作者
                    # span:nth-of-type(2)  父节点中 选择类型是span的子节点中的第二个 选择了唐诗宋词的第二个作者
                    
                    # span:nth-last-of-type(1)  类型的倒数选择

                # 奇偶选择
                    # 偶数节点 p:nth-child(even) 选的都是宋词 因为 唐诗的节点都是奇数的
                    # 奇数节点 p:nth-child(odd)
                    # span:nth-of-type(even)

            # 4.6 后续兄弟节点
                # 直接后续兄弟节点 用'+' 'p+span' 注意p后的span才是,前面的span不是. 
                # 所有后续兄弟节点 用'~' 'h3~span'


            # 4.7 select 下拉单选框和多选框
                # 练习网址 http://cdn1.python3.vip/files/selenium/test2.html
                # Selenium 专门提供了一个 Select类 进行操作。
                    # Select类 提供了如下的方法
                    # 实例化Select类于某一个父节点。
                    # 用select对象选择元素
                    # select_by_value           根据选项的 value属性值
                    # select_by_index           根据选项的 次序 （从0开始）
                    # select_by_visible_text    根据选项的 可见文本
                    # 去除 选中元素
                    # deselect_by_value
                    # deselect_by_index
                    # deselect_by_visible_text

                    # deselect_all          去除 选中所有
                    # '''
                    # 单选框
                    # 导入Select类
                    # from selenium.webdriver.support.ui import Select
                    # 创建Select对象
                    # select = Select(wd.find_element_by_id("ss_single")) 
                    # 通过 Select 对象选中小雷老师
                    # select.select_by_visible_text("小雷老师") 
                    # 对于select多选框，要选中某几个选项，要注意去掉原来已经选中的选项      **********
                    # 导入Select类
                    # from selenium.webdriver.support.ui import Select

                    # 创建Select对象
                    # select = Select(wd.find_element_by_id("ss_multi"))

                    # 清除所有 已经选中 的选项                              ***********
                    # select.deselect_all()
 
                    # 选择小雷老师 和 小凯老师
                    # select.select_by_visible_text("小雷老师")
                    # select.select_by_visible_text("小凯老师")

                    # '''

        # 5 XPath选择
            # 练习网址 http://cdn1.python3.vip/files/selenium/test1.html
            # 绝对路径'/' 相对路径'//' '//div//p'等同css'div p'
            # 通配符'*' '//div/*'等同css'div>*'
            # 属性选择'[@属性名="值"]'
                # 比如span标签id选择 '//span[@id="west"]' 进一步演化 成 '//*[@id="west"]'用通配符*就不需要指定span标签
                # select标签class选择 '//select[@class="multi_choice"]' 如果class有多个 只写一个 css可以 XPath则不行 必须写全一个都不能少 
                # '//p[@id]'等同css'p[id]' 有id属性的p标签

                # 属性值 包含contains       //*[contains(@style,'color')]       style属性值包含 'color'
                # 属性值 开头starts-with    //*[starts-with(@style,'color')]
                # 属性值 结尾ends-with      //*[ends-with(@style,'color')]     这是推测的 目前浏览器不支持

            # 次序选择'[]' 比css 更方便
                # //p[2] p类型子元素列表中的第2个子元素 等同css'p:nth-of-type(2)'
                # //div/p[2]   父元素为  div中的p类型 的 第2个子元素
                # 倒数选择
                    # //p[last()]   倒数第一
                    # //p[last()-1] 倒数第二
                    # //p[last()-2] 倒数第三

                # //div/*[2] 选择父元素为div的第2个子元素

            # 范围选择'[position()<=2]'
                # //option[position()<=2] 或者 //option[position()<3] 都是选取option类型第1到2个子元素
                # //*[@class='multi_choice']/*[position()>3]  选择class属性为multi_choice父元素中排名在第3以后的子元素
                # /*[@class='multi_choice']/*[position()>=last()-2] 选择class属性为multi_choice的后3个子元素

            # 和选择 或称 组选择 用‘|’ 等同于css 的 ‘,’
                # '//option|//h4' 等同于css 的 'option,h4'

            # 选择父节点 这是css做不到的
                # 用 前节点+'/..'选择前节点的父节点 
                # //*[@id='china']/..   选择 id 为 china 的节点的父节点
                # 还可以继续找上层父节点，比如 //*[@id='china']/../../..

            # 兄弟节点 
                # 后续 兄弟节点 'following-sibling::'
                    #  //*[@class='single_choice']/following-sibling::*  选择 class 为 single_choice 的元素的所有后续兄弟节点 
                # 前面的 兄弟节点 preceding-sibling::
                    #  //*[@class='single_choice']/preceding-sibling::* 选择 class 为 single_choice 的元素的所有前面的兄弟节点 

            # XPath 坑
                # web element对象使用xpath选择元素， 需要 在xpath表达式最前面加个点 。不然范围是整个页面（即webdriver），不是web element对象节点
                    # 像这样
                    # elements = china.find_elements_by_xpath('.//p')

    search_btn_el='div.nav-search-btn'
    keyword='小升初'

    # url='https://www.ixigua.com'
    # search_el='.search-wrap input'
    # search_btn_el='.search-btn span' # 定位到span 搜索 文字 否则有时可以有时不行
    # keyword='小升初'

    # url="https://www.ixigua.com/search/%E5%B0%8F%E5%8D%87%E5%88%9D/?logTag=oBQJEV45pQzISSgkG_KKQ&keyword=%E5%B0%8F%E5%8D%87%E5%88%9D"  

    # 一 打开浏览器

    # 创建 WebDriver 对象，载入 chrome浏览器驱动
    # wd=webdriver.Chrome(driver_path) #打开浏览器 在任务管理器后台可以看到 chromedriver.exe 在运行 程序就是通过该驱动控制浏览器的动作
    wd=webdriver.Edge(driver_path) # 要换成Edge浏览器驱动 其余都完全一样。
    # s=wd.start_session
    # 隐式等待
    # 设置最大等待时长为 5秒
    wd.implicitly_wait(5) 
    # 隐式等待的意义 当wd.find_element或wd.find_elements找不到，隐式等待就会多等一下。等待界面元素的出现
    # 不是wd.find_element或wd.find_elements找不到，隐式等待不等待，直接运行，容易报错或找不对。
    # 因此，对于不是wd.find_element或wd.find_elements的找不到，还是要sleep一下，比较稳妥。
    # 有的时候我们等待元素出现，仍然需要sleep。 


    # 二 输入网址 打开网页

    # 用WebDriver 对象 输入网址 打开网页 
    # 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
    # print("session:",s)
    wd.get(url)


    # 三 定位界面元素
    
    #  用 WebDriver 对象 选取节点   搜索范围是整个web页面             返回 WebElement对象 或 WebElement对象列表
    #  用 WebElement对象 选取节点   搜索范围是该WebElement对象节点    返回 WebElement对象 或 WebElement对象列表
    #  两者选取节点的方法一样，就是搜索的范围不同。
    # 一般使用 css 选择器 选取搜索框'.nav-search-keyword'
    # 选择的单复数 find_element和find_elements：
        # wd.find_element_by_xpath()
        # wd.find_elements_by_xpath()
        # wd.find_element_by_css_selector()
        # wd.find_elements_by_css_selector()

        # 单数返回一个wel对象，如果是多个，就返回第一个；如果没有，就抛出异常NoSuchElementException。
        # 复数返回 wel对象 列表，如果没有返回空列表。

    # 其次选择可以使用 xpath选择器  find_elements_by_xpath('xpath表达式')
    # 比如 次序选择 比 css简练  http://www.python3.vip/doc/tutorial/selenium/xpath_1/#按次序选择
    #  选择父节点 css没有       http://www.python3.vip/doc/tutorial/selenium/xpath_1/#选择父节点
    #  兄弟选择 可前可后        http://www.python3.vip/doc/tutorial/selenium/xpath_1/#选择父节点
    wel_search=wd.find_element_by_css_selector(search_el)

    # 获取网页html 通过属性选择器 获取该节点的整个html,如果要获取内部的html，则el.get_attribute('innerHTML'),由于该节点无内部节点，所以会输出空
    # print(el.get_attribute('outerHTML'))

    # 四 操作界面元素

    # 1 输入文本 
    wel_search.send_keys(keyword)
    # 在搜索框输入'小升初'并回车'\n'
    # wel_search.send_keys(f'{keyword}\n')
    #  清空 输入框
    # wel_search.clear()
    #  
    # 2 获取文本 
    # 普通WebElement对象 比如 span、p、i、div等 获取网页文本，直接用el.text即可
    # 对于input 要用el.get_attribute('value')才能获取输入框内的值
    # print(wel_search.get_attribute('value'))

    # 3 点击click()

    # 保存当前窗口的句柄 便于 跳回

    mainWindow=wd.current_window_handle
    print('点击前窗口句柄',mainWindow)
    #  如果在搜索框中不输入回车 就要点击搜索按钮。
    #  用wd获取搜索按钮
    wel_search_btn=wd.find_element_by_css_selector(search_btn_el)
    wel_search_btn.click()
    # print('搜索按钮外部节点：',wel_search_btn.get_attribute('outerHTML'))
    # print('搜索按钮内部节点：',wel_search_btn.get_attribute('innerHTML'))

    # print('搜索页')
    print('window_handles',wd.window_handles) #窗口句柄

    # 4 更多操作 http://www.python3.vip/doc/tutorial/selenium/skills_2/#更多动作

    # 五 页面跳转 窗口切换 http://www.python3.vip/doc/tutorial/selenium/frame/#切换到新的窗口

    
    print('click后当前窗口',wd.current_window_handle)
    # time.sleep(5)
    # 2 跳到搜索结果页 

    # WebDriver对象有window_handles 属性，这是一个列表对象， 里面包括了当前浏览器里面所有的窗口句柄。
    for handle in wd.window_handles:
        print('for',handle)
        # time.sleep(10)
        if handle == mainWindow:
            print('1')
            time.sleep(5)
            continue
        # 先切换到页面
        wd.switch_to.window(handle) # 这步切换不是画面切换,而是指wd切换到handle页,也就是说wd变成handle的wd,然后就可以操作handle页,否则就是上一个handle的wd,不能操作本handle页.
        # 如果 是 我们要的窗口 就 break
        if keyword in wd.title:
            print(wd.title)
            # time.sleep(5)#如果不等待 又可能下面找不到节点 因为太快而报错
            break
    
    search_url=wd.current_url
    print(search_url)
    # 找到结果列表节点 ul='ul.video-list.clearfix'
    ul='ul.video-list.clearfix'
    wul=wd.find_element_by_css_selector(ul)
    # print(wul.get_attribute('innerHTML'))
    # 找到列表中的每个节点,打印每个节点中a标签的title
    item='li'
    witems=wul.find_elements_by_css_selector(item)
    for i in witems:
        i_a=i.find_element_by_css_selector('a')
        title=i_a.get_attribute('title')
        print(title)

    
    # print("session:",wd.session_id)
    

    # 3 跳回
    # time.sleep(5)
    wd.close()#只关闭搜索结果页
    wd.switch_to.window(mainWindow)#切换到开始页
    time.sleep(5)
    

    # 退出 会关闭浏览器
    wd.quit()
# one()


# 六 分析页面 页面冻结 http://www.python3.vip/doc/tutorial/selenium/skills_2/#冻结界面 
    # 有些元素甚至页面 需要鼠标放在上面才有，离开就消失，不利于进行页面分析。
    # 因此在 开发者工具栏 console 里面执行如下js代码

    # setTimeout(function(){debugger}, 5000) 便会在5秒后执行function(){debugger}调式模式冻结页面，即使鼠标移开也不会消失，

    # 5秒后 页面出现 paused in debugger界面，页面暂停了。
    # 这样就可捕捉元素，分析页面了。

    # 在paused in debugger界面点击 右箭头 继续就跳出了，页面就恢复了。

# 七 捕捉弹出对话框 不是html 无法选择 不是模态框
    # 通知框    Alert
    #    获取提示信息 driver.switch_to.alert.text
    #    点击ok或确认 driver.switch_to.alert.accept()

    # 确认框    Confirm
    #    以上两点与Alert一致
    #    点击cancel或取消 driver.switch_to.alert.dismiss()


    # 输入确认框  Prompt
    #     以上三点一致
    #     在输入框中输入 driver.switch_to.alert.send_keys('输入的内容')

# 八 执行js 打开选项卡
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

# 九 xpath 选择

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


# 十 页面高级操作
    # 1 移动页面元素 
    # actionchains是selenium里面专门处理鼠标相关的操作 
    # 使用click() 方法可以模拟鼠标单击操作,
    # 但是鼠标操作还包括:右击context_click(wel)、双击double_click()、悬停move_to_element()、鼠标拖拽drag_and_drop()等复杂功能就可以使用actionchains对象。


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
    deceleration_point=distancex*3/4

    # 初始距离
    cs=0
    while cs<distancex:
        if cs<deceleration_point:
            # 匀加速
            a=2
        else:
            # 匀减速
            a=-3

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

    else:
        # 先移过去一点，再移回来，更像人的移动
        ActionChains(wd).move_by_offset(xoffset=2.5,yoffset=0).perform()
        ActionChains(wd).move_by_offset(xoffset=-2.5,yoffset=0).perform()
    # 释放
    time.sleep(0.5) #0.5秒后释放鼠标
    ActionChains(wd).release().perform()

def move_el():
    
    # driver = webdriver.Chrome(driver_path)
    driver=webdriver.Edge(driver_path) 
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