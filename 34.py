# -*- coding: utf-8 -*-

# debug的的方式：print assert logging pdb
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!' #AssertionError: n is zero!
    return 10 / n

# foo('0') # python -O 34.py 关闭断言

import logging
logging.basicConfig(level=logging.INFO) # logging可以深入研究
s = '0'
n = int(s)
logging.info('n = %d' % n)
# print 10 / n

s = '0'
n = int(s)
# print 10 /n # python -m pdb 34.py

import pdb
s = '0'
n = int(s)
pdb.set_trace()
print 10 /n # python 34.py

# IDE PyCharm or Eclipse + pydev
