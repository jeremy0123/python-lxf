# -*- coding: utf-8 -*-

#dict 字典 键值对 HashMap
d = {'Machael': 95, 'Bob': 75, 'Tracy': 85}
print d
print d['Machael']
# print d['Thomas'] # Error!

# 预防读取字典错误的方法01
if 'Thomas' in d:
    print d['Thomas']

# 预防读取字典错误的方法02
print d.get('Thomas')
# 自己制定Value，当get的为None时，显示value
print d.get('Thomas', -1)

# key的存放顺序和放入顺序无关
print d.pop('Bob')
print d

# 和list比较，dict有以下几个特点：
# *查找和插入的速度极快，不会随着key的增加而增加；
# *需要占用大量的内存，内存浪费多。

# set 一组key的集合，但是不存储value，key不能重复
# 创建set 需要list作为输入集合
s = set([1, 2, 3])
print s
print set([1, 1, 2, 2, 3, 3, 4])

# set的add() remove()
s.add(5)
print s
s.add(5)
print s
s.remove(2)
print s
# s.remove(2) # Error
# print s

# set的交集和并集
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print s1 & s2
print s1 | s2

# list str的讨论 list的sort()以及str的replace()
a = ['c', 'a', 'b']
a.sort()
print a

a = 'abc'
print a.replace('a', 'A')
print a

# dict tuple set list 混合 :(
d = {(1, 2, 3): 12}
print d
# d = {(1, [2, 3]): 12} # Error! # TypeError: unhashable type: 'list'
# print d
s = set([(1, 2, 3), 1, 2])
print s
# s = set([(1, [2, 3]), 1, 2]) # Error
