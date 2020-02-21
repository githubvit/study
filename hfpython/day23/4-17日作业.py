4-17日作业
    1、判断一个对象是否属于str类型，判断一个类是否是另外一个类的子类
    2、有俩程序员，一个lili，一个是egon，lili在写程序的时候需要用到egon所写的类(放到了另外一个文件中)，但是egon去跟女朋友度蜜月去了，还没有完成他写的类，
        class FtpClient:
            """
            ftp客户端,但是还么有实现具体的功能
            """
            def __init__(self,addr):
                print('正在连接服务器[%s]' %addr)
                self.addr=addr

            此处应该完成一个get功能


    lili想到了反射，使用了反射机制lili可以继续完成自己的代码，等egon度蜜月回来后再继续完成类的定义并且去实现lili想要的功能。


    3、定义一个老师类，定制打印对象的格式为‘<name:egon age:18 sex:male>’

    4、定义一个自己的open类，控制文件的读或写，在对象被删除时自动回收系统资源

    5、自定义元类，把自定义类的数据属性都变成大写，必须有文档注释，类名的首字母必须大写

    6、用三种方法实现单例模式，参考答案:http://www.cnblogs.com/linhaifeng/articles/8029564.html#_label5