#-*- coding:utf8 -*-
import xml.etree.ElementTree as ET

new_xml = ET.Element("namelist") #root
person = ET.SubElement(new_xml, "personinfo", attrib={"enrolled": "yes"})
name=ET.SubElement(person,'name')
name.text='alex'
age = ET.SubElement(person, "age", attrib={"checked": "no"})
sex = ET.SubElement(person, "sex")
age.text = '33'
person2 = ET.SubElement(new_xml, "personinfo", attrib={"enrolled": "no"})
name2=ET.SubElement(person2,'name')
name2.text='sgq'
age = ET.SubElement(person2, "age")
age.text = '19'

et = ET.ElementTree(new_xml)  # 生成文档对象
print et
et.write("test.xml", encoding="utf-8", xml_declaration=True)
# # 没有xml_declaration=True，就没有xml文档的第一行
# # <?xml version='1.0' encoding='utf-8'?>

ET.dump(new_xml)  # 打印生成的格式,xml模块像json一样也有dump