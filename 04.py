# -*- coding: utf-8 -*-
# 转义字符串
print 'I\'m ok.'
print '\\\n\\'
print '\\\t\\'
print r'\\\t\\' # r'' 表示''中字符串默认不转义
print '''line1
line2
line3''' #''' ... ''' 表示多行内容，也可以加r配合使用

# True False and or not
print 3 > 2
print 3 > 2 and 2 > 3
print not False

age = 19
if age < 18:    print 'Not Adult'
if age == 18:
    print '18'
else:
    print 'Adult'

#None 类似于null
print None

# Python解释器干了两件事情：
# * 在内存中创建了一个'ABC'的字符串；
# * 在内存中创建了一个名为a的变量，并把它指向'ABC'。
a = 'ABC'
print a

# 在Python中，通常用全部大写的变量名表示常量 PI 
PI = 3.14159265359
print PI
