# -*- coding:utf-8 -*-

# 类和实例
class Student(object):
    # 类中定义函数永远以self开头
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

class Student(object):
    pass

bart = Student()
print bart
print Student

bart.name = 'Bart Simpson' # 增加类的属性
print bart.name

