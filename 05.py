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

