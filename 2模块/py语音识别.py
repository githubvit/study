'''
python 语音识别
'''
# 
import speech_recognition as sr
# 创建识别器对象
r=sr.Recognizer()
# 引入本地要操作的文件 作为 要识别的源
# with sr.AudioFile(r"C:\Users\69598\Downloads\Video\paju5-bxw6n.wav") as source: #只能是wav格式 英文
with sr.AudioFile(r"C:\Users\69598\Downloads\Video\tt1.wav") as source: #中文
    # 如果音频文件有噪声，进行降噪处理，可以提高识别度 ,好像没什么大用, 
    # 默认会使用duration关键字参数来调整adjust_for_ambient_noise（）命令的时间分析范围，该参数单位为秒，默认为 1，现将此值降低到 0.5。
    # 提高识别精度，不然第1秒会丢失。
    r.adjust_for_ambient_noise(source,duration=0.5)
    # 声明一个音频对象audio 来自于识别器r录制的源 这样audio 这个转录后的音频对象就是我们要识别的源
    audio=r.record(source)

# 接下来的操作，为防止意外 使用try excepter

try:
    # 1. 打印识别后的文本 
    # print(r.recognize_google(audio)) # 来自识别器调用的谷歌的语音识别api的识别结果 要可以科学上网
    # print(r.recognize_bing(audio,key)) #也可以使用bing\IBM等的语音识别api的识别结果 要key
    
    # 可以离线识别的引擎 Sphinx是由美国卡内基梅隆大学开发的大词汇量、非特定人、连续英语语音识别系统。
    # print(r.recognize_sphinx(audio)) 

    print(r.recognize_sphinx(audio,language="zh-cn",show_all=True).__module__) # 指定中文 用show_all=True 返回所有可能的结果
    '''
    中文语音识别:
        下载语言包,解压,重命名包名和文件名,放入 'D:\pyj\st\venv\Lib\site-packages\speech_recognition\pocketsphinx-data\' 文件夹下 
        该文件夹下原来只有一个语言包:en-US,
        我们将下来的中文语言包重命名为:zh-cn,里面的文件和文件夹按照原来 en-US语言包 里面的文件夹和文件命名即可.
        进到zh-cn包重命名里面的一个文件夹和两个文件,参考如下.
        参考:
            下载地址：

            https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/

            选择： Mandarin->cmusphinx-zh-cn-5.2.tar.gz

            配置数据：

            复制代码
            cd py36asr/lib/python3.6/site-packages/speech_recognition/pocketsphinx-data/
            tar zxvf cmusphinx-zh-cn-5.2.tar.gz
            mv cmusphinx-zh-cn-5.2 zh-cn
            cd zh-cn
            mv zh_cn.cd_cont_5000 acoustic-model
            mv zh_cn.lm.bin language-model.lm.bin
            mv zh_cn.dic pronounciation-dictionary.dict
    '''
except sr.UnknownValueError : # 发现未识别的错误时
    print('Google 语音识别未能理解音频内容')

except sr.RequestError as e: # 发生请求故障，比如不能科学上网
    print(f'未能从 Google 语音识别服务器请求到结果；{e}') 

