4月16
	1、定义MySQL类（参考答案：http://www.cnblogs.com/linhaifeng/articles/7341177.html#_label5）

	　　1.对象有id、host、port三个属性

	　　2.定义工具create_id，在实例化时为每个对象随机生成id，保证id唯一

	　　3.提供两种实例化方式，方式一：用户传入host和port 方式二：从配置文件中读取host和port进行实例化

	　　4.为对象定制方法，save和get_obj_by_id，save能自动将对象序列化到文件中，文件路径为配置文件中DB_PATH,文件名为id号，保存之前验证对象是否已经存在，若存在则抛出异常，;get_obj_by_id方法用来从文件中反序列化出对象

	2、定义一个类：圆形，该类有半径，周长，面积等属性，将半径隐藏起来，将周长与面积开放
		参考答案（http://www.cnblogs.com/linhaifeng/articles/7340801.html#_label4）


	3、明日默写
		1、简述面向对象三大特性：继承、封装、多态
		2、定义一个人的类，人有名字，身高，体重，用property讲体质参数封装成人的数据属性
		3、简述什么是绑定方法与非绑定方法，他们各自的特点是什么？


	4、完善选课系统作业

