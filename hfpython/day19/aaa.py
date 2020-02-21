import hashlib

m = hashlib.md5()
m.update(b'hello')
m.update(b'1')
m.update(b'2')
print(m.hexdigest()) #9141de76717e095d4dd05f1e686ad6a8
m.update(b'3')
m.update(b'4') #b'hello1234'
print(m.hexdigest()) #9a1996efc97181f0aee18321aa3b3b12


# m1=hashlib.md5()
# m1.update(b'34')
# print(m1.hexdigest()) #e369853df766fa44e1ed0ff613f563bd

m2=hashlib.md5()
m2.update(b'hello1234')
print(m2.hexdigest()) #9a1996efc97181f0aee18321aa3b3b12
