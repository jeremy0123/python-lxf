# -*- coding: utf-8 -*-

# try except else finally

try:
    print 'try...'
    r = 10 / int('1')
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
else:
    print 'no error!'
finally:
    print 'finally'

print 'END'

# https://docs.python.org/2/library/exceptions.html#exception-hierarchy

print '-------------------------------------------------------------------------'

# logging
import logging
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        logging.exception(e) # 不捕获错误，只打印，让程序继续

main()
print 'END'

print '-------------------------------------------------------------------------'

class FooError(StandardError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        print e

main()
print 'END'

print '-------------------------------------------------------------------------'
def foo(s):
    n = int(s)
    return 10 / n

def bar(s):
    try:
        return foo(s) * 2
    except StandardError, e:
        print 'Error!'
        raise # 不带参数，原样抛出错误

def main():
    bar('0')

main()
