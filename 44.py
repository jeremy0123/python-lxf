# -*- coding: utf-8 -*-

# 多线程
# Python的标准库提供了两个模块：thread和threading 只需要使用threading这个高级模块。

import time, threading

def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >> %s' % (threading.current_thread().name, n)
    print 'thread %s ended.' % threading.current_thread().name

print 'thread %s is running...' % threading.current_thread().name
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print 'thread %s ended.' % threading.current_thread().name
