#==========================================>查
import xml.etree.ElementTree as ET
#
# tree=ET.parse('a.xml')
# root=tree.getroot()
#三种查找节点的方式
# res=root.iter('rank') # 会在整个树中进行查找，而且是查找到所有
# for item in res:
#     # print(item)
#     print('='*50)
#     print(item.tag) # 标签名
#     print(item.attrib) #属性
#     print(item.text) #文本内容


# res=root.find('country') # 只能在当前元素的下一级开始查找。并且只找到一个就结束
# print(res.tag)
# print(res.attrib)
# print(res.text)
# nh=res.find('neighbor')
# print(nh.attrib)


# cy=root.findall('country') # 只能在当前元素的下一级开始查找,
# print([item.attrib for item in cy])




#==========================================>改
# import xml.etree.ElementTree as ET
# tree=ET.parse('a.xml')
# root=tree.getroot()
#
# for year in root.iter('year'):
#     year.text=str(int(year.text) + 10)
#     year.attrib={'updated':'yes'}
#
#
# # tree.write('b.xml')
# tree.write('a.xml')



#==========================================>增
import xml.etree.ElementTree as ET
tree=ET.parse('a.xml')
root=tree.getroot()

for country in root.iter('country'):
    # print(country)
    year=country.find('year')
    # print(year)
    if int(year.text) > 2020:
        # print(country.attrib)
        # ele=ET.Element('egon')
        # ele.attrib={'nb':'yes'}
        # ele.text='非常帅'
        # country.append(ele)
        country.remove(year)
tree.write('b.xml')