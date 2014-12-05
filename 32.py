# -*- coding:utf-8 -*-

# type()创建类
from Test import Hello
h = Hello()
h.hello()
print type(Hello) # <type 'type'>
print type(h) # <class 'Test.Hello'>
# class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。

def fn(self, name='world'): # 先定义函数
    print 'Hello, %s.' % name

Hello = type('A', (object, ), dict(hello=fn)) # 创建Hello class
h = Hello()
h.hello()
print type(Hello)
print type(h)

#type() 参数
#class的名称；
#继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
#class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

print '-------------------------------------------------------------------------'
# metaclass 元类
# metaclass的类名总是以Metaclass结尾
class ListMetaclass(type): # metaclass是创建类，所以必须从`type`类型派生
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        # return type.__new__(cls, name, bases, attrs)
        return super(ListMetaclass, cls).__new__(cls, name, bases, attrs) # 也可以用这种方式


class MyList(list):
    __metaclass__ = ListMetaclass

l = MyList()
l.add(1)
print l

# __new__()的参数
# 当前准备创建的类的对象；
# 类的名字；
# 类继承的父类集合；
# 类的方法集合。

# 用途：ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的
# 一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。
