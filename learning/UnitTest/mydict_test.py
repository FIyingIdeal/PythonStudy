# -*- coding: utf-8 -*-
import unittest

from UnitTest.mydict import Dict


class TestDict(unittest.TestCase):

    # 每调用一个测试方法之前会被执行
    def setUp(self):
        print('setUp...')

    # 测试方法必须以test开头，否则就不被认为是测试方法，在测试的时候不会被执行
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)

    def test_keyerror(self):
        d = Dict()
        # 期待抛出指定类型的Error，如下我们期待抛出KeyError
        with self.assertRaises(KeyError):
            value = d['empty']

    # 每调用一个测试方法之后会被执行
    def tearDown(self):
        print('teatDown...')


# 将mydict_test.py当做正常的python脚本运行
if __name__ == '__main__':
    unittest.main()
