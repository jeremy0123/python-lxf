# -*-coding: utf-8 -*-

# 偏函数 partial function

print int('12345')
print int('12345', base=8)
print int('12345', base=16)

def int2(x, base=2):
    return int(x, base)

print int2('1000000')
print int2('1010101')

import functools
int2 = functools.partial(int, base=2)
print int2('1000000')
print int2('1010101')

# 简单总结functools.partial的作用就是，把一个函数的某些参数（不管有没有默认值）
# 给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
print int2('1000000', base=10) # base虽然有默认值，但也可以传入其他值
