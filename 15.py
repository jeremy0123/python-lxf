# -*- coding: utf-8 -*-

# 列表生成式
print [x * x for x in range(1, 11)]

print [x * x for x in range(1, 11) if x % 2 == 0]

print [m + n for m in 'ABC' for n in 'XYZ'] # +号表示字符串连接

# 打印当前文件夹和目录
import os
print [d for d in os.listdir('.')]

d = {
    'a': 1,
    'b': 2,
    'c': 3
}

print [k + '=' + str(v) for k,v in d.iteritems()]

L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]

L = ['Hello', 'World', 18, 'IBM', 'Apple']
print [s.lower() for s in L if isinstance(s, str)]
