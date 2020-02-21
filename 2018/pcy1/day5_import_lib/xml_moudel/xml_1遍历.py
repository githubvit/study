#-*- coding:utf8 -*-
import xml.etree.ElementTree as ET

tree = ET.parse('xml_test.xml') #建立对象
root = tree.getroot()#获取根节点
# print root #内存地址
# print(root.tag)#标签名

# 遍历xml文档
# <rank updated="yes">2</rank>

# for child in root:
#     print(child.tag, child.attrib,child.text)#rank是tag，
#     for i in child:
#         print(i.tag,i.attrib,i.text)#rank是tag，updated="yes"是attrib，2是text
# 解析结果('rank', {'updated': 'yes'}, '2')
#对于自结束标签<neighbor name="Switzerland" direction="W"/>的解析结果
#    ('neighbor', {'direction': 'W', 'name': 'Switzerland'}, None) text为None


# 只遍历year 节点
for node in root.iter('year'):
    print(node.tag, node.text)
print('-----------------------------')

#用递归函数处理xml文档的遍历，可以根据标签的text中是否有回车换行'\n'来判断是否有子标签。
def findall_xml(s):
    for j in s:
        print(j.tag, j.attrib, j.text)
        if  j.text==None: #对于没有text的处理，也就是自结束标签的处理
            continue
        elif '\n' in j.text: #有子标签就递归
            findall_xml(j)
        #如果用return findall_xml(j) 递归第一个节点的子标签就结束。
        #也就是说return 递归，是单边递进，到最里面就结束，不会返回上层。
        #记住在递归函数中————>用return不return，要return就不return。
        else:
            continue

findall_xml(root)

# 可以根据text中\n后的空格数量来判断节点的层级
# ('country', {'name': 'Liechtenstein'}, '\n        ')8个空格
# ('info', {}, '\n            ')12个空格
print('-----------------------------')

# 遍历子节点
for node in root.iter('info'):
    findall_xml(node)