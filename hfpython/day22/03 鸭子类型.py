class Foo:
    def f1(self):
        print('from foo.f1')

    def f2(self):
        print('from foo.f2')

class Bar:
    def f1(self):
        print('from bar.f1')

    def f2(self):
        print('from bar.f2')


obj1=Foo()
obj2=Bar()


obj1.f1()
obj1.f2()

obj2.f1()
obj2.f2()




class Disk:
    def read(self):
        print('disk read')

    def write(self):
        print('disk write')


class Txt:
    def read(self):
        print('txt read')

    def write(self):
        print('txt write')


class Process:
    def read(self):
        print('process read')

    def write(self):
        print('process write')


obj1=Disk()
obj2=Txt()
obj3=Process()


obj1.read()
obj2.read()
obj3.read()