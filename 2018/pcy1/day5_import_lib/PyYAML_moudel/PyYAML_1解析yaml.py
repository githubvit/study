#-*- coding:utf8 -*-
import yaml
# 字典
# document = """
#   a: 1
#   b:
#     c: 3
#     d: 4
# """
# print yaml.load(document)#已经把字符串load成了字典
# print type(yaml.load(document))
# print yaml.dump(yaml.load(document))#再把字典dump成字符串，但还不够彻底yaml
# print type(yaml.dump(yaml.load(document)))
# print yaml.dump(yaml.load(document),default_flow_style=False) #彻底yaml

# 列表
# print yaml.load("""
# - Hesperiidae
# - Papilionidae
# - Apatelodidae
# - Epiplemidae
# """)
#
document = """
- Hesperiidae
- - Papilionidae
  - abc  
- - Apatelodidae
  - dfg
- Epiplemidae
"""
print yaml.load(document)
print type(yaml.load(document))
print yaml.dump(yaml.load(document))

# 综合
# document = """
# house:
#   family:
#     name: Doe
#     parents:
#       - John
#       - Jane
#     children:
#       - Paul
#       - Mark
#       - Simone
#   address:
#     number: 34
#     street: Main Street
#     city: Nowheretown
#     zipcode: 12345
# """
# print yaml.load(document)
#
# document = {'house':
#                 {'family':
#                      {'parents': ['John', 'Jane'],
#                       'name': 'Doe',
#                       'children': ['Paul', 'Mark', 'Simone']},
#                  'address':
#                      {'city': 'Nowheretown',
#                       'street': 'Main Street',
#                       'number': 34,
#                       'zipcode': 12345}
#                  }
#             }
# print yaml.dump(document,default_flow_style=False)


