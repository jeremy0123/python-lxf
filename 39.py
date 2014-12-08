# -*- coding: utf-8 -*-

# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，
# 在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。

# Python提供两个模块来实现序列化：cPickle和pickle。这两个模块功能是一样的，
# 区别在于cPickle是C语言写的，速度快，pickle是纯Python写的，速度慢

try:
    import cPickle as pickle
except ImportError:
    import pickle

d = dict(name='bob', age=20, score=88)
f = open('/home/ww/python/python-lxf/dump.txt', 'wb')
pickle.dump(d,f)
f.close()

f = open('/home/ww/python/python-lxf/dump.txt', 'rb')
d = pickle.load(f)
f.close()
print d

# Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，
# 并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，
# 不能成功地反序列化也没关系。

# 使用json
import json
d = dict(name='bob', age=20, score=88)
f = open('/home/ww/python/python-lxf/dump.json', 'wb')
print json.dumps(d)
f.close()

json_str = '{"age": 20, "score": 88, "name": "bob"}'
print json.loads(json_str)

print '--------'
# json 序列化一个类
import json
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    def show(self):
        print self.name, self.age, self.score

s = Student('bob', 20, 88)
# print json.dumps(s) # TypeError: <__main__.Student object at 0x1ca50d0> is not JSON serializable

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

print json.dumps(s, default=student2dict)

# 通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。
print json.dumps(s, default=lambda obj: obj.__dict__)

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print json.loads(json_str, object_hook=dict2student) # object_hook
s = json.loads(json_str, object_hook=dict2student) # object_hook
s.show()
