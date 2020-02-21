#-*- coding:utf8 -*-
import xml.etree.ElementTree as ET

tree = ET.parse('xml_test.xml')
root = tree.getroot()

# xml文件修改，
# 修改所有year子节点，<year>2008</year>、<year>2011</year>、<year>2011</year>
# for node in root.iter('year'):
#     new_year = int(node.text) + 1 #年份加1，
#     node.text = str(new_year)#修改了text
#     node.set("updated_by", "sgq")#修改属性attrib updated=‘yes’
#
# tree.write("xmltest.xml") #写入另一个文件xmltest.xml，当然也可以写入源文件
# <year updated_by="sgq">2009</year>
# <year updated_by="sgq">2012</year>

# 删除node
# <country name="Panama">
#         <rank updated="yes">69</rank>
# 删除排名大于50的国家，Panama被删除
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank ==5:
        root.remove(country)
#
# tree.write('output.xml')
# 删除的断落紧接着root标签的结束符，比如</data>，那么</data>与开始<data>将不在同一条线。
