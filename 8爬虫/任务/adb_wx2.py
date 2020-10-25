import time,datetime,random
from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey 
# from appium.webdriver.common.touch_action import TouchAction
from threading import Timer
import os
from adb_wxzz import wxzz #引入wxzz
from PIL import Image

# 三个层次：
    # 总流程
        # 一个总流程 由 多个 次流程 组成
        # 定时任务 没结束 就是一个总流程 

    # 次流程
        # 一个次流程 由 多个 轮流程 组成
        # 一次定时任务 就是 一个次流程 是一次Appium操作过程 生成wd又退出了wd


    # 轮流程
        # 一个轮流程 是对 一次下滑前或下滑后（返回后）的 静止画面的记录 
        # 嵌入在次流程中，是在一次Appium操作过程中发生的多次操作流程
        # 是操作流程 的最小单位

# 总流程变量
# 今日收款通知节点

today_list=[]   # 记录 收款节点 的“今日第 笔收款，共计”
today_uuid=[]   # 记录 收款节点 的uuid
today_n=[]      # 从“今日第 笔收款，共计”中的“第”和“笔”中的数字序号
today_sum=[]    # 从“今日第 笔收款，共计”中的“共计”后面的汇总金额
today_price=[]  # 记录 收款节点 的单笔金额。
cnt=0   # 定时器 的 第几次 运行

screen_pixel=[] # 每次 定时器 开始时 画面 特定位置的 像素点 以便 下次 定时器开始时 捕捉 画面 对照 

# 特定坐标点(x,y)

coordinate_points=[(89,226),
(412,226),(440,226),(468,226),(490,229),(515,228),(523,226),(558,238),(573,226),(603,226),
(342,280),(355,280),(389,280),
(101,328+24),(101,403+24),(101,454+28),(101,590+28),
(101,765),(494,765),(537,774),(552,766),(574,768),(591,769),
(101,885+24),
(458,1001+24),(458+19,1001+24),(458+19+19,1001+24),
(101,1244+24),
(412,226+1042),(440,226+1042),(468,226+1042),(490,229+1042),(515,228+1042),(523,226+1042),(558,238+1042),(573,226+1042),(603,226+1042),
(342,280+1042),(355,280+1042),(389,280+1042),
(101,1370+24),(101,1445+24),(101,1660),
]
# 异常变量
is_exception=False

# appium 操作
class WxPay():
    def __init__(self):
        
        # 连接手机 不打开任何app
        self.desired_caps = {
          'platformName': 'Android', # 平台名称 被测手机是安卓
          'platformVersion': '6', # 平台版本 手机安卓版本
          'deviceName': '4ee7dd3f', # 设备名，安卓手机可以随意填写
          'unicodeKeyboard': True, # 安装unicodeKeyboard的输入法，便于输入中文，填True
          'resetKeyboard': True, # 执行完程序恢复原来输入法
          'noReset': True,       # 不要重置App           很重要 *****  否则每次都是刚刚安装打开的状态 数据都没有了
          'newCommandTimeout': 6000, # 客户端 命令的 超时时间
          'automationName' : 'UiAutomator2',  # 原来是第1代，现在第2代速度快一点。
          # 'app': r'd:\apk\bili.apk',
        
        } 

        # 开始画面
        self.one_pixel=False # 同一画面

        # 两个开关 三种状态
        self.go_swipe=False # 下滑
        self.go_back=False   # 返回

        self.is_duplicate=False  # 找到上次流程的重复点 是结束下滑，进行返回或结束的一个标志
        self.is_swiped=False # 下滑过
        self.is_backed=False # 返回过

        # 次流程变量
        self.c_list=[] #本次新增收款节点列表
        self.c_uuid=[] #本次新增uuid列表
        self.c_price=[]

        # 轮流程变量
        self.l_list=[] # 本轮 记录的收款节点列表
        self.l_uuid=[] # 本轮 记录的uuid列表
        self.l_price=[]

        # 连接 appium server
        self.wd = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        # 隐式等待
        # 设置缺省等待时间
        self.wd.implicitly_wait(10)

    # 判断当前页面是否是微信支付页面
    def check_wxpay_page(self):
        try:

            page=self.wd.find_elements_by_xpath('//*[@resource-id="com.tencent.mm:id/ls"][@text="微信支付"]')
            if page:
                print(f'开启页面主程序，开始第{cnt}次流程')
                self.page_main()

            else:
                # 1 看看 是不是 微信首页
                pay_code='new UiSelector().resourceId("com.tencent.mm:id/bag").text("微信支付")'
                pay=self.wd.find_elements_by_android_uiautomator(pay_code) # 要用复数
                if pay:
                    pay[0].click()
                    # 2 从 微信页面 点击 到达微信支付页面
                    print(f'进入微信支付页面，开启页面主程序，开始第{cnt}次流程')
                    time.sleep(2)
                    self.page_main()
                else:
                    print(f'找不到"微信支付"页面,退出,结束第{cnt}次流程')
                    self.wd.quit()
                    
        except Exception as e:
            print('开始就异常,报错:',e)
            print('标记本次异常，本次结束时，不执行同步总列表操作')
            global is_exception
            is_exception=True
            self.wd.quit()
                  

    #1 页面 主程序
    def page_main(self):
        # 处理上一次流程是否异常，
            # 如果异常，就去返回，让页面得到一次刷新，并关闭异常开关
            # 这样，就把异常发生的次流程也处理了，不会遗漏uuid。
        global is_exception
        if is_exception:
            print('上一次流程发生异常')
            print('关闭异常开关') 
            is_exception=False
            print('用返回去刷新页面')
            self.back_back()

        # 抓屏 获取像素点 和上一轮像素点 对比 
        self.get_pixel()
        if self.one_pixel:
            print(f'同一画面，退出，结束第{cnt}次流程')
            self.over_wd()
        else:
            print('开始 轮流程，找节点')
            self.check_nodes()
            pass


    #  获取开始屏幕 像素点
    def get_pixel(self):
        # 抓屏 并 保存
        filename=r'D:\pyj\st\study\8爬虫\任务\test.png'
        im=self.wd.get_screenshot_as_file(filename)
        img=Image.open(filename)
        # 获取 屏幕 图片 特定 位置 的 像素点
        now_pixel=[]
        for i in coordinate_points:
            now_pixel.append(img.load()[i][:3])
        global screen_pixel
        if screen_pixel:
            # 比较
            for i in range(len(coordinate_points)):
                r1,g1,b1=now_pixel[i]
                r2,g2,b2=screen_pixel[i]
                if r1==r2 and g1==g2 and b1==b2:
                    self.one_pixel=True
                else:
                    # 不是同一画面
                    self.one_pixel=False
                    # 更新 对比 画面 
                    screen_pixel=now_pixel
                    return
        else:#第一次screen_pixel是空的
            screen_pixel=now_pixel

        pass

    # 2 一个页面找：
        # 没有要找的（要记录的、要结束的）
            # 下滑
        # 找到要记录的
            # 要记录的点：新增的收款节点 uuid price。
            # 下滑
        # 找到要结束的
            # 结束点：第一次 是盘点节点，以后就是 已经记录的点。 
            # 如果是下滑过来的，就要停止下滑并返回；
            # 否则，就静止（什么也不做）并退出。

    #  轮操作
    def check_nodes(self):
        try:
            # 找节点
            # 如果有'135****3627' id'com.tencent.mm:id/aq3' 说明到了上次盘点的 地方，
            pd_nodes=self.wd.find_elements_by_xpath('//*[@resource-id="com.tencent.mm:id/aq3"][@text="135****3627"]')
            # 找到resource-id=com.tencent.mm:id/aq3 以'今日第'开头 并且包含'笔收款，共计'
            sk_nodes=self.wd.find_elements_by_xpath('//*[@resource-id="com.tencent.mm:id/aq3"][starts-with(@text,"今日第")][contains(@text,"笔收款，共计")]')

            # 页面的三种情况
            if not pd_nodes and not sk_nodes:
                print('没有要找的，下滑')
                self.go_swipe=True
            elif pd_nodes:
                print('找到盘点节点，不能下滑，要么停止,要么返回')
                # 盘点节点操作
                self.pd_nodes_op(pd_nodes,sk_nodes)
            else:
                # sk_nodes:
                print('没有盘点节点，只有记录节点，同步列表')
                # 先把收款节点记录到 本轮的 节点和uuid列表里
                for sk_node in sk_nodes:
                    self.sk_node_op(sk_node)
                # 在本轮结束时  再和总的列表和uuid列表比较
                # 如果同位置的节点和uuid对应总列表同一位置的节点和uuid，就是重复了，出现重复就要退出，
                # 而不重复的点就要加入 本次节点列表 和 本次uuid列表。
                self.find_duplicate_record()

            # 页面动作
            if self.go_swipe:
                self.down_swipe()
            elif self.go_back:
                self.back_back()
            else:
                print('----------既不用下滑也不用返回，那么就结束本次流程---------')
                self.over_wd()
                
        except Exception as e:
            print('报错:',e)
            print('标记本次异常，本次结束时，不执行同步总列表操作')
            global is_exception
            is_exception=True
            self.over_wd()

    # 盘点节点 操作
    def pd_nodes_op(self,pd_nodes,sk_nodes):
        # 取出最下一个盘点节点的y
        y1=pd_nodes[-1].location['y']
        print('看到了盘点转账点，不能下滑,要么返回，要么退出')
        
        # 如果 收款 节点 在下方，就同步列表
        if sk_nodes:
            for sk_node in sk_nodes:
                if sk_node.location['y']>y1:
                    print('发现盘点节点下方有收款节点，进行收款节点操作，同步列表')
                    self.sk_node_op(sk_node)
            # 本轮收款节点操作结束，查找重复和记录到次列表。
            self.find_duplicate_record()

        print('找到了盘点转账点，终止下滑')
        self.go_swipe=False  # 不管怎么样 都终止下滑 
      
        if self.is_swiped:
            print('是下滑到盘点节点的，终止下滑，去返回')
            self.go_back=True
        else:
            print(f'开始就发现了盘点节点,退出，结束第{cnt}次流程')
            # self.wd.quit()
            # return
        
     
    # 在 wxzf 页面中 一轮操作
        # 看 两个节点
            # 一个是盘点节点
                # 是第一次下滑过程中结束下滑的唯一标志，因此，本系统一开始，就要先用本机账号向手机转账账号转账，否则，无法终止下滑。
            # 一个是收款节点
                # 这是要捕捉并记录uuid的节点。

        # 记录 到轮列表

        # 记录后 找重复 记录到次列表


        # 做 两个动作
            # 下滑 同步列表
            # 返回再回来 滑到盘点节点或已记录的节点，就用该方法刷新。


    # 单个记录节点操作 记录 到轮列表
    def sk_node_op(self,sk_node):
        print('单个收款节点操作，找同一节点下的各个元素，同步各个列表')
        # 获取 今日 文本
        sk_text=sk_node.get_attribute('text')
        # 先记录到 本轮的 节点和uuid列表里
        
        self.l_list.append(sk_text)
            
        # 查找同一节点内的uuid 同步添加 uuid列表 today_uuid
        self.uuid_node(sk_node)
        # 查找同一节点内的uuid 同步添加 金额列表 today_price
        self.price_node(sk_node)
        

    # 轮流程中记录后的操作
        # 在轮列表和总列表找重复
        # 记录到次列表 

        # 在本轮结束时  再和总的列表和uuid列表比较
        # 如果同位置的节点和uuid对应总列表同一位置的节点和uuid，就是重复了，出现重复就要退出，
        # 而不重复的点就要加入 本次节点列表 和 本次uuid列表。
    def find_duplicate_record(self):
        if self.l_list:
            for l_text in self.l_list:
                l_uuid=self.l_uuid[self.l_list.index(l_text)]
                l_price=self.l_price[self.l_list.index(l_text)]
                if not l_uuid == 'no_find':
                    print('找重复')
                    global today_list
                    global today_uuid
                    if today_list:
                        if l_text in today_list and l_uuid == today_uuid[today_list.index(l_text)]:
                            print('找到了重复的记录，本轮结束后就不能下滑了，要返回或结束本次流程')
                            self.is_duplicate=True
                            continue
                    print('去记录')
                    if not l_price == 'no_find':
                        # 在列表里，并且同位置的uuid还相同
                        if l_text in self.c_list and  l_uuid == self.c_uuid[self.c_list.index(l_text)]:
                            print('次列表已经记录')
                        else:
                            print('记录到次列表')
                            self.c_list.append(l_text)
                            self.c_uuid.append(l_uuid)
                            self.c_price.append(l_price)                    

        time.sleep(2)
        # 本轮结束后的动作开关
        if self.is_duplicate:
            self.go_swipe=False
            if self.is_swiped:#如果是下滑到重复点，就要返回
                print('下滑到重复点，要返回')
                self.go_back=True
        else:
            print('没找到重复点，要下滑')
            self.go_swipe=True    

        time.sleep(2)           
        # 清空本轮列表
        if self.l_list:
            print('清空本轮列表')
            self.l_list=[]
            self.l_uuid=[]
            self.l_price=[] 
    
    # 结束动作
    def over_wd(self):
        # print('次节点列表',self.c_list)
        # print('次uuid列表',self.c_uuid)
        # print('次price列表',self.c_price)
        global is_exception
        if not is_exception and self.c_list:
            # 内部次列表会记录重复，比如在记录的过程中发生来了通知的时候，发生了位置替换。
            # 记录过程中的位置替换：
                # 正在记录的瞬间，11的位置被12替换，12被13替换，
                # 这时记录的uuid是后面的uuid,11记录的uuid是12的.
            # 因此在同步总列表前，要去重，但注意，这个去重不是简单的去重，而是要同时重（list和uuid）的才去。
            print('次列表去重')
            lup=[]
            for i in range(len(self.c_list)):
                item=[]
                item.append(self.c_list[i])
                item.append(self.c_uuid[i])
                item.append(self.c_price[i])
                if item not in lup:
                    lup.append(item)

            print('把去重后的次列表添加到总列表')
            global today_list
            global today_uuid
            global today_price
            for i,v in enumerate(lup):
                # 在总列表里，并且同位置的uuid还相同 再一次 去重
                if v[0] in today_list and  v[1] == today_uuid[today_list.index(v[0])]:
                    print('总列表已经记录')
                else:
                    today_list.append(v[0])
                    today_uuid.append(v[1])
                    today_price.append(v[2])
        else:
            if is_exception:
                print('本次异常，不同步列表')
            else:
                print('次列表为空，不同步列表')
        time.sleep(2)
        print('总节点列表',today_list)
        print('总uuid列表',today_uuid)
        print('总price列表',today_price)
        time.sleep(2)
        print(f'退出，结束第{cnt}次流程')
        self.wd.quit()
        

    def uuid_node(self,sk_node):
        print('找uuid')
        time.sleep(2)
        uuid_code='//*[@resource-id="com.tencent.mm:id/aq3"][starts-with(@text,"uuid")]'
        uuid_node=self.find_node(sk_node,130,uuid_code,self.l_uuid)
        
    def price_node(self,sk_node):
        print('找price')
        time.sleep(2)
        price_code='//*[@resource-id="com.tencent.mm:id/as_"]'
        price_node=self.find_node(sk_node,310,price_code,self.l_price)


    # 查找同一节点内 小节点 找到 同步 节点列表， 没找到 添加'no_find'到节点列表
    # m_node:主节点 根
    # dh:距离主节点的距离、范围等实测边界
    # node_code:xpath 要找的小节点的xpath，在范围内查找的节点类型
    # t_list：需同步记录的列表
    def find_node(self,m_node,dh,node_code,t_list):
        y1=m_node.location['y'] 
        m_text=m_node.get_attribute('text')
        nodes=self.wd.find_elements_by_xpath(node_code)
        if nodes:
            for node in nodes:
                y2=node.location['y']
                if abs(y1-y2)<dh:
                    print('找到了,返回节点')
                    text=node.get_attribute('text')
                    print(f'找到了同一节点的{text},加入{t_list}')
                    if len(t_list)<len(self.l_list):#新增
                        t_list.append(text)
                    else:
                        t_list[today_list.index(m_text)]=text #不能用append 替换'no_find'
                    return 
   
        print('没找到,下滑')
         # 如果节点列表没有添加 就 没找到 因此 添加'no_find'  打开 下滑 开关
        if len(t_list)<len(self.l_list):
            t_list.append('no_find')
            print(f'本次没有找到，添加"no_find"到{t_list}')
        # self.go_swipe=True

    
    # 下滑   
    def down_swipe(self):
        print('下滑')
        # 1 获取整体节点
        all_code='new UiSelector().resourceId("com.tencent.mm:id/af")'
        all_node=self.wd.find_element_by_android_uiautomator(all_code)
        # 2 下滑尺寸
        s_x=all_node.location['x']+all_node.size['width']/2-8
        s_y=all_node.location['y']+all_node.size['height']/2+11
        e_x=s_x+11
        e_y=all_node.location['y']+all_node.size['height']
        # 3 下滑
        self.wd.swipe(s_x,s_y,e_x,e_y,duration=2000)
        # print("标记下滑过,重新设置self.go_swipe、self.is_backed为初始值False")
        # 4 标记下滑过
        self.is_swiped=True

        # 5 重新设置为初始值
        # 下滑开关
        self.go_swipe=False

        # 返回过
        self.is_backed=False

       

        # 6 重新开始
        print("下滑完毕，开始新的一轮")
        print('--------------')
        time.sleep(2)
        self.check_nodes()#下滑后，调用节点查找程序，以便同步列表。
        

    # 返回再进入
    def back_back(self):
        # 1 返回 微信页面
        print('返回微信页面')
        self.wd.press_keycode(4)
        time.sleep(2)
        pay_code='new UiSelector().resourceId("com.tencent.mm:id/bag").text("微信支付")'
        pay=self.wd.find_element_by_android_uiautomator(pay_code)
        # 2 从 微信页面 点击 到达微信支付页面
        print('进入微信支付页面')
        pay.click()

        # 3 标记返回过
        # print('标记返回过，重新设置self.go_swipe、self.is_swiped、self.go_back为初始值False')
        self.is_backed=True

        # 4 重新设定为初始值

        # 下滑开关
        self.go_swipe=False
        # 下滑过
        self.is_swiped=False
        # 返回开关
        self.go_back=False
        

        # 5 重新开始
        print('返回完毕，开始新的一轮，要对比画面')
        print('-------------- -------------- --------------')
        time.sleep(2)
        self.page_main()#返回后，要调用页面主程序，看是不是开始的画面，如果是，就要结束本次流程

# 定时任务
class WxTimer():
    def __init__(self,time_stamp):
        
        self.time_stamp=time_stamp # 获取定时任务结束 盘点时间戳
        print(f'盘点时间{self.get_format_time(self.time_stamp)}')
        self.run_one()

        
    # 一次调度流程
    def run_one(self):
        global cnt # 声明操作模块的全局变量
        global today_price
        global today_list
        global today_uuid
        global screen_pixel
        global coordinate_points
        cnt+=1
        st=time.time()
        print(f'开始-----第{cnt}次------>')

        wp=WxPay()
        wp.check_wxpay_page()
    
        dt=time.time()-st
        dt=round(dt)#取整
        h,s1=divmod(dt,3600)#求商 余
        m,s=divmod(s1,60)

        print(f'第{cnt}次运行时间持续：{h}小时{m}分钟{s}秒')
        
        # 如果当前时间戳小于盘点时间戳，就运行定时任务 否则 就盘点
        t_n=time.time()
        if t_n < self.time_stamp:
            self.timer=Timer(20,self.run_one)
            self.timer.start()
            self.kill_timer()
        else:
            print('准备盘点，返回到微信页面,点击 返回') # [0,60][108,190]
            time.sleep(5)
            # 1 返回到微信页面
            os.popen('adb shell input tap 60 120')

            # 2 盘点 
            time.sleep(5)
            print('开始盘点')
            # 2.1 转账
            
            
            if today_price:
                price=0
                for p in today_price:
                    price+=float(p)
                wxzz(p_num=13507983627,price=price,time_code='123456',pwd='710102')
                
            else:
                print('金额汇总列表为空')
                wxzz(p_num=13507983627,price=0.01,time_code='0',pwd='710102')
                
            # 2.2 清空
            today_list=[]
            today_uuid=[]
            today_price=[]
            cnt=0 #重新计数
            print(f'结束盘点,时间为: {self.get_format_time(time.time())}')

            


    def kill_timer(self):
        print('输入q，退出定时器')
        inp=input('>>: ').strip()
        if inp=='q':
            self.timer.cancel()

    
    # 将时间戳转为格式时间
    def get_format_time(self,time_stamp):
        # 获取时间戳的时间元组
        t_t=time.localtime(time_stamp)
        # 转换为格式时间
        t_f=time.strftime('%Y-%m-%d %X',t_t)
        return t_f

# 产生时间戳
def get_time_stamp(pd_time):
    t1=datetime.datetime.now()
    y=str(t1.year)
    m=str(t1.month)
    d=str(t1.day)
    # 获取当前时间的日期 加上 23:45:00 组成 %Y-%m-%d %X 格式 
    t_f=f'{y}-{m}-{d} {pd_time}'
    # 将该格式 转为元组 再转为 时间戳
    t_c=time.mktime(time.strptime(t_f,'%Y-%m-%d %X'))
    return t_c


if __name__ == "__main__":

    pd_time='23:58:0'
    time_stamp=get_time_stamp(pd_time)
    while True:
        WxTimer(time_stamp)
        time.sleep(30)
        # time_stamp += 3600

    pass

# 错误原因
# Original error: Error: socket hang up
#  这种情况，应该是上个进程占用导致的，
# 1、首先把设备里的Appium 那两个app删除干净，或者给服务器换个端口号例如4723 换成4725，在把设备重启一下。可以解决的跟彻底一些。
# 2、在代码级别，防止这个问题发生。在启动appium 需要添加--session-override 如启动用这个命令

# appium -a 127.0.0.1 -p 4723 --session-override
# 在代码层级里自动化任务跑完最后面一定要调用driver.quit 等操作，或者代码出现致命错误，的时候也要去执行quit。以防下次自动化任务跑失败。

# 个人看法：
# 没有正确退出造成的,没有wd.quit()
# 要处理异常，当出现异常时，也要wd.quit()