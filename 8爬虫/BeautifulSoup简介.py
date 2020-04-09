# 解析库 BeautifulSoup 

# 1 安装
    # pip install beautifulsoup4
    # 安装解析器：lxml,具有容错功能：在html代码不完整的情况下,使用该模块可以识别该错误。
        # pip install lxml
from bs4 import BeautifulSoup

def bs1():
    # 定义不完整的html
    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>
    """
    # 建立soup对象
    soup=BeautifulSoup(html_doc,'lxml') #用lxml库解析，具有容错功能
    # soup=BeautifulSoup(open('a.html','r',enconding='utf-8'),'lxml') #打开一个html 文件(默认模式就是'r',)，用lxml库解析，建立soup对象。
    # soup=BeautifulSoup(open('a.html'),'lxml') #打开一个html 文件(默认模式就是'r',)，用lxml库解析，建立soup对象。
    res=soup.prettify() #处理好缩进，结构化显示
    print(res)
# bs1()
# 结果
    # <html>
    #  <head>
    #   <title>
    #    The Dormouse's story
    #   </title>
    #  </head>
    #  <body>
    #   <p class="title">
    #    <b>
    #     The Dormouse's story
    #    </b>
    #   </p>
    #   <p class="story">
    #    Once upon a time there were three little sisters; and their names were
    #    <a class="sister" href="http://example.com/elsie" id="link1">
    #     Elsie
    #    </a>
    #    ,
    #    <a class="sister" href="http://example.com/lacie" id="link2">
    #     Lacie
    #    </a>
    #    and
    #    <a class="sister" href="http://example.com/tillie" id="link3">
    #     Tillie
    #    </a>
    #    ;
    #     and they lived at the bottom of a well.
    #   </p>
    #   <p class="story">
    #    ...
    #   </p>
    #  </body>
    # </html>


  
# 2 使用
# 2.1 选择器
# 2.1.1标签选择 ： 就是遍历文档树
def bsbq():
    #标签选择：点方式，即直接通过标签名字选择，特点是选择速度快，但如果存在多个相同的标签则只返回第一个
    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p id="my p" class="title"><b id="bbb" class="boldest">The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>
    """
    soup=BeautifulSoup(html_doc,'lxml')

    #1、用法
    print(soup.p) #存在多个相同的标签则只返回第一个 
    # <p class="title" id="my p"><b class="boldest" id="bbb">The Dormouse's story</b></p>
    
    print(soup.a) #存在多个相同的标签则只返回第一个
    # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

    #2、获取标签的名称 是不是有点傻
    print(soup.p.name) # p

    #3、获取标签的属性
    print(soup.p.attrs) # {'id': 'my p', 'class': ['title']}

    #4、获取标签的内容
    print(soup.p.string) # p下的文本只有一个时，取到，否则为None
    
    #  The Dormouse's story
    print(soup.p.strings) #拿到一个生成器对象, 取到该p下所有的文本内容
    #  <generator object Tag._all_strings at 0x000002C7D2448D48>

    for i in soup.p.strings: #保留空白,删掉第一个p,结果是第二个p的内容
        print(i)
    # 结果
        # nce upon a time there were three little sisters; and their names were

        # Elsie
        # ,

        # Lacie
        #  and

        # Tillie
        # ;
        #     and they lived at the bottom of a well.
    
    print(soup.p.text) #取到p下所有的文本内容,删掉第一个p,结果是第二个p的内容
    # 结果
        # Once upon a time there were three little sisters; and their names were
        #     Elsie,
        #     Lacie and
        #     Tillie;
        #     and they lived at the bottom of a well.
    
    for line in soup.stripped_strings: #整篇标签内容，去掉空白
        print(line)
    # 结果
        # The Dormouse's story
        # The Dormouse's story
        # Once upon a time there were three little sisters; and their names were
        # Elsie
        # ,
        # Lacie
        # and
        # Tillie
        # ;
        #     and they lived at the bottom of a well.
        # ...

    #5、嵌套选择
    print(soup.head.title.string)
    print(soup.body.a.string)
    # The Dormouse's story
    # Elsie

    #6、子节点、子孙节点
    print(soup.p.contents) #p下所有子节点 [<b class="boldest" id="bbb">The Dormouse's story</b>]
    print(soup.p.children) #得到一个迭代器,包含p下所有子节点
    # <list_iterator object at 0x00000285524C19C8>

    for i,child in enumerate(soup.p.children):
        print(i,child)
    # 0 <b class="boldest" id="bbb">The Dormouse's story</b>

    print(soup.p.descendants) #获取子孙节点生成器对象,p下所有的标签都会选择出来
    # <generator object Tag.descendants at 0x00000285524A94C8>
    for i,child in enumerate(soup.p.descendants):
        print(i,child)
    # 0 <b class="boldest" id="bbb">The Dormouse's story</b>
    # 1 The Dormouse's story

    #7、父节点、祖先节点
    print(soup.a.parent) #获取a标签的父节点
    # <p class="story">Once upon a time there were three little sisters; and their names were
    # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    # <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
    # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
    # and they lived at the bottom of a well.</p>
    print(soup.a.parents) #找到a标签所有的祖先节点，父亲的父亲，父亲的父亲的父亲...
    # <generator object PageElement.parents at 0x00000285524A94C8>

    #8、兄弟节点
    print('=====>')
    print(soup.a.next_sibling) #下一个兄弟 
    #  ,
    print(soup.a.previous_sibling) #上一个兄弟 
    # Once upon a time there were three little sisters; and their names were

    print(list(soup.a.next_siblings)) #下面的兄弟们=>生成器对象
    # [',\n    ', <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, ' and\n    ', 
    # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>, ';\n    and they lived at the bottom of a well.']

    print(soup.a.previous_siblings) #上面的兄弟们=>生成器对象 
    # <generator object PageElement.previous_siblings at 0x00000285524A94C8>
# bsbq()

# 2.1.2 find_all、find：搜索文档树
    # 唯一的区别是 find_all() 方法的返回结果是值包含一个元素的列表,而 find() 方法直接返回结果.
    # find_all() 方法没有找到目标是返回空列表, find() 方法找不到目标时,返回 None .

    # 选取元素find的5套过滤方法
        # 字符串
        # 正则
        # 列表
        # True
        # 函数

def bs_find_all():
    #搜索文档树：BeautifulSoup定义了很多搜索方法,这里着重介绍2个: find() 和 find_all() .其它方法的参数和用法类似
    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p id="my p" class="title"><b id="bbb" class="boldest">The Dormouse's story</b>
    </p>

    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>
    """
    soup=BeautifulSoup(html_doc,'lxml')
    # def find_all(self, name=None, attrs={}, recursive=True, text=None,
    #              limit=None, **kwargs):

    #1、五种过滤器: 针对name=、attrs={}、text=字段可以使用字符串、正则表达式、列表、True、方法五种过滤器。
    #1.1、字符串：即标签名
    print(soup.find_all(name='b')) # 等同于 print(soup.find_all('b')) 
     # [<b class="boldest" id="bbb">The Dormouse's story</b>]
    print(soup.find_all(attrs={'class':'sister'}))
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, 
    # <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, 
    # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
    print(soup.find_all(text="The Dormouse's story")) # 找到了两个文本
    # ["The Dormouse's story", "The Dormouse's story"]
    print(soup.find_all(name='title',text="The Dormouse's story"))
    # [<title>The Dormouse's story</title>]

    print(soup.find(name='p',class_='story').a) # find和find_all用法相同，结合标签选择器，找到该p标签下的第一个a标签
    # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

    #1.2、正则表达式
    import re
    
    # print(soup.find_all(re.compile('^b'))) #找出b开头的标签，结果有body和b标签
    # 结果
        # [<body>
        # <p class="title" id="my p"><b class="boldest" id="bbb">The Dormouse's story</b>
        # </p>
        # <p class="story">Once upon a time there were three little sisters; and their names were
        #     <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
        #     <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
        #     <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
        #     and they lived at the bottom of a well.</p>
        # <p class="story">...</p>
        # </body>, <b class="boldest" id="bbb">The Dormouse's story</b>]

    #1.3、列表：如果传入列表参数,Beautiful Soup会将与列表中任一元素匹配的内容返回.下面代码找到文档中所有<a>标签和<b>标签:
    # print(soup.find_all(name=['a','b'])) # 同 soup.find_all(['a','b'])
    # 结果 
    # [<b class="boldest" id="bbb">The Dormouse's story</b>, 
    # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, 
    # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
    print(soup.find_all(text=[re.compile('E'),re.compile('^L')])) #查找包含E的文本、和以L开头的文本
    # ['Elsie', 'Lacie']

    #1.4、True：可以匹配任何值,下面代码查找到所有的tag,但是不会返回字符串节点
    # print(soup.find_all(True))
    # 结果
        # [<html><head><title>The Dormouse's story</title></head>
        # <body>
        # <p class="title" id="my p"><b class="boldest" id="bbb">The Dormouse's story</b>
        # </p>
        # <p class="story">Once upon a time there were three little sisters; and their names were
            # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
            # <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
            # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
            # and they lived at the bottom of a well.</p>
        # <p class="story">...</p>
        # </body></html>, 
        # <head><title>The Dormouse's story</title></head>, 
        # <title>The Dormouse's story</title>, 
        # <body>
        # <p class="title" id="my p"><b class="boldest" id="bbb">The Dormouse's story</b>
        # </p>
        # <p class="story">Once upon a time there were three little sisters; and their names were
            # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
            # <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
            # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
            # and they lived at the bottom of a well.</p>
        # <p class="story">...</p>
        # </body>, 
        # <p class="title" id="my p"><b class="boldest" id="bbb">The Dormouse's story</b>
        # </p>, 
        # <b class="boldest" id="bbb">The Dormouse's story</b>, 
        # <p class="story">Once upon a time there were three little sisters; and their names were     
            # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
            # <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
            # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
            # and they lived at the bottom of a well.</p>, 
        # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
        # <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
        # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>, 
        # <p class="story">...</p>]

    # for tag in soup.find_all(True):
        # print(tag.name)
    # 结果
        # html
        # head
        # title
        # body
        # p
        # b
        # p
        # a
        # a
        # a
        # p

    print(soup.find_all(attrs={'id':True})) #找到 具有id属性的标签
    # [<p class="title" id="my p"><b class="boldest" id="bbb">The Dormouse's story</b></p>, 
    # <b class="boldest" id="bbb">The Dormouse's story</b>, 
    # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, 
    # <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, 
    # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

    print(soup.find_all(name='p',attrs={'id':True})) #找到 具有id属性的p标签
    # [<p class="title" id="my p"><b class="boldest" id="bbb">The Dormouse's story</b></p>]

    #1.5、方法:如果没有合适过滤器,那么还可以定义一个方法,方法只接受一个元素参数 ,
    # 如果这个方法返回 True 表示当前元素匹配并且被找到,如果不是则反回 False
    def has_class_but_no_id(tag):
        return tag.has_attr('class') and not tag.has_attr('id')

    print(soup.find_all(name=has_class_but_no_id)) #在find_all(func)只传递函数名即可
    # 结果
        # [<p class="story">Once upon a time there were three little sisters; and their names were
            # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
            # <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
            # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
            # and they lived at the bottom of a well.</p>, 
        # <p class="story">...</p>]
   
    print(soup.find(name=has_class_but_no_id,text=re.compile('\.')))#从has_class_but_no_id标签中，过滤出文本包含'.'的标签。
    # <p class="story">...</p>


    #2、find_all( name , attrs , recursive , text , **kwargs )
    #2.1、name: 搜索name参数的值可以使任一类型的 过滤器 ,字符窜,正则表达式,列表,方法或是 True .
    print(soup.find_all(name=re.compile('^t'))) # [<title>The Dormouse's story</title>]

    #2.2、keyword: key=value的形式，value可以是过滤器：字符串 , 正则表达式 , 列表, True .
    print(soup.find_all(id=re.compile('my')))
    #  [<p class="title" id="my p"><b class="boldest" id="bbb">The Dormouse's story</b></p>]

    print(soup.find_all(href=re.compile('lacie'),id=re.compile('\d'))) #注意类要用class_
    # [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]


    print(soup.find_all(id=True)) #查找有id属性的标签
    #  [<p class="title" id="my p"><b class="boldest" id="bbb">The Dormouse's story</b>
    # </p>, <b class="boldest" id="bbb">The Dormouse's story</b>, <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
   

    # 有些tag属性在搜索不能使用,比如HTML5中的 data-* 属性:
    data_soup = BeautifulSoup('<div data-foo="value">foo!</div>','lxml')

    # data_soup.find_all(data-foo="value") #报错：SyntaxError: keyword can't be an expression
    # 但是可以通过 find_all() 方法的 attrs 参数定义一个字典参数来搜索包含特殊属性的tag:
    print(data_soup.find_all(attrs={"data-foo": "value"}))
    # [<div data-foo="value">foo!</div>]

    #2.3、按照类名查找，注意关键字是class_，class_=value,value可以是五种选择器之一
    print(soup.find_all('a',class_='sister')) #查找类为sister的a标签
    print(soup.find_all('a',class_='sister ssss')) #查找类为sister和sss的a标签，顺序错误也匹配不成功
    print(soup.find_all(class_=re.compile('^sis'))) #查找类为sister的所有标签
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, 
    # <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, 
    # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
    # []
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, 
    # <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, 
    # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

    #2.4、attrs
    print(soup.find_all('p',attrs={'class':'story'}))
    # [<p class="story">Once upon a time there were three little sisters; and their names were
    # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    # <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
    # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
    # and they lived at the bottom of a well.</p>, <p class="story">...</p>]

    #2.5、text: 值可以是：字符，列表，True，正则
    print(soup.find_all(text='Elsie'))
    print(soup.find_all('a',text='Elsie'))
    # ['Elsie']
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

    #2.6、limit参数:如果文档树很大那么搜索会很慢.如果我们不需要全部结果,可以使用 limit 参数限制返回结果的数量.效果与SQL中的limit关键字类似,当搜索到的结果数量达到 limit 的限制时,就停止搜索返回结果
    print(soup.find_all('a',limit=2))
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, 
    # <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>] 

    #2.7、recursive:调用tag的 find_all() 方法时,Beautiful Soup会检索当前tag的所有子孙节点,
    # 如果只想搜索tag的直接子节点,可以使用参数 recursive=False .
    print(soup.html.find_all('a'))
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, 
    # <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, 
    # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
     
    print(soup.html.find_all('a',recursive=False)) #[]


    '''
    像调用 find_all() 一样调用tag
    find_all() 几乎是Beautiful Soup中最常用的搜索方法,所以我们定义了它的简写方法. 
    BeautifulSoup 对象和 tag 对象可以被当作一个方法来使用,这个方法的执行结果与调用这个对象的 find_all() 方法相同,下面两行代码是等价的:
    soup.find_all("a")
    soup("a")
    这两行代码也是等价的:
    soup.title.find_all(text=True)
    soup.title(text=True)
    '''
bs_find_all()

# 2.1.3 css 选择器： select
def bs_select():
    
    #该模块提供了select方法来支持css,详见官网:https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#id37
    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title">
        <b>The Dormouse's story</b>
        Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">
            <span>Elsie</span>
        </a>
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        <div class='panel-1'>
            <ul class='list' id='list-1'>
                <li class='element'>Foo</li>
                <li class='element'>Bar</li>
                <li class='element'>Jay</li>
            </ul>
            <ul class='list list-small' id='list-2'>
                <li class='element'><h1 class='yyyy'>Foo</h1></li>
                <li class='element xxx'>Bar</li>
                <li class='element'>Jay</li>
            </ul>
        </div>
        and they lived at the bottom of a well.
    </p>
    <p class="story">...</p>
    """
    
    soup=BeautifulSoup(html_doc,'lxml')

    #1、CSS选择器
    print(soup.p.select('.sister'))
    # [<a class="sister" href="http://example.com/elsie" id="link1"><span>Elsie</span></a>, 
    # <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, 
    # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

    print(soup.select('.sister span'))
    #  [<span>Elsie</span>]


    print(soup.select('#link1'))
    #  [<a class="sister" href="http://example.com/elsie" id="link1"><span>Elsie</span></a>]

    print(soup.select('#link1 span'))
    # [<span>Elsie</span>]

    print(soup.select('#list-2 .element.xxx'))
    # [<li class="element xxx">Bar</li>]

    print(soup.select('#list-2')[0].select('.element')) #可以一直select,但其实没必要,一条select就可以了
    # [<li class="element"><h1 class="yyyy">Foo</h1></li>, <li class="element xxx">Bar</li>, <li class="element">Jay</li>]

    # 2、获取属性
    print(soup.select('#list-2 h1')[0].attrs)
    # {'class': ['yyyy']}


    # 3、获取内容
    print(soup.select('#list-2 h1')[0].get_text())
    # Foo

# bs_select()

# 总结:
#1、推荐使用lxml解析库
#2、讲了三种选择器:标签选择器,find与find_all，css选择器
    # 1、标签选择器筛选功能弱,但是速度快
    # 2、建议使用find,find_all查询匹配单个结果或者多个结果
     
    # 3、如果对css选择器非常熟悉建议使用select

    # 4、三种选择器可以结合使用：
        # soup.p.find_all()
        # soup.p.select()
        # soup.find(name='p',class_='story').a  搜索文档树结合遍历文档数，查找该p标签下的第一个a标签。
#3、记住常用的获取属性attrs和文本值get_text()的方法

