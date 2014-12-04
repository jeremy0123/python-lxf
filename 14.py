# -*- coding: utf-8 -*-

# 迭代 itervalues() iteritems()
d = {
    'a': 1,
    'b': 2,
    'c': 3
}

print d
for key in d:
    print key

for value in d.itervalues():
    print value

for k, v in d.iteritems():
    print k, "=", v

# str也可以迭代

# 判断一个对象是否是可迭代的，通过collections的Iterable类型判断
from collections import Iterable
print isinstance('abc', Iterable)
print isinstance([1, 2, 3], Iterable)
print isinstance(123, Iterable)

# 下标循环 enumerate把list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print i, value
