import shelve
# info1={'age':18,'height':180,'weight':80}
# info2={'age':73,'height':150,'weight':80}
#
# d=shelve.open('db.shv')
# d['egon']=info1
# d['alex']=info2
# d.close()


# d=shelve.open('db.shv')
# # print(d['egon'])
# # print(d['alex'])
# d.close()


# d=shelve.open('db.shv',writeback=True)
# d['alex']['age']=10000
# # print(d['alex'])
# d.close()


# d=shelve.open('db.shv',writeback=True)
# print(d['alex'])
# d.close()


import json

l={'a':1,'b':2,'c':3}
json.dump(l,open('a.json','wt',encoding='utf-8'))

