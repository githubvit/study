# import abc
# class File(metaclass=abc.ABCMeta): #同一类事物:文件
#     @abc.abstractmethod
#     def clickk(self):
#         pass


class Text: #文件的形态之一:文本文件
    def click(self):
        print('open file')

class ExeFile: #文件的形态之二:可执行文件
    def click(self):
        print('execute file')

class Process:
    def click(self):
        pass



