# name=input('名字>>: ')
# age=input('年龄>>: ')
# print('my name is %s my age is %s' %(name,age))

# print('my name is %s my age is %s' %('egon',18))
# print('my name is %s my age is %d' %('egon',18))
x='my name is %s my age is %d' %('egon',18)
print(x)


name=input('name: ')
msg="""
------------ info of %s -----------
Name  : %s
------------- end -----------------
""" %(name,name)
print(msg)