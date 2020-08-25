import time,datetime,random
from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey #键盘输入用
from appium.webdriver.common.touch_action import TouchAction
# 还是不好 不稳定，最长时间为28分钟 300次循环
class Wx_pay:
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
        # while 开关
        self.is_while=True
        self.start_time=time.time()
        self.uuid_list=[] # uuid 列表
        self.uuid_time_list=[] # 加入uuid列表的时间列表
        self.time_line_list=[] # 时间条标记列表
        self.is_backed=False # 返回过

        # 连接 appium server
        self.wd = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        # 隐式等待
        # 设置缺省等待时间
        self.wd.implicitly_wait(10)

        # 运行
        self.wx_pay_run()

    # 返回
    def go_back(self):
        if not self.is_backed: # 本次下滑没有返回过就返回
            # 1 返回 微信页面
            print('返回')
            self.wd.press_keycode(4)
            time.sleep(2)
            pay_code='new UiSelector().resourceId("com.tencent.mm:id/bag").text("微信支付")'
            pay=self.wd.find_element_by_android_uiautomator(pay_code)

            # 2 从 微信页面 点击 到达微信支付页面
            print('进入')
            pay.click()

            # 3 标记返回过
            self.is_backed=True


    # 下滑
    def swipe_down(self):
        # 下滑开关
        is_swipe=False
        # 查找时间条 并标记
        time_code='new UiSelector().resourceId("com.tencent.mm:id/ah")'
        time_lines=self.wd.find_elements_by_android_uiautomator(time_code)
        # 如果有时间条
        if time_lines:
            # time_lines=wd.find_elements_by_xpath('//*[@resource-id="com.tencent.mm:id/ah"]')
            for time_node in time_lines:
                time_line_text=time_node.get_attribute('text')
                # 如果 时间条 不在 时间条列表中
                if time_line_text not in self.time_line_list:
                    if '昨天' in time_line_text:
                        print('发现下滑的时间条包含"昨天",应该返回')
                        break
                    else:
                        self.time_line_list.append(time_line_text) #标记
                        print(f'将该时间条时间 {time_line_text} 添加到时间条列表，继续下滑',)
                        is_swipe=True #应该下滑

            if is_swipe:
                print('下滑')
                # 如果有多个个时间条 就从第一个时间条下滑到最下一个时间条
                if len(time_lines)>1:
                    self.wd.scroll(time_lines[0],time_lines[-1],duration=2000)

                # 如果只有一个时间条 就从该时间条下滑到 最底下 更多 位置
                else:
                    # 获取 更多节点
                    more_node=self.wd.find_element_by_xpath('//*[@resource-id="com.tencent.mm:id/aqu"][@text="更多"]')
                    self.wd.scroll(time_lines[0],more_node,duration=2000)

                # 滑动过 就将返回过 重新设为False
                if self.is_backed:
                    print('重设 返回过标志 为False')
                    self.is_backed=False 
            else:
                self.go_back()
        else:
            # 获取整体节点
            all_code='new UiSelector().resourceId("com.tencent.mm:id/af")'
            all_node=self.wd.find_element_by_android_uiautomator(all_code)
            s_x=all_node.location['x']+all_node.size['width']/2-8
            s_y=all_node.location['y']+all_node.size['height']/2+11
            e_x=s_x+11
            e_y=all_node.location['y']+all_node.size['height']
            self.wd.swipe(s_x,s_y,e_x,e_y,duration=2000)

    # 获取uuid 
    def get_uuid(self):
        # 直接在 微信支付页面 操作页面
        # 1 检查 微信支付 是否有通知，
        # pay_code='new UiSelector().resourceId("com.tencent.mm:id/bag").text("微信支付")'
        # pay=wd.find_element_by_android_uiautomator(pay_code)
        # time.sleep(2)
        # 2 微信支付 点击 到达微信支付页面
        # pay.click()
        # time.sleep(2)
        # 3 返回上一页
        # wd.press_keycode(4)

        # 获取 uuid 节点

        uuid_node_list=self.wd.find_elements_by_xpath('//*[@resource-id="com.tencent.mm:id/aq3"][starts-with(@text,"uuid")]')
        # 如果有uuid 
        if uuid_node_list:
            is_add=False
            for uuid_node in uuid_node_list:
                uuid_text=uuid_node.get_attribute('text')
                print('uuid:',uuid_text)
                # 如果uuid不在列表就添加 并记录时间戳 并下滑
                if uuid_text not in self.uuid_list:
                    self.uuid_list.append(uuid_text)
                    self.uuid_time_list.append(time.time())
                    is_add=True
            # 如果有新增 就下滑 找新的uuid 看看有没有遗漏
            if is_add:
                print('将该uuid添加到列表--下滑')
                self.swipe_down()
            else:
                print('该uuid已经在列表中-- 返回 或 静止')
                # self.is_while=False
                # 返回
                self.go_back()
                    
        else:
            # 如果没有uuid 并不在时间条列表中 就标记 该时间条 并 下滑
            self.swipe_down()
    # 循环监控
    def while_watch(self,while_cnt):
        while True:
            t1=time.time()-self.start_time
            print(f'循环监控,距启动{t1:.2f} 秒')
            while_cnt+=1
            print(f'开始第{while_cnt}次循环监控')
            if self.is_while:
                self.get_uuid()
                t2=time.time()-self.start_time
                dt=t2-t1
                print(f'---------------------第{while_cnt}次循环监控结束 持续{dt:.2f}秒---------------------')

                time.sleep(5)
            else:
                break

    # 主程序
    def wx_pay_run(self):
        print(f'主程序开始,距启动{(time.time()-self.start_time):.2f} 秒')
        while_cnt=0
        try:
            self.while_watch(while_cnt)
            # 定时启动
            # 如果没有任何操作，会产生‘ 错误 ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))’。
            # 中断连接 因此 要在时间条上点击
            print('is_while',self.is_while)
            print(self.uuid_list)
            print(self.uuid_time_list)
            print(self.time_line_list)
        except Exception as e:
            print(self.uuid_list)
            print(self.uuid_time_list)
            print(self.time_line_list)
            print('错误',e)
            end_time=time.time()-self.start_time
            end_time=round(end_time)#取整
            h,s1=divmod(end_time,3600)#求商 余
            m,s=divmod(s1,60)

            print(f'本次运行时间持续：{h}小时{m}分钟{s}秒')

if __name__ == "__main__":
    
    Wx_pay()
    