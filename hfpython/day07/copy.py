import sys

l=sys.argv # 把命令行中解释器后空格分割的所有参数都存成列表
# print(l)

src_file_path=l[1]
dst_file_path=l[2]
# print(src_file_path)
# print(dst_file_path)

with open(r'%s' %src_file_path,mode='rb') as src_f,\
        open(r'%s' %dst_file_path,mode='wb') as dst_f:

    for line in src_f:
        dst_f.write(line)