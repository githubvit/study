# 使用  
        
    # 库
        在mongodb里，没有创建数据库和创建表的命令，只有插入记录的命令。
        空的数据库和空的表永远不会显示。
        怎么建库呢，切换即创建库，比如原来没有db1库,use db1 即可。
        就是没有也可以切换，use db1,
        但是 show dbs 是看不到db1，因为此时db1为空。
        '''
        > use db1
        switched to db db1
        > db
        db1
        > show dbs
        admin   0.000GB
        config  0.000GB
        local   0.000GB
        >
        '''
        # 增
            use db1     # 有则切换，无则新增
        # 查
            show dbs    #查看所有数据库
            db          #查看当前数据库
        
        # 删
            db.dropDatabase()   #所谓删除当前数据库 实际上是清空了数据，数据库不是建的，是有数据才有的，空数据库不显示。
            
            # 删除db1数据库
            > show dbs
            admin   0.000GB
            config  0.000GB
            db1     0.000GB
            local   0.000GB
            test    0.000GB
            > use db1           # 切换到数据库db1
            switched to db db1
            > db.dropDatabase() # 删除当前数据库db1
            { "dropped" : "db1", "ok" : 1 }
            > show dbs          # 因为清空了数据 所以 db1 不显示。
            admin   0.000GB
            config  0.000GB
            local   0.000GB
            test    0.000GB
            > db                #继续查看当前数据库 还是在db1，因此，所谓删除当前数据库 实际上是清空了数据，
            db1
            >

    # 集合（表）
        # 增
            db.集合（表）
            db.user
            但是此时，show tables 是看不见user的，user为空。
            db.user.info
            表用点命名，表明名义上的逻辑关系。表的命名空间有120个字符。
            user表和user.info表只有名义上的逻辑关系，实际是两个独立的关系，没有任何瓜葛。

            '''
            > db.user.insert({"_id":1,"name":"alex"})
            WriteResult({ "nInserted" : 1 })
            > db.user.find()
            { "_id" : 1, "name" : "alex" }
            > db.user.info.insert({"age":18,"sex":"m"})
            WriteResult({ "nInserted" : 1 })
            > show tables 
            user
            user.info
            >
            '''
        # 查
            show collections
            show tables         #为了和原来关系型数据库保持一致
            db.user.help()      #查看 user表的操作 帮助
            '''
            > db.user             建表或集合
            db1.user
            > show collections    查看  空 不显示
            > show tables
            >
            > db.user.insert({"_id":1,"name":"egon"})  在user表中插入一条记录或称一个文档
            WriteResult({ "nInserted" : 1 })           
            > show tables                              此时查看 可以看到 当前数据库中不为空的表
            user
            > show collections
            user
            >
            > show dbs                                 此时 db1数据库不为空 用数据库查看命令也可以看到 db1数据库
            admin   0.000GB
            config  0.000GB
            db1     0.000GB
            local   0.000GB
            > db.user.help()                           查看user表的帮助 
            DBCollection help
                    db.user.find().help() - show DBCursor help
                    。。。
                    db.user.drop() drop the collection
                    。。。
                    db.user.latencyStats() - display operation latency histograms for this collection
            >
            '''
        # 删
            db.user.drop() #删除 user表
            '''
            > db.user.info.drop()
            true
            > show tables
            user
            >
            '''

    # 文档（记录）
        # 增 
            insert（{mongodb数据}）
            db.user.insert({"_id":1,"name":"egon"})
            
            mongodb的数据类型
                数据结构：{key：value}键值对形式。
                key的数据类型就是字符串，用双引号“”，value的类型如下：
                    包括Json的六种基本类型（字符串、数字、数组、对象、布尔、Null），还增加了日期、正则、ObjectId（对象id）

            # 在t1表插入一行包含日期、正则、ObjectId（对象id）三种类型的数据。
                > db.t1.insert({"x":new Date(),"pattern":/^egon.*?$/i,"z":ObjectId()})
                WriteResult({ "nInserted" : 1 })
                # 正则写在／／内，后面的i代表:
                    # i 忽略大小写
                    # m 多行匹配模式
                    # x 忽略非转义的空白字符
                    # s 单行匹配模式

            # 查看插入的结果
                > db.t1.find()
                { "_id" : ObjectId("5e8fe6bdc674d55a3e7b2b3a"), "x" : ISODate("2020-04-10T03:23:41.387Z"), "pattern" : /^egon.*?$/i, "z" : ObjectId("5e8fe6bdc674d55a3e7b2b39") }
            
            # 查看结果，并美化输出。
                > db.t1.find().pretty()
                {
                        "_id" : ObjectId("5e8fe6bdc674d55a3e7b2b3a"),#发现了“_id”字段，尽管我们没有插入该字段，但mongodb会自动插入，值为ObjectId（对象id）类型。
                        "x" : ISODate("2020-04-10T03:23:41.387Z"),
                        "pattern" : /^egon.*?$/i,
                        "z" : ObjectId("5e8fe6bdc674d55a3e7b2b39")
                }
                >

            关于 ObjectId（对象id）：
                ObjectId是"_id"的默认类型。因为设计MongoDb的初衷就是用作分布式数据库，所以能够在分片环境中生成
                唯一的标识符非常重要，而常规的做法：在多个服务器上同步自动增加主键既费时又费力，这就是MongoDB采用
                ObjectId的原因。
                ObjectId采用12字节的存储空间，是一个由24个十六进制数字组成的字符串
                    0|1|2|3|   4|5|6|     7|8    9|10|11    
                    时间戳      机器      PID    计数器

                时间戳、机器mac地址、进程号PID、同一个进程内的第几次请求

                标明 该记录 是 在 什么时间 由 哪一台机器 的 什么进程 发送的 第几次请求 建立的。


                对象id的作用：
                    1 对象id保证了记录的唯一性，记载了大量有用的信息，可以通过一些接口取出这些相关信息。  

                    2 便于分布式布置，分散压力，提高效率、提高健壮性。

                #创建ObjectId
                > newObjectId = ObjectId()
                ObjectId("5ece005ddeef26fe3d1e092c")
                # 用变量名从ObjectId获取时间 报错
                > ObjectId(newObjectId).getTimestamp()
                2020-05-27T13:56:44.852+0800 E  QUERY    [js] Error: invalid object id: length :
                @(shell):1:1
                >
                # 用创建的ObjectId获取时间 成功 这个时间是国际时即ISO时间不是中国时区 在’T05:53:33Z‘要+8，北京时间应该是13:53:33.
                > ObjectId("5ece005ddeef26fe3d1e092c").getTimestamp()
                ISODate("2020-05-27T05:53:33Z")

            单行插入insert(user0)
            多行插入insertMany([user1,user2,user3,user4])
                > db.user.drop()
                true
                > user0={
                ...     "name":"egon",
                ...     "age":10,
                ...     'hobbies':['music','read','dancing'],
                ...     'addr':{
                ...         'country':'China',
                ...         'city':'BJ'
                ...     }
                ... }
                {
                        "name" : "egon",
                        "age" : 10,
                        "hobbies" : [
                                "music",
                                "read",
                                "dancing"
                        ],
                        "addr" : {
                                "country" : "China",
                                "city" : "BJ"
                        }
                }
                # 单行插入
                > db.user.insert(user0)
                WriteResult({ "nInserted" : 1 })
                > db.user.find()
                { "_id" : ObjectId("5e8ffb00c674d55a3e7b2b3b"), "name" : "egon", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }
                > user1={
                ...     "_id":1,
                ...     "name":"alex",
                ...     "age":10,
                ...     'hobbies':['music','read','dancing'],
                ...     'addr':{
                ...         'country':'China',
                ...         'city':'weifang'
                ...     }
                ... }
                {
                        "_id" : 1,
                        "name" : "alex",
                        "age" : 10,
                        "hobbies" : [
                                "music",
                                "read",
                                "dancing"
                        ],
                        "addr" : {
                                "country" : "China",
                                "city" : "weifang"
                        }
                }
                > user2={
                ...     "_id":2,
                ...     "name":"wupeiqi",
                ...     "age":20,
                ...     'hobbies':['music','read','run'],
                ...     'addr':{
                ...         'country':'China',
                ...         'city':'hebei'
                ...     }
                ... }
                {
                        "_id" : 2,
                        "name" : "wupeiqi",
                        "age" : 20,
                        "hobbies" : [
                                "music",
                                "read",
                                "run"
                        ],
                        "addr" : {
                                "country" : "China",
                                "city" : "hebei"
                        }
                }
                > user3={
                ...     "_id":3,
                ...     "name":"yuanhao",
                ...     "age":30,
                ...     'hobbies':['music','drink'],
                ...     'addr':{
                ...         'country':'China',
                ...         'city':'heibei'
                ...     }
                ... }
                {
                        "_id" : 3,
                        "name" : "yuanhao",
                        "age" : 30,
                        "hobbies" : [
                                "music",
                                "drink"
                        ],
                        "addr" : {
                                "country" : "China",
                                "city" : "heibei"
                        }
                }
                > user4={
                ...     "_id":4,
                ...     "name":"jingliyang",
                ...     "age":40,
                ...     'hobbies':['music','read','dancing','tea'],
                ...     'addr':{
                ...         'country':'China',
                ...         'city':'BJ'
                ...     }
                ... }
                {
                        "_id" : 4,
                        "name" : "jingliyang",
                        "age" : 40,
                        "hobbies" : [
                                "music",
                                "read",
                                "dancing",
                                "tea"
                        ],
                        "addr" : {
                                "country" : "China",
                                "city" : "BJ"
                        }
                }
                > user5={
                ...     "_id":5,
                ...     "name":"jinxin",
                ...     "age":50,
                ...     'hobbies':['music','read',],
                ...     'addr':{
                ...         'country':'China',
                ...         'city':'henan'
                ...     }
                ... }
                {
                        "_id" : 5,
                        "name" : "jinxin",
                        "age" : 50,
                        "hobbies" : [
                                "music",
                                "read"
                        ],
                        "addr" : {
                                "country" : "China",
                                "city" : "henan"
                        }
                }
                # 多行插入 由于user0没有"_id",所以可以再次插入
                > db.user.insertMany([user1,user2,user3,user4,user5,user0])
                {
                        "acknowledged" : true,
                        "insertedIds" : [
                                1,
                                2,
                                3,
                                4,
                                5,
                                ObjectId("5e8ffbe6c674d55a3e7b2b3c")
                        ]
                }
                > db.user.find()
                { "_id" : ObjectId("5e8ffb00c674d55a3e7b2b3b"), "name" : "egon", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }
                { "_id" : 1, "name" : "alex", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "weifang" } }
                { "_id" : 2, "name" : "wupeiqi", "age" : 20, "hobbies" : [ "music", "read", "run" ], "addr" : { "country" : "China", "city" : "hebei" } }
                { "_id" : 3, "name" : "yuanhao", "age" : 30, "hobbies" : [ "music", "drink" ], "addr" : { "country" : "China", "city" : "heibei" } }
                { "_id" : 4, "name" : "jingliyang", "age" : 40, "hobbies" : [ "music", "read", "dancing", "tea" ], "addr" : { "country" : "China", "city" : "BJ" } }
                { "_id" : 5, "name" : "jinxin", "age" : 50, "hobbies" : [ "music", "read" ], "addr" : { "country" : "China", "city" : "henan" } }
                { "_id" : ObjectId("5e8ffbe6c674d55a3e7b2b3c"), "name" : "egon", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }
                >

            save有相同的"_id"则覆盖,无则新增
            db.t1.save({"_id":1,"z"})

                > db.t1.drop()
                true
                > db.t1.insert({"_id":1,"a":1,"b":2})
                WriteResult({ "nInserted" : 1 })
                > db.t1.find()
                { "_id" : 1, "a" : 1, "b" : 2 }
                # 有相同"_id"则覆盖
                > db.t1.save({"_id":1,"z":1})
                WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
                > db.t1.find()
                { "_id" : 1, "z" : 1 }
                # 无相同"_id"则新增
                > db.t1.save({"e":2})
                WriteResult({ "nInserted" : 1 })
                > db.t1.find()
                { "_id" : 1, "z" : 1 }
                { "_id" : ObjectId("5e901dbec674d55a3e7b2b3d"), "e" : 2 }
                >
        # 查
            db.t1.find()    # 查所有 select * from db.t1 
            db.t1.find().pretty() # 查看结果，并美化输出。
            db.t1.findOne() # 查一个

            # 1 比较运算
                # 运算符比较
                #   SQL     MongoDB：
                    # =     {key:value}代表什么等于什么, 不仅限于数字,
                    # !=    "$ne",不仅限于数字,
                    # >     "$gt",
                    # <     "$lt",
                    # >=    "gte",
                    # <=    "lte",
                    # 其中"$ne"能用于所有数据类型

                # 例
                #1、select * from db1.user where name = "alex";
                db.user.find({'name':'alex'})
                
                #2、select * from db1.user where name != "alex";
                db.user.find({"name":{"$ne":"alex"}})
                
                #3、select * from db1.user where id > 2;
                db.user.find({'_id':{'$gt':2}})
                
                #4、select * from db1.user where id < 3;
                db.user.find({'_id':{'$lt':3}})
                
                #5、select * from db1.user where id >= 2;
                db.user.find({"_id":{"$gte":2,}})
                
                #6、select * from db1.user where id <= 2;
                db.user.find({"_id":{"$lte":2}})

            # 2 逻辑运算
                # SQL：and，or，not
                # MongoDB：
                    # and 
                        # 字典中逗号分隔的多个条件是and关系
                        # select * from db1.user where id >= 5 and name = "alex";
                        {{'_id':{"$gte":5}},{"name":"alex"}}

                        # 或
                        {
                        "$and":[
                            {'_id':{"$gte":5}},
                            {"name":"alex"}
                            ]
                        }
                    # or
                        # select * from db1.user where id >= 5 or name = "alex";
                        {
                        "$or":[
                            {'_id':{"$gte":5}},
                            {"name":"alex"}
                            ]
                        }
                    # not 
                        # select * from db1.user where id % 2=1
                        {"$not":{"$mod":[2,1]}}

                    

                #1、select * from db1.user where id >= 2 and id < 4;
                db.user.find({'_id':{"$gte":2,"$lt":4}})

                #2、select * from db1.user where id >= 2 and age < 40;
                db.user.find({"_id":{"$gte":2},"age":{"$lt":40}})

                #3、select * from db1.user where id >= 5 or name = "alex";
                db.user.find({
                    "$or":[
                        {'_id':{"$gte":5}},
                        {"name":"alex"}
                        ]
                })
                

                #4、select * from db1.user where id % 2=1; 取奇, 对2取余,余1 应该是1,3,5...奇数
                db.user.find({'_id':{"$mod":[2,1]}})

                #5、上题，对取奇取反 ,即取偶
                db.user.find({'_id':{"$not":{"$mod":[2,1]}}})

            # 3 成员运算
                # SQL：in，not in
                # MongoDB："$in","$nin"

                #1、select * from db1.user where age in (20,30,31);
                db.user.find({"age":{"$in":[20,30,31]}})

                #2、select * from db1.user where name not in ('alex','yuanhao');
                db.user.find({"name":{"$nin":['alex','yuanhao']}})

                

            # 4 正则运算
                # SQL: regexp 正则
                # MongoDB: /正则表达/i

                #1、select * from db1.user where name regexp '^j.*?(g|n)$';
                db.user.find({'name':/^j.*?(g|n)$/i}) #找到name字段以j开头,以g或n结尾的文档

            # 5 返回指定字段
                db.user.find({'name':/^j.*?(g|n)$/i},{需要的字段1:1,需要的字段2:1}) 这样还有"_id"
                    > db.user.find({'name':/^j.*?(g|n)$/i},{'name':1,'age':1})
                    { "_id" : 4, "name" : "jingliyang", "age" : 40 }
                    { "_id" : 5, "name" : "jinxin", "age" : 50 }

                db.user.find({'name':/^j.*?(g|n)$/i},{需要的字段1:1,需要的字段2:1,"_id":0}) 这样就没有"_id"
                    > db.user.find({'name':/^j.*?(g|n)$/i},{'_id':0,'name':1,'age':1})
                    { "name" : "jingliyang", "age" : 40 }
                    { "name" : "jinxin", "age" : 50 }

            # 6 查询 数组 "hobbies"
                # 查找"hobbies"有'dancing'的
                    > db.user.find({"hobbies":'dancing'})
                    { "_id" : ObjectId("5e8ffb00c674d55a3e7b2b3b"), "name" : "egon", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }
                    { "_id" : 1, "name" : "alex", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "weifang" } }
                    { "_id" : 4, "name" : "jingliyang", "age" : 40, "hobbies" : [ "music", "read", "dancing", "tea" ], "addr" : { "country" : "China", "city" : "BJ" } }
                    { "_id" : ObjectId("5e8ffbe6c674d55a3e7b2b3c"), "name" : "egon", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }
                    >

                # 查找"hobbies"既有'dancing'又有'tea'的      "$all"关键字
                    db.user.find({
                        "hobbies":{'dancing','tea'} 错
                    })
                    # 报错
                    2020-04-10T18:11:11.915+0800 E  QUERY    [js] uncaught exception: SyntaxError: missing : after property id :
                    @(shell):2:37
                    
                    # 条件的写法要用:{"$all":['dancing','tea']}
                    db.user.find({
                        "hobbies":{
                            "$all":['dancing','tea']
                        }
                    })
                    { "_id" : 4, "name" : "jingliyang", "age" : 40, "hobbies" : [ "music", "read", "dancing", "tea" ], "addr" : { "country" : "China", "city" : "BJ" } }
                    >

                # 查找"hobbies"中第3个值是'dancing'的
                    > db.user.find({"hobbies.2":'dancing'})
                    { "_id" : ObjectId("5e8ffb00c674d55a3e7b2b3b"), "name" : "egon", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }
                    { "_id" : 1, "name" : "alex", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "weifang" } }
                    { "_id" : 4, "name" : "jingliyang", "age" : 40, "hobbies" : [ "music", "read", "dancing", "tea" ], "addr" : { "country" : "China", "city" : "BJ" } }
                    { "_id" : ObjectId("5e8ffbe6c674d55a3e7b2b3c"), "name" : "egon", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }
                    >

                # 查找所有的后两个爱好   "$slice"关键字
                    db.user.find(
                        {},                             # {}表示查询所有
                        {
                            "_id":0,
                            "hobbies":{"$slice":-2},   #在返回的字段中 用{"$slice":-2} 指定即可
                            "age":0,
                            "_id":0,
                            "name":0,
                            "addr":0
                        }
                    )
                    { "hobbies" : [ "read", "dancing" ] }
                    { "hobbies" : [ "read", "dancing" ] }
                    { "hobbies" : [ "read", "run" ] }
                    { "hobbies" : [ "music", "drink" ] }
                    { "hobbies" : [ "dancing", "tea" ] }
                    { "hobbies" : [ "music", "read" ] }
                    { "hobbies" : [ "read", "dancing" ] }
                    >

                # 查看所有人的第2个到第3个爱好
                    > db.user.find({},{'hobbies':{"$slice":[1,2]},"age":0,"_id":0,"name":0,"addr":0})
                    { "hobbies" : [ "read", "dancing" ] }
                    { "hobbies" : [ "read", "dancing" ] }
                    { "hobbies" : [ "read", "run" ] }
                    { "hobbies" : [ "drink" ] }
                    { "hobbies" : [ "read", "dancing" ] }
                    { "hobbies" : [ "read" ] }
                    { "hobbies" : [ "read", "dancing" ] }
                    >

            # 7 查询 对象addr
                # 查看"city"是 "hebei"的 
                > db.user.find({"addr.city":"hebei"})
                { "_id" : 2, "name" : "wupeiqi", "age" : 20, "hobbies" : [ "music", "read", "run" ], "addr" : { "country" : "China", "city" : "hebei" } }
                >
                # 查看"country"是 "China"的 
                > db.user.find({"addr.country":"china"}) #mongodb是区分大小写的
                > db.user.find({"addr.country":"China"})
                { "_id" : ObjectId("5e8ffb00c674d55a3e7b2b3b"), "name" : "egon", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }
                { "_id" : 1, "name" : "alex", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "weifang" } }
                { "_id" : 2, "name" : "wupeiqi", "age" : 20, "hobbies" : [ "music", "read", "run" ], "addr" : { "country" : "China", "city" : "hebei" } }
                { "_id" : 3, "name" : "yuanhao", "age" : 30, "hobbies" : [ "music", "drink" ], "addr" : { "country" : "China", "city" : "heibei" } }
                { "_id" : 4, "name" : "jingliyang", "age" : 40, "hobbies" : [ "music", "read", "dancing", "tea" ], "addr" : { "country" : "China", "city" : "BJ" } }
                { "_id" : 5, "name" : "jinxin", "age" : 50, "hobbies" : [ "music", "read" ], "addr" : { "country" : "China", "city" : "henan" } }
                { "_id" : ObjectId("5e8ffbe6c674d55a3e7b2b3c"), "name" : "egon", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }
                >

            # 8 排序
               # 排序:--1代表升序，-1代表降序
                db.user.find().sort({"name":1,})
                

            # 9 分页
                #  分页:--limit代表取多少个document，skip代表跳过前多少个document。
                    # 连续翻页
                    db.user.find().limit(2).skip(0) 
                    db.user.find().limit(2).skip(2) 
                    db.user.find().limit(2).skip(4) 
                    db.user.find().limit(2).skip(6)  
                    
                    > db.user.find().limit(2).skip(0)
                    { "_id" : ObjectId("5e8ffb00c674d55a3e7b2b3b"), "name" : "egon", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }
                    { "_id" : 1, "name" : "alex", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "weifang" } }
                    > db.user.find().limit(2).skip(2)
                    { "_id" : 2, "name" : "wupeiqi", "age" : 20, "hobbies" : [ "music", "read", "run" ], "addr" : { "country" : "China", "city" : "hebei" } }
                    { "_id" : 3, "name" : "yuanhao", "age" : 30, "hobbies" : [ "music", "drink" ], "addr" : { "country" : "China", "city" : "heibei" } }
                    > db.user.find().limit(2).skip(4)
                    { "_id" : 4, "name" : "jingliyang", "age" : 40, "hobbies" : [ "music", "read", "dancing", "tea" ], "addr" : { "country" : "China", "city" : "BJ" } }
                    { "_id" : 5, "name" : "jinxin", "age" : 50, "hobbies" : [ "music", "read" ], "addr" : { "country" : "China", "city" : "henan" } }
                    > db.user.find().limit(2).skip(6)  #共7条,所以到最后只有1条
                    { "_id" : ObjectId("5e8ffbe6c674d55a3e7b2b3c"), "name" : "egon", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }
                    >

                
                db.user.find().sort({'age':1}).limit(1).skip(2)
                > db.user.find().sort({'age':1}).limit(1).skip(2)
                { "_id" : ObjectId("5e8ffbe6c674d55a3e7b2b3c"), "name" : "egon", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }
                
            # 10 获取数量 统计.count()
                > db.user.find().count()
                7

            # 11 杂项
                #1、{'key':null} 匹配key的值为null或者没有这个key
                db.t2.insert({'a':10,'b':111})
                db.t2.insert({'a':20})
                db.t2.insert({'b':null})

                > db.t2.find({"b":null})
                { "_id" : ObjectId("5a5cc2a7c1b4645aad959e5a"), "a" : 20 }
                { "_id" : ObjectId("5a5cc2a8c1b4645aad959e5b"), "b" : null }

                #2、查找所有
                db.user.find() #等同于db.user.find({})
                db.user.find().pretty()

                #3、查找一个，与find用法一致，只是只取匹配成功的第一个
                db.user.findOne({"_id":{"$gt":3}})
             
                #4、查找包含某个字段的 {字段：{"$exists":true}}
                # 查包含'hobbies'字段的
                db.user.find({'hobbies':{"$exists":true}})

                > db.user.find({'hobbies':{"$exists":true}})
                { "_id" : ObjectId("5e8ffb00c674d55a3e7b2b3b"), "name" : "egon", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }
                { "_id" : 1, "name" : "潘_alex", "age" : 73, "hobbies" : [ "music", "piao", "dancing" ], "addr" : { "country" : "China", "city" : "weifang" } }
                { "_id" : 3, "name" : "yuanhao", "age" : 30, "hobbies" : [ "music", "drink" ], "addr" : { "country" : "Japan", "city" : "heibei" } }
                { "_id" : 4, "name" : "jingliyang", "age" : 40, "hobbies" : [ "music", "read", "dancing", "tea" ], "addr" : { "country" : "China", "city" : "BJ" } }
                { "_id" : 5, "name" : "jinxin", "age" : 50, "hobbies" : [ "music", "read" ], "addr" : { "country" : "China", "city" : "henan" } }
                { "_id" : ObjectId("5e8ffbe6c674d55a3e7b2b3c"), "name" : "egon", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }
                >
            
        # 改
            一 语法:
                db.table.update(
                    条件,
                    修改字段,
                    其他参数
                )

                db.table.update(
                    {},                  # {}指查找或匹配所有的
                    {"age":11},          # 将匹配文档的"age"字段的值设为11
                    {
                        "multi":true,    # update 默认只改匹配的第一个, 这样设置,才能让update 修改所有匹配的记录.
                        "upsert":true    # 加该参数的作用,是有匹配到的记录就修改,无匹配到的记录就新增一条记录.
                    }

                )

            1 覆盖式修改 和 局部式修改 "$set"
                #将'wupeiqi'的年龄改为23,名字改为大郎
                update db1.user set age=23,name="大郎" where name='wupeiqi' 
                #覆盖式修改  顺序也覆盖
                    db.user.update(
                        {"name":"wupeiqi"},
                        {"name":"大郎","age":23} 
                    )
                    # user 数据
                    > db.user.find()
                    { "_id" : ObjectId("5e8ffb00c674d55a3e7b2b3b"), "name" : "egon", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }
                    { "_id" : 1, "name" : "alex", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "weifang" } }
                    { "_id" : 2, "name" : "wupeiqi", "age" : 20, "hobbies" : [ "music", "read", "run" ], "addr" : { "country" : "China", "city" : "hebei" } }
                    { "_id" : 3, "name" : "yuanhao", "age" : 30, "hobbies" : [ "music", "drink" ], "addr" : { "country" : "China", "city" : "heibei" } }
                    { "_id" : 4, "name" : "jingliyang", "age" : 40, "hobbies" : [ "music", "read", "dancing", "tea" ], "addr" : { "country" : "China", "city" : "BJ" } }
                    { "_id" : 5, "name" : "jinxin", "age" : 50, "hobbies" : [ "music", "read" ], "addr" : { "country" : "China", "city" : "henan" } }
                    { "_id" : ObjectId("5e8ffbe6c674d55a3e7b2b3c"), "name" : "egon", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }

                    # 修改'wupeiqi'的年龄改为23,名字改为大郎
                    > db.user.update(
                    ...                     {"name":"wupeiqi"},
                    ...                     {"name":"大郎","age":23}
                    ...                 )
                    WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
                    # 看到原来记录被覆盖了
                    > db.user.find({"name":"大郎"})
                    { "_id" : 2, "name" : "大郎", "age" : 23 }   
                    >
                #局部式修改 "$set" 不改变顺序 没有该字段 就增加
                    db.user.update(
                        {"name":"alex"},
                        {"$set":{"name":"潘_alex","age":73} }
                    )

                    WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })   #匹配1条，新增0条，修改1条。
                    > db.user.find()
                    { "_id" : ObjectId("5e8ffb00c674d55a3e7b2b3b"), "name" : "egon", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }
                    { "_id" : 1, "name" : "潘_alex", "age" : 73, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "weifang" } }
                    { "_id" : 2, "name" : "大郎", "age" : 23 }
                    { "_id" : 3, "name" : "yuanhao", "age" : 30, "hobbies" : [ "music", "drink" ], "addr" : { "country" : "China", "city" : "heibei" } }
                    { "_id" : 4, "name" : "jingliyang", "age" : 40, "hobbies" : [ "music", "read", "dancing", "tea" ], "addr" : { "country" : "China", "city" : "BJ" } }
                    { "_id" : 5, "name" : "jinxin", "age" : 50, "hobbies" : [ "music", "read" ], "addr" : { "country" : "China", "city" : "henan" } }
                    { "_id" : ObjectId("5e8ffbe6c674d55a3e7b2b3c"), "name" : "egon", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }
                    >

            2 改多条 {"multi":true }
                # 把id大于等于1，小于等于2的年龄都改成43
                update db1.user set age=43 where id>=1 and id<=2
                db.user.update(
                    {"_id":{"$gte":1,"$lte":2}},
                    {"$set":{"name":43}},
                    {"multi":true }
                )

              
                WriteResult({ "nMatched" : 2, "nUpserted" : 0, "nModified" : 2 })
                > db.user.find()
                { "_id" : ObjectId("5e8ffb00c674d55a3e7b2b3b"), "name" : "egon", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }
                { "_id" : 1, "name" : 43, "age" : 73, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "weifang" } }
                { "_id" : 2, "name" : 43, "age" : 23 }
                { "_id" : 3, "name" : "yuanhao", "age" : 30, "hobbies" : [ "music", "drink" ], "addr" : { "country" : "China", "city" : "heibei" } }
                { "_id" : 4, "name" : "jingliyang", "age" : 40, "hobbies" : [ "music", "read", "dancing", "tea" ], "addr" : { "country" : "China", "city" : "BJ" } }
                { "_id" : 5, "name" : "jinxin", "age" : 50, "hobbies" : [ "music", "read" ], "addr" : { "country" : "China", "city" : "henan" } }
                { "_id" : ObjectId("5e8ffbe6c674d55a3e7b2b3c"), "name" : "egon", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }
                >

            3 没有就新增  {"upsert":true}
                # 查找 name=gq 的 将名字 改为大写 GQ 年龄 改为 18
                db.user.update(
                    {"name":"gq"},
                    {"$set":{"name":"GQ","age":18}},
                    {"upsert":true}
                )
                WriteResult({
                        "nMatched" : 0,
                        "nUpserted" : 1,
                        "nModified" : 0,
                        "_id" : ObjectId("5e90fed48db2db4921c0f912")
                })
                > db.user.find()
                { "_id" : ObjectId("5e8ffb00c674d55a3e7b2b3b"), "name" : "egon", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }
                { "_id" : 1, "name" : 43, "age" : 73, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "weifang" } }
                { "_id" : 2, "name" : 43, "age" : 23 }
                { "_id" : 3, "name" : "yuanhao", "age" : 30, "hobbies" : [ "music", "drink" ], "addr" : { "country" : "China", "city" : "heibei" } }
                { "_id" : 4, "name" : "jingliyang", "age" : 40, "hobbies" : [ "music", "read", "dancing", "tea" ], "addr" : { "country" : "China", "city" : "BJ" } }
                { "_id" : 5, "name" : "jinxin", "age" : 50, "hobbies" : [ "music", "read" ], "addr" : { "country" : "China", "city" : "henan" } }
                { "_id" : ObjectId("5e8ffbe6c674d55a3e7b2b3c"), "name" : "egon", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }
                { "_id" : ObjectId("5e90fed48db2db4921c0f912"), "name" : "GQ", "age" : 18 }
                >

            
                # 把yuanha的国家改为japan
                db.user.update(
                    {"name":"yuanha"},
                    {"$set":{"addr.country":"Japan"}},
                    {"multi":true,"upsert":true}
                )

                WriteResult({
                        "nMatched" : 0,
                        "nUpserted" : 1,
                        "nModified" : 0,
                        "_id" : ObjectId("5e9101c38db2db4921c0f91f")
                })
                > db.user.find()
                { "_id" : ObjectId("5e8ffb00c674d55a3e7b2b3b"), "name" : "egon", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }
                { "_id" : 1, "name" : 43, "age" : 73, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "weifang" } }
                { "_id" : 2, "name" : 43, "age" : 23 }
                { "_id" : 3, "name" : "yuanhao", "age" : 30, "hobbies" : [ "music", "drink" ], "addr" : { "country" : "China", "city" : "heibei" } }
                { "_id" : 4, "name" : "jingliyang", "age" : 40, "hobbies" : [ "music", "read", "dancing", "tea" ], "addr" : { "country" : "China", "city" : "BJ" } }
                { "_id" : 5, "name" : "jinxin", "age" : 50, "hobbies" : [ "music", "read" ], "addr" : { "country" : "China", "city" : "henan" } }
                { "_id" : ObjectId("5e8ffbe6c674d55a3e7b2b3c"), "name" : "egon", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }
                { "_id" : ObjectId("5e90fed48db2db4921c0f912"), "name" : "GQ", "age" : 18 }
                { "_id" : ObjectId("5e9101c38db2db4921c0f91f"), "name" : "yuanha", "addr" : { "country" : "Japan" } }

            4 修改 对象addr
                # 把yuanhao的国家改为japan
                db.user.update(
                    {"name":"yuanhao"},
                    {"$set":{"addr.country":"Japan"}},
                    {"multi":true,"upsert":true}
                )
                WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
                > db.user.find()
                { "_id" : ObjectId("5e8ffb00c674d55a3e7b2b3b"), "name" : "egon", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }
                { "_id" : 1, "name" : 43, "age" : 73, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "weifang" } }
                { "_id" : 2, "name" : 43, "age" : 23 }
                { "_id" : 3, "name" : "yuanhao", "age" : 30, "hobbies" : [ "music", "drink" ], "addr" : { "country" : "Japan", "city" : "heibei" } }
                { "_id" : 4, "name" : "jingliyang", "age" : 40, "hobbies" : [ "music", "read", "dancing", "tea" ], "addr" : { "country" : "China", "city" : "BJ" } }
                { "_id" : 5, "name" : "jinxin", "age" : 50, "hobbies" : [ "music", "read" ], "addr" : { "country" : "China", "city" : "henan" } }
                { "_id" : ObjectId("5e8ffbe6c674d55a3e7b2b3c"), "name" : "egon", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }
                { "_id" : ObjectId("5e90fed48db2db4921c0f912"), "name" : "GQ", "age" : 18 }
                { "_id" : ObjectId("5e9101c38db2db4921c0f91f"), "name" : "yuanha", "addr" : { "country" : "Japan" } }
                >

            5 修改 数组hobbies
                # 把id=1的name改回潘——alex
                db.user.update({"_id":1},{"$set":{"naem":"潘——alex"}})
                # 把潘-alex的第2个爱好hobbies改为piao
                db.user.update(
                    {"naem":"潘——alex"},
                    {"$set":{"hobbies.1":"piao"}})
                )
                WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
                > db.user.find()                                       }})                                                  }})
                { "_id" : ObjectId("5e8ffb00c674d55a3e7b2b3b"), "name" : "egon", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }
                { "_id" : 1, "name" : 43, "age" : 73, "hobbies" : [ "music", "piao", "dancing" ], "addr" : { "country" : "China", "city" : "weifang" }, "naem" : "潘——alex" }
                { "_id" : 2, "name" : 43, "age" : 23 }
                { "_id" : 3, "name" : "yuanhao", "age" : 30, "hobbies" : [ "music", "drink" ], "addr" : { "country" : "Japan", "city" : "heibei" } }
                { "_id" : 4, "name" : "jingliyang", "age" : 40, "hobbies" : [ "music", "read", "dancing", "tea" ], "addr" : { "country" : "China", "city" : "BJ" } }
                { "_id" : 5, "name" : "jinxin", "age" : 50, "hobbies" : [ "music", "read" ], "addr" : { "country" : "China", "city" : "henan" } }
                { "_id" : ObjectId("5e8ffbe6c674d55a3e7b2b3c"), "name" : "egon", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }
                { "_id" : ObjectId("5e90fed48db2db4921c0f912"), "name" : "GQ", "age" : 18 }
                { "_id" : ObjectId("5e9101c38db2db4921c0f91f"), "name" : "yuanha", "addr" : { "country" : "Japan" } }
                >

            6 删除字段 {"$unset":{字段:""}}
                # 删除id=1的naem字段{"$unset":{"naem":''},}，修改name为"潘_alex"
                db.user.update(
                    {"_id":1},
                    {"$unset":{"naem":''},"$set":{"name":"潘_alex"}}
                )

                > db.user.update(
                ...                     {"_id":1},
                ...                     {"$unset":{"naem":''},"$set":{"name":"潘_alex"}}
                ...                 )
                WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
                > db.user.find()                                                                                                                      )
                { "_id" : ObjectId("5e8ffb00c674d55a3e7b2b3b"), "name" : "egon", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }
                { "_id" : 1, "name" : "潘_alex", "age" : 73, "hobbies" : [ "music", "piao", "dancing" ], "addr" : { "country" : "China", "city" : "weifang" } }
                { "_id" : 2, "name" : 43, "age" : 23 }
                { "_id" : 3, "name" : "yuanhao", "age" : 30, "hobbies" : [ "music", "drink" ], "addr" : { "country" : "Japan", "city" : "heibei" } }
                { "_id" : 4, "name" : "jingliyang", "age" : 40, "hobbies" : [ "music", "read", "dancing", "tea" ], "addr" : { "country" : "China", "city" : "BJ" } }
                { "_id" : 5, "name" : "jinxin", "age" : 50, "hobbies" : [ "music", "read" ], "addr" : { "country" : "China", "city" : "henan" } }
                { "_id" : ObjectId("5e8ffbe6c674d55a3e7b2b3c"), "name" : "egon", "age" : 10, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }
                { "_id" : ObjectId("5e90fed48db2db4921c0f912"), "name" : "GQ", "age" : 18 }
                { "_id" : ObjectId("5e9101c38db2db4921c0f91f"), "name" : "yuanha", "addr" : { "country" : "Japan" } }
                >

            7 增加 减少 "$inc"
                # 把所有人的年龄加1
                db.user.update(
                    {},
                    {"$inc":{"age":1}},
                    {"multi":true}
                )
                WriteResult({ "nMatched" : 9, "nUpserted" : 0, "nModified" : 9 })
                > db.user.find()
                { "_id" : ObjectId("5e8ffb00c674d55a3e7b2b3b"), "name" : "egon", "age" : 11, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }
                { "_id" : 1, "name" : "潘_alex", "age" : 74, "hobbies" : [ "music", "piao", "dancing" ], "addr" : { "country" : "China", "city" : "weifang" } }
                { "_id" : 2, "name" : 43, "age" : 24 }
                { "_id" : 3, "name" : "yuanhao", "age" : 31, "hobbies" : [ "music", "drink" ], "addr" : { "country" : "Japan", "city" : "heibei" } }
                { "_id" : 4, "name" : "jingliyang", "age" : 41, "hobbies" : [ "music", "read", "dancing", "tea" ], "addr" : { "country" : "China", "city" : "BJ" } }
                { "_id" : 5, "name" : "jinxin", "age" : 51, "hobbies" : [ "music", "read" ], "addr" : { "country" : "China", "city" : "henan" } }
                { "_id" : ObjectId("5e8ffbe6c674d55a3e7b2b3c"), "name" : "egon", "age" : 11, "hobbies" : [ "music", "read", "dancing" ], "addr" : { "country" : "China", "city" : "BJ" } }
                { "_id" : ObjectId("5e90fed48db2db4921c0f912"), "name" : "GQ", "age" : 19 }
                { "_id" : ObjectId("5e9101c38db2db4921c0f91f"), "name" : "yuanha", "addr" : { "country" : "Japan" }, "age" : 1 } #没有age字段的 新增了该字段
                >

                # 把所有人的年龄减1
                db.user.update(
                    {},
                    {"$inc":{"age":-1}},
                    {"multi":true}
                )
                WriteResult({ "nMatched" : 9, "nUpserted" : 0, "nModified" : 9 })
                
                # 
                db.emp.update(
                    {},
                    {'recode':{
                        't1':[],
                        'tr':[],

                    }}
                )

            8 数组 hobbies 添加或删除组内元素 "$push" "$each"  "$pop" "$pull"
                往数组内尾部添加元素:"$push" 不考虑重复
                    #1、为名字为yuanhao的人添加一个爱好
                    db.user.update({"name":"yuanhao"},{"$push":{"hobbies":"烫头"}})

                    #2、为名字为yuanhao的人一次添加多个爱好 "$each"关键字 循环 每次添加1个爱好
                    db.user.update(
                        {"name":"yuanhao"},
                        {"$push":{"hobbies":{"$each":["纹身","抽烟"]}}}
                    )

                按照位置且只能从开头或结尾删除元素： "$pop"
                    #3、{"$pop":{"key":1}} 从数组末尾删除一个元素

                    db.user.update(
                        {"name":"yuanhao"},
                        {"$pop":{"hobbies":1}}
                    )
                    db.user.update(
                        {'name':'egon'},
                        {'$pop':{'hobbies':2}}
                    )

                    #4、{"$pop":{"key":-1}} 从头部删除
                    db.user.update(
                        {"name":"yuanhao"},
                        {"$pop":{"hobbies":-1}}
                    )
                    db.user.update({'_id':5},{"$pop":{"hobbies":-1}})
                把符合条件的统统删掉："$pull"
                    #5、按照条件删除元素,："$pull" 把符合条件的统统删掉，而$pop只能从两端删
                    db.user.update(
                        {'name':"yuanhao"},
                        {"$pull":{"hobbies":"read"}},
                        {"multi":true}
                    )

            9 避免添加重复："$addToSet"

                db.urls.insert({"_id":1,"urls":[]})

                db.urls.update({"_id":1},{"$addToSet":{"urls":'http://www.baidu.com'}})
                db.urls.update({"_id":1},{"$addToSet":{"urls":'http://www.baidu.com'}})
                db.urls.update({"_id":1},{"$addToSet":{"urls":'http://www.baidu.com'}})

                db.urls.update({"_id":1},{
                    "$addToSet":{
                        "urls":{
                        "$each":[
                            'http://www.baidu.com',
                            'http://www.baidu.com',
                            'http://www.xxxx.com'
                            ]
                        }
                    }
                })

            10 其他
                #1、了解：限制大小"$slice"，只留最后n个
                db.user.update({"_id":5},{
                    "$push":{"hobbies":{
                        "$each":["read",'music','dancing'],
                        "$slice":-2
                        }   
                    }
                })

                #2、了解：排序The $sort element value must be either 1 or -1"
                db.user.update({"_id":5},{
                    "$push":{"hobbies":{
                        "$each":["read",'music','dancing'],
                        "$slice":-1,
                        "$sort":-1
                        }
                    }
                })
                
                db.user.update({"_id":5},{
                    "$push":{"hobbies":{
                        "$each":["read",'music','dancing'],
                       
                        }
                    }
                })
                #注意：不能只将"$slice"或者"$sort"与"$push"配合使用，且必须使用"$each"


        # 删
            #1、删除多个中的第一个
            db.user.deleteOne({ 'age': 8 })

            #2、删除国家为China的全部
            db.user.deleteMany( {'addr.country': 'China'} ) 

            #3、删除全部
            db.user.deleteMany({}) 