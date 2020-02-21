"""
编写Python脚本，分析xx.log文件，按域名统计访问次数

xx.log文件内容如下：
https://www.sogo.com/ale.html
https://www.qq.com/3asd.html
https://www.sogo.com/teoans.html
https://www.bilibili.com/2
https://www.sogo.com/asd_sa.html
https://y.qq.com/
https://www.bilibili.com/1
https://dig.chouti.com/
https://www.bilibili.com/imd.html
https://www.bilibili.com/


输出：
4 www.bilibili.com
3 www.sogo.com
1 www.qq.com
1 y.qq.com
1 dig.chouti.com

"""
import re
from collections import Counter

# 1. 读取出内容
with open('xx.log', 'r', encoding='utf-8') as f:
    data = f.read()

# 2. 取域名信息
ret = re.findall(r'https://(.*?)/.*?', data)
# print(ret)

# 3. 统计
# dic = {}
# for i in ret:
#     if i not in dic:
#         dic[i] = 1
#     else:
#         dic[i] += 1
# print(dic)
#
# # 4. 排序
# ret2 = sorted(dic, key=lambda x: dic[x], reverse=True)
# print(ret2)
#
# for k in ret2:
#     print(dic[k], k)

dic = Counter(ret)
# print(dic)

# 排序
ret2 = sorted(dic.items(), key=lambda x:x[1], reverse=True)
for k, v in ret2:
    print(v, k)

# for i in dic.items():
#     print(i)
