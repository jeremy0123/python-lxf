# -*- coding: utf-8 -*-

# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
# Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。

# map reduce函数

def f(x):
    return x * x

# map() 能够接收函数作为参数的函数，称之为高阶函数 Higher-order function
print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print map(f, [9])

# reduce() 把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) == f(f(f(x1, x2), x3), x4)
# 所以作为reduce的参数的函数必须有2个参数

def add(x, y):
    return x + y

print reduce(add, [1, 3, 5, 7, 9])

def fn(x, y):
    return 10 * x + y

print reduce(fn, [1, 3, 5, 7, 9])

# str转换为int
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))
print str2int('13579')
print str2int('0123')

# 排序 高阶函数sorted
# 通常规定，对于两个元素x和y，如果认为x < y，则返回-1，如果认为x == y，则返回0，如果认为x > y，则返回1
print sorted([26, 5, 12, 9, 21])
# 反向排序
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0

print sorted([26, 5, 12, 9, 21], reversed_cmp)

print sorted(['about', 'bob', 'Zoo', 'Credit'])

# 字符串排序
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0

print sorted(['about', 'bob', 'Zoo', 'Credit'], cmp_ignore_case)

# 函数作为返回值 闭包Closure：相关参数和变量都保存在返回的函数中
def lazy_sum(*args): # 不需要立刻求和，而是在后面的代码中，根据需要再计算
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 5, 7, 9) # 函数赋值
print f
print f() #函数调用

f2 = lazy_sum(1, 3, 5, 7, 9)
print f == f2



def f(x):
    return x * x

# 自定义map()
def my_map(func, list):
    backlist = []
    for l in list:
        backlist.append(func(l))
    return backlist
print my_map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print my_map(f, [9])
