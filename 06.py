# -*- coding: utf-8 -*-

# list
classmates = ['Machael', 'Bob', 'Tracy']
print classmates

print len(classmates)

print classmates[0]
print classmates[1]
print classmates[2]
# print classmates[3] # Error!

# -1 最后一个元素
print classmates[-1]

# insert append pop
classmates.append('Adam')
print classmates

classmates.insert(1, 'Jack')
print classmates

print classmates.pop()
print classmates

print classmates.pop(0)
print classmates

classmates[1] = 'Sarah'
print classmates

print ['Apple', 123, True]
print ['python', 'java', ['asp', 'php'], 'scheme']
print len(['python', 'java', ['asp', 'php'], 'scheme'])
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
print s[2][1] # php
print len([])
