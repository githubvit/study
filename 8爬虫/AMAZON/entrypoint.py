# 调命令行的执行器 执行 scrapy crawl amazon 命令 运行爬虫

# 要切换到 项目目录下 运行该py 不然会报 no active project
# (venv) D:\pyj\st\study>d:/pyj/st/venv/Scripts/python.exe d:/pyj/st/study/8爬虫/AMAZON/entrypoint.py
# Scrapy 2.0.1 - no active project

# Unknown command: crawl

# Use "scrapy" to see available commands
from scrapy.cmdline import execute

# execute(['scrapy','crawl','amazon'])
# execute(['scrapy','crawl','--nolog','amazon']) # 如果爬虫的parse是pass,干掉了日志信息，就什么都没有了
# 给url传参 keyword=''
execute(['scrapy','crawl','amazon','-a','参数key=value','--nolog'])

