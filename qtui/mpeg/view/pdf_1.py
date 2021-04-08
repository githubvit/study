# pip install PyMuPDF 
# 该库的标准Python import语句是import fitz
# http://blog.yixao.net/share/12997.html
# https://pymupdf.readthedocs.io/en/latest/tutorial.html 官方信息
import fitz

pdf_file=r'F:\OneDrive - 中国加油！武汉加油！\02初中\数学\初中数学朱韬\人教版 初中数学\第01讲 有理数初步（一）.pdf'


doc=fitz.open(pdf_file)
print(doc.pageCount)    # 页数（int）      2
print(doc.getToC())     # 获取目录（列表） []
print(doc.metadata)     # 元数据（dict）
# {
    # 'format': 'PDF 1.5', 
    # 'title': '<4D6963726F736F667420576F7264202D203031D3D0C0EDCAFDB3F5B2BDA3A8D2BBA3A92D2DD6ECE8BA2E646F63>', 
    # 'author': 'Administrator', 
    # 'subject': '', 
    # 'keywords': '', 
    # 'creator': 'PScript5.dll Version 5.2.2', 
    # 'producer': 'Acrobat Distiller 9.0.0 (Windows)', 
    # 'creationDate': "D:20130402165613+08'00'", 
    # 'modDate': "D:20130402165613+08'00'",
    # 'trapped': '', 
    # 'encryption': None
# }
print(doc.loadPage(0))  # 阅读页面 
# page 0 of F:\OneDrive - 中国加油！武汉加油！\02初中\数学\初中数学朱韬\人教版 初中数学\第01讲 有理数初步（一）.pdf

# print(dir(doc))
t_name='t1.txt'
with open(t_name,'wb') as f:
    for i,page in enumerate(doc):
        # 转为图形并保存为图片
        pix=page.getPixmap(alpha=False)
        pix.writePNG(f'page-{i}.png')
        # 提取文字
        text=page.getText().encode('utf-8')
        f.write(text)
        
        # 提取图片
        # print(dir(page)) 
        # 通过page.getImageList()提取到图片列表信息，然后在使用fitz.Pixmap提取对应的图片内容，就是这么简单，
        imglist=page.getImageList()
        if len(imglist):
            for j,img in enumerate(imglist):

                # print(img) # (10, 0, 643, 44, 8, 'Indexed', '', 'Im37', 'FlateDecode')
                # print(dir(img))  # [..., 'count', 'index']]
                # print(type(img)) # 元组 <class 'tuple'>

                i_pix=fitz.Pixmap(doc,img[0])
                i_pix.writeImage(f'pdf_{j}.jpg')

                # 删除PDF中的图片 得到新的pdf
                doc._deleteObject(img[0])

#重新保存 pdf
doc.save('del_img.pdf') 