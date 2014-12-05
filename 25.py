# -*- coding: utf-8 -*-

# 访问控制限制
# 让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)

bart = Student('Bart Simpson', 59)
#print bart.__name # Error
print bart._Student__name # 可以通过_Student__name来访问__name变量，但是不推荐使用
bart.print_score()

# 变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
# 特殊变量是可以直接访问的，不是private变量


