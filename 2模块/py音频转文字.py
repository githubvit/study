'''
python 音频转文字模块


speech

    使用微软开发的win10自带的语音接口SAPI，实现文字转音频。
    SAPI是微软Speech API , 是微软公司推出的语音接口，
    文章：
        1. python之语音识别（speech模块） 
        https://www.cnblogs.com/uniquefu/p/9336793.html

        2. 说说python自带的speech和speech_recognition的使用以及效果 
        https://www.cnblogs.com/zhe-hello/p/13273523.html

        3. 微软SAPI（The Microsoft Speech API）：让你的软件能说会道
        http://www.jizhuomi.com/software/614.html

    安装
        pip install speech 

    示例
        import speech

        #这边三行是自己会说话
        speech.say("小王王 你好呀")
        speech.say("hello world")
        speech.say("要开始啦")

    报错及修改源文件 speech.py
    1. 修改源文件：年代原因 py2 使用 print 和 py3 不同，加()
        (venv) D:\pyj\st\study>d:/pyj/st/venv/Scripts/python.exe d:/pyj/st/study/2模块/py音频转文字.py
        Traceback (most recent call last):
          File "d:/pyj/st/study/2模块/py音频转文字.py", line 6, in <module>
            import speech
          File "d:\pyj\st\venv\lib\site-packages\speech.py", line 157
            print prompt
                       ^
        SyntaxError: Missing parentheses in call to 'print'. Did you mean print(prompt)?

        修改为 print(prompt)

    2. 安装模块：win32com 模块没装 

        (venv) D:\pyj\st\study>d:/pyj/st/venv/Scripts/python.exe d:/pyj/st/study/2模块/py音频转文字.py
        Traceback (most recent call last):
          File "d:/pyj/st/study/2模块/py音频转文字.py", line 6, in <module>
            import speech
          File "d:\pyj\st\venv\lib\site-packages\speech.py", line 55, in <module>
            from win32com.client import constants as _constants
        ModuleNotFoundError: No module named 'win32com'

        安装win32com 包名 pyWin32  :
            pip install pyWin32 -i https://pypi.doubanio.com/simple/

    3. 修改源文件：py2的线程包名 thread 在 py3 包名改为threading 
        
            原来的写法： import thread          改为            import threading

    4. 修改源文件：最后一行修改：      
            原来的写法： _eventthread = thread.start_new_thread(loop, ()) 
                改为：   _eventthread = threading._start_new_thread(loop, ())

    5. 安装模块：安装pythoncom模块
        pip install pythoncom -i https://pypi.doubanio.com/simple/  

    6. 过程：

        (venv) D:\pyj\st\study>pip install win32com -i https://pypi.doubanio.com/simple/
        Looking in indexes: https://pypi.doubanio.com/simple/
        ERROR: Could not find a version that satisfies the requirement win32com (from versions: none)
        ERROR: No matching distribution found for win32com
        WARNING: You are using pip version 20.2.4; however, version 21.0.1 is available.
        You should consider upgrading via the 'd:\pyj\st\venv\scripts\python.exe -m pip install --upgrade pip' command.

        (venv) D:\pyj\st\study>pip install win32com                                     
        ERROR: Could not find a version that satisfies the requirement win32com (from versions: none)
        ERROR: No matching distribution found for win32com
        WARNING: You are using pip version 20.2.4; however, version 21.0.1 is available.
        You should consider upgrading via the 'd:\pyj\st\venv\scripts\python.exe -m pip install --upgrade pip' command.

        (venv) D:\pyj\st\study>
        Looking in indexes: https://pypi.doubanio.com/simple/
        Collecting pyWin32
        Downloading https://pypi.doubanio.com/packages/25/54/177ee28fec4ecd23fa539f3df78067e7a4927515b84eac34e36060fcdb8d/pywin32-300-cp37-cp37m-win_amd64.whl (9.2 MB)
            |████████████████████████████████| 9.2 MB 3.3 MB/s
        Installing collected packages: pyWin32
        Successfully installed pyWin32-300
        WARNING: You are using pip version 20.2.4; however, version 21.0.1 is available.
        You should consider upgrading via the 'd:\pyj\st\venv\scripts\python.exe -m pip install --upgrade pip' command.

        (venv) D:\pyj\st\study>d:/pyj/st/venv/Scripts/python.exe d:/pyj/st/study/2模块/py音频转文字.py
        Traceback (most recent call last):
        File "d:/pyj/st/study/2模块/py音频转文字.py", line 6, in <module>
            import speech
        File "d:\pyj\st\venv\lib\site-packages\speech.py", line 59, in <module>
            import thread
        ModuleNotFoundError: No module named 'thread'

        (venv) D:\pyj\st\study>pip install thread -i https://pypi.doubanio.com/simple/
        Looking in indexes: https://pypi.doubanio.com/simple/
        ERROR: Could not find a version that satisfies the requirement thread (from versions: none)
        ERROR: No matching distribution found for thread
        WARNING: You are using pip version 20.2.4; however, version 21.0.1 is available.
        You should consider upgrading via the 'd:\pyj\st\venv\scripts\python.exe -m pip install --upgrade pip' command.

        (venv) D:\pyj\st\study>pip install pythoncom -i https://pypi.doubanio.com/simple/
        Looking in indexes: https://pypi.doubanio.com/simple/
        ERROR: Could not find a version that satisfies the requirement pythoncom (from versions: none)
        ERROR: No matching distribution found for pythoncom
        WARNING: You are using pip version 20.2.4; however, version 21.0.1 is available.
        You should consider upgrading via the 'd:\pyj\st\venv\scripts\python.exe -m pip install --upgrade pip' command.

        (venv) D:\pyj\st\study>d:/pyj/st/venv/Scripts/python.exe d:/pyj/st/study/2模块/py音频转文字.py

        (venv) D:\pyj\st\study>


SpeechRecognition-3.8.1
'''
import speech

def 文字转语音():
    
    speech.say("小王王 你好呀")
    speech.say("hello world")
    speech.say("要开始啦")
    speech.say("Hello students, my name is Brian Stewart.")
    speech.say("I will be your teacher for today. Today, we're going over part one in our textbook, Life science 。and specifically，we will be talking about the parts of plants. If you think about it, plants are all around us, aren't they? We use plants for many things. We use plants for food. We use plants for shelter.")
while True:
    print("开始说话")
    say = speech.input()  # 接收语音
    speech.say("you said:" + say)  # 说话
    print(u"说话结束")
    if say == "你好":
        speech.say("How are you?")
    elif say == "天气":
        speech.say("今天天气棒棒棒!")
    elif say == "小王王":
        speech.say("小王王 棒棒棒")
    elif say == "小丽平":
        speech.say("小丽平 六六六")
    else:
        speech.say("对不起 我不知道你说什么")
'''   
speech.say("Say something.")

print("You said:")
var=speech.input()

# 两个回调
def L1callback(phrase, listener):
    print(phrase)

def L2callback(phrase, listener):
    if phrase == "wow":
        listener.stoplistening()
    speech.say(phrase)

# callbacks are executed on a separate events thread. 回调在单独的事件线程上执行。
L1 = speech.listenfor(["hello", "good bye"], L1callback) #命令模式
L2 = speech.listenforanything(L2callback) #听写模式

assert speech.islistening() #系统的侦听状态
assert L2.islistening() # L2侦听器的侦听状态

L1.stoplistening()
assert not L1.islistening()

speech.stoplistening()
'''