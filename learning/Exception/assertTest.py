# -*- coding: utf-8 -*-


def foo(s):
    n = int(s)
    # 断言失败 assert语句本身就会抛出AssertionError
    assert n != 0, 'n is zero'
    return 10 / n


# foo('0')


import logging
logging.basicConfig(level = logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

