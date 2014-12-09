# -*- coding: utf-8 -*-

# itertools

import itertools
natuals = itertools.count(1)
cs = itertools.cycle('abc')
# for n in natuals:
#     print n

ns = itertools.repeat('A', 10)
for n in ns:
    print n

# 无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。
# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
for n in ns:
    print n

# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC', 'XYZ'):
    print c

# groupby()把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AAABBCCCAA'):
    print key, list(group)

# imap()和map()的区别在于，imap()可以作用于无穷序列，并且，如果两个序列的长度不一致，以短的那个为准。
for x in itertools.imap(lambda x, y: x * y, [10, 20, 30], itertools.count(1)):
    print x
# 注意imap()返回一个迭代对象，而map()返回list。当你调用map()时，已经计算完毕
# imap()实现了“惰性计算”，也就是在需要获得结果的时候才计算。
r = itertools.imap(lambda x: x*x, itertools.count(1))
for n in itertools.takewhile(lambda x: x < 100, r):
    print n
