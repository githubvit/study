import random

# print(random.random()) #0,1
# print(random.randint(1,3))
# print(random.randrange(1,3))
# print(random.choice([1,'a',[1,2,3]]))
# print(random.sample([1,2,3,4,5],3))
# print(random.uniform(1,3))

# item=[1,3,5,7,9]
# random.shuffle(item)
# print(item)


import random

def make_code(n=5):
    res=''
    for i in range(n):
        s1=str(random.randint(0,9))
        s2=chr(random.randint(65,90))
        res+=random.choice([s1,s2])
    return res

print(make_code(10))