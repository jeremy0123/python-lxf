# -*- coding: utf-8 -*-


# @property 强封装
class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be integer!')
        if score < 0 or score > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = score

s = Student()
s.set_score(60)
print s.get_score()
# s.set_score(9999) # Error
s._score = 900 # 还是能绕开判断
print s.get_score()

print '-------------------------------------------------------------------------'

class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    # 不定义setter方法就是一个只读属性
    @property
    def age(self):
        return 2014 - self._birth

    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self, value):
        self._birth = value

s = Student()
s.score = 60
print s.score
# s.score = 9999 #error
s.birth = 1983
print s.age
