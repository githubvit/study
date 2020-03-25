# 模拟浏览器与网站交互

import requests
import selenium_webauto

# 关于 requests http://2.python-requests.org/zh_CN/latest/user/quickstart.html



# 打开网页

def open_page(url):
    # 产生会话对象 即携带cookie
    s=requests.Session()
    print("session",)
    # 请求头 都必须是str
    response=s.get(url,headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    })
    return response

# 打开搜索页

def open_search_page(page,keyword):
    pass

def main(url):
    
    response=open_page(url)
    
    print('\n\n--------------------Http response * begin--------------------')
    print(response.status_code)
    for k,v in response.headers.items():
        print(f"{k}:{v}")
    print('')    
    print(response.content.decode('utf8'))
    print('--------------------Http response * end--------------------')
    
    # print(dir(response.cookies))


if __name__ == "__main__":
    url='https://search.bilibili.com/all?keyword=小升初&from_source=nav_search_new'
    # url='https://www.ixigua.com/search/%E5%B0%8F%E5%8D%87%E5%88%9D/?logTag=oBQJEV45pQzISSgkG_KKQ&keyword=%E5%B0%8F%E5%8D%87%E5%88%9D'
    # url='https://www.dalipan.com/search?keyword=%E5%B0%8F%E5%8D%87%E5%88%9D'
    # url='https://www.ixigua.com'
    # search_el='.search-wrap input'
    # search_btn_el='.search-btn span' # 定位到span 搜索 文字 否则有时可以有时不行
    # keyword='小升初'
    # # 用selenium获取 列表页
    # seach_url=selenium_webauto.index_search(url,search_el,search_btn_el,keyword)
    # print(seach_url)
    # main(seach_url)
    main(url)