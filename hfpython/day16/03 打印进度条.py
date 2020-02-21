# print('[                 ]')
# print('[##               ]')
# print('[###              ]')
# print('[####             ]')
# print('[#####            ]')


# print('[%-50s]' %'#')
# print('[%-50s]' %'##')
# print('[%-50s]' %'###')


# 第一个%是取消第二个%号的特殊意义的
# num=30
# print('%s%%' %num)


# width=30
# print(('[%%-%ds]' %width) %'#')
# print(('[%%-%ds]' %width) %'##')
# print(('[%%-%ds]' %width) %'###')


def progress(percent,width=50):
    if percent > 1:
        percent=1
    show_str=('[%%-%ds]' %width) %(int(width*percent) * '#')
    print('\r%s %d%%' %(show_str,int(100*percent)),end='')

import time
recv_size=0
total_size=8097
while recv_size < total_size:
    time.sleep(0.1)
    recv_size+=8096
    percent=recv_size / total_size
    progress(percent)

