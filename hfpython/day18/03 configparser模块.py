import configparser

config=configparser.ConfigParser()
config.read('my.ini')

# secs=config.sections()
# print(secs)

# print(config.options('egon'))

# age=config.get('egon','age')`
# age=config.getint('egon','age')
# print(age,type(age))

# salary=config.getfloat('egon','salary')
# print(salary,type(salary))

b=config.getboolean('egon','is_beatifull')
print(b,type(b))