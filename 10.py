# -*- coding: utf-8 -*-

#自定义函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print my_abs(10)

# 空函数 pass语句
def foo():
    pass # 占位符，类似{}，如果不写会报错

print foo()

# 参数检测
def my_abs(x):
    if not isinstance(x, (int, float)):
        #raise TypeError('bad operand type')
        raise TypeError('错误的参数')
    if x >= 0:
        return x
    else:
        return -x

# print my_abs('a') # Error

# 返回多个值
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print x, y

# 返回多个值是返回tuple
# 在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
r = move(100, 100, 60, math.pi / 6)
print r
