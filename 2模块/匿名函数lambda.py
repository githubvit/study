def f1():
    def start(e):
        print('start',e)
        return e

    return start

def f2(v):
    print('f2',v)

f2=f1()
print(f2)
print(f2(2))
