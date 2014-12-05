# -*- coding:utf-8 -*-

# 函数和类的定义，不是编译时定义的，而是运行时动态创建的

class Hello(object):
    def hello(self, name="world"):
        print 'Hello, %s' % name
