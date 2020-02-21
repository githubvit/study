#_*_coding:utf-8_*_
import os
class C:

    def __init__(self):
        self.name = 'alex'
    def base_dir(self):
        Base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return Base_path

# --------test
# test_c=C()
# print test_c.name
# print test_c.base_dir()