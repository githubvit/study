# 协程 的 结果

async def one():

    return 'res'  

# print(one)      # 1. func 被认可 是函数

# <function one at 0x00000231D6CF50D8>

# print(one())    # 2. func() 不是执行函数 而是生成了 协程对象 

# <coroutine object one at 0x0000021FA909A5C8>

# print(dir(one())) # 3. 协程对象 有哪些方法

# ['__await__', '__class__', '__del__', '__delattr__', '__dir__',
#  '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', 
# '__lt__', '__name__', '__ne__', '__new__', '__qualname__', 
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
# '__sizeof__', '__str__', '__subclasshook__', 
# 'close', 'cr_await', 'cr_code', 'cr_frame', 'cr_origin', 
# 'cr_running', 'send', 'throw']

# one().send(None)    # 4. 协程对象的执行 固定格式： coro_obj.send(None)
# 结果 抛出StopIteration异常，并：结果
# StopIteration: res

try:
    one().send(None)  # 5. 捕捉StopIteration异常和结果。
except StopIteration as e:
    print(e)

async def two(n):
    while n>0:
        print(n)
        n -=1
    return 'two-res'  

# 用普通函数 执行 协程 并 捕获结果
def act_two(n):
    try:
        two(n).send(None)  # 5. 捕捉StopIteration异常和结果。
    except StopIteration as e:
        print(e)   

act_two(10)      

# 结果
    # 10
    # 9
    # 8
    # 7
    # 6
    # 5
    # 4
    # 3
    # 2
    # 1
    # two-res  