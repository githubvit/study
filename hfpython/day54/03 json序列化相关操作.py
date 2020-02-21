"""
python中json序列化相关操作
"""

import json

# 序列化 python对象 -> JSON格式的字符串

d = {"name": "Egon", "age": 18}
ret = json.dumps(d)
print(ret, type(ret))

# 反序列化 JSON格式的字符串 -> Python对象
p_str = '{"name": "Egon", "age": 18}'
d2 = json.loads(p_str)
print(d2, type(d2))
