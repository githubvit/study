# 聚合：按条件归类或分组
# 如果你有数据存储在MongoDB中，你想做的可能就不仅仅是将数据提取出来那么简单了；
# 你可能希望对数据进行分析并加以利用。MongoDB提供了以下聚合工具：
    #1、聚合框架
    #2、MapReduce(详见MongoDB权威指南)
    #3、几个简单聚合命令：count、distinct和group。(详见MongoDB权威指南)

# 聚合框架：
    # 可以使用多个构件创建一个管道，上一个构件的结果传给下一个构件。
    # 这些构件包括（括号内为构件对应的操作符）：筛选($match)、投射($project)、分组($group)、排序($sort)、限制($limit)、跳过($skip)
    # 不同的管道操作符可以任意组合，重复使用


# 数据准备 pymongo

def data_ready():
    from pymongo import MongoClient
    import datetime
    # 1 连接 mongo 数据库

    client=MongoClient("mongodb://gq:another333@localhost:27017/")
    # client=MongoClient(host=,port=,username=,password=) #关键字方式

    # 2 切换数据库 操作表
    # 切换到db1数据库 use db1
    # db=client.db1
    # db=client['db1']这样也可以

    # 切换到user表 完全和操作mongo的命令一致。
    # db.user.find()
    # db.user.insert()
    # db.user.save()
    # db.user.drop()
    # db.user.update()    
    # db.user.aggregate()    

    # 查询的结果是pymongo对象，循环该对象即可取得每行的记录
    # rows=db.user.find({"_id":{"$gt":10}})
    # for line in rows:
    #     print(line)

    # 3 也可以这样一步搞定 切换到db1数据库建立emp表
    table=client['db1']['emp'] # 相当于切换到 'db1'建立 'emp'表
    # table=client.db1.emp
    # table.drop() 清空表

    # 原始数据
    l=[
    ('egon','male',18,'20170301','老男孩驻沙河办事处外交大使',7300.33,401,1), #以下是教学部
    ('alex','male',78,'20150302','teacher',1000000.31,401,1),
    ('wupeiqi','male',81,'20130305','teacher',8300,401,1),
    ('yuanhao','male',73,'20140701','teacher',3500,401,1),
    ('liwenzhou','male',28,'20121101','teacher',2100,401,1),
    ('jingliyang','female',18,'20110211','teacher',9000,401,1),
    ('jinxin','male',18,'19000301','teacher',30000,401,1),
    ('成龙','male',48,'20101111','teacher',10000,401,1),

    ('歪歪','female',48,'20150311','sale',3000.13,402,2), #以下是销售部门
    ('丫丫','female',38,'20101101','sale',2000.35,402,2),
    ('丁丁','female',18,'20110312','sale',1000.37,402,2),
    ('星星','female',18,'20160513','sale',3000.29,402,2),
    ('格格','female',28,'20170127','sale',4000.33,402,2),

    ('张野','male',28,'20160311','operation',10000.13,403,3), #以下是运营部门
    ('程咬金','male',18,'19970312','operation',20000,403,3),
    ('程咬银','female',18,'20130311','operation',19000,403,3),
    ('程咬铜','male',18,'20150411','operation',18000,403,3),
    ('程咬铁','female',18,'20140512','operation',17000,403,3)
    ]

    # 把原始数据写入表（save方式：有相同id则覆盖无则新增）
    for n,item in enumerate(l):
        d={
            "_id":n,
            'name':item[0],
            'sex':item[1],
            'age':item[2],
            'hire_date':datetime.datetime.strptime(item[3],'%Y%m%d'),
            'post':item[4],
            'salary':item[5]
        }
        table.save(d)

# data_ready()

# 聚合 
    db.table.aggregate()

#  一 筛选（匹配）：$match 
    例： 从 年龄 大于20岁的人中 列出 岗位平均工资 大于10000元 的 岗位
        select post from db1.emp where age>20 group by post having avg(salary)>10000

        # 1 找到年龄大于20的
            select post from db1.emp where age>20
            db.emp.aggregate(
                {"$match":{"age":{"$gt":20}}}
            )
            > db.emp.aggregate(
            ...         {"$match":{"age":{"$gt":20}}}
            ...     )
            { "_id" : 1, "name" : "alex", "sex" : "male", "age" : 78, "hire_date" : ISODate("2015-03-02T00:00:00Z"), "post" : "teacher", "salary" : 1000000.31 }
            { "_id" : 2, "name" : "wupeiqi", "sex" : "male", "age" : 81, "hire_date" : ISODate("2013-03-05T00:00:00Z"), "post" : "teacher", "salary" : 8300 }
            { "_id" : 3, "name" : "yuanhao", "sex" : "male", "age" : 73, "hire_date" : ISODate("2014-07-01T00:00:00Z"), "post" : "teacher", "salary" : 3500 }
            { "_id" : 4, "name" : "liwenzhou", "sex" : "male", "age" : 28, "hire_date" : ISODate("2012-11-01T00:00:00Z"), "post" : "teacher", "salary" : 2100 }
            { "_id" : 7, "name" : "成龙", "sex" : "male", "age" : 48, "hire_date" : ISODate("2010-11-11T00:00:00Z"), "post" : "teacher", "salary" : 10000 }
            { "_id" : 8, "name" : "歪歪", "sex" : "female", "age" : 48, "hire_date" : ISODate("2015-03-11T00:00:00Z"), "post" : "sale", "salary" : 3000.13 }
            { "_id" : 9, "name" : "丫丫", "sex" : "female", "age" : 38, "hire_date" : ISODate("2010-11-01T00:00:00Z"), "post" : "sale", "salary" : 2000.35 }
            { "_id" : 12, "name" : "格格", "sex" : "female", "age" : 28, "hire_date" : ISODate("2017-01-27T00:00:00Z"), "post" : "sale", "salary" : 4000.33 }
            { "_id" : 13, "name" : "张野", "sex" : "male", "age" : 28, "hire_date" : ISODate("2016-03-11T00:00:00Z"), "post" : "operation", "salary" : 10000.13 }
            >
        # 2 找到年龄大于20的 按岗位分组 
            # 分组语法：{"$group":{"_id":分组依据}}  该""_id"不是每行记录的id，而是表示分组唯一的依据是谁的意思
            #  分组依据是岗位字段，不能写"post",要写"$post",表示取的是该字段的值,即岗位，则应该写成：{"$group":{"_id":"$post"}} 
            select post from db1.emp where age>20 group by post
            db.emp.aggregate(
                {"$match":{"age":{"$gt":20}}},
                {"$group":{"_id":"$post"}}
            )
            > db.emp.aggregate(
            ...                 {"$match":{"age":{"$gt":20}}},
            ...                 {"$group":{"_id":"$post"}}
            ...             )
            # 这是聚合后的结果{"_id":"岗位"}
            { "_id" : "teacher" }
            { "_id" : "sale" }
            { "_id" : "operation" }

        # 3 找到年龄大于20的 按岗位分组 并显示 岗位平均工资
            select post,avg(salary)as avg_salary from db1.emp where age>20 group by post 
            db.emp.aggregate(
                {"$match":{"age":{"$gt":20}}},
                {"$group":{"_id":"$post","avg_salay":{"$avg":"$salary"}}}
            )
            > db.emp.aggregate(
            ...                 {"$match":{"age":{"$gt":20}}},
            ...                 {"$group":{"_id":"$post","avg_salay":{"$avg":"$salary"}}}
            ...             )
            { "_id" : "sale", "avg_salay" : 3000.27 }
            { "_id" : "operation", "avg_salay" : 10000.13 }
            { "_id" : "teacher", "avg_salay" : 204780.062 }
            >
            db.emp.aggregate(
                {"$match":{}}, #匹配所有
                {"$group":{"_id":"$post","avg_salay":{"$avg":"$salary"}}}
            )
            > db.emp.aggregate(
            ...                 {"$match":{}},
            ...                 {"$group":{"_id":"$post","avg_salay":{"$avg":"$salary"}}}
            ...             )
            { "_id" : "teacher", "avg_salay" : 151842.90142857144 }
            { "_id" : "老男孩驻沙河办事处外交大使", "avg_salay" : 7300.33 }
            { "_id" : "sale", "avg_salay" : 2600.294 }
            { "_id" : "operation", "avg_salay" : 16800.026 }
            >
        # 4 找到年龄大于20的 按岗位分组 并显示 岗位平均工资  过滤出 岗位平均工资>10000的
            select post,avg(salary)as avg_salary from db1.emp where age>20 group by post having avg(salary)>10000
            db.emp.aggregate(
                {"$match":{"age":{"$gt":20}}},
                {"$group":{"_id":"$post","avg_salay":{"$avg":"$salary"}}},
                {"$match":{"avg_salay":{"$gt":10000}}}
            )
            # 从上面看出一聚合aggregate就是建立了管道，每步把结果放到管道里，下一步从管道取出执行又放到管道里，
            # 每步都从管道里拿上一步输出的结果作为输入。
            > db.emp.aggregate(
            ...                 {"$match":{"age":{"$gt":20}}},
            ...                 {"$group":{"_id":"$post","avg_salay":{"$avg":"$salary"}}},
            ...                 {"$match":{"avg_salay":{"$gt":10000}}}
            ...             )
            { "_id" : "teacher", "avg_salay" : 204780.062 }
            { "_id" : "operation", "avg_salay" : 10000.13 }
            >

            > db.emp.aggregate(
            ... {'$match':{}},
            ... {'$group':{'_id':'$post','avg_salary':{'$avg':'$salary'}}},
            ... {'$match':{'avg_salary':{'$gte':10000}}}
            ... )
            { "_id" : "teacher", "avg_salary" : 151842.90142857144 }
            { "_id" : "operation", "avg_salary" : 16800.026 }
            >


# 二 投射：$project 把数据处理成自己想要的新数据
    把原始数据处理成新的数据，基于新数据进行聚合;或者把聚合后的数据处理成新数据；都可以用投射$project。
    # 语法：
        {"$project":{"要保留的字段":1,"要去掉的字段":0,"新增的字段":"表达式"}}
    
    
    例：取出平均年薪大于1000000的部门 
        # 1 先把原来的数据处理成只保留岗位即部门和年薪"annual_salary"的样子
        db.emp.aggregate(
            {"$project":{"_id":0,"post":1,"annual_salary":{"$multiply":[12,"$salary"]}}}           
        )
        > db.emp.aggregate(
        ...         {"$project":{"_id":0,"post":1,"annual_salary":{"$multiply":[12,"$salary"]}}}
        ...     )
        { "post" : "老男孩驻沙河办事处外交大使", "annual_salary" : 87603.95999999999 }
        { "post" : "teacher", "annual_salary" : 12000003.72 }
        { "post" : "teacher", "annual_salary" : 99600 }
        { "post" : "teacher", "annual_salary" : 42000 }
        { "post" : "teacher", "annual_salary" : 25200 }
        { "post" : "teacher", "annual_salary" : 108000 }
        { "post" : "teacher", "annual_salary" : 360000 }
        { "post" : "teacher", "annual_salary" : 120000 }
        { "post" : "sale", "annual_salary" : 36001.56 }
        { "post" : "sale", "annual_salary" : 24004.199999999997 }
        { "post" : "sale", "annual_salary" : 12004.44 }
        { "post" : "sale", "annual_salary" : 36003.479999999996 }
        { "post" : "sale", "annual_salary" : 48003.96 }
        { "post" : "operation", "annual_salary" : 120001.56 }
        { "post" : "operation", "annual_salary" : 240000 }
        { "post" : "operation", "annual_salary" : 228000 }
        { "post" : "operation", "annual_salary" : 216000 }
        { "post" : "operation", "annual_salary" : 204000 }
        >

        # 2 再基于新表聚合部门，并显示部门平均年薪
        db.emp.aggregate(
            {"$project":{"_id":0,"post":1,"annual_salary":{"$multiply":[12,"$salary"]}}},
            {"$group":{"_id":"$post","平均年薪":{"$avg":"$annual_salary"}}}
        )
        > db.emp.aggregate(
        ...         {"$project":{"_id":0,"post":1,"annual_salary":{"$multiply":[12,"$salary"]}}},
        ...         {"$group":{"_id":"$post","平均年薪":{"$avg":"$annual_salary"}}}
        ...     )
        { "_id" : "teacher", "平均年薪" : 1822114.8171428572 }
        { "_id" : "老男孩驻沙河办事处外交大使", "平均年薪" : 87603.95999999999 }
        { "_id" : "sale", "平均年薪" : 31203.528 }
        { "_id" : "operation", "平均年薪" : 201600.312 }
        >

        # 3 过滤出平均年薪大于1000000的部门
        db.emp.aggregate(
            {"$project":{"_id":0,"post":1,"annual_salary":{"$multiply":[12,"$salary"]}}},
            {"$group":{"_id":"$post","平均年薪":{"$avg":"$annual_salary"}}},
            {"$match":{"平均年薪":{"$gt":1000000}}}
        )
        > db.emp.aggregate(
        ...             {"$project":{"_id":0,"post":1,"annual_salary":{"$multiply":[12,"$salary"]}}},
        ...             {"$group":{"_id":"$post","平均年薪":{"$avg":"$annual_salary"}}},
        ...             {"$match":{"平均年薪":{"$gt":1000000}}}
        ...         )
        { "_id" : "teacher", "平均年薪" : 1822114.8171428572 }
        >

        # 4 把""_id"改成 "部门",再次投射
        db.emp.aggregate(
            {"$project":{"_id":0,"post":1,"annual_salary":{"$multiply":[12,"$salary"]}}},  #投射
            {"$group":{"_id":"$post","平均年薪":{"$avg":"$annual_salary"}}},                #分组
            {"$match":{"平均年薪":{"$gt":1000000}}},                                        #筛选
            {"$project":{"_id":0,"部门":"$_id","平均年薪":1}}                               #再次投射
        )
        > db.emp.aggregate(
        ...             {"$project":{"_id":0,"post":1,"annual_salary":{"$multiply":[12,"$salary"]}}},
        ...             {"$group":{"_id":"$post","平均年薪":{"$avg":"$annual_salary"}}},
        ...             {"$match":{"平均年薪":{"$gt":1000000}}},
        ...             {"$project":{"_id":0,"部门":"$_id","平均年薪":1}}
        ...         )
        { "平均年薪" : 1822114.8171428572, "部门" : "teacher" }
        >
    # 1 表达式之数学表达式
        {"$add":[expr1,expr2,...,exprN]} #相加
        {"$subtract":[expr1,expr2]} #第一个减第二个
        {"$multiply":[expr1,expr2,...,exprN]} #相乘
        {"$divide":[expr1,expr2]} #第一个表达式除以第二个表达式的商作为结果
        {"$mod":[expr1,expr2]} #第一个表达式除以第二个表达式得到的余数作为结果

    # 2 表达式之日期表达式:
        # $year,$month,$week,$dayOfMonth,$dayOfWeek,$dayOfYear,$hour,$minute,$second

        # 设置 'hire_date'字段就是按照datatime模块的strptime格式，等于mongodb的日期数据类型，所以可以直接取年月日
            #  'hire_date':datetime.datetime.strptime(item[3],'%Y%m%d'),

        显示name字段和入职年份hire_year，由原来的入职日期取出年份即可 {"$year":"$hire_date"}
        #例如：select name,date_format("%Y") as hire_year from db1.emp
        db.emp.aggregate(
            {"$project":{"name":1,"hire_year":{"$year":"$hire_date"}}}
        )

        #例如查看每个员工的工作多长时间 用当前年份减去入职年份即可
        db.emp.aggregate({
            "$project":{
                "name":1,
                "hire_period":{
                    "$subtract":[ {"$year":new Date()}, {"$year":"$hire_date"}]
                }
            }
        })
    
    
    # 3 字符串表达式
        {"$substr":[字符串/$值为字符串的字段名,起始位置,截取几个字节]}
            mongdb默认是"utf-8"编码，对应汉字是3字节表示一个汉字。
            emp表中的name字段中有些是中文表示，当要截取字符串时，"$substr"是按照字节截取。
            因此，必须按3字节的倍数截取"$substr":["$name",0,3]，否则报错。
            # 取除名字为egon外的其余人的名字的前3个字节
                db.emp.aggregate(
                    {"$match":{"name":{"$ne":"egon"}}},
                    {"$project":{
                        "new_name":{
                            "$substr":["$name",0,3]
                        }
                    }}
                    )

                { "_id" : 1, "new_name" : "ale" }
                { "_id" : 2, "new_name" : "wup" }
                { "_id" : 3, "new_name" : "yua" }
                { "_id" : 4, "new_name" : "liw" }
                { "_id" : 5, "new_name" : "jin" }
                { "_id" : 6, "new_name" : "jin" }
                { "_id" : 7, "new_name" : "成" }
                { "_id" : 8, "new_name" : "歪" }
                { "_id" : 9, "new_name" : "丫" }
                { "_id" : 10, "new_name" : "丁" }
                { "_id" : 11, "new_name" : "星" }
                { "_id" : 12, "new_name" : "格" }
                { "_id" : 13, "new_name" : "张" }
                { "_id" : 14, "new_name" : "程" }
                { "_id" : 15, "new_name" : "程" }
                { "_id" : 16, "new_name" : "程" }
                { "_id" : 17, "new_name" : "程" }
                >
            # 取除名字为egon外的其余人的名字的前4个字节 "$substr":["$name",0,4] 报错
                > db.emp.aggregate(
                ...                 {"$match":{"name":{"$ne":"egon"}}},
                ...                 {"$project":{
                ...                     "new_name":{
                ...                         "$substr":["$name",0,4]
                ...                     }
                ...                 }}
                ...                 )
                2020-04-11T22:58:59.425+0800 E  QUERY    [js] uncaught exception: Error: command failed: {
                        "ok" : 0,
                        "errmsg" : "$substrBytes:  Invalid range, ending index is in the middle of a UTF-8 character.",
                        "code" : 28657,
                        "codeName" : "Location28657"
                } : aggregate failed :
                _getErrorWithCode@src/mongo/shell/utils.js:25:13
                doassert@src/mongo/shell/assert.js:18:14
                _assertCommandWorked@src/mongo/shell/assert.js:583:17
                assert.commandWorked@src/mongo/shell/assert.js:673:16
                DB.prototype._runAggregate@src/mongo/shell/db.js:266:5
                DBCollection.prototype.aggregate@src/mongo/shell/collection.js:1012:12
                @(shell):1:1
                >


        {"$concat":[expr1,expr2,...,exprN]} # 指定的表达式或字符串连接在一起返回,只支持字符串拼接
        {"$toLower":expr}
        {"$toUpper":expr}
    
        db.emp.aggregate( {"$project":{"NAME":{"$toUpper":"$name"}}})
    
    # 4 逻辑表达式
        $and
        $or
        $not  


# 三 分组：$group
    {"$group":{"_id":分组字段,"新的字段名":聚合操作符}}

    {"$group":{"_id":"$sex"}} #按照性别分组
    {"$group":{"_id":"$post"}} #按照职位分组
    {"$group":{"_id":{"state":"$state","city":"$city"}}} #按照多个字段分组，比如按照州市分组


    sql聚合操作符：max\min\sum\avg\count\group_concat

    聚合操作符：$sum、$avg、$max、$min、$first、$last
        对应sql count统计  mongdb 使用 {"$sum":1} 表示来一个加一个。
        对应sql group_concat (将group by产生的同一个分组中的值连接起来，返回一个字符串结果)
        mongodb 可以使用 数组将group by产生的同一个分组中的值加进来，可以用push或addtoset去重的方式来解决。


    select post,max(age),min(id),avg(salary),count(1),group_concat(name) from db1.emp group by post
    db.emp.aggregate(
        {"$group":{
            "_id":"$post", # 分组依据：按部门
            "max_age":{"$max":"$age"},          # 本组中最大年龄
            "min_id":{"$min":"$_id"},           # 本组中最小的id
            "avg_salary":{"$avg":"$salary"},    # 本组平均工资
            "sum_salary":{"$sum":"$salary"},    # 本组工资总额
            "count":{"$sum":1},                 # 统计本组记录数
            "names":{"$push":"$name"}           # 把同组中的名字放进一个列表
        }}
    ).pretty()

        {
                "_id" : "teacher",
                "max_age" : 81,
                "min_id" : 1,
                "avg_salary" : 151842.90142857144,
                "sum_salary" : 1062900.31,
                "count" : 7,
                "names" : [
                        "alex",
                        "wupeiqi",
                        "yuanhao",
                        "liwenzhou",
                        "jingliyang",
                        "jinxin",
                        "成龙"
                ]
        }
        {
                "_id" : "老男孩驻沙河办事处外交大使",
                "max_age" : 18,
                "min_id" : 0,
                "avg_salary" : 7300.33,
                "sum_salary" : 7300.33,
                "count" : 1,
                "names" : [
                        "egon"
                ]
        }
        {
                "_id" : "sale",
                "max_age" : 48,
                "min_id" : 8,
                "avg_salary" : 2600.294,
                "sum_salary" : 13001.47,
                "count" : 5,
                "names" : [
                        "歪歪",
                        "丫丫",
                        "丁丁",
                        "星星",
                        "格格"
                ]
        }
        {
                "_id" : "operation",
                "max_age" : 28,
                "min_id" : 13,
                "avg_salary" : 16800.026,
                "sum_salary" : 84000.13,
                "count" : 5,
                "names" : [
                        "张野",
                        "程咬金",
                        "程咬银",
                        "程咬铜",
                        "程咬铁"
                ]
        }
        >

        db.emp.aggregate(
            {"$group":{
                "_id":"$post", 
                "max_age":{"$max":"$age"},          
                "min_id":{"$min":"$_id"},           
                "avg_salary":{"$avg":"$salary"},    
                "sum_salary":{"$sum":"$salary"},    
                "count":{"$sum":1},                 
                "names":{"$push":"$name"},           
                "ids":{"$push":"$_id"}         
            }}
        ).pretty()

# 四 排序：$sort、限制：$limit、跳过：$skip
    {"$sort":{"字段名":1,"字段名":-1}} # 1升序，-1降序
    {"$limit":n} # 取n个
    {"$skip":n}  # 跳过多少个文档

    #例1、取平均工资最高的前两个部门
    db.emp.aggregate(
        {
            "$group":{"_id":"$post","平均工资":{"$avg":"$salary"}}
        },
        {
            "$sort":{"平均工资":-1}
        },
        {
            "$limit":2
        }
    )
    #例2、取平均工资第2高和第3高的部门
    db.emp.aggregate(
        {
            "$group":{"_id":"$post","平均工资":{"$avg":"$salary"}}
        },
        {
            "$sort":{"平均工资":-1}
        },
        {
            "$skip":1
        },
        {
            "$limit":2
        }
    )

# 五 随机选取n个：{"$sample":{"size":n}}
    #集合users包含的文档如下
    { "_id" : 1, "name" : "dave123", "q1" : true, "q2" : true }
    { "_id" : 2, "name" : "dave2", "q1" : false, "q2" : false  }
    { "_id" : 3, "name" : "ahn", "q1" : true, "q2" : true  }
    { "_id" : 4, "name" : "li", "q1" : true, "q2" : false  }
    { "_id" : 5, "name" : "annT", "q1" : false, "q2" : true  }
    { "_id" : 6, "name" : "li", "q1" : true, "q2" : true  }
    { "_id" : 7, "name" : "ty", "q1" : false, "q2" : true  }

    #下述操作时从users集合中随机选取3个文档
    db.users.aggregate(
       [ { "$sample": { "size": 3 } } ]
    )

# mongodb 图形化操作界面 Robo 3T https://robomongo.org/download  类似于mysql的navicat
    # MongoDB可视化工具--Robo 3T 使用教程 https://www.bbsmax.com/A/obzb7V2BJE/
    # 注意：
        # 聚合时无效：限制：$limit、跳过：$skip 是没有效果的。
            db.emp.aggregate(
                {
                    "$group":{"_id":"$post","平均工资":{"$avg":"$salary"}}
                },
                {
                    "$sort":{"平均工资":-1}
                },
                # 下面两条是无效的，Robo会都展示出来
                {
                    "$skip":1
                },
                {
                    "$limit":2
                }
            )

        # 查询的分页limit和跳过skip是有效的。
            db.user.find().limit(2).skip(2)