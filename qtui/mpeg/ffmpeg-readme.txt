一 音视频基础

    1. FFmpeg简介
    
        FFmpeg的名称来自MPEG视频编码标准，前面的“FF”代表“Fast Forward”，

        FFmpeg是一套可以用来记录、转换数字音频、视频，并能将其转化为流的开源计算机程序。可以轻易地实现多种视频格式之间的相互转换

        FFmpeg的用户有Google，Facebook，Youtube，优酷，爱奇艺，土豆等


    2. 基础知识

        容器/文件(Conainer/File)：即特定格式的多媒体文件，比如mp4、flv、mkv等。

        媒体流（Stream）：表示时间轴上的一段连续数据，如一段声音数据、一段视频数据或一段字幕数据，

            可以是压缩的，也可以是非压缩的，压缩的数据需要关联特定的编解码器。

        数据帧/数据包(Frame/Packet)：通常，一个媒体流是由大量的数据帧组成的，对于压缩数据，

            帧对应着编解码器的最小处理单元，分属于不同媒体流的数据帧交错存储于容器之中。

        编码格式：视频和音频都需要经过编码，才能保存成文件。
            
            不同的编码格式（CODEC），有不同的压缩率，会导致文件大小和清晰度的差异。
            
            常用的视频编码格式H.262、H.264、H.265，上面的编码格式都是有版权的，但是可以免费使用。
            
            此外，还有几种无版权的视频编码格式VP8、VP9、AV1。
            
            常用的音频编码格式MP3、AAC等。

        编码器：编码器（encoders）是实现某种编码格式的库文件。
            
            只有安装了某种格式的编码器，才能实现该格式视频/音频的编码和解码。

            以下是一些 FFmpeg 内置的视频编码器：

                
                libx264：最流行的开源 H.264 编码器
                
                NVENC：基于 NVIDIA GPU 的 H.264 编码器
                
                libx265：开源的 HEVC 编码器
                
                libvpx：谷歌的 VP8 和 VP9 编码器
                
                libaom：AVI 编码器
                
            音频编码器如下：

                libfdk-aac
                
                aac
 


    3. 一般情况下：

        Frame对应压缩前的数据，Packet对应压缩后的数据。

        编解码器(Codec)：以帧为单位实现压缩数据和原始数据之间的相互转换的

        复用(mux)：把不同的流按照某种容器的规则放入容器，这种行为叫做复用（mux）

        解复用(mux)：把不同的流从某种容器中解析出来，这种行为叫做解复用(demux)


    4. 基础知识-解复用器

        复用(mux)：把不同的流按照某种容器的规则放入容器，这种行为叫做复用（mux）

            复用器muxer比如MP4/FLV

            ---------
            | 视频流 |----- 
            ---------      |
            | 音频流 |-----      ------------------------------       ----------------------------
            ---------      |----| 按容器规则（MP4\FLV...）组合 |-------| 封装成视频文件（mp4或flv等）|
            | 字幕流 |-----      ------------------------------       ----------------------------
            ---------      |
            | 其他流 |-----
            ---------       

        解复用(mux)：把不同的流从某种容器中解析出来，这种行为叫做解复用(demux)

            解复用器demuxer MP4/FLV
                                                                    ---------
                                                               -----| 视频流 |
                                                               |    --------- 
            ------------------------      ---------------      -----| 音频流 |
            | 视频文件（mp4或flv等）|------| 按容器规则拆分|------|     --------- 
            ------------------------      ---------------      -----| 字幕流 |
                                                               |    --------- 
                                                               -----| 其他流 |
                                                                    ---------     


    5. 基础知识-编解码器codec
    
        编解码器(Codec)：以帧为单位实现压缩数据和原始数据之间的相互转换的

        视频编解码器
                                    H264编码器
                        ---------------->>-------------
                        |                              | 
                ---------------                   -----------
                |  图像YUV数据 |                   |  H264帧 |
                ---------------                   -----------  
                        |                              | 
                        ----------------<<-------------
                                    H264解码器

        音频编解码器
                                    AAC编码器
                        ---------------->>-------------
                        |                              | 
                ---------------                   ----------
                |  声音PCM数据 |                   |  AAC帧 |
                ---------------                   ----------  
                        |                              | 
                        ----------------<<-------------
                                    AAC解码器


    6. 基础知识-码率和帧率

        码率和帧率是视频文件的最重要的基本特征，对于他们的特有设置会决定视频质量。

        如果我们知道码率和时长那么可以很容易计算出输出文件的大小。

        帧率：
            帧率也叫帧频率，帧率是视频文件中每一秒的帧数，肉眼想看到连续移动图像至少需要15帧。

        码率：
            比特率(也叫码率，数据率)是一个确定整体视频/音频质量的参数，秒为单位处理的位数，码率和视频质量成正比，

        在视频文件中中比特率用bps来表达。

二 ffmpeg 常用命令

    ffmpeg -formats     查看 FFmpeg 支持的容器格式

    ffmpeg -codecs      查看 FFmpeg 支持的编码格式

    ffmpeg -encoders    查看 FFmpeg 已安装的编码器

    ffmpeg -i 输入文件名（如果文件名有空格就要用引号，因为命令行是以空格作为分隔符的）

    FFmpeg 的使用格式

        FFmpeg 的命令行参数非常多，可以分成五个部分。

        $ffmpeg {1} {2} -i {3} {4} {5}

        上面命令中，五个部分的参数依次如下。

            1 全局参数
            2 输入文件参数
            3 输入文件
            4 输出文件参数
            5 输出文件

        参数太多的时候，为了便于查看，ffmpeg 命令可以写成多行。

            $ ffmpeg \
            [全局参数] \
            [输入文件参数] \
            -i [输入文件] \
            [输出文件参数] \
            [输出文件]

        下面是一个例子：
            $ ffmpeg \
            -y \ # 全局参数
            -c:a libfdk_aac -c:v libx264 \ # 输入文件参数
            -i input.mp4 \ # 输入文件
            -c:v libvpx-vp9 -c:a libvorbis \ # 输出文件参数
            output.webm # 输出文件

        上面的命令将 mp4 文件转成 webm 文件，这两个都是容器格式。
        输入的 mp4 文件的音频编码格式是 aac，视频编码格式是 H.264；
        输出的 webm 文件的视频编码格式是 VP9，音频格式是 Vorbis。

        如果不指明编码格式，FFmpeg 会自己判断输入文件的编码。
        因此，上面的命令可以简单写成下面的样子：
            $ ffmpeg -i input.avi output.mp4

三、常用命令行参数

    FFmpeg 常用的命令行参数如下。
        
        -c：指定编码器
        
        -c copy：直接复制，不经过重新编码（这样比较快）
        
        -c:v：指定视频编码器
        
        -c:a：指定音频编码器
        
        -i：指定输入文件
        
        -an：去除音频流
        
        -vn： 去除视频流
        
        -preset：指定输出的视频质量，会影响文件的生成速度，
                有以下几个可用的值 ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow。
        
        -y：不经过确认，输出时直接覆盖同名文件。


        来自其他：
            一、主要参数
                ◼ -i 设定输入流
                ◼ -f 设定输出格式(format)
                ◼ -ss 开始时间
                ◼ -t 时间长度

            二、音频参数：
                ◼ -aframes 设置要输出的音频帧数
                ◼ -b:a 音频码率  为了保证音频质量 通常单声道的码率为64k，所以立体声就应为128k
                ◼ -ar 设定采样率
                ◼ -ac 设定声音的Channel数 声道 -ac 1 单声道 人声用单声道就够了， -ac 2 立体声
                ◼ -c:a  设定声音编解码器，如果用copy表示原始编解码数据必须被拷贝。
                ◼ -an 去除音频
                ◼ -af 音频过滤器

            三、视频参数：
                ◼ -vframes 设置要输出的视频帧数
                ◼ -b 设定视频码率
                ◼ -b:v 视频码率
                ◼ -r 设定帧速率
                ◼ -s 设定画面的宽与高
                ◼ -vn 去除视频
                ◼ -aspect aspect 设置横纵比 4:3 16:9 或 1.3333 1.7777
                ◼ -vcodec 设定视频编解码器，如果用copy表示原始编解码数据必须被拷贝。
                ◼ -vf 视频过滤器 滤镜 有上百种 比如 裁剪画面 缩放画面

        文件信息代表的意义：
            tbr代表帧率，每秒多少帧；
            tbn代表文件层（st）的时间精度，比如 1200k tbn，即1S=1200k，和duration相关；
            tbc代表视频层（st->codec）的时间精度，比如 50 tbc，即1S=50，和strem->duration和时间戳相关
四、常见用法

    下面介绍 FFmpeg 几种常见用法。
    参考：https://www.youtube.com/channel/UCAxM536O_1ls-nNnO8I0HOA

        a. 把大体积的视频压小：
            节约存储、节约带宽

            如何科学的将视频压缩变小（尽量不损失画质）？
            实际上这个问题就是如何控制码率，选择编码器对应的压制方式？

            首先，要明白封装格式即容器格式（mkv\mp4\webm\flv....）和清晰度即画质无关,只是'杯子'而已。
                mkv复用器支持多种编码、多音轨、多字幕，所以用的非常多。

            其次，编码是对每一帧画面的进行的，现在提高压缩比，就是利用帧与帧间的变化来提高压缩率：
                
                I1 -> p1 -> B2-> I2 -> P2 -> B3 -> I3 ...
                
                I帧：帧内压缩，这一帧是完整记录的，就像一张完整的jpg图片。
                
                P帧：帧间压缩，这一帧是I帧的前面一帧，记录的是与I帧的变化，帧与帧相似度越高，压缩比就越高。
                
                B帧：帧间压缩，这一帧是I帧的后面一帧，即是记录与前一帧P帧的变化，也是记录与后一帧I帧的变化。
                    比如B2 即记录了与P1的变化，也记录了与I2的变化。 

                    I1 -> p1 -> B2-> I2 -> P2 -> B3 -> I3 ...

                GTX1660或更高的显卡，才支持这种高压缩比方式的压缩。


            要想压制高质量的视频：
                1.  片源质量要好; 

                2.  选用优秀的编码器如x264、x265;

                3.  新手一般会直接选择码率，用多了浪费，用少了变成渣画质，
                    而每部片子的复杂度不同，则采用的码率也不同。
                    比如固定机位拍摄的人物访谈，可能用1000kbps码率就可以获得好的观感，
                    而在森林中奔跑的视频，就是用3000kbps还是渣画质。
                    所以，我们不能想当然的用某个码率去压片。
                    而是应该给出预期的‘质量值’。
                    让程序自己决定用多少码率。
                    这样，既不浪费存储空间，节约带宽，又取得满意的画质，这才是最优解。

                4： 码率控制(bitrate control):
                    以x264编码器为例，有三种码率控制方式，这三种方法用了各自的‘码率分配方法’,
                    就象是分蛋糕，既可以平均分，也可以按照每个人的胃口大小来分，

                    第一种 bitrate模式：不推荐。除非你要精确控制体积
                        ABR(Average Biterate) 一次编码 码率振幅最小  无法了解整段视频的复杂度分布，因此会造成质量的不均衡。
                        2pass 二次编码  第一次 先了解整段视频的复杂度分布，第二次，会更合理额分配码率，在烈度高的地方用高码率，烈度低的地方用低码率。质量
                        .
                        .
                        npass

                        2pass转码耗时比ABR几乎翻倍。压制DVD高质量的视频可以用2pass，其余的pass没有必要。

                        -b:v 码率 比如 -b:v 9000k
    
                    第二种 QP模式(Constant QP)
                        是一个量化值，是软件认为的某种级别的画面质量。

                        -q:v 质量 比如 -q:v 17

                    第三种 CRF模式(Constant Rate Factor):比QP模式更省码率。*****
                        是在QP模式的基础上开发的，它降低了某些‘不太重要’的帧的质量，
                        因此，可以做到，QP模式和CRF模式取同一值，crf模式的体积要更小，并且两种模式的画质肉眼几乎看不出来。
                        crf默认的值是23，取值范围是0~51，值越小画质越高码率越高，体积越大。


                        注意：只能在x264 x265编码器中使用

                        -crf 17

                5.  x264 preset的值  预设的值 ：组合了一些对转码速度影响比较大的参数

                    越快：压缩比越低，越占用空间。

                    越慢：压缩比越高，节约空间，但是压制就耗时。

                    预设值列表

                        序	name	    名称	b-adapt	bframes	direct	me	    merange	partitions	rc-lookahead	ref	subme	trellis	weightp	other
                        
                        1	ultrafast	极快	0	    0	 	        dia	 	        none	    0	            1	0	    0	    0	    no-8x8dct aq-mode0 no-cabac no-deblock no-mbtree no-mixed-refs scenecut0 no-weightb
                        
                        2	superfast	超快	 	 	 	            dia	 	        i8x8,i4x4	0	            1	1	    0	    1	    no-mixed-refsno-mbtree
                        
                        3	veryfast	很快	 	 	 	 	 	 	                            10	            1	2	    0	    1	    no-mixed-refs
                        
                        4	faster	    较快	 	 	 	 	 	 	                            20	            2	4	 	        1	    no-mixed-refs
                        
                        5	fast	    快	 	 	 	 	 	 	                                30	            2	6	 	        1	 
                        
                        6	medium	    中	 	 	 	 	 	 	 	 	 	 	 	 
                        
                        7	slow	    慢	    2	 	        auto	umh	 	 	                50	            5	8	 	 	 
                        
                        8	slower	    较慢	2	 	        auto	umh	 	        all	        60	            8	9	    2	 	 
                        
                        9	veryslow	很慢	2	    8	    auto	umh	    24	    all	        60	            16	10	    2	 	 
                        
                        10	placebo	 	        2	    16	    auto	tesa	24	    all	        60	            16	11	    2	 	        slow-firstpass no-fast-pskip
                        


                        b-adapt：设定弹性B帧位置决策算法。此设定控制x264如何决定要放置P帧或B帧。

                        bframes：在I帧与P帧之间可插入B帧数量（Number of B-frames）的最大值，范围0－16。

                        direct："direct"动态向量（motion vectors）的预测模式。有两种模式可用：spatial和temporal。可以指定none来停用direct动态向量，和指定auto来允许x264在两者之间切换为适合的模式。

                        me：全像素（full-pixel）运动估计（motion estimation）的算法。

                        merange：控制运动估计的最大范围（单位是像素）。对于hex和dia，范围限制在4~16。对于umh和esa，它可以增加到超过默认值16来允许范围更广的动态搜寻，对于HD视讯和高动态镜头很有用。注意，对于umh、esa和tesa，增加merange会大幅减慢编码速度。

                        partitions：H.264视讯在压缩过程中划分为16x16的宏区块。这些区块可以进一步划分为更小的分割，这就是此选项要控制的部分。

                        rc-lookahead：设定mb-tree位元率控制和vbv-lookahead使用的帧数。最大允许值是250。对于mb-tree部分，增加帧数带来更好的效果但也会更慢。mb-tree使用的最大缓冲值是MIN(rc-lookahead, --keyint)。

                        ref：控制解码图片缓冲（DPB：Decoded Picture Buffer）的大小。范围是从0到16。总之，此值是每个P帧可以使用先前多少帧作为参照帧的数目（B帧可以使用的数目要少一或两个，取决于它们是否作为参照帧）。可以被参照的最小ref数是1。

                        subme：设定子像素（subpixel）估算复杂度。值越高越好。层级1~5只是控制子像素细分（refinement）强度。层级6为模式决策启用RDO，而层级8为动态向量和内部预测模式启用RDO。RDO层级明显慢于先前的层级。

                        trellis：执行Trellis quantization来提高效率。

                        weightp：使x264能够使用明确加权预测（explicit weighted prediction）来改善P帧的压缩。亦改善淡入／淡出的品质。模式越高越慢。

                        no-8x8dct：停用弹性8x8离散余弦转换（Adaptive 8x8 DCT）。

                        aq-mode：弹性量化模式。没有AQ时，x264很容易分配不足的位元数到细节较少的部分。AQ是用来更好地分配视讯里所有宏区块之间的可用位元数。

                        no-cabac：停用弹性内容的二进制算数编码（CABAC：Context Adaptive Binary Arithmetic Coder）资料流压缩，切换回效率较低的弹性内容的可变长度编码（CAVLC：Context Adaptive Variable Length Coder）系统。大幅降低压缩效率（通常10~20%）和解码的硬件需求。

                        no-deblock：停用循环筛选（loop filter。亦称为持续循环去区块(inloop deblocker)）。

                        no-mbtree：停用宏区块树（macroblock tree）位元率控制。使用宏区块树位元率控制会改善整体压缩率，借由追踪跨帧的时间传播（temporal propagation）并相应地加权。

                        no-mixed-refs：混合参照会以每个8x8分割为基础来选取参照，而不是以每个宏区块为基础。当使用多个参照帧时这会改善品质，虽然要损失一些速度。设定此选项会停用该功能。

                        scenecut：设定I/IDR帧位置的阈值（场景变更侦测）。

                        no-weightb：停用“加权”B帧的参照。

                        slow-firstpass：慢速pass。

                        no-fast-pskip：停用P帧的早期略过侦测（early skip detection）。非常轻微地提高品质，但要损失很多速度。

                    压片组常用的值是 veryslow

                    preset (高参数=龟速)：
                        影响：
                            bitrate模式下，提高参数→提升画质
                            qp/crf模式下，提高参数→节约码率

                        边际效应：
                            1. 把preset
                                从veryfast改到slow，提升是明显的；
                                从veryslow改到placebo，提升非常不明显，而压制的时间令人难以接受。

                            2. 极高码率下，无论用什么参数，不会有太大区别，
                                比如某720p片子码率高达20Mbps，从veryfast改到slow，不可能看出两者在画质上的区别。
                                因此，高参数在低码率片子的作用下更明显，更有效。

                        值：0(ultrafast 超快)~9（placebo 超慢）默认值是5
                        
                        使用： -preset 2
                6. 各个编码器有各自的参数：输入 ffmpeg -h encoder=编码器的名称 ，就可以获取相关参数。
                    比如想知道 英伟达显卡HEVC编码器的用法： ffmpeg -h encoder=hevc_nvenc

                所以，要制作小体积、高画质的视频：
                    1.  选择对的编码器，比如x265
                    2.  设置合适的质量值，而不是直接选择码率，比如 -crf 17
                    3.  尝试提高preset的值（在能接受的速度范围内）比如 -preset 2
                    4.  如果片源有大量噪点，要先降噪，噪点是非常消耗码率的。

                比如 ：
                    要将某素材视频进行编辑，编辑软件不支持素材视频格式，要进行格式转换，ffmpeg怎么设置转换参数？

                    1. 首先在格式方面应将素材视频转换为主流的H.264编码格式、mp4封装格式。这样支持的软件最多。
                    2. 尽量不损失画质、而且转换速度尽量要快。所以，使用的码率控制方式为x264的qp或crf模式，为了
                    保证画质，质量值最好低于20；为了加快编码速度，要使用较低的preset的值，所以将preset的值设为 2。

                    ffmpeg -i in.mkv -c:v libx264 -crf 17 -preset 2 -c:a aac -b:a 320k out.mp4

        b. 改变格式：
            以便满足其他软件、硬件的需要；
            或是使用新的编解码器，以获得更高的压缩比，达到减小体积，节约存储和带宽的目的。

        c. 改变内容本身：
            滤镜 : -vf（video filter）
                这里的滤镜不是大家认为的'美颜滤镜'，而是一整套对视频加工处理的方法，
                有上百种，滤镜之间要有','号分隔，注意滤镜添加的顺序对结果有重大影响。
                
                裁剪画面  crop=宽:高:x坐标:y坐标   比如 crop=1920:800:0:140 
                         前两个参数 宽:高：裁剪后的宽与高，
                         后两个参数 x坐标:y坐标: 表示从哪里开始裁剪。

                缩放画面  scale=缩放后的宽:缩放后的高 或者 缩放参数:缩放后的高度 
                            比如 scale=-2:480  
                            -2表示自动，480是缩放后的高度，这就不用去计算宽度了，宽度会自动缩放。


                比如：
                    把一段1920*1050的h264的mkv片子（source.mkv），高度方向去掉140的黑边，再缩放到高度480，宽度自动-2。
                    然后转换为视频编码为h265,音频编码为mp3，容器格式还是mkv的视频(ok.mkv)。

                    ffmpeg -i source.mkv -vf crop=1920:800:0:140,scale=-2:480 -c:v libx265 -c:a libmp3lame -y ok.mkv
                    
                    -y 表示如果输出时有同名文件就覆盖，不用再确认。

                    注意：这里的滤镜就不能搞错顺序，必须是先裁剪再缩放，否则都缩放成480了，怎么执行crop=1920:800:0:140的裁剪啊？

                添加字幕
                    用到 subtitles 滤镜 或 ass 滤镜

                    字幕分为：srt字幕 和 ass字幕
                        相比ass字幕，srt字幕不包含字体、颜色等 样式 信息。

                    如何用ffmpeg设置 srt字幕的样式 并 压制为‘硬字幕’？
                        压制 srt ass字幕.

                            ffmpeg -i "test.mkv" -vf "subtitle=test.srt" -c:v libx264 -crf 19 -c:a copy  ok.mkv
                            subtitle=字幕的文件名 test.srt 
                            或 ass字幕文件滤镜 
                            ffmpeg -i "test.mkv" -vf ass=test.ass  -c:v libx264 -crf 19 -c:a copy  ok.mkv
                            ass=test.ass 

                            默认输出的 中文字幕样式 会是：雅黑、白色字体+黑色描边
                        
                        定义 srt 样式.
                            ffmpeg -i "test.mkv" -vf "subtitle=test.srt:force_style='some code here'" \
                            -c:v libx264 -crf 19 -c:a copy  ok.mkv
                            在字幕文件名后加入样式代码 :force_style='some code here' 即可定义字幕样式
                            比如 我们要设置的字体 为 思源黑体 字号20 黄色字体
                                ffmpeg -i "test.mkv" -vf "subtitle=test.srt:force_style='fontname=Source Han Sans CN bole,\
                                FontSize=20, PrimaryColour=&H0000ffff, outlineColour=&H00888888, \
                                outline=0,MarginV=50'" \
                                -c:v libx264 -crf 19 -c:a copy  ok.mkv

                                PrimaryColour=&H0000ffff, 字体颜色  看后六位  根据下面的解读 为 黄色
                                outlineColour=&H00888888, 边框颜色 灰色 888888
                                outline=0       边框粗细，为0 表示无边框
                                MarginV=50      表示字幕与底边的距离

                        有关 颜色代码.
                            字体颜色的代码用的是ASS color（B-G-R）颜色，与HTML color（R-G-B）模式不同,

                            所以要把html的取色结果头尾两个码倒一下。
                                        HTML color（R-G-B） ASS color（B-G-R
                                 黑     000000              000000
                                 白     FFFFFF              FFFFFF
                                 红     FF0000              0000FF
                                 绿     00FF00              00FF00
                                 蓝     0000FF              FF0000
                                 黄     FFFF00              00FFFF

                        实例（自定义边框、阴影、背景色等）

                            ffmpeg -i "test.mkv" -vf "subtitle=test.srt:force_style='fontname=Source Han Sans CN bole,\
                            FontSize=20, PrimaryColour=&H0000ffff, backColour=&H00888888, Shadow=1,\
                            outline=0'" \
                            -c:v libx264 -crf 19 -c:a copy  ok.mkv

                            backColour=&H00888888, 阴影颜色 灰色888888
                            Shadow=1 表示阴影深度

                            YouTube默认的cc字幕样式 黑底白字
                            就要添加 BorderStyle=3 此时outlineColour就定义了字幕的背景色 而不是边框的颜色
                            ffmpeg -i "test.mkv" -vf "subtitle=test.srt:force_style='fontname=Source Han Sans CN bole,\
                            FontSize=20, PrimaryColour=&H00ffffff, outlineColour=&H00000000,BorderStyle=3'" \
                            -c:v libx264 -crf 19 -c:a copy  ok.mkv

            截取片段 
                -ss 开始时间点 -to 结束时间点
                或
                -ss 开始时间点 -t 往后多长时间
                或
                -sseof 末尾时间点 -t 往前多长时间

                截取一段视频 从5分钟开始到10分钟结束

                  ffmpeg -ss 0:5:0 -to 0:10:0 -i source.mp4 -c:v libx265 -c:a aac ok.mkv

                如果不进行音视频格式转换，直接拷贝 copy 更快，如下：
                
                  ffmpeg -ss 0:5:0 -to 0:10:0 -i source.mp4 -c:v copy -c:a copy ok.mkv

                  也可简写为：ffmpeg -ss 0:5:0 -to 0:10:0 -i source.mp4 -c copy ok.mkv

                  注意 copy模式下无法精确切割，应该‘留有余地’，多截取一点，比如往前后各30秒。

                  ffmpeg -ss 0:4:30 -to 0:10:30 -i source.mp4 -c copy ok.mkv

                  ffmpeg -ss 0:4:30 -i source.mp4 -to 0:10:30  -c copy ok.mkv  #这样挎着写 会使用关键帧，单时间不一定准
                  ffmpeg -ss 0:4:30 -i source.mp4 -to 0:10:30  -c copy -copyts ok.mkv  # 加入 -copyts  会保留时间戳，使得时间尽量准。

                  ffmpeg -i source.mp4 -ss 0:4:30  -to 0:10:30  -c copy ok.mkv 

            合并文件：
                方法一：FFmpeg concat 协议，文件分隔符 ‘|’ 前后不能有空格*****。
                    ffmpeg -i "concat:01.mp4|02.mp4|03.mp4" -c copy out.mp4
                
                方法二：FFmpeg concat 分离器
                    需要 FFmpeg 1.1 以上版本。先创建一个文本文件filelist.txt：文件名不用引号。
                        file input1.mkv
                        file input2.mkv
                        file input3.mkv
                    然后：
                        ffmpeg -f concat -i filelist.txt -c copy output.mkv

                    如果文件名有奇怪的字符，就要用 英文单引号“'”,而不能用英文双引号，否则在合并时报错：]Impossible to open。
                        file 'input1.mkv'
                        file 'input2.mkv'
                        file 'input3.mkv'
                    并且在合并时要加参数 -safe 0, 不然会报错： Unsafe file name
                        ffmpeg -f concat -safe 0 -i filelist.txt -c copy output.mkv

                方法三：转码+合并 使用 FFmpeg concat 过滤器重新编码（有损）
                    ffmpeg -i input1.mp4 -i input2.webm -i input3.avi -filter_complex '[0:0] [0:1] [1:0] [1:1] [2:0] [2:1] concat=n=3:v=1:a=1 [v] [a]' -map '[v]' -map '[a]' <编码器选项> output.mkv

                    如你所见，上面的命令合并了三种不同格式的文件，FFmpeg concat 过滤器会重新编码它们。注意这是有损压缩。
                    [0:0] [0:1] [1:0] [1:1] [2:0] [2:1] 
                        分别表示第一个输入文件的视频、音频、第二个输入文件的视频、音频、第三个输入文件的视频、音频。
                    concat=n=3:v=1:a=1 
                        表示有三个输入文件，输出一条视频流和一条音频流。
                    [v] [a] 就是得到的视频流和音频流的名字，
                    注意在 bash 等 shell 中需要用引号，防止通配符扩展。

                    实例：
                        对四个输入的音频使用concat过滤器进行转码+合并。

                        ffmpeg -i sbq419.m4a -i sbq420.m4a -i sbq421.m4a -i sbq422.m4a -filter_complex '[0:0] [1:0] [2:0] [3:0] concat=n=4:v=0:a=1 [a]' -map '[a]' -vn -c:a libmp3lame -y sbq19_22_1.mp3
                    
                        ffmpeg -i sbq419.m4a -i sbq420.m4a -i sbq421.m4a -i sbq422.m4a      ## 四个输入文件
                        -filter_complex '[0:0] [1:0] [2:0] [3:0] concat=n=4:v=0:a=1 [a]'    ## 使用concat过滤器合并成0个视频1个音频:只选择四个输入文件的0#音轨 不需要视频
                        -map '[a]'          ## 只选择音轨
                        -vn -c:a libmp3lame ## 转码： 编码器选项 去掉视频 -vn 音频编码使用mp3编码器 -c:a libmp3lame 进行转码
                        -y sbq19_22_1.mp3   ## 输出 并覆盖

                    对比转码后再合并：大小几乎一致，略小一点。并没有感觉有损。



            轨道选择 -map
                比如某部电影有国/粤/英三条音轨。
                想把国语音轨编码为mp3格式，粤语音轨编码为opus格式，丢弃英语音轨。

                ffmpeg -i source.mkv -map v -map a:0 -map a:1 -c:v libx265 -c:a:0 libmp3lame -c:a:1 libopus ok.mkv

                -map v -map a:0 -map a:1 解读： 
                    -map 用来选择所需输出的轨道， 
                    -map v 表示输出视频轨道，
                    -map a:0表示输出第一条音轨，
                    -map a:1表示输出第二条音轨。

                -c:a:0 libmp3lame -c:a:1 libopus：第一条音轨编码为mp3，第二条音轨编码为opus。

            截图、加水印、制作gif：
                截图

                    ffmpeg -i source.mp4 -ss 5  -vframes 1 img1.jpg

                    截取视频 第5秒 的 第一帧 画面，输出为img1.jpg

                加水印

                    ffmpeg -i source.mp4 -i logo.png -filter_complex "overlay=20:20" out.mp4

                    水印logo的位置位于距离左边20距离顶部20的位置，即左上角。

                作动图

                    ffmpeg -i source.mp4 -ss 7.5 -to 8.5 -s 640x320 -r 15 out.gif

                    设置起始时间 -ss 7.5 -to 8.5
                    缩放一下大小 -s 640x320
                    降低一下帧率 -r 15  每秒15帧
                    输出为out.gif动画

            
            录屏、直播

                录屏：
                    ffmpeg -f gdigrab -i desktop rec.mp4

                    只能录制视频 没有声音，声音要后期加上。
                    -f 指录屏的格式，对于windows 默认就是gdigrab这个格式。

               

                直播：
                    利用推流，实现录播，边录边播

                    ffmpeg -re -i rec.mp4 按照网站要求编码 -f flv "你的rtmp地址/你的直播码"

                    -re 按照视频的帧率推流


                更好的录屏和直播推荐 OBS  Studio 免费开源稳定功能强大。

    4.1 查看文件信息
        
        查看视频文件的元信息，比如编码格式和比特率，可以只使用-i参数。
            $ ffmpeg -i input.mp4

        上面命令会输出很多冗余信息，加上-hide_banner参数，可以只显示元信息。
            $ ffmpeg -i input.mp4 -hide_banner

    4.2 转换编码格式
    
        转换编码格式（transcoding）指的是， 将视频文件从一种编码转成另一种编码。
        比如转成 H.264 编码，一般使用编码器libx264，所以只需指定输出文件的视频编码器即可。

            $ ffmpeg -i [input.file] -c:v libx264 output.mp4
        
        下面是转成 H.265 编码的写法。

            $ ffmpeg -i [input.file] -c:v libx265 output.mp4
    
    4.3 转换容器格式
        
        转换容器格式（transmuxing）指的是，将视频文件从一种容器转到另一种容器。
        
        下面是 mp4 转 webm 的写法。
            $ ffmpeg -i input.mp4 -c copy output.webm
        
        上面例子中，只是转一下容器，内部的编码格式不变，所以使用-c copy指定直接拷贝，不经过转码，这样比较快。

    4.4 调整码率
        
        调整码率（transrating）指的是，改变编码的比特率，一般用来将视频文件的体积变小。
        下面的例子指定码率最小为964K，最大为3856K，缓冲区大小为 2000K。
            $ ffmpeg \
            -i input.mp4 \
            -minrate 964K -maxrate 3856K -bufsize 2000K \
            output.mp4

    4.5 改变分辨率（transsizing）

        下面是改变视频分辨率（transsizing）的例子，从 1080p 转为 480p 。

            $ ffmpeg \
            -i input.mp4 \
            -vf scale=480:-1 \
            output.mp4

    4.6 提取音频
        有时，需要从视频里面提取音频（demuxing），可以像下面这样写。

            $ ffmpeg \
            -i input.mp4 \
            -vn -c:a copy \
            output.aac

        上面例子中，-vn表示去掉视频，-c:a copy表示不改变音频编码，直接拷贝。

    4.7 添加音轨
        添加音轨（muxing）指的是，将外部音频加入视频，比如添加背景音乐或旁白。

            $ ffmpeg \
            -i input.aac -i input.mp4 \
            output.mp4

        上面例子中，有音频和视频两个输入文件，FFmpeg 会将它们合成为一个文件。

    4.8 截图
        下面的例子是从指定时间开始，连续对1秒钟的视频进行截图。

            $ ffmpeg \
            -y \
            -i input.mp4 \
            -ss 00:01:24 -t 00:00:01 \
            output_%3d.jpg
        
        如果只需要截一张图，可以指定只截取一帧。

            $ ffmpeg \
            -ss 01:23:45 \
            -i input \
            -vframes 1 -q:v 2 \
            output.jpg

        上面例子中，-vframes 1指定只截取一帧，-q:v 2表示输出的图片质量，一般是1到5之间（1 为质量最高）。

    4.9 裁剪
        裁剪（cutting）指的是，截取原始视频里面的一个片段，输出为一个新视频。
        可以指定开始时间（start）和持续时间（duration），也可以指定结束时间（end）。


            $ ffmpeg -ss [start] -i [input] -t [duration] -c copy [output]
            $ ffmpeg -ss [start] -i [input] -to [end] -c copy [output]
        
        下面是实际的例子。

            $ ffmpeg -ss 00:01:50 -i [input] -t 10.5 -c copy [output]
            $ ffmpeg -ss 2.5 -i [input] -to 10 -c copy [output]

        上面例子中，-c copy表示不改变音频和视频的编码格式，直接拷贝，这样会快很多。

    4.10 为音频添加封面
        有些视频网站只允许上传视频文件。如果要上传音频文件，必须为音频添加封面，将其转为视频，然后上传。

        下面命令可以将音频文件，转为带封面的视频文件。

            $ ffmpeg \
            -loop 1 \
            -i cover.jpg -i input.mp3 \
            -c:v libx264 -c:a aac -b:a 192k -shortest \
            output.mp4
        
        上面命令中，有两个输入文件，一个是封面图片cover.jpg，另一个是音频文件input.mp3。
        -loop 1参数表示图片无限循环，-shortest参数表示音频文件结束，输出视频就结束。

五 ffmpeg帮助：

    Hyper fast Audio and Video encoder
    
        usage: ffmpeg [options] [[infile options] -i infile]... {[outfile options] outfile}...


    
    Getting help:
    
        -h      -- print basic options
    
        -h long -- print more options
    
        -h full -- print all options (including all format and codec specific options, very long)
    
        -h type=name -- print all options for the named decoder/encoder/demuxer/muxer/filter/bsf/protocol
    
        See man ffmpeg for detailed description of the options.


    
    Print help / information / capabilities:
    
        -L                  show license

        -h topic            show help

        -? topic            show help

        -help topic         show help

        --help topic        show help

        -version            show version
    
        -buildconf          show build configuration

        -formats            show available formats

        -muxers             show available muxers

        -demuxers           show available demuxers

        -devices            show available devices

        -codecs             show available codecs

        -decoders           show available decoders

        -encoders           show available encoders
    
        -bsfs               show available bit stream filters

        -protocols          show available protocols

        -filters            show available filters

        -pix_fmts           show available pixel formats

        -layouts            show standard channel layouts

        -sample_fmts        show available audio sample formats

        -colors             show available color names

        -sources device     list sources of the input device

        -sinks device       list sinks of the output device

        -hwaccels           show available HW acceleration methods


    
    Global options (affect whole program instead of just one file):
    
        -loglevel loglevel  set logging level

        -v loglevel         set logging level

        -report             generate a report

        -max_alloc bytes    set maximum size of a single allocated block

        -y                  overwrite output files

        -n                  never overwrite output files
    
        -ignore_unknown     Ignore unknown stream types

        -filter_threads     number of non-complex filter threads

        -filter_complex_threads  number of threads for -filter_complex

        -stats              print progress report during encoding

        -max_error_rate maximum error rate  ratio of errors (0.0: no errors, 1.0: 100% errors) above which ffmpeg returns an error instead of success.

        -bits_per_raw_sample number  set the number of bits per raw sample

        -vol volume         change audio volume (256=normal)


    
    Per-file main options:
    
        -f fmt              force format

        -c codec            codec name
    
        -codec codec        codec name

        -pre preset         preset name

        -map_metadata outfile[,metadata]:infile[,metadata]  set metadata information of outfile from infile

        -t duration         record or transcode "duration" seconds of audio/video

        -to time_stop       record or transcode stop time

        -fs limit_size      set the limit file size in bytes

        -ss time_off        set the start time offset

        -sseof time_off     set the start time offset relative to EOF

        -seek_timestamp     enable/disable seeking by timestamp with -ss

        -timestamp time     set the recording timestamp ('now' to set the current time)
    
        -metadata string=string  add metadata

        -program title=string:st=number...  add program with specified streams

        -target type        specify target file type ("vcd", "svcd", "dvd", "dv" or "dv50" with optional prefixes "pal-", "ntsc-" or "film-")

        -apad               audio pad

        -frames number      set the number of frames to output

        -filter filter_graph  set stream filtergraph

        -filter_script filename  read stream filtergraph description from a file

        -reinit_filter      reinit filtergraph on input parameter changes

        -discard            discard

        -disposition        disposition


    
    Video options:
    
        -vframes number     set the number of video frames to output

        -r rate             set frame rate (Hz value, fraction or abbreviation)

        -s size             set frame size (WxH or abbreviation)

        -aspect aspect      set aspect ratio (4:3, 16:9 or 1.3333, 1.7777)
    
        -bits_per_raw_sample number  set the number of bits per raw sample

        -vn                 disable video

        -vcodec codec       force video codec ('copy' to copy stream)

        -timecode hh:mm:ss[:;.]ff  set initial TimeCode value.

        -pass n             select the pass number (1 to 3)

        -vf filter_graph    set video filters

        -ab bitrate         audio bitrate (please use -b:a)

        -b bitrate          video bitrate (please use -b:v)

        -dn                 disable data


    
    Audio options:
    
        -aframes number     set the number of audio frames to output

        -aq quality         set audio quality (codec-specific)

        -ar rate            set audio sampling rate (in Hz)

        -ac channels        set number of audio channels

        -an                 disable audio

        -acodec codec       force audio codec ('copy' to copy stream)

        -vol volume         change audio volume (256=normal)

        -af filter_graph    set audio filters


    
    Subtitle options:
    
        -s size             set frame size (WxH or abbreviation)

        -sn                 disable subtitle

        -scodec codec       force subtitle codec ('copy' to copy stream)

        -stag fourcc/tag    force subtitle tag/fourcc

        -fix_sub_duration   fix subtitles duration

        -canvas_size size   set canvas size (WxH or abbreviation)

        -spre preset        set the subtitle options to the indicated preset


    超快速音频和视频编码器
    
        用法：ffmpeg [选项] [[infile选项] -i infile] ... {[outfile选项] outfile} ...


    获得帮助：
    
        -h-打印基本选项
    
        -h long-打印更多选项
    
        -h full-打印所有选项（包括所有格式和编解码器特定的选项，很长）
    
        -h type = name-打印命名的解码器/编码器/解复用器/复用器/过滤器/ bsf /协议的所有选项
    
        有关选项的详细说明，请参见man ffmpeg。

  
    打印帮助/信息/功能：
    
        -L演出许可证

        -h主题显示帮助

        -？主题显示帮助

        -help主题显示帮助

        --help主题显示帮助


    版本显示版本
    
        -buildconf显示构建配置

        -formats显示可用格式

        -muxers显示可用的muxers

        -demuxers显示可用的多路分解器

        -devices显示可用设备

        -codecs显示可用的编解码器

        -decoders显示可用的解码器

        -encoders显示可用的编码器

        -bsfs显示可用的位流过滤器

        -协议显示可用协议

        -filters显示可用的过滤器

        -pix_fmts显示可用的像素格式

        -layouts显示标准的频道布局

        -sample_fmts显示可用的音频样本格式

        -colors显示可用的颜色名称

        -sources设备列出输入设备的来源

        -sinks输出设备的设备列表接收器

        -hwaccels显示可用的硬件加速方法

    
    全局选项（影响整个程序，而不只是一个文件）：
    
        -loglevel loglevel设置日志记录级别

        -v loglevel设置日志记录级别

        -report生成报告

        -max_alloc字节设置单个分配块的最大大小

        -y覆盖输出文件

        -n从不覆盖输出文件

        -ignore_unknown忽略未知的流类型

        -filter_threads非复杂过滤器线程数

        -filter_complex_threads -filter_complex的线程数

        -stats在编码期间打印进度报告

        -max_error_rate最大错误率的错误率（0.0：无错误，1.0：100％错误），高于此比率ffmpeg将返回错误而不是成功。

        -bits_per_raw_sample number设置每个原始样本的位数

        -vol音量更改音频音量（256 =正常）


    
    每个文件的主要选项：
    
        -f fmt强制格式

        -c编解码器编解码器名称

        -codec编解码器编解码器名称

        -pre预设预设名称

        -map_metadata outfile [，metadata]：infile [，metadata]设置infile中outfile的元数据信息

        -t持续时间记录或对音频/视频的“持续时间”秒进行转码

        -to time_stop记录或转码停止时间

        -fs limit_size设置限制文件大小（以字节为单位）

        -ss time_off设置开始时间偏移

        -sseof time_off设置相对于EOF的开始时间偏移

        -seek_timestamp使用-ss按时间戳启用/禁用查找

        -timestamp time设置录制时间戳（“ now”设置当前时间）

        -metadata string =字符串添加元数据

        -program title = string：st = number ...添加具有指定流的程序

        -target type指定目标文件类型（“ vcd”，“ svcd”，“ dvd”，“ dv”或“ dv50”，带有可选的前缀“ pal-”，“ ntsc-”或“ film-”）

        -apad音频垫

        -frames number设置要输出的帧数

        -filter filter_graph设置流filtergraph

        -filter_script filename从文件中读取流filtergraph描述

        -reinit_filter在输入参数更改时重新初始化过滤器图

        -丢弃丢弃

        -处置处置


    
    视频选项：
    
        -vframes number设置要输出的视频帧数

        -r速率设置帧速率（Hz值，分数或缩写）

        -s size设置帧大小（WxH或缩写）

        -aspect宽高比设置宽高比（4：3、16：9或1.3333、1.7777）

        -bits_per_raw_sample number设置每个原始样本的位数

        -vn禁用视频

        -vcodec编解码器强制视频编解码器（“复制”以复制流）

        -timecode hh：mm：ss [：;。] ff设置初始TimeCode值。

        -pass n选择通过次数（1到3）

        -vf filter_graph设置视频过滤器

        -ab比特率音频比特率（请使用-b：a）

        -b比特率视频比特率（请使用-b：v）

        -dn禁用数据



    音频选项：

        -aframes number设置要输出的音频帧数
    
        -aq quality设置音频质量（特定于编解码器）
    
        -ar rate设置音频采样率（以Hz为单位）
    
        -ac频道设置音频频道数
    
        -禁用音频
    
        -acodec编解码器强制音频编解码器（“复制”以复制流）
    
        -vol音量更改音频音量（256 =正常）
    
        -af filter_graph设置音频过滤器



    字幕选项：

        -s size设置帧大小（WxH或缩写）

        -sn禁用字幕

        -scodec编解码器强制字幕编解码器（“复制”以复制流）

        -stag fourcc / tag强制字幕tag / fourcc

        -fix_sub_durati固定字幕时长

        -canvas_size size设置画布大小（WxH或缩写）

        -spre预设将字幕选项设置为指示的预设