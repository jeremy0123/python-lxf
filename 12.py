# -*- coding: utf-8 -*-

# 函数递归
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print fact(1)
print fact(5)
print fact(100)
# print fact(1000) #Error #RuntimeError: maximum recursion depth exceeded # 栈溢出

# 在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，
# 栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，
# 递归调用的次数过多，会导致栈溢出。

# 解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，
# 所以，把循环看成是一种特殊的尾递归函数也是可以的。

# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
# 这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，
# 都只占用一个栈帧，不会出现栈溢出的情况。

def fact(n):
    return fact_iter(1, 1, n)

def fact_iter(product, count, max):
    if count > max:
        return product
    return fact_iter(product * count, count + 1, max)

print fact(5)
# print fact(1000) # python并未做尾递归优化

# 下列代码可以进行优化
# This program shows off a python decorator
# which implements tail call optimization. It
# does this by throwing an exception if it is
# it's own grandparent, and catching such
# exceptions to recall the stack.

import sys

class TailRecurseException:
  def __init__(self, args, kwargs):
    self.args = args
    self.kwargs = kwargs

def tail_call_optimized(g):
  """
  This function decorates a function with tail call
  optimization. It does this by throwing an exception
  if it is it's own grandparent, and catching such
  exceptions to fake the tail call optimization.
  This function fails if the decorated
  function recurses in a non-tail context.
  """
  def func(*args, **kwargs):
    f = sys._getframe()
    if f.f_back and f.f_back.f_back \
        and f.f_back.f_back.f_code == f.f_code:
      raise TailRecurseException(args, kwargs)
    else:
      while 1:
        try:
          return g(*args, **kwargs)
        except TailRecurseException, e:
          args = e.args
          kwargs = e.kwargs
  func.__doc__ = g.__doc__
  return func
# ------------------------------------------------------------------------------

def fact(n):
    return fact_iter(1, 1, n)

@tail_call_optimized
def fact_iter(product, count, max):
    if count > max:
        return product
    return fact_iter(product * count, count + 1, max)

print fact(5)
print fact(1000) #Welldone
