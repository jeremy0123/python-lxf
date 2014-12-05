# -*- coding: utf-8 -*-

# 给实例绑定属性和方法
class Student(object):
    pass

s = Student()
s.name = "Machael"
print s.name

def set_age(self, age):
    self.age = age

from types import MethodType # 部分引入
s.set_age = MethodType(set_age, s, Student) # 给实例绑定方法
s.set_age(25)
print s.age

s2 = Student()
# s2.set_age(25) #Error 另一个实例不存在此方法

def set_score(self, score):
    self.score = score
Student.set_score = MethodType(set_score, None, Student) # 给类绑定方法
s.set_score(61)
s2.set_score(59)
print s.score
print s2.score

print '-------------------------------------------------------------------------'

# __slots__ 限制属性
class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Machael'
s.age = 25
# s.score = 99 # Error
# s.set_age = MethodType(set_age, s, Student) # Error

# __slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的

class GraduateStudent(Student):
    __slots__ = 'set_age'

g = GraduateStudent()
g.name = 'jeremy'
g.age = 30
g.set_age = MethodType(set_age, g, GraduateStudent)
# g.score = 99 # Error

# 子类中也定义__slots__，子类允许定义的属性就是自身的__slots__加上父类的__slots__。
