# -*- coding:utf-8 -*-

# 获取对象信息
def hello():
    print 'hello world'

print type(hello)
# print isinstance(hello, func)
print hasattr(hello, '__call__') # 注意判断一个obj是否是一个函数

print type(123)
print type('str')
print type(None)

import types
print type('abc') == types.StringType
print type(u'abc') == types.UnicodeType
print type([]) == types.ListType
print type(str) == types.TypeType #所有类型本身的类型就是TypeType
print type(hello) == types.FunctionType # 判断是否是一个函数

# str和unicode都是从basestring继承下来的

print '------------------------------------------------------------------------'
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
print dir('abc')

# getattr()、setattr()以及hasattr()
class MyObj(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObj()
print hasattr(obj, 'x')
print hasattr(obj, 'y')
setattr(obj, 'y', 19)
print hasattr(obj, 'y')
print getattr(obj, 'y')
print obj.y
print getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
print hasattr(obj, 'power')
print getattr(obj, 'power')
fn = getattr(obj, 'power')
print fn
print fn()
