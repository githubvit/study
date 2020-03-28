# 爬虫实战 二
# http requests 爬取信息 https://www.bilibili.com/video/BV1NJ411L7GE?p=2



# 上次 用 web自动化 爬取信息，优点：操作直观，缺点：效率太低。

# 而用requests 代替 浏览器 爬取信息，优点：效率高，缺点：不直观，特点：需要分析。

# 1 针对Network中的一堆请求，根据response，分析应该发起哪个请求。
# 2 如何构建需要的请求。
# 3 如何用re 正则 从页面 获取 数据。


#  1 针对Network中的一堆请求，根据response，分析应该发起哪个请求。
#  keyword:python city:北京
#  https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=

#  keyword:python city:上海
#  https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=

#  keyword:java   city:上海
#  https://search.51job.com/list/020000,000000,0000,00,9,99,java,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=
#  keyword:java   city:上海 第2页
#  https://search.51job.com/list/020000,000000,0000,00,9,99,java,2,2.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=

#  构造请求如下
# url=f'https://search.51job.com/list/{city_code},000000,0000,00,9,99,{keyword},2,{pagenum}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='

# 怎么获取city_code? 
    # 在network 找不到  city_code的线索
    # 跳到首页，在network中发现 名为area_array_c.js?20200305 的请求，返回为：
    # /* update - 2020/03/05 
    #   create by backstage <createDbFile.sh> */
    # var area={
    # "010000":"北京",
    # "010100":"东城区",
    # "010200":"西城区",
    # "010500":"朝阳区",
    # "010600":"丰台区",
    # "010700":"石景山区",
    # "010800":"海淀区",
    # "010900":"门头沟区",
    # "011000":"房山区",
    # "011100":"通州区",
    # "011200":"顺义区",
    # "011300":"昌平区",
    # "011400":"大兴区",
    # "011500":"怀柔区",
    # "011600":"平谷区",
    # "011700":"密云区",
    # "011800":"延庆区",
    # "020000":"上海",
    # "020100":"黄浦区",
    # "020300":"徐汇区",
    # ...
    # ...
    # "365002":"新西兰",
    # "366000":"其他",
    # "01":"珠三角"
    # };

# 该请求的url:https://js.51jobcdn.com/in/js/2016/layer/area_array_c.js?20200305



import requests
import json
import re
import csv
    


class QCWY:
    def __init__(self,url,keyword,city,maxpagenum=1):
        self.url=url
        self.keyword=keyword
        self.city=city
        self.maxpagenum=maxpagenum

    # 获取city_code
    def get_city_code(self):
        url='https://js.51jobcdn.com/in/js/2016/layer/area_array_c.js'
        res=requests.get(url)
        # 截取{}内的字符串
        code2area_str=res.text.split('area=')[1].split(';')[0]
        # 转为字典
        code2area_obj=json.loads(code2area_str)
        # 反转字典    将 码：城市 反转为 城市：码
        area2code_obj={v:k for k,v in code2area_obj.items()}    

        # print(area2code_obj)  

        # 获取输入城市码
        if self.city not in area2code_obj:
            print(f'查无此地：{self.city}')
            exit() 
            # exit(0)：无错误退出 
            # exit(1)：有错误退出

        # print(f'{self.city}:{area2code_obj[self.city]}')
        return area2code_obj[self.city]

    def run(self):
        # 构建请求url
        city_code=self.get_city_code()
        url=f'https://search.51job.com/list/{city_code},000000,0000,00,9,99,{self.keyword},2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
        
        # 发送请求
        response=requests.get(url)
        # 获取字符串
        html_str=response.content.decode('gbk')
        
        # 打开csv
        with open(f'前程无忧{self.city}{self.keyword}.csv','w',newline='',encoding='utf8') as f:
            # 定义 字典头 
            f_csv=csv.DictWriter(f,['职位名称','详细链接','公司名称',
                    '工作地点','薪资','发布时间','职位信息'])     
            # 写表头
            f_csv.writeheader()   
            # 用正则 提取 数据
            # 在浏览器分析网页 用到 点可匹配换行 re.DOTALL 
            # 普通情况 点是匹配除换行外的其余字符
            # print(html_str)
            pattern=r'class=\"el\".*?\"t1 \".*?<a.*?href=\"(?P<lj>.*?)\".*?>\s*(?P<zw>.*?)\s*</a.*?\"t2\".*?<a.*?>\s*(?P<gs>.*?)\s*</a.*?\"t3\">\s*(?P<dd>.*?)\s*<.*?\"t4\">\s*(?P<xz>.*?)\s*<.*?\"t5\">\s*(?P<rq>.*?)\s*<'
            p=re.compile(pattern,re.DOTALL)
            for i in p.finditer(html_str):
                row={
                    '职位名称':i.group('zw'),
                    '详细链接':i.group('lj'),
                    '公司名称':i.group('gs'),
                    '工作地点':i.group('dd'),
                    '薪资':i.group('xz'),
                    '发布时间':i.group('rq'),
                    '职位信息':''
                }
                # 到详情页爬取职位信息
                res2=requests.get(i.group('lj'))
                d_html=res2.content.decode('gbk')
                # 先截取该段信息
                d_html_jq=d_html.split('职位信息')[1].split('<div class="mt10">')[0]
                # 如果有再来匹配信息
                if len(d_html_jq):
                    d_pattern=r'>(.*?)<'
                    p=re.compile(d_pattern)
                    for i in p.findall(d_html_jq):
                        if i:
                            row['职位信息'] += i

                # 最后把整个结果写入csv
                f_csv.writerow(row)

        

url='https://www.51job.com/'
keyword='python'
city='上海'
# maxpagenum=3
QCWY(url,keyword,city).run()