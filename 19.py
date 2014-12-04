# -*- coding: utf-8 -*-

# 装饰器 decorator

def now():
    print '2014-12-03'

f = now
f()
# 函数也是一个对象 函数对象有一个__name__属性
print now.__name__
print f.__name__

# ------------------------------------------------------------------------------
# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

@log # 等价于 now = log(now)
def now():
    print '2014-12-03'

now()
print now.__name__ # wrapper 已经改变了属性，需要改回来

# ------------------------------------------------------------------------------
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log('exectute') #等价于 now = log('execute')(now)
def now():
    print '2014-12-03'

now()
print now.__name__ # wrapper 已经改变了属性，需要改回来

# ------------------------------------------------------------------------------
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
@log # 等价于 now = log(now)
def now():
    print '2014-12-03'
now()
print now.__name__ # now

# ------------------------------------------------------------------------------
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        #wrapper.__name__ = func.__name__ # 替换@functools.wraps(func)
        return wrapper
    return decorator

@log('exectute') #等价于 now = log('execute')(now)
def now():
    print '2014-12-03'
now()
print now.__name__ # now
