# -*- coding: utf-8 -*-

# 单元测试的执行
import unittest
from mydict import Dict

class TestDict(unittest.TestCase):

    # 以test开头的方法就是测试方法，不以test开头的方法不被认为
    # 是测试方法，测试的时候不会被执行。
    def test_init(self):
        d = Dict(a = 1, b = 'test')
        self.assertEquals(d.a, 1)
        self.assertEquals(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEquals(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEquals(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    # setUp tearDown为执行测试函数之前和之后执行的函数，比如数据库打开关闭
    def setUp(self):
        print 'setUp...'

    def tearDown(self):
        print 'tearDown...'

if __name__ == '__main__':
   unittest.main()
# 如果不加上面两行，执行python -m unittest 35
