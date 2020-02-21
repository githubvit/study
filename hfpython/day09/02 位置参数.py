'''
1、位置参数
    位置即顺序，位置参参数指的就是按照从左到右的顺序依次定义的参数

2、分两种








'''
#2.1 在定义函数时，按照位置定义的形参，称为位置形参
def foo(x,y,z):
    print(x,y,z)

#注意：
#位置形参的特性是：在调用函数时必须为其传值，而且多一个不行，少一个也不行

# foo(1,2) #TypeError: foo() missing 1 required positional argument: 'z'
# foo(1,2,3,4) #TypeError: foo() takes 3 positional arguments but 4 were given




#2.2 在调用函数时，按照位置定义的实参，称为位置实参
#注意：位置实参会与形参一一对应
foo(1,3,2)