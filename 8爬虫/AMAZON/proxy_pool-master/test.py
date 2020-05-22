# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test.py  
   Description :  
   Author :       JHao
   date：          2017/3/7
-------------------------------------------------
   Change Activity:
                   2017/3/7: 
-------------------------------------------------
"""
__author__ = 'JHao'

# from Config.ConfigGetter import config

# if __name__ == '__main__':
#    print(config.db_type)
#    print(config.db_name)
#    print(config.db_host)
#    print(config.db_port)
#    print(config.proxy_getter_functions)
#    print(config.host_ip)
#    print(config.host_port)
#    print(config.db_password)

# from Schedule.ProxyScheduler import runScheduler
# if __name__ == "__main__":
#     runScheduler()



# from Test import testConfig

# if __name__ == '__main__':
#     testConfig.testConfig()
# 结果
   # (venv) D:\pyj\st\study\8爬虫\AMAZON\proxy_pool-master>d:/pyj/st/venv/Scripts/python.exe d:/pyj/st/study/8爬虫/AMAZON/proxy_pool-master/test.py
   # MONGODB
   # proxy
   # 127.0.0.1
   # 27017

   # ['freeProxy01', 'freeProxy03', 'freeProxy04', 'freeProxy05', 'freeProxy07', 'freeProxy09', 'freeProxy13', 'freeProxy14', 'freeProxy14']

# from Test import testWebRequest

# if __name__ == '__main__':
#    testWebRequest.testWebRequest()
# 结果
 
# from Test import testProxyClass

# if __name__ == '__main__':
#    testProxyClass.testProxyClass()
# 结果
   # (venv) D:\pyj\st\study>d:/pyj/st/venv/Scripts/python.exe d:/pyj/st/study/8爬虫/AMAZON/proxy_pool-master/test.py 
   # {'proxy': '127.0.0.1:8080', 'fail_count': 0, 'region': '', 'type': '', 'source': '', 'check_count': 0, 'last_status': '', 'last_time': ''}
   # {"proxy": "127.0.0.1:8080", "fail_count": 0, "region": "", "type": "", "source": "test", "check_count": 0, "last_status": "", "last_time": ""}
   # {'proxy': '127.0.0.1:8080', 'fail_count': 0, 'region': '', 'type': '', 'source': 'test', 'check_count': 0, 'last_status': '', 'last_time': ''}
   # {'proxy': '127.0.0.1:8080', 'fail_count': 0, 'region': '', 'type': '', 'source': '', 'check_count': 0, 'last_status': '', 'last_time': ''}
   # {"proxy": "127.0.0.1:8080", "fail_count": 0, "region": "", "type": "", "source": "test", "check_count": 0, "last_status": "", "last_time": ""}
   # {'proxy': '127.0.0.1:8080', 'fail_count': 0, 'region': '', 'type': '', 'source': 'test', 'check_count': 0, 'last_status': '', 'last_time': ''}

# from Test import testLogHandler

# if __name__ == '__main__':
#    testLogHandler.testLogHandler()
# 结果
   # (venv) D:\pyj\st\study>d:/pyj/st/venv/Scripts/python.exe d:/pyj/st/study/8爬虫/AMAZON/proxy_pool-master/test.py 
   # 2020-04-23 22:16:31,482 testLogHandler.py[line:25] INFO this is a log from test
   # 2020-04-23 22:16:31,482 testLogHandler.py[line:28] INFO this is a log from test1
   # 2020-04-23 22:16:31,484 testLogHandler.py[line:31] INFO this is a log from test2

# from Test import testGetFreeProxy

# if __name__ == '__main__':
#     testGetFreeProxy.testGetFreeProxy()
# 结果
   # (venv) D:\pyj\st\study\8爬虫\AMAZON\proxy_pool-master>d:/pyj/st/venv/Scripts/python.exe d:/pyj/st/study/8爬虫/AMAZON/proxy_pool-master/test.py
   # freeProxy01: fetch proxy 182.46.111.190:9999,proxy_count:0
   # freeProxy01: fetch proxy 120.83.96.70:9999,proxy_count:1
   # freeProxy01: fetch proxy 163.125.157.34:8888,proxy_count:2
   # freeProxy01: fetch proxy 59.38.62.107:9797,proxy_count:3
   # freeProxy01: fetch proxy 219.131.240.246:9797,proxy_count:4
   # freeProxy01: fetch proxy 118.114.194.229:8118,proxy_count:5
   # freeProxy01: fetch proxy 122.241.225.227:60004,proxy_count:6
   # freeProxy01: fetch proxy 121.237.148.247:3000,proxy_count:7
   # freeProxy01: fetch proxy 112.194.112.175:8118,proxy_count:8
   # freeProxy01: fetch proxy 113.121.20.64:9999,proxy_count:9
   # freeProxy01: fetch proxy 117.64.235.243:1133,proxy_count:10
   # freeProxy01: fetch proxy 175.43.57.18:9999,proxy_count:11
   # freeProxy01: fetch proxy 144.123.69.180:9999,proxy_count:12
   # freeProxy01: fetch proxy 113.194.30.179:9999,proxy_count:13
   # freeProxy01: fetch proxy 59.62.4.5:9000,proxy_count:14
   # freeProxy01: fetch proxy 60.186.147.216:9000,proxy_count:15
   # freeProxy01: fetch proxy 60.168.206.95:8010,proxy_count:16
   # freeProxy01: fetch proxy 59.62.54.152:9000,proxy_count:17
   # freeProxy01: fetch proxy 113.195.225.42:9999,proxy_count:18
   # freeProxy01: fetch proxy 113.120.34.157:9999,proxy_count:19
   # freeProxy03: fetch proxy 27.188.65.244:8060,proxy_count:0
   # freeProxy03: fetch proxy 101.132.190.101:80,proxy_count:1
   # freeProxy03: fetch proxy 101.200.81.61:80,proxy_count:2
   # freeProxy03: fetch proxy 60.190.250.120:8080,proxy_count:3
   # freeProxy03: fetch proxy 115.46.116.170:8123,proxy_count:4
   # freeProxy03: fetch proxy 120.198.76.45:41443,proxy_count:5
   # freeProxy03: fetch proxy 218.59.193.14:47138,proxy_count:6
   # freeProxy03: fetch proxy 121.237.149.63:3000,proxy_count:7
   # freeProxy03: fetch proxy 121.237.148.31:3000,proxy_count:8
   # freeProxy03: fetch proxy 117.88.177.197:3000,proxy_count:9
   # freeProxy03: fetch proxy 117.88.176.55:3000,proxy_count:10
   # freeProxy03: fetch proxy 119.180.173.81:8060,proxy_count:11
   # freeProxy03: fetch proxy 222.95.144.202:3000,proxy_count:12
   # freeProxy03: fetch proxy 117.88.176.170:3000,proxy_count:13
   # freeProxy03: fetch proxy 121.237.148.241:3000,proxy_count:14
   # freeProxy03: fetch proxy 183.195.106.118:8118,proxy_count:15
   # freeProxy03: fetch proxy 114.104.134.142:8888,proxy_count:16
   # freeProxy03: fetch proxy 223.68.190.130:8181,proxy_count:17
   # freeProxy03: fetch proxy 121.237.149.218:3000,proxy_count:18
   # freeProxy03: fetch proxy 110.189.152.86:52277,proxy_count:19
   # freeProxy03: fetch proxy 115.219.168.69:8118,proxy_count:20
   # freeProxy03: fetch proxy 27.184.157.205:8118,proxy_count:21
   # freeProxy03: fetch proxy 112.194.112.175:8118,proxy_count:22
   # freeProxy03: fetch proxy 202.107.233.123:8090,proxy_count:23
   # freeProxy03: fetch proxy 119.84.112.137:80,proxy_count:24
   # freeProxy03: fetch proxy 211.159.219.225:8118,proxy_count:25
   # freeProxy03: fetch proxy 115.29.108.117:8118,proxy_count:26
   # freeProxy03: fetch proxy 183.250.255.86:63000,proxy_count:27
   # freeProxy03: fetch proxy 117.62.172.230:8118,proxy_count:28
   # freeProxy03: fetch proxy 111.222.141.127:8118,proxy_count:29
   # freeProxy03: fetch proxy 218.76.253.201:61408,proxy_count:30
   # freeProxy03: fetch proxy 117.94.213.119:8118,proxy_count:31
   # freeProxy03: fetch proxy 218.203.132.117:808,proxy_count:32
   # freeProxy03: fetch proxy 221.193.94.18:8118,proxy_count:33
   # freeProxy03: fetch proxy 121.237.149.206:3000,proxy_count:34
   # freeProxy03: fetch proxy 220.173.143.242:808,proxy_count:35
   # freeProxy03: fetch proxy 1.197.203.247:9999,proxy_count:36
   # freeProxy03: fetch proxy 171.35.172.5:9999,proxy_count:37
   # freeProxy03: fetch proxy 118.114.96.78:8118,proxy_count:38
   # freeProxy03: fetch proxy 117.87.72.226:8118,proxy_count:39
   # freeProxy03: fetch proxy 117.88.5.40:3000,proxy_count:40
   # freeProxy03: fetch proxy 125.123.19.197:8118,proxy_count:41
   # freeProxy03: fetch proxy 61.150.96.27:46111,proxy_count:42
   # freeProxy03: fetch proxy 182.32.234.18:9999,proxy_count:43
   # freeProxy03: fetch proxy 171.35.167.220:9999,proxy_count:44
   # freeProxy03: fetch proxy 171.35.167.224:9999,proxy_count:45
   # freeProxy03: fetch proxy 123.168.136.2:9999,proxy_count:46
   # freeProxy03: fetch proxy 113.194.49.94:9999,proxy_count:47
   # freeProxy03: fetch proxy 222.85.28.130:40505,proxy_count:48
   # freeProxy03: fetch proxy 123.206.54.52:8118,proxy_count:49
   # freeProxy03: fetch proxy 27.184.141.239:8118,proxy_count:50
   # freeProxy03: fetch proxy 124.93.201.59:59618,proxy_count:51
   # freeProxy03: fetch proxy 117.114.149.66:53281,proxy_count:52
   # freeProxy03: fetch proxy 121.237.149.107:3000,proxy_count:53
   # freeProxy03: fetch proxy 180.117.98.96:8118,proxy_count:54
   # freeProxy03: fetch proxy 123.132.232.254:37638,proxy_count:55
   # freeProxy03: fetch proxy 139.224.233.103:8118,proxy_count:56
   # freeProxy03: fetch proxy 221.218.102.146:33323,proxy_count:57
   # freeProxy03: fetch proxy 118.24.155.27:8118,proxy_count:58
   # freeProxy03: fetch proxy 113.12.202.50:40498,proxy_count:59
   # freeProxy03: fetch proxy 222.190.125.3:8118,proxy_count:60
   # freeProxy03: fetch proxy 175.148.69.90:1133,proxy_count:61
   # freeProxy03: fetch proxy 218.75.69.50:39590,proxy_count:62
   # freeProxy03: fetch proxy 118.78.196.186:8118,proxy_count:63
   # freeProxy03: fetch proxy 222.95.144.59:3000,proxy_count:64
   # freeProxy03: fetch proxy 121.237.149.136:3000,proxy_count:65
   # freeProxy03: fetch proxy 117.88.5.250:3000,proxy_count:66
   # freeProxy03: fetch proxy 171.35.168.177:9999,proxy_count:67
   # freeProxy03: fetch proxy 121.237.148.179:3000,proxy_count:68
   # freeProxy03: fetch proxy 223.241.118.200:8010,proxy_count:69
   # freeProxy03: fetch proxy 58.215.219.2:8000,proxy_count:70
   # freeProxy03: fetch proxy 180.117.234.56:8118,proxy_count:71
   # freeProxy03: fetch proxy 117.88.176.93:3000,proxy_count:72
   # freeProxy03: fetch proxy 123.171.5.132:8118,proxy_count:73
   # freeProxy03: fetch proxy 119.129.203.140:8118,proxy_count:74
   # freeProxy03: fetch proxy 117.88.4.12:3000,proxy_count:75
   # freeProxy03: fetch proxy 117.88.177.153:3000,proxy_count:76
   # freeProxy03: fetch proxy 115.219.104.68:8010,proxy_count:77
   # freeProxy03: fetch proxy 60.188.77.31:3000,proxy_count:78
   # freeProxy03: fetch proxy 115.204.198.148:8118,proxy_count:79
   # freeProxy03: fetch proxy 117.88.4.132:3000,proxy_count:80
   # freeProxy03: fetch proxy 115.46.102.33:8123,proxy_count:81
   # freeProxy03: fetch proxy 49.235.253.240:8888,proxy_count:82
   # freeProxy03: fetch proxy 183.147.225.74:8118,proxy_count:83
   # freeProxy03: fetch proxy 122.51.49.88:8888,proxy_count:84
   # freeProxy03: fetch proxy 211.149.252.155:8888,proxy_count:85
   # freeProxy03: fetch proxy 118.25.10.200:8080,proxy_count:86
   # freeProxy03: fetch proxy 122.4.44.124:8010,proxy_count:87
   # freeProxy03: fetch proxy 115.223.124.35:8010,proxy_count:88
   # freeProxy03: fetch proxy 115.223.122.190:8010,proxy_count:89
   # freeProxy03: fetch proxy 121.13.252.58:41564,proxy_count:90
   # freeProxy03: fetch proxy 115.219.106.175:8010,proxy_count:91
   # freeProxy03: fetch proxy 114.99.54.65:8118,proxy_count:92
   # freeProxy03: fetch proxy 122.51.183.224:808,proxy_count:93
   # freeProxy03: fetch proxy 117.64.237.165:1133,proxy_count:94
   # freeProxy03: fetch proxy 112.16.217.191:808,proxy_count:95
   # freeProxy03: fetch proxy 183.23.72.51:808,proxy_count:96
   # freeProxy03: fetch proxy 183.166.136.49:8888,proxy_count:97
   # freeProxy03: fetch proxy 117.88.4.85:3000,proxy_count:98
   # freeProxy03: fetch proxy 106.110.65.16:8118,proxy_count:99
   # freeProxy03: fetch proxy 122.224.65.201:3128,proxy_count:100
   # freeProxy03: fetch proxy 60.191.11.249:3128,proxy_count:101
   # freeProxy03: fetch proxy 60.216.20.210:8001,proxy_count:102
   # freeProxy03: fetch proxy 221.229.252.98:8080,proxy_count:103
   # freeProxy03: fetch proxy 125.123.139.19:9000,proxy_count:104
   # freeProxy03: fetch proxy 163.125.18.50:8888,proxy_count:105
   # freeProxy03: fetch proxy 122.225.45.66:43391,proxy_count:106
   # freeProxy03: fetch proxy 49.85.211.224:8118,proxy_count:107
   # freeProxy03: fetch proxy 163.125.113.249:8088,proxy_count:108
   # freeProxy03: fetch proxy 218.75.158.153:3128,proxy_count:109
   # freeProxy03: fetch proxy 14.20.235.73:808,proxy_count:110
   # freeProxy03: fetch proxy 222.190.125.5:8118,proxy_count:111
   # freeProxy03: fetch proxy 123.163.24.113:3128,proxy_count:112
   # freeProxy03: fetch proxy 119.129.236.70:3128,proxy_count:113
   # freeProxy03: fetch proxy 60.177.170.155:8118,proxy_count:114
   # freeProxy03: fetch proxy 125.123.143.58:9000,proxy_count:115
   # freeProxy03: fetch proxy 125.123.142.64:9000,proxy_count:116
   # freeProxy03: fetch proxy 125.123.16.197:9000,proxy_count:117
   # freeProxy03: fetch proxy 118.24.1.252:1080,proxy_count:118
   # freeProxy03: fetch proxy 60.191.11.246:3128,proxy_count:119
   # freeProxy03: fetch proxy 58.249.55.222:9797,proxy_count:120
   # freeProxy03: fetch proxy 60.191.11.229:3128,proxy_count:121
   # freeProxy03: fetch proxy 211.147.226.4:8118,proxy_count:122
   # freeProxy03: fetch proxy 14.126.207.71:8118,proxy_count:123
   # freeProxy03: fetch proxy 58.251.228.48:9000,proxy_count:124
   # freeProxy03: fetch proxy 117.144.188.207:3128,proxy_count:125
   # freeProxy03: fetch proxy 27.38.96.201:9797,proxy_count:126
   # freeProxy03: fetch proxy 1.196.161.10:9999,proxy_count:127
   # freeProxy03: fetch proxy 60.211.218.78:53281,proxy_count:128
   # freeProxy03: fetch proxy 14.115.106.102:808,proxy_count:129
   # freeProxy03: fetch proxy 118.89.51.66:5000,proxy_count:130
   # freeProxy03: fetch proxy 183.215.206.39:55443,proxy_count:131
   # freeProxy03: fetch proxy 222.249.238.138:8080,proxy_count:132
   # freeProxy03: fetch proxy 139.224.133.150:3128,proxy_count:133
   # freeProxy03: fetch proxy 180.141.90.145:53281,proxy_count:134
   # freeProxy03: fetch proxy 60.216.20.211:8001,proxy_count:135
   # freeProxy03: fetch proxy 103.21.117.82:3128,proxy_count:136
   # freeProxy03: fetch proxy 115.29.199.16:8118,proxy_count:137
   # freeProxy03: fetch proxy 163.125.159.121:8888,proxy_count:138
   # freeProxy03: fetch proxy 120.79.184.148:8118,proxy_count:139
   # freeProxy03: fetch proxy 61.164.39.67:53281,proxy_count:140
   # freeProxy03: fetch proxy 61.164.39.69:53281,proxy_count:141
   # freeProxy03: fetch proxy 119.57.108.73:53281,proxy_count:142
   # freeProxy03: fetch proxy 60.191.11.237:3128,proxy_count:143
   # freeProxy03: fetch proxy 218.27.204.240:8000,proxy_count:144
   # freeProxy03: fetch proxy 27.38.155.218:8088,proxy_count:145
   # freeProxy03: fetch proxy 60.5.254.169:8081,proxy_count:146
   # freeProxy03: fetch proxy 120.234.138.102:53779,proxy_count:147
   # freeProxy03: fetch proxy 36.22.208.248:8118,proxy_count:148
   # freeProxy03: fetch proxy 116.196.85.150:3128,proxy_count:149
   # freeProxy03: fetch proxy 59.38.63.103:9797,proxy_count:150
   # freeProxy03: fetch proxy 163.125.149.118:9797,proxy_count:151
   # freeProxy03: fetch proxy 139.155.41.15:8118,proxy_count:152
   # freeProxy03: fetch proxy 203.110.164.139:52144,proxy_count:153
   # freeProxy03: fetch proxy 112.95.26.121:8088,proxy_count:154
   # freeProxy03: fetch proxy 163.125.159.124:8888,proxy_count:155
   # freeProxy03: fetch proxy 112.95.205.64:8888,proxy_count:156
   # freeProxy03: fetch proxy 112.95.26.150:8088,proxy_count:157
   # freeProxy03: fetch proxy 118.187.58.35:53281,proxy_count:158
   # freeProxy03: fetch proxy 112.95.205.60:8888,proxy_count:159
   # freeProxy03: fetch proxy 103.10.86.203:8080,proxy_count:160
   # freeProxy03: fetch proxy 49.85.211.213:8118,proxy_count:161
   # freeProxy03: fetch proxy 125.32.80.29:8080,proxy_count:162
   # freeProxy03: fetch proxy 115.233.210.218:808,proxy_count:163
   # freeProxy03: fetch proxy 180.139.113.198:8118,proxy_count:164
   # freeProxy03: fetch proxy 221.122.91.61:8080,proxy_count:165
   # freeProxy03: fetch proxy 116.252.39.176:53281,proxy_count:166
   # freeProxy03: fetch proxy 61.133.87.228:55443,proxy_count:167
   # freeProxy03: fetch proxy 112.95.205.52:9999,proxy_count:168
   # freeProxy03: fetch proxy 183.247.152.98:53281,proxy_count:169
   # freeProxy03: fetch proxy 111.160.169.54:42626,proxy_count:170
   # freeProxy03: fetch proxy 221.13.156.158:55443,proxy_count:171
   # freeProxy03: fetch proxy 58.251.228.113:9797,proxy_count:172
   # freeProxy03: fetch proxy 110.191.252.240:8118,proxy_count:173
   # freeProxy03: fetch proxy 112.95.205.59:8888,proxy_count:174
   # freeProxy03: fetch proxy 112.95.205.68:8888,proxy_count:175
   # freeProxy03: fetch proxy 14.115.106.245:808,proxy_count:176
   # freeProxy03: fetch proxy 183.11.235.48:9292,proxy_count:177
   # freeProxy03: fetch proxy 183.185.177.144:9797,proxy_count:178
   # freeProxy03: fetch proxy 163.125.71.185:8888,proxy_count:179
   # freeProxy03: fetch proxy 211.101.154.105:43598,proxy_count:180
   # freeProxy03: fetch proxy 113.59.99.138:8910,proxy_count:181
   # freeProxy03: fetch proxy 182.88.119.144:9797,proxy_count:182
   # freeProxy03: fetch proxy 163.125.71.182:8888,proxy_count:183
   # freeProxy03: fetch proxy 27.38.98.196:9797,proxy_count:184
   # freeProxy03: fetch proxy 183.196.168.194:9000,proxy_count:185
   # freeProxy03: fetch proxy 14.115.104.21:808,proxy_count:186
   # freeProxy03: fetch proxy 163.125.222.213:8088,proxy_count:187
   # freeProxy03: fetch proxy 118.25.13.185:8118,proxy_count:188
   # freeProxy03: fetch proxy 183.196.170.247:9000,proxy_count:189
   # freeProxy03: fetch proxy 60.191.11.241:3128,proxy_count:190
   # freeProxy03: fetch proxy 59.37.18.243:3128,proxy_count:191
   # freeProxy03: fetch proxy 122.241.225.227:60004,proxy_count:192
   # freeProxy03: fetch proxy 163.125.220.174:8088,proxy_count:193
   # freeProxy03: fetch proxy 27.38.98.203:9797,proxy_count:194
   # freeProxy03: fetch proxy 163.125.222.215:8088,proxy_count:195
   # freeProxy03: fetch proxy 163.125.71.176:8888,proxy_count:196
   # freeProxy03: fetch proxy 163.125.71.184:8888,proxy_count:197
   # freeProxy03: fetch proxy 163.125.71.180:9999,proxy_count:198
   # freeProxy03: fetch proxy 106.37.195.199:8080,proxy_count:199
   # freeProxy04: fetch proxy 182.46.111.190:12219,proxy_count:0
   # freeProxy04: fetch proxy 120.83.96.70:12219,proxy_count:1
   # freeProxy04: fetch proxy 163.125.157.34:8888,proxy_count:2
   # freeProxy04: fetch proxy 59.38.62.107:9797,proxy_count:3
   # freeProxy04: fetch proxy 219.131.240.246:9797,proxy_count:4
   # freeProxy04: fetch proxy 118.114.194.229:8318,proxy_count:5
   # freeProxy04: fetch proxy 122.241.225.227:60004,proxy_count:6
   # freeProxy04: fetch proxy 121.237.148.247:3000,proxy_count:7
   # freeProxy04: fetch proxy 112.194.112.175:8318,proxy_count:8
   # freeProxy04: fetch proxy 113.121.20.64:12219,proxy_count:9
   # freeProxy04: fetch proxy 117.64.235.243:3133,proxy_count:10
   # freeProxy04: fetch proxy 175.43.57.18:12219,proxy_count:11
   # freeProxy04: fetch proxy 144.123.69.180:12219,proxy_count:12
   # freeProxy04: fetch proxy 113.194.30.179:12219,proxy_count:13
   # freeProxy04: fetch proxy 59.62.4.5:9000,proxy_count:14
   # freeProxy04: fetch proxy 60.186.147.216:9000,proxy_count:15
   # freeProxy04: fetch proxy 60.168.206.95:8010,proxy_count:16
   # freeProxy04: fetch proxy 59.62.54.152:9000,proxy_count:17
   # freeProxy04: fetch proxy 113.195.225.42:12219,proxy_count:18
   # freeProxy04: fetch proxy 113.120.34.157:12219,proxy_count:19
   # freeProxy05: fetch proxy 110.243.2.66:9999,proxy_count:0
   # freeProxy05: fetch proxy 171.13.203.95:9999,proxy_count:1
   # freeProxy05: fetch proxy 163.204.245.179:9999,proxy_count:2
   # freeProxy05: fetch proxy 171.13.201.147:9999,proxy_count:3
   # freeProxy05: fetch proxy 171.11.33.206:9999,proxy_count:4
   # freeProxy05: fetch proxy 106.42.216.54:9999,proxy_count:5
   # freeProxy05: fetch proxy 182.46.206.6:9999,proxy_count:6
   # freeProxy05: fetch proxy 27.188.64.70:8060,proxy_count:7
   # freeProxy05: fetch proxy 113.121.43.66:9999,proxy_count:8
   # freeProxy05: fetch proxy 115.218.3.160:9000,proxy_count:9
   # freeProxy05: fetch proxy 118.113.246.227:9999,proxy_count:10
   # freeProxy05: fetch proxy 171.11.178.36:9999,proxy_count:11
   # freeProxy05: fetch proxy 36.249.49.30:9999,proxy_count:12
   # freeProxy05: fetch proxy 124.65.136.2:8060,proxy_count:13
   # freeProxy05: fetch proxy 163.204.247.73:9999,proxy_count:14
   # freeProxy05: fetch proxy 221.229.252.98:9797,proxy_count:15
   # freeProxy05: fetch proxy 124.237.83.14:53281,proxy_count:16
   # freeProxy05: fetch proxy 218.22.7.62:53281,proxy_count:17
   # freeProxy05: fetch proxy 123.163.96.80:9999,proxy_count:18
   # freeProxy05: fetch proxy 123.139.56.238:9999,proxy_count:19
   # freeProxy05: fetch proxy 163.125.18.59:8888,proxy_count:20
   # freeProxy05: fetch proxy 125.46.0.62:53281,proxy_count:21
   # freeProxy05: fetch proxy 117.141.155.241:53281,proxy_count:22
   # freeProxy05: fetch proxy 125.46.0.62:53281,proxy_count:23
   # freeProxy05: fetch proxy 163.125.18.65:8888,proxy_count:24
   # freeProxy05: fetch proxy 125.46.0.62:53281,proxy_count:25
   # freeProxy05: fetch proxy 123.139.56.238:9999,proxy_count:26
   # freeProxy05: fetch proxy 124.205.155.153:9090,proxy_count:27
   # freeProxy05: fetch proxy 58.249.55.222:9797,proxy_count:28
   # freeProxy05: fetch proxy 123.139.56.238:9999,proxy_count:29
   # freeProxy07: fetch proxy 58.215.219.2:8000,proxy_count:0
   # freeProxy07: fetch proxy 59.62.25.95:9000,proxy_count:1
   # freeProxy07: fetch proxy 47.244.126.160:8081,proxy_count:2
   # freeProxy07: fetch proxy 163.204.242.102:9999,proxy_count:3
   # freeProxy07: fetch proxy 175.24.18.94:8888,proxy_count:4
   # freeProxy07: fetch proxy 118.212.107.33:9999,proxy_count:5
   # freeProxy07: fetch proxy 149.129.117.44:80,proxy_count:6
   # freeProxy07: fetch proxy 211.142.169.4:808,proxy_count:7
   # freeProxy07: fetch proxy 47.52.220.222:8080,proxy_count:8
   # freeProxy07: fetch proxy 103.125.218.47:80,proxy_count:9
   # freeProxy07: fetch proxy 183.166.111.135:9999,proxy_count:10
   # freeProxy07: fetch proxy 113.194.31.206:9999,proxy_count:11
   # freeProxy07: fetch proxy 113.120.37.0:9999,proxy_count:12
   # freeProxy07: fetch proxy 113.194.29.75:9999,proxy_count:13
   # freeProxy07: fetch proxy 60.162.74.167:9000,proxy_count:14
   # freeProxy07: fetch proxy 110.243.11.58:9999,proxy_count:15
   # freeProxy07: fetch proxy 118.113.244.118:9999,proxy_count:16
   # freeProxy07: fetch proxy 182.32.224.30:9999,proxy_count:17
   # freeProxy07: fetch proxy 183.245.6.118:8080,proxy_count:18
   # freeProxy07: fetch proxy 183.166.96.195:9999,proxy_count:19
   # freeProxy07: fetch proxy 182.32.234.5:9999,proxy_count:20
   # freeProxy07: fetch proxy 122.192.29.142:9999,proxy_count:21
   # freeProxy07: fetch proxy 171.13.201.192:9999,proxy_count:22
   # freeProxy07: fetch proxy 110.243.19.140:9999,proxy_count:23
   # freeProxy07: fetch proxy 103.140.24.21:34925,proxy_count:24
   # freeProxy07: fetch proxy 113.194.31.229:9999,proxy_count:25
   # freeProxy07: fetch proxy 113.240.254.157:8080,proxy_count:26
   # freeProxy07: fetch proxy 123.169.96.159:9999,proxy_count:27
   # freeProxy07: fetch proxy 27.43.191.87:9999,proxy_count:28
   # freeProxy07: fetch proxy 124.244.135.88:3128,proxy_count:29
   # freeProxy09: fetch proxy 221.0.115.102:80,proxy_count:0
   # freeProxy09: fetch proxy 58.61.154.153:8080,proxy_count:1
   # freeProxy09: fetch proxy 58.220.95.90:9401,proxy_count:2
   # freeProxy09: fetch proxy 58.220.95.54:9400,proxy_count:3
   # freeProxy09: fetch proxy 61.135.185.92:80,proxy_count:4
   # freeProxy09: fetch proxy 61.135.186.80:80,proxy_count:5
   # freeProxy09: fetch proxy 61.135.185.78:80,proxy_count:6
   # freeProxy09: fetch proxy 61.135.186.243:80,proxy_count:7
   # freeProxy09: fetch proxy 61.135.185.90:80,proxy_count:8
   # freeProxy09: fetch proxy 58.220.95.79:10000,proxy_count:9
   # freeProxy09: fetch proxy 61.135.186.222:80,proxy_count:10
   # freeProxy09: fetch proxy 61.135.185.69:80,proxy_count:11
   # freeProxy09: fetch proxy 121.69.26.14:8080,proxy_count:12
   # freeProxy09: fetch proxy 61.135.185.153:80,proxy_count:13
   # freeProxy09: fetch proxy 61.135.185.38:80,proxy_count:14
   # freeProxy13: fetch proxy 122.4.28.243:9999,proxy_count:0
   # freeProxy13: fetch proxy 117.186.49.50:55443,proxy_count:1
   # freeProxy13: fetch proxy 183.166.137.242:8888,proxy_count:2
   # freeProxy13: fetch proxy 218.75.69.50:47979,proxy_count:3
   # freeProxy13: fetch proxy 118.78.196.186:8118,proxy_count:4
   # freeProxy13: fetch proxy 125.108.68.149:9000,proxy_count:5
   # freeProxy13: fetch proxy 113.194.29.99:9999,proxy_count:6
   # freeProxy13: fetch proxy 36.248.133.9:9999,proxy_count:7
   # freeProxy13: fetch proxy 120.83.97.66:9999,proxy_count:8
   # freeProxy13: fetch proxy 171.35.171.223:9999,proxy_count:9
   # freeProxy13: fetch proxy 110.243.13.189:9999,proxy_count:10
   # freeProxy13: fetch proxy 124.205.155.148:9090,proxy_count:11
   # freeProxy13: fetch proxy 110.243.6.83:9999,proxy_count:12
   # freeProxy13: fetch proxy 163.204.243.52:9999,proxy_count:13
   # freeProxy13: fetch proxy 36.249.52.17:9999,proxy_count:14
   # freeProxy13: fetch proxy 182.34.36.186:9999,proxy_count:15
   # freeProxy13: fetch proxy 58.253.159.131:9999,proxy_count:16
   # freeProxy13: fetch proxy 110.243.23.4:9999,proxy_count:17
   # freeProxy13: fetch proxy 110.243.10.127:9999,proxy_count:18
   # freeProxy13: fetch proxy 1.199.30.61:9999,proxy_count:19
   # freeProxy14: fetch proxy 47.107.160.99:8118,proxy_count:0
   # freeProxy14: fetch proxy 36.255.86.229:82,proxy_count:1
   # freeProxy14: fetch proxy 119.119.248.109:9000,proxy_count:2
   # freeProxy14: fetch proxy 119.254.94.114:34422,proxy_count:3
   # freeProxy14: fetch proxy 115.218.213.35:9000,proxy_count:4
   # freeProxy14: fetch proxy 171.35.166.93:9999,proxy_count:5
   # freeProxy14: fetch proxy 222.21.112.8:80,proxy_count:6
   # freeProxy14: fetch proxy 111.13.241.170:80,proxy_count:7
   # freeProxy14: fetch proxy 183.245.149.27:8080,proxy_count:8
   # freeProxy14: fetch proxy 171.35.161.92:9999,proxy_count:9
   # freeProxy14: fetch proxy 202.109.157.66:9000,proxy_count:10
   # freeProxy14: fetch proxy 113.68.160.145:1080,proxy_count:11
   # freeProxy14: fetch proxy 183.245.149.11:8080,proxy_count:12
   # freeProxy14: fetch proxy 118.212.104.7:9999,proxy_count:13
   # freeProxy14: fetch proxy 183.237.147.129:8080,proxy_count:14
   # freeProxy14: fetch proxy 115.218.3.219:9000,proxy_count:15
   # freeProxy14: fetch proxy 183.245.144.116:8080,proxy_count:16
   # freeProxy14: fetch proxy 120.25.90.253:8118,proxy_count:17
   # freeProxy14: fetch proxy 182.34.34.148:9999,proxy_count:18
   # freeProxy14: fetch proxy 123.101.237.21:9999,proxy_count:19
   # freeProxy14: fetch proxy 115.213.228.132:3000,proxy_count:20
   # freeProxy14: fetch proxy 61.130.181.231:20195,proxy_count:21
   # freeProxy14: fetch proxy 120.83.106.82:9999,proxy_count:22
   # freeProxy14: fetch proxy 49.235.69.138:8118,proxy_count:23
   # freeProxy14: fetch proxy 115.29.42.152:80,proxy_count:24
   # freeProxy14: fetch proxy 218.75.158.153:3128,proxy_count:25
   # freeProxy14: fetch proxy 221.122.91.64:80,proxy_count:26
   # freeProxy14: fetch proxy 221.226.94.218:110,proxy_count:27
   # freeProxy14: fetch proxy 58.253.157.135:9999,proxy_count:28
   # freeProxy14: fetch proxy 163.204.243.254:9999,proxy_count:29
   # freeProxy14: fetch proxy 47.107.160.99:8118,proxy_count:0
   # freeProxy14: fetch proxy 36.255.86.229:82,proxy_count:1
   # freeProxy14: fetch proxy 119.119.248.109:9000,proxy_count:2
   # freeProxy14: fetch proxy 119.254.94.114:34422,proxy_count:3
   # freeProxy14: fetch proxy 115.218.213.35:9000,proxy_count:4
   # freeProxy14: fetch proxy 171.35.166.93:9999,proxy_count:5
   # freeProxy14: fetch proxy 222.21.112.8:80,proxy_count:6
   # freeProxy14: fetch proxy 111.13.241.170:80,proxy_count:7
   # freeProxy14: fetch proxy 183.245.149.27:8080,proxy_count:8
   # freeProxy14: fetch proxy 171.35.161.92:9999,proxy_count:9
   # freeProxy14: fetch proxy 202.109.157.66:9000,proxy_count:10
   # freeProxy14: fetch proxy 113.68.160.145:1080,proxy_count:11
   # freeProxy14: fetch proxy 183.245.149.11:8080,proxy_count:12
   # freeProxy14: fetch proxy 118.212.104.7:9999,proxy_count:13
   # freeProxy14: fetch proxy 183.237.147.129:8080,proxy_count:14
   # freeProxy14: fetch proxy 115.218.3.219:9000,proxy_count:15
   # freeProxy14: fetch proxy 183.245.144.116:8080,proxy_count:16
   # freeProxy14: fetch proxy 120.25.90.253:8118,proxy_count:17
   # freeProxy14: fetch proxy 182.34.34.148:9999,proxy_count:18
   # freeProxy14: fetch proxy 123.101.237.21:9999,proxy_count:19
   # freeProxy14: fetch proxy 115.213.228.132:3000,proxy_count:20
   # freeProxy14: fetch proxy 61.130.181.231:20195,proxy_count:21
   # freeProxy14: fetch proxy 120.83.106.82:9999,proxy_count:22
   # freeProxy14: fetch proxy 49.235.69.138:8118,proxy_count:23
   # freeProxy14: fetch proxy 115.29.42.152:80,proxy_count:24
   # freeProxy14: fetch proxy 218.75.158.153:3128,proxy_count:25
   # freeProxy14: fetch proxy 221.122.91.64:80,proxy_count:26
   # freeProxy14: fetch proxy 221.226.94.218:110,proxy_count:27
   # freeProxy14: fetch proxy 58.253.157.135:9999,proxy_count:28
   # freeProxy14: fetch proxy 163.204.243.254:9999,proxy_count:29