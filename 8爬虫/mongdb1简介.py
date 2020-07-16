# 存储库  mongdb
    # 通用数据库 非关系型数据库
    # 高效且支持分布式，易于扩展。
    # 记录的数据结构：字典，一行记录就是一个字典对象，一行记录也叫一个文档。
    # 表在这里称为集合，没有表关联的概念，是独立的。

# 下载和安装都有坑

# 下载 https://www.mongodb.com/download-center/community 这里是网站公开的下载页 太慢了。。。
    # 真正的下载页：下载列表 http://dl.mongodb.org/dl/win32/x86_64 这里有适合windows的各个版本，
    # 我在公开的页面，填好了平台和package，点击下载，看到下载的文件名，在真正的下载列表页中点击该文件名下载，可以正常下载。

# 安装 4.2.5版本过程
    # 安装过程中，当出现Service Configuration服务配置界面时，不要选择，使用默认的选项，直接选next。
        # 我就是选了其他的选择，我选择了作为一个本地或域用户，然后配置了用户名和密码，
        # 当我点next，弹窗报错，说不合适的配置，back返回，改回默认的，还是不能恢复，只有取消安装，重来。
    # windows10系统下安装mongoDB数据库出现权限问题2503、2502
        # 现象：弹窗报2503和2502错误，点确定后，会出现finshed。但是完成后，没有看到安装的目录，意思应该是没有执行安装包的权限。
        # 解决：
        # 1 以管理员身份运行powshell
        # 2 输入命令：msiexec /package D:\360极速浏览器下载\mongodb-win32-x86_64-2012plus-4.2.5-signed.msi
            # PS C:\WINDOWS\system32> msiexec /package D:\360极速浏览器下载\mongodb-win32-x86_64-2012plus-4.2.5-signed.msi 
            # 此时会打开安装包
        # 3 安装过程中当启动mongodb服务时，又会报没有权限，
            # 现象：弹窗 报错：Service'MongoDB Server' failed to start. Verify that you have sufficient privileges to start system services
            # 不要动弹窗，在刚刚用管理员权限打开的powshell窗口运行services.msc 。
                # 打开了win10的服务窗口，找到MongoDB Server,
                # 右击选择属性 然后选择登录→选择本地登陆 然后应用
                # 在安装目录的bin 文件夹下找到 mongod.cfg 文件，删掉最后一行'mp:'。
            # 再去报错弹窗点击Retry，即可。

# 环境配置
    # 把安装目录的bin文件夹路径（D:\MongoDB\bin）加入环境变量 path 

# 配置服务
    # 环境配置完毕，打开命令行 输入mongo 可以看到版本号等一系列信息，其中有warning信息，可以执行命令 
        # 查看数据库
        # > show dbs
        # admin   0.000GB
        # config  0.000GB
        # local   0.000GB
        # 切换到admin数据库
        # > use admin
        # switched to db admin
        # db是mongo的全局变量，db就是当前数据库，
        # > db
        # admin
        # 退出 mongo 客户端
        # > exit
        # bye

        # 说明当前mongdb服务已经启动，
        # 当前的登录 是不用输入用户名和密码就登录了，是绕开了认证机制（跳过授权表）的登录。也是Mongodb的初始登录。

    # 初始配置无认证服务 创建用户 以管理员权限
        # 1 停止当前MongoDB服务
        PS C:\WINDOWS\system32> net stop MongoDB
        # 2 把该服务从系统服务中移除
        PS C:\WINDOWS\system32> mongod --remove
        # 3 用命令加载含无需认证信息的服务配置 
            # 1 在data目录下新建db文件夹，
            # 2 执行如下命令，配置无认证服务
            PS C:\WINDOWS\system32> mongod --bind_ip 0.0.0.0 --port 27017 --logpath D:\MongoDB\log\mongod.log --logappend --dbpath D:\MongoDB\data\db  --serviceName "MongoDB" --serviceDisplayName "MongoDB"  --install
        # 4 启动mongodb服务
        PS C:\WINDOWS\system32> net start MongoDB

        # 5 配置用户
        
                # 在哪个数据库创建的用户，就要在哪个库下登录。
                    #账号管理：https://docs.mongodb.com/master/tutorial/enable-authentication/
            #1、创建账号
            # 先造一个 超级用户 gq 当然要在admin数据库创建。
            use admin
            db.createUser(
              {
                user: "gq",
                pwd: "another333",
                roles: [ { role: "root", db: "admin" } ]
              }
            )
            '''
            > db.createUser(
            ...           {
            ...             user: "gq",
            ...             pwd: "another333",
            ...             roles: [ { role: "root", db: "admin" } ]
            ...           }
            ...         )
            Successfully added user: {
                    "user" : "gq",
                    "roles" : [
                            {
                                    "role" : "root",
                                    "db" : "admin"
                            }
                    ]
            }
            >
            '''
            # 再造一个普通用户egon,对test数据库有读写权限，对db1数据库只能读。
            use test
            db.createUser(
              {
                user: "egon",
                pwd: "123",
                roles: [ { role: "readWrite", db: "test" },
                         { role: "read", db: "db1" } ]
              }
            )
            '''
            > db.createUser(
            ...   {
            ...     user: "egon",
            ...     pwd: "123",
            ...     roles: [ { role: "readWrite", db: "test" },
            ...              { role: "read", db: "db1" } ]
            ...   }
            ... )
            Successfully added user: {
                    "user" : "egon",
                    "roles" : [
                            {
                                    "role" : "readWrite",
                                    "db" : "test"
                            },
                            {
                                    "role" : "read",
                                    "db" : "db1"
                            }
                    ]
            }
            '''
    # 当我们创建好用户后，就要配置有认证机制的登录 必须以管理员权限
        # 1 要先停止MongoDB服务。
            PS C:\WINDOWS\system32> net stop MongoDB
            MongoDB 服务正在停止.
            MongoDB 服务已成功停止。
        # 2 把该服务从系统服务中移除。
            # 必须以管理员权限 
            PS C:\WINDOWS\system32> services.msc
            PS C:\WINDOWS\system32> mongod --remove
            2020-04-09T16:08:43.350+0800 I  CONTROL  [main] Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'
            2020-04-09T16:08:43.779+0800 W  ASIO     [main] No TransportLayer configured during NetworkInterface startup
            2020-04-09T16:08:43.779+0800 I  CONTROL  [main] Trying to remove Windows service 'MongoDB'
            2020-04-09T16:08:43.781+0800 I  CONTROL  [main] Service 'MongoDB' removed
       
        # 3 用命令加载含有授权信息的服务 
            # 执行如下命令，重启服务
            PS C:\WINDOWS\system32> mongod --bind_ip 0.0.0.0 --port 27017 --logpath D:\MongoDB\log\mongod.log --logappend --dbpath D:\MongoDB\data\db  --serviceName "MongoDB" --serviceDisplayName "MongoDB"  --install --auth
            PS C:\WINDOWS\system32> net start MongoDB
            MongoDB 服务正在启动 .
            MongoDB 服务已经启动成功。

    # 登录
        # 以超级用户gq登录
                在命令行输入mongo,
                可以看到原来的警告和提示都没有了。
                输入show dbs，没有应答。
                默认登录的数据库是test,
                切换到gq所在数据库admin，
                用db.auth("gq","another333")登录，看到结果为1表示成功。
                此时再用show dbs可以看到结果了。

                C:\Users\69598>mongo
                MongoDB shell version v4.2.5
                connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
                Implicit session: session { "id" : UUID("75e6bd45-c19c-46c8-acce-6c20299ab553") }
                MongoDB server version: 4.2.5
                > show dbs
                > db
                test

                > use admin
                switched to db admin
                > db.auth("gq","another333")
                1

                > show dbs
                admin   0.000GB
                config  0.000GB
                db1     0.000GB
                local   0.000GB
                >
        # 以普通用户egon登录，在db1只能读，不能写，在test可以读写
                C:\Users\69598>mongo
                MongoDB shell version v4.2.5
                connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
                Implicit session: session { "id" : UUID("8e3b71f7-4e07-4a5e-98e5-53b69e3edf3f") }
                MongoDB server version: 4.2.5
                > show dbs
                > db
                test
                > db.auth("egon","123")
                1
                > show tables
                > db
                test
                > use db1
                switched to db db1
                > show tables
                user
                > db.user.fing()
                2020-04-09T17:26:11.141+0800 E  QUERY    [js] uncaught exception: TypeError: db.user.fing is not a function :
                @(shell):1:1
                > db.user.find()
                { "_id" : 1, "name" : "egon" }
                > db.user.insert({"_id":2,"name":"alex"})
                WriteCommandError({
                        "ok" : 0,
                        "errmsg" : "not authorized on db1 to execute command { insert: \"user\", ordered: true, lsid: { id: UUID(\"8e3b71f7-4e07-4a5e-98e5-53b69e3edf3f\") }, $db: \"db1\" }",
                        "code" : 13,
                        "codeName" : "Unauthorized"
                })
                > use test
                switched to db test
                > db.t1.insert({"_id":1,"name":"alex"})
                WriteResult({ "nInserted" : 1 })
                > db.t1.find()
                { "_id" : 1, "name" : "alex" }
        # 输入 用户名 密码 该用户所在的库 登录
            C:\Users\69598>mongo -u "gq" -p "another333" --authenticationDatabase "admin"
            MongoDB shell version v4.2.5
            connecting to: mongodb://127.0.0.1:27017/?authSource=admin&compressors=disabled&gssapiServiceName=mongodb
            Implicit session: session { "id" : UUID("d8b28424-d760-4e8b-a7b4-90c635ad80dd") }
            MongoDB server version: 4.2.5
            ---
            Enable MongoDB's free cloud-based monitoring service, which will then receive and display
            metrics about your deployment (disk utilization, CPU, operation statistics, etc).
            The monitoring data will be available on a MongoDB website with a unique URL accessible to you
            and anyone you share the URL with. MongoDB may use this information to make product
            improvements and to suggest MongoDB products and deployment options to you.
            To enable free monitoring, run the following command: db.enableFreeMonitoring()
            To permanently disable this reminder, run the following command: db.disableFreeMonitoring()
            ---
            > show dbs
            admin   0.000GB
            config  0.000GB
            db1     0.000GB
            local   0.000GB
            test    0.000GB
            >
        # 输入 exit 退出
            > exit
            bye
