# import shutil
# import time
# ret = shutil.make_archive(
#     "day15_bak_%s" %time.strftime('%Y-%m-%d'),
#     'gztar',
#     root_dir=r'D:\code\SH_fullstack_s1\day15'
# )

import tarfile
t=tarfile.open('day15_bak_2018-04-08.tar.gz','r')
t.extractall(r'D:\code\SH_fullstack_s1\day16\解包目录')
t.close()


