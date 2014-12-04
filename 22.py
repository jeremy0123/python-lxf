# -*- coding:utf-8 -*-

# Python提供了__future__模块，把下一个新版本的特性导入到当前版本，于是我们就可以
# 在当前版本中测试一些新版本的特性。

# still running on Python 2.7

from __future__ import unicode_literals

print '\'xxx\' is unicode?', isinstance('xxx', unicode)
print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
print '\'xxx\' is str?', isinstance('xxx', str)
print 'b\'xxx\' is str?', isinstance(b'xxx', str)

# 2.x里的字符串用'xxx'表示str，Unicode字符串用u'xxx'表示unicode，而在3.x中，
# 所有字符串都被视为unicode，因此，写u'xxx'和'xxx'是完全一致的，而在2.x中以'xxx'
# 表示的str就必须写成b'xxx'，以此表示“二进制字符串”。
