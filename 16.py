# -*- coding: utf-8 -*-

# 生成器Generator
# 一边循环一边计算的机制，不必创建完整的list，从而节省大量的空间

# 创建generator方法一，将[]改成()
g = (x * x for x in range(10))
print g
print g.next()
print g.next() # g保存的是算法，next()调用，计算出下一个值

for n in g:
    print n

print '--------------------------------'
# 创建generator方法二，函数加yield关键字
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1
fib(6)

print '--------------------------------'
# 执行next()的时，遇到yield语句返回， 再次执行时从上次返回的yield语句处继续执行。
def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 3
    print 'step 3'
    yield 5

o = odd()
o.next()
o.next()
o.next()
#o.next() #error

print '--------------------------------'
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b # 执行next()的时，遇到yield语句返回， 再次执行时从上次返回的yield语句处继续执行。
        a, b = b, a + b
        n = n + 1
print fib(6)

for n in fib(6):
    print n
