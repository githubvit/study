import re
# print(re.findall('\w','ab 12\+- *&_'))
#                                  \w
# print(re.findall('\W','ab 12\+- *&_'))
# print(re.findall('\s','ab \r1\n2\t\+- *&_'))
# print(re.findall('\S','ab \r1\n2\t\+- *&_'))
# print(re.findall('\d','ab \r1\n2\t\+- *&_'))
                    #                    \d
# print(re.findall('\D','ab \r1\n2\t\+- *&_'))

# print(re.findall('\w_sb','egon alex_sb123123wxx_sb,lxx_sb'))
#                                                       \w_sb

# print(re.findall('\Aalex','abcalex is salexb'))
# print(re.findall('\Aalex','alex is salexb'))
# print(re.findall('^alex','alex is salexb'))
# print(re.findall('sb\Z','alexsb is sbalexbsb'))
# print(re.findall('sb$','alexsb is sbalexbsb'))
#                                           sb

# print(re.findall('^ebn$','ebn1'))
#                           ebn


# print(re.findall('a\nc','a\nc a\tc a1c'))


# 重复匹配：
#.   ?   *   +  {m,n}  .*  .*?
#1、.:代表除了换行符外的任意一个字符
# print(re.findall('a.c','abc a1c aAc aaaaaca\nc'))
#                                           a.c
# print(re.findall('a.c','abc a1c aAc aaaaaca\nc',re.DOTALL))

#2、？：代表左边那一个字符重复0次或1次
# print(re.findall('ab?','a ab abb abbb abbbb abbbb'))
#                                      ab?

#3、*：代表左边那一个字符出现0次或无穷次
# print(re.findall('ab*','a ab abb abbb abbbb abbbb a1bbbbbbb'))
#                                                   ab*

#4、+ ：代表左边那一个字符出现1次或无穷次
# print(re.findall('ab+','a ab abb abbb abbbb abbbb a1bbbbbbb'))
#                                                    ab+

#5、{m,n}:代表左边那一个字符出现m次到n次
# print(re.findall('ab?','a ab abb abbb abbbb abbbb'))
# print(re.findall('ab{0,1}','a ab abb abbb abbbb abbbb'))

# print(re.findall('ab*','a ab abb abbb abbbb abbbb a1bbbbbbb'))
# print(re.findall('ab{0,}','a ab abb abbb abbbb abbbb a1bbbbbbb'))

# print(re.findall('ab+','a ab abb abbb abbbb abbbb a1bbbbbbb'))
# print(re.findall('ab{1,}','a ab abb abbb abbbb abbbb a1bbbbbbb'))


# print(re.findall('ab{1,3}','a ab abb abbb abbbb abbbb a1bbbbbbb'))


#6、.*：匹配任意长度，任意的字符=====》贪婪匹配
# print(re.findall('a.*c','ac a123c aaaac a *123)()c asdfasfdsadf'))
#                        a.*c

#7、.*？：非贪婪匹配
# print(re.findall('a.*?c','a123c456c'))




# ():分组
# print(re.findall('(alex)_sb','alex_sb asdfsafdafdaalex_sb'))

#                            (alex)_sb

# print(re.findall(
#     'href="(.*?)"',
#     '<li><a id="blog_nav_sitehome" class="menu" href="http://www.cnblogs.com/">博客园</a></li>')
# )
# <li><a id="blog_nav_sitehome" class="menu" href="http://www.cnblogs.com/">博客园</a></li>
#                                           href=".*?"


# []:匹配一个指定范围内的字符（这一个字符来自于括号内定义的）
# print(re.findall('a[0-9][0-9]c','a1c a+c a2c a9c a11c a-c acc aAc'))

#当-需要被当中普通符号匹配时，只能放到[]的最左边或最 右边
# print(re.findall('a[-+*]c','a1c a+c a2c a9c a*c a11c a-c acc aAc'))

# print(re.findall('a[a-zA-Z]c','a1c a+c a2c a9c a*c a11c a-c acc aAc'))


# []内的^代表取反的意思
# print(re.findall('a[^a-zA-Z]c','a c a1c a+c a2c a9c a*c a11c a-c acc aAc'))
# print(re.findall('a[^0-9]c','a c a1c a+c a2c a9c a*c a11c a-c acc aAc'))


# print(re.findall('([a-z]+)_sb','egon alex_sb123123wxxxxxxxxxxxxx_sb,lxx_sb'))
#                                                [a-z]+_sb



# | :或者
# print(re.findall('compan(ies|y)','Too many companies have gone bankrupt, and the next one is my company'))

# (?:):代表取匹配成功的所有内容，而不仅仅只是括号内的内容
# print(re.findall('compan(?:ies|y)','Too many companies have gone bankrupt, and the next one is my company'))

# print(re.findall('alex|sb','alex sb sadfsadfasdfegon alex sb egon'))




# re模块的其他方法：
# print(re.findall('alex|sb','123123 alex sb sadfsadfasdfegon alex sb egon'))
# print(re.search('alex|sb','123213 alex sb sadfsadfasdfegon alex sb egon').group())
# print(re.search('^alex','123213 alex sb sadfsadfasdfegon alex sb egon'))

# print(re.search('^alex','alex sb sadfsadfasdfegon alex sb egon').group())
# print(re.match('alex','alex sb sadfsadfasdfegon alex sb egon').group())
# print(re.match('alex','123213 alex sb sadfsadfasdfegon alex sb egon'))


# info='a:b:c:d'
# print(info.split(':'))
# print(re.split(':',info))

# info=r'get :a.txt\3333/rwx'
# print(re.split('[ :\\\/]',info))


# print('egon is beutifull egon'.replace('egon','EGON',1))

# print(re.sub('(.*?)(egon)(.*?)(egon)(.*?)',r'\1\2\3EGON\5','123 egon is beutifull egon 123'))

#              (123 )(egon)( is beutifull )(egon)( 123)

#\1\2\3EGON\5

# print(re.sub('(lqz)(.*?)(SB)',r'\3\2\1',r'lqz is SB'))
# print(re.sub('([a-zA-Z]+)([^a-zA-Z]+)([a-zA-Z]+)([^a-zA-Z]+)([a-zA-Z]+)',r'\5\2\3\4\1',r'lqzzzz123+ is SB'))

#(lqzzzz)(123+ )(is)( )(SB)


pattern=re.compile('alex')
print(pattern.findall('alex is alex alex'))
print(pattern.findall('alexasdfsadfsadfasdfasdfasfd is alex alex'))

