import time,datetime,random
from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey 
# from appium.webdriver.common.touch_action import TouchAction
from threading import Timer
import os
from adb_wxzz import wxzz #引入wxzz
from PIL import Image
'''
一 流程：找到 当下  今天所有笔收款 并 记录 uuid
初始页面 ：微信支付
1 有'今日第n笔收款',
    1.1 n没有记录，就记录n
        # 执行如下 流程一 备注判定
        1.1.1 本节点有收款方备注,就记录 
            # 流程二 n判定
            1.1.1.1 如果n==1,
                # 流程三 下滑判定
                1.1.1.1.1 有下滑过，就返回上一页，再进入当前页，返回到第一层，就进入循环。
                1.1.1.1.2 没有下滑过，就结束。
            1.1.1.2 如果n>1，则看比n小的节点n-1有没有记录，
                1.1.1.2.1 没有就继续下滑,返回到第一层，就进入循环。
                1.1.1.2.2 有，
                    1.1.1.2.2.1 有下滑过，就返回上一页，再进入当前页,返回到第一层，就进入循环。
                    1.1.1.2.2.2 没有下滑过，就结束。

        1.1.2 本节点没有收款方备注，就下滑，返回到第一层，就进入循环。
               
    1.2 n有记录，但收款方备注没有记录：
        #  执行 流程一

    1.3 n有记录，收款方备注也有记录：
        #  执行 流程二

2 没有'今日第n笔收款':
    2.1 没有返回过，就下滑，返回到第一层，就进入循环。。
    2.2 有返回过，就结束


二 测量节点的距离
同一节点下：
    text:今日第9笔收款，共计￥0.09   id:com.tencent.mm:id/aq3  坐标：[326,1424][839,1480] [326,1364][839,1420]
    text:收款方备注                 id:com.tencent.mm:id/aq2  坐标：[86,1304][326,1352]
    text:uuidee735312602b4a0da5c06907bcbb   id:com.tencent.mm:id/aq3  坐标：[326,1298][994,1405]
    
    垂直方向最大距离
        1424-1298=126
    1 获取 今日 节点 的y向坐标 y1
    2 获取 uuid 节点的y向坐标 y2
    3 如果  abs(y1-y2) < 130 则 为 同一节点，  ******
        则记录节点uuid.
    4 否则 ：
        获取 收款方 节点的y向坐标 y3
        如果 abs(y1-y3) < 130 则 为 同一节点，记录为：其他备注
        否则：下滑

    text:今日第5笔收款，共计￥0.05   id:com.tencent.mm:id/aq3  坐标：[326,1364][839,1420]
    text:0.01                      id:com.tencent.mm:id/as_   坐标:[464,1057][664,1157]
    垂直方向最大距离
        1364-1057=307

三 编写代码
1 生成 收款二维码 已写完 有待完善 下一步 实现精简二维码大小
2 实现 通过 监控 微信支付 获取 已扫码的收款二维码的uuid 流程的 单循环 ***
3 每日  盘点 day_stocktake
    转账
        将 该（营业号）微信支付账号 当日收到的金额 支付给另一个 移动手机账号 微信支付账号（一级总账号）。
    清空监控列表
    

4 推广码 分享码 这个模块与支付的关系就是uuid 其他没有什么关系
'''
# 今日收款通知节点

today_list=[]   # 记录 收款节点 的“今日第 笔收款，共计”
today_uuid=[]   # 记录 收款节点 的uuid
today_n=[]      # 从“今日第 笔收款，共计”中的“第”和“笔”中的数字序号
today_sum=[]    # 从“今日第 笔收款，共计”中的“共计”后面的汇总金额
today_price=[]  # 记录 收款节点 的单笔金额。
cnt=0   # 定时器 的 第几次 运行
pd_node_finded=False    # 是否找到盘点节点

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
        # 三个开关 两种状态
        # 本轮 结束 开关
        # self.go_over=False
        
        self.go_swipe=False # 下滑
        
        self.go_back=False   # 返回

        self.is_swiped=False # 下滑过
        self.is_backed=False # 返回过

       

        # 连接 appium server
        self.wd = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        # 隐式等待
        # 设置缺省等待时间
        self.wd.implicitly_wait(10)


    # 判断当前页面是否是微信支付页面
    def check_wxpay_page(self):
        page=self.wd.find_elements_by_xpath('//*[@resource-id="com.tencent.mm:id/ls"][@text="微信支付"]')
        if page:
            self.wxpay_main()
            
        else:
            # 1 看看 是不是 微信首页
            pay_code='new UiSelector().resourceId("com.tencent.mm:id/bag").text("微信支付")'
            pay=self.wd.find_elements_by_android_uiautomator(pay_code) # 要用复数
            if pay:
                pay[0].click()
                # 2 从 微信页面 点击 到达微信支付页面
                print('进入微信支付页面')
                time.sleep(2)
                self.wxpay_main()
            else:
                print('找不到"微信支付"页面,退出')
                self.wd.quit()
                return None



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
     
    
    # 一次下滑 一次下滑并返回  退出结束一次流程

    # 在 wxzf 页面中

    # 记录

    # 找 盘点 节点，是本次记录开始的起点，也是页面首次下滑查找元素的终点。
        # 找到该节点，也意味着：
            # 如果是下滑过来的，就要停止下滑并返回；
            # 否则，就静止（什么也不做）并退出。

    # 在 收款通知 节点中 找到该节点下 uuid  price  的值

    # 这是我已经记录过的节点：
        # 如果是下滑过来的，就要停止下滑并返回；
        # 否则，就静止（什么也不做）并退出。

    
    # 看 两个节点
    # 一个是盘点节点
        # 是第一次下滑过程中结束下滑的唯一标志，因此，本系统一开始，就要先用本机账号向手机转账账号转账，否则，无法终止下滑。
    # 一个是收款节点
        # 这是要捕捉并记录uuid的节点。

    # 做 两个动作
    # 下滑 同步列表
    # 返回再回来 滑到盘点节点或已记录的节点，就用该方法刷新。


   

    def wxpay_main(self):
        # 找节点
        # 如果有'135****3627' id'com.tencent.mm:id/aq3' 说明到了上次盘点的 地方，
        pd_nodes=self.wd.find_elements_by_xpath('//*[@resource-id="com.tencent.mm:id/aq3"][@text="135****3627"]')
        # 找到resource-id=com.tencent.mm:id/aq3 以'今日第'开头 并且包含'笔收款，共计'
        sk_nodes=self.wd.find_elements_by_xpath('//*[@resource-id="com.tencent.mm:id/aq3"][starts-with(@text,"今日第")][contains(@text,"笔收款，共计")]')

        self.wxzz_node(pd_nodes,sk_nodes)

        # 动作
        if self.go_swipe:
            self.down_swipe()
        elif self.is_swiped: # 下滑过 说明是滑到这里来的 又不用再下滑，说明到盘点节点或已记录的节点
            self.back_back() # 那就去刷新   
        else:#没有动作 就结束
            if self.is_added:
                print('今日节点列表',today_list)
                print('今日uuid列表',today_uuid)
                print('今日序号列表',today_n)
                print('今日金额汇总列表',today_sum)
                print('今日金额列表',today_price)
                print('记账完毕，结束本次监测')

            print(f'第{cnt}次监测结束')
            self.wd.quit()
            return None
       


    # 看盘点转账节点
    def wxzz_node(self,pd_nodes,sk_nodes):
       
        if pd_nodes:
            # 取出最下一个
            y1=pd_nodes[-1].location['y']
            print('看到了盘点转账点，不能下滑，要么停止,要么返回')
            # 告诉找到了
            pd_node_finded=True
            
            # 如果 收款 节点 在下方，
            if sk_nodes:
                for sk_node in sk_nodes:
                    if sk_node.location['y']>y1:
                        self.sk_node_op(sk_node)

            self.go_swipe=False  # 不管怎么样 都终止下滑 
                
        else:
            print('没有盘点转账点，去找收款通知点')
            # 再看今日收款 到账通知节点
            self.wxsk_node(sk_nodes) 

    # 判断页面是否有 今日... 找到 当下  今天所有笔收款 并 记录 uuid
    def wxsk_node(self,sk_nodes):                       #   *******************************
             
        if sk_nodes:
            for sk_node in sk_nodes:
                # 单个节点操作 找节点 同步列表
                self.sk_node_op(sk_node)

            if pd_node_finded:#找到 盘点节点 作为终止节点

                # 跨1怎么判断 如何做到 随时 可盘点              *******************************
                # 1. 可以在找到 盘点节点时，
                    # 就取序号列表的最小值。
                # 2. 如果，后一轮发现的序号是 1  
                if today_n:
                    min_idx=min(today_n)

                    # 比较sk_n 是否到min_idx,不到min_idx 都要 下滑
                    for i in range(min_idx,max(today_n)):
                        if i not in today_n:
                            print(f'没有{i}')
                            self.go_swipe=True
                            break
            else:
                print('没有找到盘点节点,go swipe')
                self.go_swipe=True
        else:
            print('没有 今日收款通知 节点')
            if self.is_backed:
                print('已经监测过，去结束本次监测')
                print(f'第{cnt}次监测结束')
                self.wd.quit()
                return None
            else:
                print('当前无收款记账点，去下滑找今日节点')
                self.go_swipe=True               

    # 单个节点操作 同步各个列表
    def sk_node_op(self,sk_node):
        print('单个收款节点操作，找同一节点下的各个元素，同步各个列表')
        # 获取 今日 文本
        sk_text=sk_node.get_attribute('text')
        
        if sk_text not in  today_list:
            
            
            # 今天第几笔账
            sk_n=int(sk_text.split('第')[1].split('笔')[0])#取第和笔之间的值
            # 添加到序号列表
            today_n.append(sk_n)

            # 当天当时的总金额
            sk_sum=sk_text.split('￥')[1]
            # 添加到汇总列表
            today_sum.append(sk_sum)

            print(f'将 {sk_text} 加入今日列表 -- {sk_n}加入序号列表 -- {sk_sum}加入金额汇总表 ')
            
            # 查找同一节点内的uuid 同步添加 uuid列表 today_uuid
            self.uuid_node(sk_node)
            # 查找同一节点内的uuid 同步添加 金额列表 today_price
            self.price_node(sk_node)

            self.is_added=True 
        else:
            # 在 today_list 列表 无uuid
            if today_uuid[today_list.index(sk_text)]=='no_find':
                print(f'{sk_text}在今日列表中，但uuid没找到，找uuid')
                # 查找同一节点内的uuid 同步添加 
                self.uuid_node(sk_node)
                self.price_node(sk_node)#没有uuid 也必然没有price

            # 有uuid 没有price
            if today_price[today_list.index(sk_text)]=='no_find':
                print(f'{sk_text}在今日列表中，备注列表也有，但金额列表没找到，找金额price')
                self.price_node(sk_node)

        

                

    def uuid_node(self,sk_node):
        # 找uuid
        uuid_code='//*[@resource-id="com.tencent.mm:id/aq3"][starts-with(@text,"uuid")]'
        uuid_node=self.find_node(sk_node,130,uuid_code,today_uuid)

    def price_node(self,sk_node):
        # 找price
        price_code='//*[@resource-id="com.tencent.mm:id/as_"]'
        price_node=self.find_node(sk_node,310,price_code,today_price)


    # 查找同一节点内 小节点 找到 同步 节点列表， 没找到 添加'no_find'到节点列表
    # m_node:主节点 根
    # dh:距离主节点的距离 
    # node_code:xpath 要找的小节点的xpath
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
                    if len(t_list)<len(today_list):#新增
                        t_list.append(text)
                    else:
                        t_list[today_list.index(m_text)]=text #不能用append 替换'no_find'
                    self.is_added=True

                    return None
   
        print('没找到,下滑')
         # 如果节点列表没有添加 就 没找到 因此 添加'no_find'  打开 下滑 开关
        if len(t_list)<len(today_list):
            t_list.append('no_find')
            print(f'本次没有找到，添加"no_find"到{t_list},打开下滑开关')
        self.go_swipe=True

    
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
        print("标记下滑过,重新设置self.go_swipe、self.is_backed为初始值False")
        # 4 标记下滑过
        self.is_swiped=True

        # 5 重新设置为初始值
        # 下滑开关
        self.go_swipe=False

        # 返回过
        self.is_backed=False

       

        # 6 重新开始
        print("下滑完毕，返回到第一层，重新开始")
        time.sleep(2)
        self.wxpay_main()
        

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
        print('标记返回过，重新设置self.go_swipe、self.is_swiped、self.go_back为初始值False')
        self.is_backed=True

        # 4 重新设定为初始值

        # 下滑开关
        self.go_swipe=False
        # 下滑过
        self.is_swiped=False
        # 返回开关
        self.go_back=False
        

        # 5 重新开始
        print('返回完毕，返回到第一层，重新开始')
        time.sleep(2)
        self.wxpay_main()

   


class WxTimer():
    def __init__(self,time_stamp):
        
        self.time_stamp=time_stamp # 获取定时任务结束 盘点时间戳
        print(f'盘点时间{self.get_format_time(self.time_stamp)}')
        self.run_one()

        
    # 一次调度流程
    def run_one(self):
        global cnt # 声明操作模块的全局变量
        global pd_node_finded
        global today_price
        global today_list
        global today_notes
        global today_n
        global today_sum
        global end_point
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
            self.timer=Timer(100,self.run_one)
            self.timer.start()
            self.kill_timer()
        else:
            time.sleep(2)
            # 1 返回到微信页面
            print('准备盘点，返回到微信页面,点击 返回') # [0,60][108,190]
            os.popen('adb shell input tap 60 120')

            # 2 盘点 
            time.sleep(2)
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
            today_notes=[]
            today_n=[]
            today_sum=[]
            today_price=[]
            cnt=0 #重新计数
            print(f'结束盘点,时间为: {self.get_format_time(time.time())}')

            return

            # 3  再次启动定时任务
            self.time_stamp += 3600 #定义新的终止时间戳
            print(f'盘点时间{self.get_format_time(self.time_stamp)}')
            self.timer=Timer(310,self.run_one)
            self.timer.start()
            self.kill_timer()

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

    pd_time='18:0:0'
    time_stamp=get_time_stamp(pd_time)
    while True:
        WxTimer(time_stamp)
        time.sleep(100)
        time_stamp += 3600

    pass