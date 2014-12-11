# -*- coding: utf-8 -*-

# 正则表达式

# 用\d可以匹配一个数字，\w可以匹配一个字母或数字
# .可以匹配任意字符
# 要匹配变长的字符，在正则表达式中，用*表示任意个字符（包括0个），用+表示至少一个
# 字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符
# 由于'-'是特殊字符，在正则表达式中，要用'\'转义

# 要做更精确地匹配，可以用[]表示范围
# A|B可以匹配A或B，所以[P|p]ython可以匹配'Python'或者'python'。
# ^表示行的开头，^\d表示必须以数字开头。
# $表示行的结束，\d$表示必须以数字结束。

# Python的字符串本身也用\转义 所以使用r前缀
# s = 'ABC\\-001'
# print s

import re
print re.match(r'^\d{3}\-\d{3,8}$', '010-012345')
print re.match(r'^\d{3}\-\d{3,8}$', '010 012345')

# 切分字符串
print 'a b   c'.split(' ') # 无法识别连续的空格
print re.split(r'\s+', 'a b   c')
print re.split(r'[\s\,]+', 'a, b,   c           d')
print re.split(r'[\s\,\;]+', 'a, b, ;;  c           d')

# 分组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-012345')
print m
print m.group(0)
print m.group(1)
print m.group(2)

# 贪婪匹配 匹配尽可能多的字符 \d 匹配了后面的0*
print re.match(r'^(\d+)(0*)$', '102300').groups()
# 加个?就可以让\d+采用非贪婪匹配
print re.match(r'^(\d+?)(0*)$', '102300').groups()

# 编译
# 当我们在Python中使用正则表达式时，re模块内部会干两件事情：
# 编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
# 用编译后的正则表达式去匹配字符串。
# 出于效率的考虑，我们可以预编译该正则表达式

re_tele = re.compile(r'^(\d{3})-(\d{3,8})$')
print re_tele.match('010-12345').groups()
print re_tele.match('010-8086').groups()
