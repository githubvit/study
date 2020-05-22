Python3 使用you-get,youtube-dl,ffmpeg 下载全网视频并剪切视频

lnmp技术爱好者

发布时间：03-1115:54
现在视频网站很多，我们看的视频也越来越多了。有时候看到某些视频的片段非常的不错，想要剪切下来的冲动的次数也越来越多。一个视频剪切倒还好，但是多个视频的情况下，就比较麻烦了。

所以本人用python写了个脚本，只需要以下两个步骤就可以按你所需要的下载并剪切视频：(需自己安装python3.6,ffmpeg,you-get,youtube-dl)

一：新建个url.txt文件


下载链接与剪切时间说明
二：python代码如下：


需要源码或者不懂的可以私信我
附上源码：

import youtube_dl

import os

import sys

import you_get

class GetItem(object):

    #使用you-get下载

    def download_you_get(self,url,key,s_time,e_time):

        output = str(key)+"_jq.mp4"

        res = os.system("you-get -o ./download/ -O "+key+" "+url)

        #使用ffmpeg剪切视频

        os.system("ffmpeg -i ./download/"+key+".mp4 -ss "+s_time+" -t "+e_time +" " + "D:\\rjaz\\python3\\app\\视频高清\\download\\"+output)

        os.system("del .\\download\\"+ key+".mp4")

        os.system("del .\download\*.xml")

        #使用youtube-dl下载

    def download_youtube_dl(self,url,key,s_time,e_time):

        output = str(key)+"_jq.mp4"

        os.system("youtube-dl -o ./download_dl/"+key+".mp4 "+url)

        #使用ffmpeg剪切视频

        os.system("ffmpeg -i ./download_dl/"+key+".mp4 -ss "+s_time+" -t "+e_time +" " + "D:\\rjaz\\python3\\app\\视频高清\\download_dl\\"+output)

        os.system("del .\\download_dl\\"+ key+".mp4")

if __name__ == '__main__':

    getItem = GetItem()

    file=open('url.txt','r')

    line = file.readlines()

    i=0

    for res in line:

        s_time = str(res.split(',')[1])

        e_time = str(res.split(',')[2].replace('\n', ''))

        type = int(res.split(',')[3].replace('\n', ''))

        if type==1:
        
            getItem.download_youtube_dl(res.split(',')[0],str(i),s_time,e_time)

        else:

            getItem.download_you_get(res.split(',')[0],str(i),s_time,e_time)

        i+=1


# you-get 使用命令行
C:\Users\69598>you-get -o F:\video https://www.bilibili.com/video/BV19441127ba?p=209
you-get: This is a multipart video. (use --playlist to download all parts.)
site:                Bilibili
title:               人教版 初中数学 (P209. 第74讲 代数综合)
stream:
    - format:        flv720
      container:     flv
      quality:       高清 720P
      size:          135.3 MiB (141828457 bytes)
    # download-with: you-get --format=flv720 [URL]

Downloading 人教版 初中数学 (P209. 第74讲 代数综合).flv ...
10.5% ( 14.2/135.3MB) ├█████───────────────────────────────────┤[1/1]  102 kB/s

# youtub-dl 使用命令行
C:\Users\69598>youtube-dl -o 'F:\\video' https://www.bilibili.com/video/BV19441127ba?p=203
[BiliBili] 19441127ba: Downloading webpage
[BiliBili] 19441127ba: Downloading video info page
[download] Destination: 'F#\video'
[download]  47.2% of 139.71MiB at 130.31KiB/s ETA 09:40

在当前目录下产生目录 'F# 点开后里面有个文件叫 video'