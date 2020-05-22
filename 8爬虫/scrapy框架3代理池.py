# 动态代理池 jhao104
为了防止爬取过程的ip被封，一般都会使用代理池，常用的开源代理池软件：
        jhao104/proxy_pool https://github.com/jhao104/proxy_pool

加代理一般都是在下载中间件加，这样就都加了，如果代理失败会抛异常：
    在中间件处理异常的时候，就把该代理从代理池删除，同时，从代理池找出一个新代理，如此往复。

# 下载、解压到项目目录、安装依赖
    # 下载
    git clone git@github.com:jhao104/proxy_pool.git

    或者直接到https://github.com/jhao104/proxy_pool/releases 下载zip文件
    
    # 解压到项目所在目录，即需要代理的项目目录下。

    # 安装依赖
    在解压目录下安装依赖
    pip install -r requirements.txt # -r 表示读requirements.txt文件的结果

    两次报超时后，翻墙，安装成功：

        D:\pyj\st\study\8爬虫\AMAZON\proxy_pool-master>pip3 install -r requirements.txt
        Collecting APScheduler==3.2.0
          Using cached APScheduler-3.2.0-py2.py3-none-any.whl (52 kB)
        Collecting werkzeug==0.15.3
          Using cached Werkzeug-0.15.3-py2.py3-none-any.whl (327 kB)
        Collecting Flask==1.0
          Using cached Flask-1.0-py2.py3-none-any.whl (97 kB)
        Collecting requests==2.20.0
          Using cached requests-2.20.0-py2.py3-none-any.whl (60 kB)
        Collecting lxml==4.4.2
          Downloading lxml-4.4.2-cp37-cp37m-win_amd64.whl (3.7 MB)
             |████████████████████████████████| 3.7 MB 364 kB/s
        Collecting PyExecJS==1.5.1
          Downloading PyExecJS-1.5.1.tar.gz (13 kB)
        Requirement already satisfied: click==7.0 in d:\anaconda3\lib\site-packages (from -r requirements.txt (line 7)) 
        (7.0)
        Collecting gunicorn==19.9.0
          Downloading gunicorn-19.9.0-py2.py3-none-any.whl (112 kB)
             |████████████████████████████████| 112 kB 149 kB/s
        Requirement already satisfied: pymongo in d:\anaconda3\lib\site-packages (from -r requirements.txt (line 9)) (3.10.1)
        Collecting redis
          Downloading redis-3.4.1-py2.py3-none-any.whl (71 kB)
             |████████████████████████████████| 71 kB 351 kB/s
        Requirement already satisfied: six>=1.4.0 in c:\users\69598\appdata\roaming\python\python37\site-packages (from 
        APScheduler==3.2.0->-r requirements.txt (line 1)) (1.13.0)
        Requirement already satisfied: pytz in d:\anaconda3\lib\site-packages (from APScheduler==3.2.0->-r requirements.txt (line 1)) (2019.3)
        Requirement already satisfied: setuptools>=0.7 in d:\anaconda3\lib\site-packages (from APScheduler==3.2.0->-r requirements.txt (line 1)) (41.4.0)
        Collecting tzlocal>=1.2
          Downloading tzlocal-2.0.0-py2.py3-none-any.whl (15 kB)
        Requirement already satisfied: itsdangerous>=0.24 in d:\anaconda3\lib\site-packages (from Flask==1.0->-r requirements.txt (line 3)) (1.1.0)
        Requirement already satisfied: Jinja2>=2.10 in d:\anaconda3\lib\site-packages (from Flask==1.0->-r requirements.txt (line 3)) (2.10.3)
        Requirement already satisfied: certifi>=2017.4.17 in d:\anaconda3\lib\site-packages (from requests==2.20.0->-r requirements.txt (line 4)) (2019.9.11)
        Requirement already satisfied: urllib3<1.25,>=1.21.1 in d:\anaconda3\lib\site-packages (from requests==2.20.0->-r requirements.txt (line 4)) (1.24.2)
        Collecting idna<2.8,>=2.5
          Downloading idna-2.7-py2.py3-none-any.whl (58 kB)
             |████████████████████████████████| 58 kB 292 kB/s
        Requirement already satisfied: chardet<3.1.0,>=3.0.2 in d:\anaconda3\lib\site-packages (from requests==2.20.0->-r requirements.txt (line 4)) (3.0.4)
        Requirement already satisfied: MarkupSafe>=0.23 in d:\anaconda3\lib\site-packages (from Jinja2>=2.10->Flask==1.0->-r requirements.txt (line 3)) (1.1.1)
        Building wheels for collected packages: PyExecJS
          Building wheel for PyExecJS (setup.py) ... done
          Created wheel for PyExecJS: filename=PyExecJS-1.5.1-py3-none-any.whl size=14594 sha256=7700865478b96b6023d756b5c71316630e1a89ef48c95e189d783dcf69a07562
          Stored in directory: c:\users\69598\appdata\local\pip\cache\wheels\9a\ee\03\da5c0b4a8c13362beeb844eb913bbe58a89bde1de2b9157007
        Successfully built PyExecJS
        Installing collected packages: tzlocal, APScheduler, werkzeug, Flask, idna, requests, lxml, PyExecJS, gunicorn, 
        redis
          Attempting uninstall: werkzeug
            Found existing installation: Werkzeug 0.16.0
            Uninstalling Werkzeug-0.16.0:
              Successfully uninstalled Werkzeug-0.16.0
          Attempting uninstall: Flask
            Found existing installation: Flask 1.1.1
            Uninstalling Flask-1.1.1:
              Successfully uninstalled Flask-1.1.1
          Attempting uninstall: idna
            Found existing installation: idna 2.8
            Uninstalling idna-2.8:
              Successfully uninstalled idna-2.8
          Attempting uninstall: requests
            Found existing installation: requests 2.22.0
            Uninstalling requests-2.22.0:
              Successfully uninstalled requests-2.22.0
          Attempting uninstall: lxml
            Found existing installation: lxml 4.4.1
            Uninstalling lxml-4.4.1:
              Successfully uninstalled lxml-4.4.1
        Successfully installed APScheduler-3.2.0 Flask-1.0 PyExecJS-1.5.1 gunicorn-19.9.0 idna-2.7 lxml-4.4.2 redis-3.4.1 requests-2.20.0 tzlocal-2.0.0 werkzeug-0.15.3

# 修改配置Config/setting.py
    # 1 修改数据库配置
    DB_TYPE = getenv('db_type', 'MONGODB').upper()
    DB_HOST = getenv('db_host', '127.0.0.1')
    DB_PORT = getenv('db_port', 27017)
    DB_PASSWORD = getenv('db_password', '')
    # 2 修改DB目录下 MongdbClient.py
    self.client = MongoClient(f'mongodb://{username}:{pwd}@{host}:{port}')


# 代理池干了哪些事

1 从代理网站爬取代理网址，放到数据库中，形成初始代理表。
    目前实现的采集免费代理网站有(排名不分先后, 下面仅是对其发布的免费代理情况:

    厂商名称	    状态	更新速度	可用率	是否被墙	地址
    无忧代理	    可用	几分钟一次	*	否	地址        http://www.data5u.com/free/index.html
    66代理	        可用	更新很慢	*	否	地址        http://www.66ip.cn/
    西刺代理	    可用	几分钟一次	*	否	地址        http://www.xicidaili.com/
    全网代理	    可用	几分钟一次	*	否	地址        http://www.goubanjia.com/
    训代理	        已关闭免费代理	*	*	否	地址        http://www.xdaili.cn/
    快代理	        可用	几分钟一次	*	否	地址        https://www.kuaidaili.com/
    云代理	        可用	几分钟一次	*	否	地址        https://www.kuaidaili.com/
    IP海	        可用	几小时一次	*	否	地址        http://www.ip3366.net/
    免费IP代理库	 可用	    快	    *	否	地址        http://ip.jiangxianli.com/
    中国IP地址	    可用	几分钟一次	*	是	地址        http://cn-proxy.com/
    Proxy List	    可用	几分钟一次	*	是	地址       https://proxy-list.org/chinese/index.php
    ProxyList+	    可用	几分钟一次	*	是	地址       https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-1

    如果还有其他好的免费代理网站, 可以在提交在issues, 下次更新时会考虑在项目中支持。

2 用这些网址向常用的百度、新浪等发请求，成功了，就放到代理成功的表中。
3 从成功的代理表中取出地址进行交给需要代理的api。

# 代理池结构

1 应该要有存放地址的数据库，在config.ini文件中配置
