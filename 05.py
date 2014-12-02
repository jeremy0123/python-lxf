# -*- coding: utf-8 -*-

# python Unicode
print ord('A')
print chr(65)
print u'中' # u'\u4e2d'
print u'中文'

# Unicode 转换 UTF-8
print u'ABC'.encode('utf-8')
print u'中文'.encode('utf-8') # '\xe4\xb8\xad\xe6\x96\x87'

# len 返回字符串长度
print len(u'ABC')
print len('ABC')
print len(u'中文')
print len('\xe4\xb8\xad\xe6\x96\x87')

# UTF-8 转换为 Unicode
print 'abc'.decode('utf-8')
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8') 
#'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8') >>> u'\u4e2d\u6587'

# 格式化字符串
print 'Hi, %s, you have $%d.' % ('Michael', 1000000)
# Unicode 前后统一
print u'Hi, %s' % u'Michale'

# 在Python 3.x版本中，把'xxx'和u'xxx'统一成Unicode编码，即写不写前缀u都是一样的，而以字节形式表示的字符串则必须加上b前缀：b'xxx'。
