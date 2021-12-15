import os,sys
from concurrent.futures import ProcessPoolExecutor # 进程池
from concurrent.futures import ThreadPoolExecutor  # 线程池
from threading import current_thread
import time
# 用 ffmpeg 命令行 来 从多媒体中 提取 音频

# 先执行一条命令
# 输入文件
# 把源文件分隔符 '\' 改成 '/'
# input_file=r"C:/Users/69598/Downloads/Video/三体（04-06）幽灵倒计时【无删减完整版】 - YouTube.mkv"

# 编码器
# code="libmp3lame" # mp3 编码器
# code="aac"        # aac 编码器
# 输出文件夹
# output_dir=
def split_music(input_file,code='copy',output_dir=None):
    # 如果文件存在
    if os.path.exists(input_file):
        filename=input_file.split('/')[-1].split('.')[0] # 文件名
        filename_suffix=input_file.split('/')[-1].split('.')[-1] # 后缀名
        # print(filename)
        # 输出文件夹
        if not output_dir: #如果没有指定输出文件夹，那么输入文件的文件夹就是输出文件夹
            output_dir=os.path.dirname(input_file)
        # 输出的编码格式和封装格式
        if 'mp3' in code:
            output_file=f'{output_dir}/{filename}.mp3'
        elif 'aac' in code:
            output_file=f'{output_dir}/{filename}.aac'
        else:
            # 使用源文件扩展名封装格式
            output_file=f'{output_dir}/{filename}_music.{filename_suffix}'
        # print(output_file)
        # 最后 用ffmpeg分割 ∴ 必须装好了ffmpeg，否则用不了
        os.system(f'ffmpeg -i "{input_file}" -vn -c:a {code} -y "{output_file}" -hide_banner')
    else:
        print('文件不存在')

# for item in m_list:
#     split_music(item,code)
# split_music(input_file,code)

if __name__ == "__main__":
    start_time=time.time()
    m_list=['C:/Users/69598/Downloads/Video/三体（01-03）科学边界【无删减完整版】.mp4',
'C:/Users/69598/Downloads/Video/三体（04-06）幽灵倒计时【无删减完整版】 - YouTube.mkv',
'C:/Users/69598/Downloads/Video/三体（07-09）飞刃【无删减完整版】.mp4']

    # 编码器
    # code="libmp3lame" # mp3 编码器
    code="aac"        # aac 编码器
    output_dir='C:/Users/69598/Downloads/Video/test'

    # 线程池 不填数量 默认=cpu核心数量*5
    pool=ThreadPoolExecutor(3)

    # 进程池 
    # pool=ProcessPoolExecutor(3)

    # 用线程池 异步+回调
    for item in m_list:
        pool.submit(split_music,item,code,output_dir=output_dir)
    pool.shutdown()#关池

    print('主线程',current_thread().getName())
    print('耗时：',time.time()-start_time)

# 线程池
# 主线程 MainThread
# 耗时： 44.143699645996094

# 进程池
# 耗时： 44.1871919631958