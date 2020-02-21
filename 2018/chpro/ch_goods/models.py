# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
from ch_supplier.models import *

# Create your models here.
#商品用途（
# 日用瓷：
# 餐具-套、
# 碗、盘、碟、勺、烟灰缸、酒壶、酒杯。。。
# 茶具-套、
# 茶壶、茶杯、茶叶罐。。。；
# 咖啡具-套。。。
# 其他-文具套装、笔洗、笔筒、笔架、笔墨盒、印泥和、卷筒；
# 陈设瓷：
# 瓷板画、
# 画盘、
# 瓷瓶、
# 雕塑瓷、
# 其他摆件）
class goodsuseinfo(models.Model):
    gstitle=models.CharField(max_length=16,verbose_name='商品用途')
    def __unicode__(self):
        return self.gstitle
    class Meta:
        verbose_name = '商品用途'  # 改对象名
        verbose_name_plural = "商品用途列表"  # 改表名

# 商品分类(
# 胎装技法：印花、划花、刻花、堆贴、玲珑、薄胎
# 彩装技法：青花、粉彩、斗彩、法郎彩、素三彩、描金，
# 釉装技法：祭红、郎窑红、均红、玫瑰紫、美人醉、釉里红、火炎红)
class goodstype(models.Model):
    gtitle=models.CharField(max_length=16,verbose_name='商品类型')
    gcontext=models.CharField(max_length=16,verbose_name='类型描述',blank=True,null=True)
    gtfk=models.ForeignKey('self',related_name='gtty',null=True,verbose_name='所属父类',blank=True)
    ctime = models.DateTimeField(auto_now_add=True, verbose_name="建立时间")
    utime = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    is_Delete = models.BooleanField(default=False, verbose_name='删除')
    def __unicode__(self):
        return self.gtitle
    class Meta:
        verbose_name = '类型'  # 改对象名
        verbose_name_plural = "类型列表"  # 改表名



# 包装
class packaging(models.Model):
    pmateria = models.CharField(max_length=8, verbose_name="包装材质",default='纸盒')
    pw = models.IntegerField(verbose_name="长")
    pd = models.IntegerField(verbose_name="宽")
    ph = models.IntegerField(verbose_name="高")
    punti = models.CharField(max_length=4, default='mm', verbose_name="单位")
    ppic = models.ImageField(upload_to='ch_goods', verbose_name='包装图片')
    def __unicode__(self):
        return '%s(%sx%sx%s-%s )' % (self.pmateria, self.pw, self.pd, self.ph, self.punti)
    class Meta:
        verbose_name = '包装'  # 改对象名
        verbose_name_plural = "包装列表"  # 改表名

# 服务
class server(models.Model):
    stitle = models.CharField(max_length=11, verbose_name="服务承诺")
    sico = models.CharField(max_length=32, null=True, verbose_name="服务图标",blank=True)
    scont = models.CharField(max_length=64, verbose_name="服务简介",blank=True)
    def __unicode__(self):
        return self.stitle
    class Meta:
        verbose_name = '服务'  # 改对象名
        verbose_name_plural = "服务列表"  # 改表名

# 瓷画题材
class paintsub(models.Model):
    pstitle = models.CharField(max_length=11, verbose_name='绘画题材')
    def __unicode__(self):
        return self.pstitle
    class Meta:
        verbose_name = '绘画题材'  # 改对象名
        verbose_name_plural = "绘画题材列表"  # 改表名
# 瓷画风格
class paintstyle(models.Model):
    pstitle = models.CharField(max_length=11, verbose_name='绘画风格')
    def __unicode__(self):
        return self.pstitle
    class Meta:
        verbose_name = '绘画风格'  # 改对象名
        verbose_name_plural = "绘画风格列表"  # 改表名
# 瓷画定制
class customgoods(models.Model):
    cgpicsub = models.ForeignKey(paintsub, related_name="customgoods", verbose_name="绘画题材")
    cgpicstyle = models.ForeignKey(paintstyle, related_name="customgoods", verbose_name="绘画风格")
    gsprice = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="定制单价")

# 商品
class goodsinfo(models.Model):
    # 制造商填写内容
    gsupplier = models.ForeignKey(SupplierInfo, verbose_name='制造商', related_name='goods')
    gbrand = models.ForeignKey(brand, verbose_name='品牌', related_name='goods',null=True,blank=True)
    gtitle=models.CharField(max_length=32,verbose_name='商品名称')
    gscode=models.CharField(max_length=32,verbose_name='制造编码',null=True)
    gmaterials_choice=[
        (1,u'高岭土'),
        (2,u'粘土'),
        (3,u'氧化铝'),
    ]
    gmaterials=models.IntegerField(choices=gmaterials_choice,default=1,verbose_name="原料")
    gtechnique_choice=[
        (1,u'手绘'),
        (2,u'贴花'),
        (3,u'彩印'),
        (8,u'其它'),
    ]
    gtechnique=models.IntegerField(choices=gtechnique_choice,default=1,verbose_name="工艺")
    gmax = models.IntegerField(verbose_name="供应数量")
    gsynopsis = HTMLField( verbose_name='产品简介')
    gpack=models.ForeignKey(packaging,related_name='goods',verbose_name='包装')
    gserver=models.ManyToManyField(server,related_name='goods',verbose_name='服务承诺')
    goodstype = models.ManyToManyField(goodstype, related_name='goods', verbose_name='所属商品类型')
    goodsuse=models.ForeignKey(goodsuseinfo,related_name='goods',verbose_name='用途',null=True,blank=True)
    goodscustom=models.OneToOneField(customgoods,related_name="goods",verbose_name="定制",null=True,blank=True)
    ctime = models.DateTimeField(auto_now_add=True, verbose_name="建立时间")
    utime = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __unicode__(self):
        return '%s ID：1000%s - %s'%(self.gsupplier,self.pk,self.gtitle)
    class Meta:
        verbose_name='商品'#改对象名
        verbose_name_plural="商品列表"#改表名


# 商品图片列表
class goodsimages(models.Model):
    gimgoods = models.ForeignKey(goodsinfo, related_name="gim_goods", verbose_name="商品")
    gpic = models.ImageField(upload_to='ch_goods', verbose_name='商品图片')
    gpd = models.IntegerField(verbose_name="图片宽")
    gph = models.IntegerField(verbose_name="图片高")
    gppoint = models.IntegerField(verbose_name="图片位置")
    def __unicode__(self):
        return '%s 位置：%s' % (self.gimgoods, self.gppoint)
    class Meta:
        verbose_name = '图片'  # 改对象名
        verbose_name_plural = "图片列表"  # 改表名


# 器型表
class qixing(models.Model):
    qtitle = models.CharField(max_length=11, verbose_name='名称')
    def __unicode__(self):
        return self.qtitle
    class Meta:
        verbose_name = '器型'  # 改对象名
        verbose_name_plural = "器型列表"  # 改表名

# 规格组合表 作用：用来在商品中形成子类商品
class sjion(models.Model):
    sjgoods=models.ForeignKey(goodsinfo,related_name="sjion",verbose_name="所属商品")
    sjtitle=models.CharField(max_length=11,verbose_name="组合名称")
    sjpic = models.ImageField(upload_to='ch_goods/sjion', verbose_name='规格组合图片', null=True, blank=True)
    def __unicode__(self):
        return self.sjtitle
    class Meta:
        verbose_name = '规格组合'  # 改对象名
        verbose_name_plural = "规格组合列表"  # 改表名


# 器型规格尺寸表 商品组成的最小单元
class size(models.Model):
    sqixing = models.ForeignKey(qixing, related_name="s_qx", verbose_name="所属器型")
    w = models.IntegerField(verbose_name="长")
    d = models.IntegerField(verbose_name="宽")
    h = models.IntegerField(verbose_name="高")
    maxsize=models.CharField(max_length=11,verbose_name="最大外形尺寸",null=True,blank=True)
    unti = models.CharField(max_length=4, default='mm', verbose_name="测量单位")
    oldsize = models.CharField(max_length=5, verbose_name="规格")
    oldunti = models.CharField(max_length=5, default="件", verbose_name="规格单位")
    weight = models.IntegerField(verbose_name="重")
    unit = models.CharField(max_length=4, default='kg', verbose_name="重量单位")
    sprice = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="规格单价")
    # 总位数和小数位数 最大为99999.99
    num = models.IntegerField(verbose_name="规格数量",default=1)
    sizejion = models.ForeignKey(sjion, verbose_name='所属规格组合', related_name='size', blank=True, null=True)
    sgoods = models.ForeignKey(goodsinfo, verbose_name='所属商品', related_name='s_goods', blank=True, null=True)
    spic=models.ImageField(upload_to='ch_goods/size', verbose_name='规格图片',null=True,blank=True)
    def __unicode__(self):
        return '%s 规格：%s %s 尺寸：%sx%sx%s-%s ' % (
        self.sqixing, self.oldsize, self.oldunti, self.w, self.d, self.h, self.unti)
    class Meta:
        verbose_name = '规格尺寸'  # 改对象名
        verbose_name_plural = "器型规格尺寸列表"  # 改表名

# 商品统计
class goodscount(models.Model):
    gcgoods = models.OneToOneField(goodsinfo, verbose_name="商品",related_name='goods_count')
    # 商品统计内容，自动生成
    gclick = models.IntegerField(verbose_name="点击数")
    gcollection = models.IntegerField(verbose_name="购物车数",null=True,blank=True)
    gorder = models.IntegerField(verbose_name="销售数")
    gevalu = models.IntegerField(verbose_name="评论数")
    gback = models.IntegerField(verbose_name="退货数")
    def __unicode__(self):
        return self.gcgoods
    class Meta:
        verbose_name = '商品统计'  # 改对象名
        verbose_name_plural = "商品统计列表"  # 改表名

# 促销活动
# 商品id，活动开始时间，活动结束时间，折扣
class salesgoods(models.Model):
    sstart = models.DateTimeField(verbose_name="活动开始时间")
    send = models.DateTimeField(verbose_name="活动结束时间")
    stitle = models.CharField(max_length=16, verbose_name="活动名称")
    sdiscount = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="折扣",null=True,blank=True)
    def __unicode__(self):
        return self.stitle
    class Meta:
        verbose_name = '促销活动'  # 改对象名
        verbose_name_plural = "促销活动列表"  # 改表名

# 创意众筹管理（对预售商品,必须与平台合作）
'''
众筹用途：
    1，是用来落实想法的，一些想法要落实，必须要成本，那么借助众筹，可以找到有相同爱好的群体，共同驱动。
    2，实现拼团购买，让用户得到更多的实惠，同时实现商家利润。
运作：
    提出想法，制订目标（资金数量）和期限（众筹期限），平台托管资金，到期达到目标就实施，未达到就退回资金。
页面为众筹榜页面和项目页面
'''

class crfdinfo(models.Model):
    ctarget = models.IntegerField(verbose_name="目标金额")
    cmax = models.IntegerField(verbose_name="限制数量", default=1000)  # 默认1000份
    cterm = models.IntegerField(verbose_name="目标期限", default=30)  # 默认30天
    ctime = models.DateTimeField(auto_now_add=True, verbose_name="建立时间", )
    utime = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    cstatus_choice = (
        (0, u'结束众筹'),
        (1, u'正在众筹'),
    )
    cstatus = models.IntegerField(choices=cstatus_choice, default=0, verbose_name="众筹状态")  # 正在众筹，到期结束众筹
    cusernum = models.IntegerField(verbose_name="支持人数")  # 这个实际是个冗余字段，但是因为要频繁读取，就不要去跨表计算
    cclick = models.IntegerField(verbose_name="点击数")
    is_Delete = models.BooleanField(default=0, verbose_name="是否发布")

    class Meta:
        verbose_name = '众筹'  # 改对象名
        verbose_name_plural = "众筹列表"  # 改表名

    def __unicode__(self):
        return self.cstatus


# 商品制造商管理
class goodsmangent(models.Model):
    gmgoods = models.OneToOneField(goodsinfo, verbose_name="商品",related_name="goods_mangment")
    # 平台管理内容，由平台管理人员(网站编辑，审核,财务编辑,财务审核等)填写
    gxprice = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="销售单价率",default=1.2)
    is_Delete = models.BooleanField(default=False, verbose_name='发布')
    gstatus_choice = (
        (0, u'下线'),
        (1, u'上线'),
        (2, u'众筹'),
    )
    gstatus = models.IntegerField(choices=gstatus_choice, verbose_name="状态", default=0)
    grecommendation = models.BooleanField(default=False, verbose_name="推荐")  # 首页某商品分类中的推荐商品
    gcredit=models.IntegerField(default=0,verbose_name="积分",null=True,blank=True)
    gmsales = models.ManyToManyField(salesgoods, verbose_name="商品促销",null=True,blank=True)
    goodscrfd = models.ForeignKey(crfdinfo, verbose_name="众筹",null=True,blank=True)
    ctime = models.DateTimeField(auto_now_add=True, verbose_name="建立时间",)
    utime = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    def __unicode__(self):
        return '%s'%(self.gmgoods)
    class Meta:
        verbose_name = '商品管理'  # 改对象名
        verbose_name_plural = "商品管理列表"  # 改表名




# 积分(从一定程度上理解，积分是用户在购买商品时发生的储蓄，即相当于用户在你这里买了商品，另外又储蓄了积分等额的现金
# ，因此，该积分是有含金量的，应该可以购买东西。实际上是银行的钱。)
# 用户购买某商品，交易成功后，获得积分，积分是全场通用，用来对忠诚用户的奖励。提升用户的含金量。
#         用户在获得积分后，可以在下次购买时使用积分获取等额优惠，
#         或者使用积分换瓷画网馈赠的小礼品瓷（该礼品瓷由瓷画网精心打造，有瓷画网logo，用钱买不到，只能用积分换）。
# 商品id，交易成功后获得积分值，归入商品平台管理。





# 标签(给商品贴标签是吸引用户的手段和对商品的补充，比如对于促销提醒，对于买到1000数量以上的贴‘爆品’标签，对于点击量达到1000的贴‘人气’，
        # 对于编辑推荐的贴‘推荐’等等)
#标签title、标签样式，标签触发条件，标签停止条件

# class lablegm(models.Model):
#     ltitle=models.CharField(max_length=16,verbose_name="标签名")
#     lstlye=models.CharField(max_length=64,verbose_name="标签样式")
#     lstart=models.CharField(max_length=16,verbose_name="标签触发条件")
#     lstop=models.CharField(max_length=16,verbose_name="标签停止条件")
#     class Meta:
#         verbose_name = '标签'  # 改对象名
#         verbose_name_plural = "标签列表"  # 改表名
#     def __unicode__(self):
#         return self.ltitle
#标签先写在字典里



