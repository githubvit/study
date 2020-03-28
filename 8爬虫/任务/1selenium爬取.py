# 爬虫实战 一 
# 通过 selenium 自动化浏览器爬取信息 https://www.bilibili.com/video/BV1NJ411L7GE?p=1

# 任务描述
    # 从首页到列表页到详情页(index_list_detail)
    # 建立 爬取{关键字}.csv 列表文件

# 知识点：
    # 面向对象 解决问题
    # 熟悉 selenium 使用
    # csv 使用

from selenium import webdriver
import time,csv

driver_path=r'D:\chromedriver.exe'
# class ILd_page:
#     # 初始化 webdriver 对象
#     def __init__(self,index,keyword):
#         self.wd=webdriver.Chrome(driver_path)

# 前程无忧 www.51job.com
# 从前程无忧 爬取 北京 python 职位  的招聘信息
# 参数： 职位关键字 选择城市

class QCWY:
    # 初始化 webdriver 对象
    # 模拟人 输入的参数 和操作的 页面元素
    # keyword:职位关键字，city：选择的城市
    # webelement：操作的页面元素字典{
    #  'input'
    # }
    # 爬取的最大页面数maxpagenum=1
    def __init__(self,url,keyword,city,webelement,maxpagenum=1):
        self.wd=webdriver.Chrome(driver_path)
        self.url=url
        self.keyword=keyword
        self.city=city
        self.we=WebEl(webelement)
        self.maxpagenum=maxpagenum

    # 模拟人操作
    def run(self):
       
        # 打开网页
        self.wd.get(self.url)

        # 隐式等待 设置最大等待时长为 5秒
        self.wd.implicitly_wait(5)

        # 选取input 输入关键字 python
        self.wd.find_element_by_css_selector(self.we.ipt).send_keys(self.keyword)

        # 选取区域
        self.wd.find_element_by_css_selector(self.we.area).click()
        
        # 等页面稳定
        time.sleep(1)
        
        # 清除已经选择的城市 空列表 不报错
        for i in self.wd.find_elements_by_css_selector(self.we.del_citys):
            i.click()

        # 选择城市 北京
        target=None
        for i in self.wd.find_elements_by_css_selector(self.we.std_citys):
            if i.text==self.city:
                target=i
                # i.click()
                break
        if target is None:
            input(f'{self.city}不在当前热门城市列表中，请手动点击选中城市后，按回车继续。。。')
        else:
            target.click()
        
        # 选取 确定 按钮
        self.wd.find_element_by_css_selector(self.we.area_btn).click()
        

        # 选取搜索按钮
        self.wd.find_element_by_css_selector(self.we.search_btn).click()

        # 页面跳转 等待页面稳定
        time.sleep(1)

        # 当前窗口 已经 从首页 跳转到 搜索结果列表页面了

        # 1 在这里要爬取当前页的 列表数据
            #  获取列表节点
            #  获取每行数据节点
            #  获取每行数据 写入csv文件
        # 2 要进入每个详情页面，爬取其中需要的数据，写入csv文件，再返回当前列表页
        # 3 点击当前列表页的下一页按钮，进入列表页的下一页
        # 4 返回1

        # 列表页
        # 写到csv文件中去
        # csv 使用 字典 定义的 表头就是 字典key列表
        with open(f'前程无忧网{self.city}{self.keyword}招聘信息.csv',
                  'w',newline='',encoding='utf8') as f:
            # csv 字典key 列表
            f_csv=csv.DictWriter(f,['职位名称','详细链接','公司名称',
                        '工作地点','薪资','发布时间','职位信息'])
            # 表头 标题栏 
            f_csv.writeheader()

            # 操作列表页
            # 把每页数据写入csv 前面click后，当前 已经是第1页
            for page_num in range(1,self.maxpagenum+1):
                # 缩短隐式等待的时间
                self.wd.implicitly_wait(2)

                # 操作当前列表页 获取页面数据
                page_data=self.handel_one_page()
                # 把当前页数据 写入 csv 文件
                f_csv.writerows(page_data)

                # 如果输入的最大页面超过了页面的最大值
                # 如果当前页就是最后一页 就退出
                if self.isLastpage():
                    break

                # 恢复 隐式等待的时间
                self.wd.implicitly_wait(5)

                # 清空原来的页码
                self.wd.find_element_by_css_selector(self.we.page_num_input).clear()
                # 输入下一列表页 页码
                self.wd.find_element_by_css_selector(self.we.page_num_input).send_keys(page_num+1)
                # 按确定
                self.wd.find_element_by_css_selector(self.we.page_num_input_btn).click()

                # 等待页面稳定
                time.sleep(1)

    # 列表页 单页面处理  获取本页数据
    def handel_one_page(self):
         # 获取列表页的每行 节点
        rows_el=self.wd.find_elements_by_css_selector(self.we.res_rows)

        # 分析每行节点 提取需要的信息
        # 从每行节点 中 获取数据节点 row.find_elements_by_css_selector('span') 而不是从页面 self.wd中获取m
        # 提取 数据节点的文本信息 span.text 即 需要的招聘信息
        page_data_list=[]
        for row in rows_el:
            # 分析出每行中的span就是数据节点
            # 从每行中获取数据节点列表
            data_els=row.find_elements_by_css_selector('span')

            # 提取数据节点数据 用列表生成式
            row_datas=[data_el.text for data_el in data_els]

            print(row_datas)

            # 因为csv 每行输入必须是字典，要按字典进行 数据清洗
            row_dict={
                '职位名称':row_datas[0],
                '详细链接':data_els[0].find_element_by_css_selector('a').get_attribute('href'),
                '公司名称':row_datas[1],
                '工作地点':row_datas[2],
                '薪资':row_datas[3],
                '发布时间':row_datas[4],
                # '职位信息':
            }

            # 进到详情页 爬取数据 再回到当前页
            data_els[0].click()
            
            time.sleep(1)

            # print('窗口列表',self.wd.window_handles)
            # print('current_window',self.wd.current_window_handle)
            # 切换到详情页
            self.wd.switch_to.window(self.wd.window_handles[-1])

            # 获取详情页信息 
            row_dict['职位信息']=self.detail_page_handel()

            # 关闭当前详情页 *****
            self.wd.close()

            # 切回到当前列表页
            self.wd.switch_to.window(self.wd.window_handles[0])

            # 把每行数据字典加到该页数据列表中
            page_data_list.append(row_dict)

        return page_data_list

         
    # 详情页
    def detail_page_handel(self):
        # 获取详情页数据节点 有可能不存在 所以用elements来获取成列表 没有则长度为0 便于判断
        msg_el=self.wd.find_elements_by_css_selector(self.we.detail_page_info)
        # print (msg_el)
        # 如果节点 存在且长度为1 就返回文本 否则 返回None
        return  msg_el[0].text if msg_el and len(msg_el)==1 else None   
        
    # 判断是否是最后一页
    def isLastpage(self):
        # 根据页面分析，如果当前列表页是最后一页。
        # ‘下一页’按钮为灰色.
        # 即当前区域最后一个li标签中就没有a标签，点不动了，。
        next_page=self.wd.find_element_by_css_selector(self.we.next_page)

        # 当前下一页按钮 是否 包含 a标签
        last_page=next_page.find_elements_by_css_selector('a')

        return  False if len(last_page) else True    
         




# 机器人

# 按照人操作的步骤 
# 把要操作的页面元素都放到这个类中
# 按步骤 
webelement={
    # 首页 index_page
    'input':'#kwdselectid', # 输入关键字 python
    'area_select':'#work_position_click', # 点开区域选择
    'del_selected_citys':'#work_position_click_multiple_selected >span span', # 清空 原来 已选 城市
    'select_citys':'#work_position_click_center_right_list_000000 em',# 可选择城市
    'area_button':'#work_position_click_bottom_save',#点击  区域 确定按钮
    'seach_btn':'div.ush>button', # 点击 搜索 按钮 当前页 变成 搜索结果页面
    # 'seach_btn':'.header button' #错误的地方，网页上经常会存在这样的错误 
    # 如果选择了.header button 而界面上没反应，则不对。

    # 列表页 list_page
    'res_list':'#resultList', # 表单 节点
    'res_rows':'#resultList [class=el]', # 表单中的行节点 列表
    # 'res_list_rows':'#resultList .el', # 不能用，因为 这样表头标题也会包含 标题class="el title"
    # 分析 行节点 获取每行 需要的数据 
    'page_num_input':'#jump_page', # 页码 输入框
    'page_num_input_btn':'.p_in .og_but', # 页码 输入框 确定按钮
    'next_page':'.p_in li:nth-last-child(1)', # 当前页 的 下一页 按钮 来判断是不是最后一页 
    
    # 详情页 detail_page
    'detail_page_info':'.job_msg', # 职位信息


}

class WebEl:
    def __init__(self,dict):
        # 首页 index_page
        self.ipt=dict['input']
        self.area=dict['area_select']
        self.del_citys=dict['del_selected_citys']
        self.std_citys=dict['select_citys']
        self.area_btn=dict['area_button']
        self.search_btn=dict['seach_btn']

        # 列表页 list_page
        self.res_rows=dict['res_rows']
        self.page_num_input=dict['page_num_input']
        self.page_num_input_btn=dict['page_num_input_btn']
        self.next_page=dict['next_page']

        # 详情页 detail_page
        self.detail_page_info=dict['detail_page_info']

url='https://www.51job.com/'
keyword='python'
city='北京'
maxpagenum=3
QCWY(url,keyword,city,webelement,maxpagenum).run()


# 总结：
# 一 web自动化爬虫开发
    # 1 selenium web自动化 就是 模拟人 来操作浏览器

    # 2 节点类 class WebEl
    #     把模拟人操作的节点webelement按步骤记录字典，这就可以清晰看到每步操作，
    #     再把节点字典变成节点类对象，用于面向对象的爬虫类 class QCWY的初始化。
    #     self.we=WebEl(webelement)

    # 3 面向对象来开发 爬虫 
    #     实例化，把一些逻辑功能化（判断是否是最后一页，列表页单页处理），最后run起来。


#  二 内置csv文件模块用法

import csv

def one(): #写成函数形式，是可以不用注释调，只要不执行。

    # csv 使用 字典 定义的 表头就是 字典key列表
    with open(f'前程无忧网{self.city}{self.keyword}招聘信息.csv',
              'w',newline='',encoding='utf8') as f:

        # 1. 定义字典key  列表
        f_csv=csv.DictWriter(f,['职位名称','详细链接','公司名称',
                    '工作地点','薪资','发布时间','职位信息'])
        # 2. 写入表头  
        f_csv.writeheader()

        # 3. 数据格式化
        # 把要写入csv文件的每行信息字典化
        # 因为csv 每行输入必须是字典，要按字典进行 数据清洗
        row_dict={
            '职位名称':row_datas[0],
            '详细链接':data_els[0].find_element_by_css_selector('a').get_attribute('href'),
            '公司名称':row_datas[1],
            '工作地点':row_datas[2],
            '薪资':row_datas[3],
            '发布时间':row_datas[4],
            # '职位信息':
        }
        # 4. 写入数据
        #  每行写入
        f_csv.writerow(row_dict)
        #  多行写入
        #  把当前页数据 写入 csv 文件
        f_csv.writerows(page_data)
