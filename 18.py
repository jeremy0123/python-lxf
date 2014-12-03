# -*- coding: utf-8 -*-

print map(lambda x: x * x, [1, 3, 5, 7, 9])

# lambda 匿名函数，:前表示参数，只能有一个表达式，不用写return

f = lambda x, y: x * y
print f
print f(2, 4)

# Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数。
