# -*- coding: utf-8 -*-

# __len__()函数
class Test1:
    def __len__(self): # TypeError: __len__() should return an int
        # return '100' # Error
        return 100

a = Test1()
print len(a) # 只有定义了__len()__的类才能使用len()函数

# __str__ __repr__返回实例的信息
# __str__是返回给用户看的字符串
# __repr__是返回给开发者看的字符串
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__

print Student('Michael')

s = Student('Michael')
print s

print '-------------------------------------------------------------------------'
# __iter__
# 一个类想被用于for ... in循环，就必须实现一个__iter__()方法
# for循环就会不断调用该迭代对象的next()方法拿到循环的下一个值
# 直到遇到StopIteration错误时退出循环
class Fib(object):
    def __init__(self):
        self. a, self.b = 0, 1

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration();
        return self.a # 返回下一个值

for n in Fib():
    print n

print '-------------------------------------------------------------------------'
# __getitem__
# 取得某个值以及切片
class Fib(object):
    def __init__(self):
        self. a, self.b = 0, 1

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration();
        return self.a # 返回下一个值

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a

        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b, = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib()
print f[5]
print f[100]
print f[1:5]
print f[:10]
# 负数操作，step操作都没有，对__getitem__还要继续
# __setitem__() __delitem__()方法与其对应

print '-------------------------------------------------------------------------'
# __getattr__
# 在没有找到属性的情况下，调用__getattr__
class Student(object):
    def __init__(self):
        self.name = 'Michael'
    def __getattr__(self, attr):
        if attr == 'age': # 方法
            return lambda: 25
        if attr == 'score': # 属性
            return 90
        # 定义的__getattr__默认返回就是None 防止其他没有的属性返回None
        raise AttributeError("'Student' object has no attribute '%s'" % attr)

s = Student()
print s.name
print s.score
print s.age()
# print s.abc # Error

# __getattr__的应用，随便写属性
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

print Chain().status.user.timeline.list

print '-------------------------------------------------------------------------'
# __call__() 对实例进行调用
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print 'My name is %s.' % self.name

s = Student('Michael')
s() # 注意调用

# 判断一个对象是否能被调用，能被调用的对象就是一个Callable对象
print callable(Student('A'))
print callable(max)
print callable([1,2,3])
print callable('string')
