#_*_coding:utf-8_*_
'''

'''
'''
WSGI（Web Server Gateway Interface）是一种规范，
它定义了使用python编写的web app与web server之间接口格式，
实现web app与web server间的解耦。
python标准库提供的独立WSGI服务器称为wsgiref。

'''
from wsgiref.simple_server import make_server

def RunServer(environ, start_response):
    # environ 客户端以字典形式发过来的所有数据
    # start response 服务端返回给客户端响应头的数据和状态码
    start_response('200 OK', [('Content-Type', 'text/html')])
    # return 才是返回给客户端的内容
    # return [bytes('<h1>Hello, web!</h1>', encoding='utf-8'), ]#这是py3的处理，要用bytes类型
    return '<h1>Hello, web!</h1>'#这是py2.7的处理



if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)#启动socket服务 （ip、端口、处理方法）
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()



'''
# n = 1
# for i in environ:
#     print n,' ',i,'--',environ[i]
#     n+=1

environ参数信息

1   TMP -- C:\Users\hp\AppData\Local\Temp
2   PYTHONIOENCODING -- UTF-8
3   COMPUTERNAME -- GQ123
4   wsgi.multiprocess -- False
5   HTTP_REFERER -- http://127.0.0.1:8000/
6   USERDOMAIN -- GQ123
7   wsgi.multithread -- True
8   SERVER_PROTOCOL -- HTTP/1.1
9   SERVER_SOFTWARE -- WSGIServer/0.1 Python/2.7.13
10   PSMODULEPATH -- C:\Program Files\WindowsPowerShell\Modules;C:\WINDOWS\system32\WindowsPowerShell\v1.0\Modules
11   SCRIPT_NAME -- 
12   COMMONPROGRAMFILES -- C:\Program Files\Common Files
13   PROCESSOR_IDENTIFIER -- Intel64 Family 6 Model 58 Stepping 9, GenuineIntel
14   REQUEST_METHOD -- GET
15   PROGRAMFILES -- C:\Program Files
16   PROCESSOR_REVISION -- 3a09
17   MAVEN_HOME -- F:\java\apache-maven-3.3.9
18   QUERY_STRING -- 
19   SYSTEMROOT -- C:\WINDOWS
20   PYTHONUNBUFFERED -- 1
21   PROGRAMFILES(X86) -- C:\Program Files (x86)
22   CONTENT_LENGTH -- 
23   HTTP_USER_AGENT -- Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
24   HTTP_CONNECTION -- keep-alive
25   TEMP -- C:\Users\hp\AppData\Local\Temp
26   REMOTE_ADDR -- 127.0.0.1
27   WINDIR -- C:\WINDOWS
28   COMMONPROGRAMFILES(X86) -- C:\Program Files (x86)\Common Files
29   PROCESSOR_ARCHITECTURE -- AMD64
30   CATALINA_HOME -- F:\apache-tomcat-7.0.77
31   wsgi.url_scheme -- http
32   ALLUSERSPROFILE -- C:\ProgramData
33   SERVER_PORT -- 8000
34   LOCALAPPDATA -- C:\Users\hp\AppData\Local
35   FPS_BROWSER_USER_PROFILE_STRING -- Default
36   HOMEPATH -- \Users\hp
37   USERDOMAIN_ROAMINGPROFILE -- GQ123
38   M2_HOME -- F:\java\apache-maven-3.3.9
39   JAVA_HOME -- F:\Program Files\Java\jdk1.8.0_121
40   ERLANG_HOME -- F:\Program Files\erl9.1
41   USERNAME -- hp
42   MYSQL_HOME -- F:\Program Files\MySQL\MySQL Server 8.0
43   LOGONSERVER -- \\GQ123
44   COMSPEC -- C:\WINDOWS\system32\cmd.exe
45   PROGRAMDATA -- C:\ProgramData
46   PYTHONPATH -- D:\wksp1\pcy1
47   CLASSPATH -- .;F:\Program Files\Java\jdk1.8.0_121\lib\dt.jar;F:\Program Files\Java\jdk1.8.0_121\lib\tools.jar;
48   PATH -- F:\ProgramData\Anaconda2\Library\bin;F:\Program Files\erl9.1\bin;f:\ProgramData\Anaconda2;f:\ProgramData\Anaconda2\Library\mingw-w64\bin;f:\ProgramData\Anaconda2\Library\usr\bin;f:\ProgramData\Anaconda2\Library\bin;f:\ProgramData\Anaconda2\Scripts;C:\Python27\;C:\Python27\Scripts\;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;F:\Program Files\Java\jdk1.8.0_121\bin;F:\Program Files\Java\jdk1.8.0_121\jre\bin;F:\java\apache-maven-3.3.9\bin\;F:\java\apache-maven-3.3.9\bin\;F:\Program Files\MySQL\MySQL Server 8.0\bin;C:\Users\hp\AppData\Local\Programs\Python\Python36-32\Scripts\;C:\Users\hp\AppData\Local\Programs\Python\Python36-32\;C:\Users\hp\AppData\Local\Microsoft\WindowsApps;c:\ffmpeg\bin;C:\Program Files (x86)\Google\google_appengine\;
49   wsgi.input -- <socket._fileobject object at 0x0000000004D92408>
50   wsgi.errors -- <open file '<stderr>', mode 'w' at 0x000000000457B150>
51   HTTP_HOST -- 127.0.0.1:8000
52   SESSIONNAME -- Console
53   PATHEXT -- .COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC
54   PATH_INFO -- /favicon.ico
55   HTTP_ACCEPT -- images/webp,images/*,*/*;q=0.8
56   FPS_BROWSER_APP_PROFILE_STRING -- Internet Explorer
57   wsgi.file_wrapper -- wsgiref.util.FileWrapper
58   HTTP_ACCEPT_ENCODING -- gzip, deflate, sdch, br
59   wsgi.version -- (1, 0)
60   MOZ_PLUGIN_PATH -- F:\Program Files (x86)\Foxit Software\Foxit Reader\plugins\
61   HOMEDRIVE -- C:
62   SERVER_NAME -- gq123
63   wsgi.run_once -- False
64   REMOTE_HOST -- gq123
65   SYSTEMDRIVE -- C:
66   GATEWAY_INTERFACE -- CGI/1.1
67   HTTP_ACCEPT_LANGUAGE -- zh-CN,zh;q=0.8
68   PYCHARM_HOSTED -- 1
69   NUMBER_OF_PROCESSORS -- 4
70   APPDATA -- C:\Users\hp\AppData\Roaming
71   PROCESSOR_LEVEL -- 6
72   PROGRAMW6432 -- C:\Program Files
73   CONTENT_TYPE -- text/plain
74   ONEDRIVE -- C:\Users\hp\OneDrive
75   COMMONPROGRAMW6432 -- C:\Program Files\Common Files
76   OS -- Windows_NT
77   PUBLIC -- C:\Users\Public
78   USERPROFILE -- C:\Users\hp
'''