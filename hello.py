#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test mode ' # 文档注释 任何模块代码的第一个字符串都被视为模块的文档注释

__author__ = 'Jeremy0123' # 注释

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print 'Hello, world!'
    elif len(args) == 2:
        print 'Hello %s!' % args[1]
    else:
        print 'Too Many arguments!'

if __name__ == '__main__':
    test()

# 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
# 而如果在其他地方导入该hello模块时，if判断将失败，因此，
# 这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。

# ------------------------------------------------------------------------------

try:
    import cStringIO as StringIO
except ImportError: # 导入失败会捕获到ImportError
    import StringIO

try:
    import json # python >= 2.6
except ImportError:
    import simplejson as json # python <= 2.5

# 有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的。

def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
