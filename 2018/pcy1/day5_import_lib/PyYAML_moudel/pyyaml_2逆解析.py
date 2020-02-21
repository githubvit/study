#-*- coding:utf8 -*-
import yaml
# document = """
# a: 1
# b: {c: 3, d: 4}
# """
# print yaml.dump(yaml.load(document),default_flow_style=False)


document = ['Hesperiidae', ['Papilionidae','Apatelodidae'], 'Epiplemidae']
print yaml.dump(document,default_flow_style=False)