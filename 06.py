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

# tuple 元祖 一旦初始化就不能修改
classmates = ('Machael', 'Bob', 'Tracy')
print classmates

# tuple 定义一个元素时，不能写成(1)，而应该写成(1, )
print (1)
print (1, )

# 理解tuple为什么不变以及指向的关系
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X' # t[2]指向没变，但是t[2][0]的指向变了
t[2][1] = 'Y'
print t
