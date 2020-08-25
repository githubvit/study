# 用selenium 的 移动元素来破解 滑动验证
# 知识点：
    # webdriver对象截屏
        # wd.save_screenshot('snap.png')

    # 用pillow的Image对象的open方法获取图像。
        # page_img=Image.open('snap.png')

    # 直取webElement对象坐标和大小
        # 坐标 webElement.location  #结果 字典 {'x': 8, 'y': 50}
        # 大小 webElement.size      #结果 字典 {'height': 42, 'width': 165}

    # 用pillow图片image的裁剪crop 取图
        #  crop_img=page_img.crop((left,top,right,bottom))
        
    # 用pillow图片Image逐点加载load()[x,y] 取得该点的rgb
        # 循环图片的宽和高，逐点取得rgb,每个点都是一个元组(r,g,b,255)，
         # for x in range(w): 
            # for y in range(h):
                #rgb1=img1.load()[x,y] #(r,g,b,255)
        # 两幅图片逐点取得rgb就可以比较。

    # webdriver执行js 
        # 执行JavaScript 改变 背景图的display
        # wd.execute_script("document.getElementsByClassName('geetest_canvas_fullbg')[0].style.display='block'")
        # 先在浏览器的consel执行js，通过后把代码复制到里面即可。
    
    # webdriver控制鼠标
        # 按住滑块
            # ActionChains(wd).click_and_hold(slider).perform()
        # 移动  要记住的是xoffset和yoffset只能是正整数或负整数或零
            # ActionChains(wd).move_by_offset(xoffset=x,yoffset=0).perform()
        # 释放
            # ActionChains(wd).release().perform()

    
# egon破解博客园极验逻辑
    #步骤一:点击按钮，弹出没有缺口的图片

    #步骤二：获取步骤一的图片

    #步骤三：点击滑动按钮，弹出带缺口的图片

    #步骤四：获取带缺口的图片

    #步骤五：对比两张图片的所有RBG像素点，得到不一样像素点的x值，即要移动的距离

    #步骤六：模拟人的行为习惯（先匀加速拖动后匀减速拖动），把需要拖动的总距离分成一段一段小的轨迹

    #步骤七：按照轨迹拖动，完全验证

    #步骤八：完成登录

# 极验测试网 极验开始没有弹出完整背景图片，经过一番分析，
# 是因为其给完整背景图片加了display:none 看不到 关闭display:none即可看见了

#  极验 滑动验证 界面 分析
    # <div class="geetest_canvas_img geetest_absolute" style="display: block;">
    #     <div class="geetest_slicebg geetest_absolute">
                # 有缺口的背景大图
    #         <canvas class="geetest_canvas_bg geetest_absolute" height="160" width="260">
    #         </canvas>
                # 移动的小缺口图像
    #         <canvas class="geetest_canvas_slice geetest_absolute" width="260" height="160" style="opacity: 1; display: block;">
    #         </canvas>
    #     </div>
    #       这里是没有缺口的背景大图画面 开始被隐藏了 display:none 看不到 关闭display:none即可看见了
    #     <canvas class="geetest_canvas_fullbg geetest_fade geetest_absolute" height="160" width="260" style="display: none; opacity: 1;">
    #     </canvas>
    # </div>

    # 找到如下节点 class='geetest_canvas_fullbg'
    # <canvas class="geetest_canvas_fullbg geetest_fade geetest_absolute" height="160" width="260" style="display: none;opacity: 1;"></canvas>
# 关闭 display:none.
# 抓取 该节点 即可得到没有缺口的图片
# 恢复 display:none.
# 抓取 该节点 即可得到有缺口的图片


from selenium import webdriver
from selenium.webdriver import ActionChains
import time,random,re
from PIL import Image
from PIL import ImageGrab #截屏

# pip3 install pillow -i https://mirrors.aliyun.com/pypi/simple/
# driver_path=r'D:\chromedriver.exe'


# 防止被'window.navigator.webdriver'识别,使得该js值为'undefined'而不是'true'
# opt=webdriver.ChromeOptions()
# opt.add_experimental_option('excludeSwitches',['enable-automation'])
# wd=webdriver.Chrome(driver_path,options=opt)

# wd=webdriver.Chrome() # webdriver 被放到Anaconda3的脚本目录了，不用填写了，会自动找到"D:\Anaconda3\Scripts\chromedriver.exe"

# wd=webdriver.Firefox() #启动火狐浏览器，火狐的webdriver即geckodriver.exe，被复制到"D:\Anaconda3\Scripts\geckodriver.exe"路径了

# 启动极速360
option=webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])
# 极速360目录
option.binary_location=r'D:\360js\360Chrome\Chrome\Application\360chrome.exe'
# 与其对应的webdriver驱动
wd=webdriver.Chrome(r'D:\360js\chromedriver.exe',options=option)

wd.implicitly_wait(5)


# 打开主页面

url='https://auth.geetest.com/login/' #极验官方 测试接口
# url='https://www.lagou.com' # 拉勾
wd.get(url)

# l拉勾网测试
def lagou():
    # 如果有 城市登录页面
    city=wd.find_elements_by_css_selector('#changeCityBox p .tab')
    if len(city):
        time.sleep(1)
        city[0].click()
        time.sleep(1)


    # 打开登录页面
    # 找到登录按钮 [data-lg-webtj-_address_id="1p4n"]
    wd.find_element_by_css_selector('[data-lg-webtj-_address_id="1p4n"]').click()
    time.sleep(3)


    # 找到输入框 user [placeholder="请输入常用手机号/邮箱"]和 pwd [placeholder="请输入密码"]

    user_ipt=wd.find_element_by_css_selector('[placeholder="请输入常用手机号/邮箱"]')
    pwd_ipt=wd.find_element_by_css_selector('[placeholder="请输入密码"]')

    # 输入用户名、密码
    # u_name='18611453110'
    # pwd='alex3714'
    u_name='18114531111'
    pwd='aelx3714'
    user_ipt.click()
    time.sleep(0.45)
    user_ipt.send_keys(u_name)
    time.sleep(2)
    pwd_ipt.click()
    time.sleep(0.84)
    pwd_ipt.send_keys(pwd)
    time.sleep(1)

    # 找到登录按钮 [data-lg-tj-id="1m2g"][data-lg-tj-no="0003"]
    wd.find_element_by_css_selector('[data-lg-tj-id="1m2g"][data-lg-tj-no="0003"]').click()

    # 弹出滑动验证码界面
# lagou()

# 截屏操作
def get_pageimg():
    # 截取浏览器画面 保存为snap.png
    wd.save_screenshot('snap.png')
    # 用pillow的image对象的open方法获取图像
    page_img=Image.open('snap.png')
    time.sleep(5)
    return page_img

# 裁剪截屏，得到图片 学习webdriver对象抓屏，及pil模块处理图像。
def get_img(location,size):
    # 得到裁剪的边界
    left=location['x']
    top=location['y']
    right=location['x']+size['width']
    bottom=location['y']+size['height']
    
    # 取得截屏对象
    page_img=get_pageimg()
    # 裁剪截屏对象
    crop_img=page_img.crop((left,top,right,bottom))

    return crop_img
    
    

# 执行js 代码 得到无缺口的背景图片
def excute_js(location,size):
    # 执行JavaScript 改变 背景图的display
    wd.execute_script("document.getElementsByClassName('geetest_canvas_fullbg')[0].style.display='block'")
    time.sleep(0.5)
    # 截屏取得 无缺口 背景
    full_img=get_img(location,size)
    # 执行JavaScript 改回 背景图的display为none
    wd.execute_script("document.getElementsByClassName('geetest_canvas_fullbg')[0].style.display='none'")
    return full_img



# 图片比对 找到移动的x距离 拿两幅图片比较r、g、b的值
# 找到x的起始值x0，循环x，
# 再循环该x上的y，得到点(x,y),
# 查看两幅图片该点的像素，如果大于阈值，则可判断该点为缺口起始值。
    # for x in w-x0: 
        # for y in h:
def get_dx(img1,img2):
    # 阈值
    threshold=60
    # 起始x值
    left_x=57
    # 把两幅图片逐点对比
    for x in range(left_x,img1.size[0]):
        for y in range(img1.size[1]):
            #用图片的load方法 获取[x,y]该点的[r,g,b] 值
            rgb1=img1.load()[x,y]
            rgb2=img2.load()[x,y]
            print(rgb1,rgb2)

            # 比较两幅图片该点r、g、b的差
            r=abs(rgb1[0]-rgb2[0])
            g=abs(rgb1[1]-rgb2[1])
            b=abs(rgb1[2]-rgb2[2])

            # 如果差超过阈值，则判为缺口起始x
            if r>=threshold and g>=threshold and b>=threshold:
                return x-7 #经过测试，误差大概为7
    return img1.size[0]-7
            

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
        # 把当前移动距离加入轨迹列表 要取整，因为移动功能接收的移动参数只能是正整数、负整数或零
        track_list.append(round(s)) 
        # 更新当前移动总距离
        cs=cs+s
        # 更新当前速度
        v=v+a*t

    return track_list


    
# 按移动轨迹移动滑块 通过验证
def move_slid(wd,slider,track_list):
    
    # 按住滑块
    ActionChains(wd).click_and_hold(slider).perform()
    # 按轨迹移动 
    for x in track_list:
        ActionChains(wd).move_by_offset(xoffset=x,yoffset=0).perform() # 要记住的是xoffset和yoffset只能是正整数或负整数或零
    else:
        # 先移过去一点，再移回来，更像人在操作
        ActionChains(wd).move_by_offset(xoffset=2,yoffset=0).perform()
        ActionChains(wd).move_by_offset(xoffset=-2,yoffset=0).perform()
    
    # 释放
    time.sleep(0.5) #0.5秒后释放鼠标
    ActionChains(wd).release().perform()

def geetest():
    
    # 找到输入框 user [placeholder="请输入邮箱"]和 pwd [placeholder="请输入密码"]

    user_ipt=wd.find_element_by_css_selector('[placeholder="请输入邮箱"]')
    pwd_ipt=wd.find_element_by_css_selector('[placeholder="请输入密码"]')

    while True:
        # 产生随机字符窜 输入用户名、密码
        u=''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 8))
        p1=''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5))
        p2=''.join(random.sample(['z','0','1','2','3','4','5','6','7','q','p','8','n','m','9','k','j','i','h','g','f','e','d','c','b','a'], 5))
        p=p1+p2

        user_ipt.click()
        user_ipt.clear()
        time.sleep(0.5)
        user_ipt.send_keys(u)
        time.sleep(1)
        pwd_ipt.click()
        user_ipt.clear()
        time.sleep(0.8)
        pwd_ipt.send_keys(p)
    

    
        time.sleep(5)
        # 找到人机验证按钮 [aria-label="点击按钮进行验证"]
        rjl=wd.find_elements_by_css_selector('[aria-label="点击按钮进行验证"]')
        # wd.find_element_by_css_selector('.geetest_radar_tip').click()
        if len(rjl):
            rjl[0].click()

            # 获取界面区域
            pop_el=wd.find_elements_by_css_selector('.geetest_fullpage_click.geetest_float')

            if len(pop_el):
                time.sleep(5)
                                    
                # 查找 弹出界面 是否 显示 display: block
                pop_str=pop_el[0].get_attribute('style')
                print(pop_str)
                display_val=re.findall('display:\s*(.*?);',pop_str)[0]
                print(display_val)

                if display_val != 'none':
                    print('界面弹出来了吗？')
                    break
        else:
            # 验证成功 出现
            su=wd.find_elements_by_xpath('//*[@id="captchaIdLogin"]/div/div[2]/div[2]/div/div[2]/span[1]')
            if len(su):
                print(su[0].get_attribute('innerHTML'))
            
            print('没有界面')
            # 点击立即登录按钮
            wd.find_element_by_xpath('//*[@id="base"]/div[2]/div/div[2]/div[3]/div/form/div[5]').click()
            # 界面没有弹出 
            time.sleep(random.randint(3,13))
            # 点击用户输入框 消除提示
            user_ipt.click()
            time.sleep(0.5)

    # 弹出滑动验证码界面
    print('有没有滑动验证的图片节点')
    # 等待 图片稳定
    time.sleep(5)
    # 如果该节点存在，就去取无缺口图片
    full_node=wd.find_elements_by_css_selector('.geetest_canvas_fullbg')
    if len(full_node):
        
        # 获取 缺口图片的位置和大小
        location=wd.find_element_by_css_selector('.geetest_canvas_slice').location
        size=wd.find_element_by_css_selector('.geetest_canvas_slice').size
        print('有',location,size)
        # 抓图
        # 缺口图片
        img1=get_img(location,size)
        print(img1,img1.size)
        time.sleep(3)
        # 无缺口图片
        img2=excute_js(location,size)
        print(img2,img2.size)

        # 比较img1、img2取得滑动距离dx
        dx=get_dx(img1,img2)
        print('滑动距离:',dx,type(dx))

        # 产生轨迹列表
        track_list=make_track(dx)

        print('轨迹:',track_list,sum(track_list))

        # 操作滑块
        # 获取滑块
        slider=wd.find_element_by_css_selector('.geetest_slider_button')

        # 移动滑块
        move_slid(wd,slider,track_list)

        time.sleep(3)

try: 
    geetest()   
except Exception as e:
    print(e)
    pass
    
input('>>按任意键键退出')
# wd.close()
wd.quit()
