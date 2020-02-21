#_*_coding:utf-8_*_
'''动态导入模块'''

# from lib.aa import C#从lib包下的aa.py文件中引入C这个类
# obj=C()#实例化该类
# print obj.name


# mod=__import__('lib.aa') #解释器内部用的，只相当于lib
# print mod.aa#mod.aa就是lib.aa
# # obj=mod.aa.C() #这样当然可以实例化，还可以用下面的方式，主要是说明反射方法可以应用于模块（.py文件）
# instance=getattr(mod.aa,'C')#对模块（.py文件）使用反射，这句是lib.aa.C
# print instance
# obj=instance()#实例化
# print obj.name

import importlib #官方建议使用
aa=importlib.import_module('lib.aa')#使用这种方式实现字符串的映射
print aa
obj=aa.C()
print obj.name
print obj.base_dir()
