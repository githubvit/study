# 图片 OCR

# 1 首先用pillow（PIL）的 Image 打开 图像
# 2 对图像进行二值化处理：（a 将图像模式先转为灰度模式，b 根据阈值确定图片每个像素点的黑白，c 输出为黑白图像。）
# 3 用OCR识别软件 pytesseract 使用 中英文识别 将 图像 转换为  字符

# 复杂图像处理
# 使用Pillow对图片进行滤色 https://huanghaozi.cn/index.php/archives/112/
from PIL import Image
import pytesseract as pyt # ocr

# path=r'D:\pyj\st\study\8爬虫\任务\test.png'
# path=r'D:\Desktop\桌面\2020一中选拔\初一\一中2021初一一班下学期【期末】数学考试_1.jpg '
path=r'D:\Desktop\二值化.jpg '
img=Image.open(path)
#二值化图像传入图像和阈值
'''
图像二值化（ Image Binarization）就是将图像上的像素点的灰度值设置为0或255，
也就是将整个图像呈现出明显的黑白效果的过程。

在数字图像处理中，二值图像占有非常重要的地位，图像的二值化使图像中数据量大为减少，
从而能凸显出目标的轮廓。

阈值: 自定义灰度界限，大于这个值为黑色，小于这个值为白色

''' 
# 二值化
def erzhihua(image,threshold):
    # 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
    image=image.convert('L')
    table=[]
    for i in range(256):
      if i < threshold:
        table.append(0)
      else:
        table.append(1)
    return image.point(table,'1')

# 区间 二值化 去掉大的和小的，只留中间
def qzerzhihua(image,max,min):
    # 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
    image=image.convert('L')
    table=[]
    for i in range(256):
      if i < max:
        if i > min:
          table.append(0)
        else:
          table.append(1)
      else:
        table.append(1)
    return image.point(table,'1')
 
image=erzhihua(img,135) #阈值为150
# image=erzhihua(img,127) #阈值为127
# image=erzhihua(img,80) #阈值为50
# image=qzerzhihua(img,40,30) #阈值为50
image.show()
# t=pyt.image_to_string(image,lang='chi_sim+eng')
# print(t)

'''


2023 届 初 一 〈1) 班 上 学 期 期 末 数 学 试卷

az, FB | ae. G1
一 、 坊 空 题 CAEN BH 4 4p, F 68 5})
1 RS OB, 38 4y2 go “ape AY FE IOUFY 198 )

2. BIB. a _ -2 = (A-b)(a+b)(a*%qh+ hq 24+Gb+b*)

15. Bex. y, EEE 六、 ae








oS pyle 店庆
1. fa Na. eae gt on™ 2











… = ALA Sp, KID) = HPS yd- wey
3， 比 较 大 仆 3 ORB 选择 题 (等 小 及 4 分 ， 共 19-4951 COXA
V2+Vi0_< 为 + @ Foi — eR ABR, 18， 下 列 等 式 中 ， 运 算 正确 的 是 ( / ) 1--l, OY +92 434)
4 BMS y By paM, y s Sn iA, Cn#0), oy
ms ag PB ME 学。 A. 5ab—3ab =2 B. xx ad 2 :只 axes
| 二 | = > ~ 从 二 二 _ Ay _ a! Hi
xen aa yey nb 0 2-xj =x ,Nu 的 -MX ?ai D. (2x) =-Bx ky
fi Z 19. KF x (OHH Ga+20b)x+5 =O, Wade 1D) ;
= 和 FI Y(x— I)? fox, 江汉 从 从 从 228 eR ENE Cas ibe aD GE aw.
SA EE A. EM B、 非 负数 负数 iy a
Bip. 知 多 项 式 f(x) = 2x? 52 + feb 2x-+3 BER, BI m= {Be 1 2 人
六 不 等 式 1x 一 引 [一 12x-1 区 1 的 解 为 X< 出 站 7 分 段 讨 论 20. SRM 各 各 a?
te 8 MRatb=5, 2+ =50, matsp? = 15 一 1 四] CU og tS
A, 3 7 4 * 5 加 2
48 9. Jo 一 户 and [ =
titi: a,|-4 pea G2 ai F - - PE) MRAP (38 4 分 》 ，
一 -一 ~ 一 bef v2 +V5-v3 _ + LI = 人 _ 216 为 21，(5 分 ) BB: ae : .
简 ， oa ii tl 二 — 一 2 2 一 x -3 oh
a 2130-63-43 | 全 eu] Bi I-33 +123 )
ti' =4, weyctoe= 4, Mxery+r= Ba a= as
12, RF x —- RAGE? — mx + 2m—-1=0 RAAT x, x, BaP 432 <7, 一 RSH 一
ays -3 2 Azjn-4emn1= 1 8m +4 A-2 x21 2 BA 的 of.
Mx 2 A? X27 7g xa" 2x, A22N7-2(2M-1 ic oy .
baci DO* Tass seo ti
13. Ge ot eee BREET BM y 以 ce 22. ope ao ee # Fé
OPE SE @ 11-xFZ). GO, : - 人 本
EB. BD) lore 上 a= _
ZED Ipri82 = = “lat Ti % Bx sion YAR BS m2 =f Onn 站 oe) alex Doty].
14, BRM {Xs sea st) 1 ON a 证 运
x—l Fa Nt 2 LE aH + xy Rip KANG

Qo! X=42f2. :人 个 二
of R= 2 (247
HR .


1 23.(6分)计算20215-20202×(20213+2×20212+3×2022+1
2 令202令2021=x原式=5-(x-1)2[x3+2x2+3(x+1)f1
3 26.(6分)甲经营甲、乙两个服装店,每个店铺在同一时间段内都能售出A、B两种款式的服装
4 合计30件,并且每售出一件A款式和B款式服装,甲店铺获利润分别为30元和40元,乙店铺
5 款式和
6 x5-(x-1)2x+2x2+3x+4
7 获利润分别为27元和36元。某日,甲进货件A款式服装35件,B款式服装25件,怎样分配给
8 每个店铺各30件服装,可以保证乙店铺获利润不小于950元的前提下,甲获取的总利润最大?
9 x5-(x2-2x+1)(x3+2x+3x+4
10 最大总利润是多少?
11 4+32+4-2436x2解:设将分给甲x件,B(30-x件;分给乙(35-x件B
12 给乙(x-5)件
13 总利润=30x+40(30-x)+2735-X)
14 -8x+x3+2x2+3x+4
15 -5)且27(35-x)+36(x-5)7956
16 总利润二1965-x
17 5x-4
18 =101
19 且765+x750
20 185
21 24.(6分)如图,正方体的每个面都有一个正整数.已知相对的两个面上的两数之和都相等,如
22 X79
23 果13、9、3的对面的数分别为a、b、c,求a2+b2+c2-ab-bc-ca的值.
24 答:又x为整数x=21.总=1944
25 解:a2+b2+c2-ab-bc-ca
26 ①将分甲21件.B分9件;A分乙4件,
27 [(a-b)2+(b-c)2+(c-a)2
28 乙16件,②最大总利润为1944元
29 又a-b=-4b-C=-6
30 C-=10
31 27.(6分)某人沿着向上移动的自动扶梯从顶端向下走到底部用了a分钟,而他沿自动扶梯从
32 底部走到顶端用了b分钟,那么此人不动乘扶梯从底部到顶端需要几分钟?又若停电,此人沿扶
33 原式=(16+36+10D)
34 梯从底部走到顶端需要几分钟(假定此人上、下扶梯行走速度相同)
35 解
36 设以=V扶二y.共了级扶梯
37 二76
38 :a分
39 a(x-y)=
40 x70y70
41 b(xty)= a70 b70
42 S
43 分
44 25.(6分)若关于x的方程x2-(2m+1)x+m2+2m=0的两根为a和B,求(-1)2+(B-1)
45 △=(4m2+4m+1)-2(m2+2m)=1-4m
46 a-a- (a-b)= catb
47 atb
48 b.+b-S
49 -a-b
50 解,(d-1)2+(13-1)=x+-2(d+B)+2m≤
51 的最小值
52 a-a,三
53 =(a+B)-2B3-2(x+B+2
54 b-b.
55 .+13=2m+1=mm+2)
56 s, -2ab
Request
'''