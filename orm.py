# -*- coding: utf-8 -*-

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' %(self.__class__.__name__, self.name)

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)

        mappings = dict()
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                print('Found mappings: %s==>%s' % (k, v))
                mappings[k] = v
        for k in mappings.iterkeys():
            attrs.pop(k)
        attrs['__table__'] = name # 假设表名和类名一致
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        return type.__new__(cls, name, bases, attrs)

class Model(dict):
    print 'begin Model'
    __metaclass__ = ModelMetaclass
    print 'after metaclass'

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            return AttributeError(r"'Model' Object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        print key, value
        self[key] = value

    def save(self):
        field = []
        params = []
        args = []
        for k, v in self.__mappings__.iteritems():
            field.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None)) # 如果getattr没有的话，取值None
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(field), ','.join(params))

        print 'SQL: %s' % sql
        print 'ARGS: %s' % str(args)

class User(Model):
    # 定义类的属性到列的映射：
    print 'begin'
    id = IntegerField('db_id')
    # print 'hello'
    name = StringField('db_username')
    email = StringField('db_email')
    password = StringField('db_password')
    print 'end'

print '----'
u = User()
#setattr(u, 'id', 12345)
u.id = 12345 # 以上两个方法均可
setattr(u, 'name', 'jeremy')
setattr(u, 'email', 'jeremy0123@163.com')
setattr(u, 'password', 'pwd')
u.save()

print '-----'
u2 = User(id=34567, name='hello', email='test', password='123456')
u2.save()



# User类定义，先定义其父类，后定义自身，类定义结束时触发metaclass的__new__()方法，
# Model触发时，由于__new__()将其排除，故什么都没做，User触发时，将id = IntegerField('db_id')
# 映射为dict的一个键值对，并且从attr中去除，避免冲突 -- 见后面的示例
# 当u实例实际是dict，对属性赋值就是设置到了dict中
# 所以，id对应两个，一个是__mapping__中，对应IntegerField('db_id')
# 另一个是User本身，对应12345，通过save()的getattr取出

print '-------------------------------------------------------------------------'
# 类的属性和实例的属性
class Student(object):
    name = 'Student'

s = Student()
print s.name # Student
print Student.name # Student
s.name = 'Michael'
print s.name # Michael
print Student.name # Student
del s.name
print s.name # Student

# 当实例的属性被删除后，或默认加载类的属性
# 故上述例子中，需要把类的属性默认pop()掉

# http://blog.jobbole.com/21351/ 关于元类的解释
