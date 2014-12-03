# -*- coding: utf-8 -*-

# 默认参数
def power(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print power(5)
print power(10, 3)

def enroll(name, gender, age = 6, city = 'Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city', city

enroll('Sarah', 'F')
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city="Tianjin") # 特定参数
enroll('Jeremy', 'M', 31, 'Qingdao')

# 默认参数的坑
def add_end(l = []):
    l.append('END')
    return l

print add_end([1, 2, 3])
print add_end(['x', 'y', 'z'])
print add_end()
print add_end()
print add_end()
print add_end([1, 2, 3])
print add_end()

# 原因解释如下：
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是
# 一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认
# 参数的内容就变了，不再是函数定义时的[]了。
# 所以，定义默认参数要牢记一点：默认参数必须指向不变对象！

# 修改坑
def add_end(l = None):
    if l is None:
        l = []
    l.append('END')
    return l

print add_end([1, 2, 3])
print add_end(['x', 'y', 'z'])
print add_end()
print add_end()
print add_end()
print add_end([1, 2, 3])
print add_end()

# 可变参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc([1, 2, 3])
print calc((1, 3, 5, 7))

def calc(*numbers): # 定义可变参数用*号
    sum = 0
    for n in numbers: # 参数组装成tuple
        sum = sum + n * n
    return sum

print calc(1, 2)
print calc()

num = [1, 2, 3]
print calc(num[0], num[1], num[2])

# 采用*号将list或tuple的元素变成可变参数传入
print calc(*num)

tp = (2, 3, 4)
print calc(*tp)


# 关键字参数 关键字参数在内部组装成dict
def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw

person('Machael', 30)
person('Adam', 45, gender='M', job='Engineer')
kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **kw) # 字典转换为参数用**符号


# 参数组合
def func(a, b, c = 0, *args, **kw):
    print 'a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw

func(1, 2)
func(1, 2, c=3)
func(1, 2, 3)
func(1, 2, 3, 'a', 'b')
func(1, 2, 3, 'a', 'b', x=99)
args = (1, 2, 3, 4)
kw = {'x': 99}
func(*args, **kw) # tuple + dict 的调用方式
