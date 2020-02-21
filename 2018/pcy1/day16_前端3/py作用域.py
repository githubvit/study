#_*_coding:utf-8_*_
''''''
xo='alex'
def f1():
    xo='tony'
    def f2():
        print xo
    xo='eric'
    return  f2
name=f1()
# name()
