# 装饰器
# python中函数也是也是一个对象，函数对象中有一个__name__属性，可以拿到函数的名字


def now():
    print('2018-3-21 09:54:48')


print('now.__name__', now.__name__)


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now_with_log():
    print('2018-3-21 10:03:08')


now_with_log()
# call now_with_log():
# 2018-3-21 10:03:08
# 将@log放置在now_with_log()函数的定义处，相当于执行了 now_with_log = log(now_with_log)
print('after wrapper now_with_log.__name__', now_with_log.__name__)
# wrapper  发现经过装饰以后函数的名字已经变了...后边会有如何还原的方法（使用@functools.wraps()）


def log_param(text):
    def log1(func):
        def wrapper(*args, **kw):
            # wrapper.__name__ = func.__name__
            print('%s %s' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return log1


@log_param('execute')
def now_with_log_param(date):
    print(date)


now_with_log_param('2018-3-21 10:18:05')
# @log_param('execute')相当于执行了log_param('execute')(now_with_log_param)
print(now_with_log_param.__name__)  # wrapper
# 原本的函数名已经由now_with_log_param变成了wrapper


# 装饰以后使原函数名与未被装饰时的函数名相同：使用python提供的@functions.wraps(func)
import functools


def log1(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('execute %s()' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log1
def now1():
    print('2018-3-21 10:32:26')


print('now1.__name__ : ', now1.__name__)    # now1


# -----------------
import time


def metric(fn):
    def wrapper(*args, **kw):
        time1 = time.time()
        result = fn(*args, **kw)
        time2 = time.time()
        print('%s executed in %s ms' % (fn.__name__, time2 - time1))
        return result
    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
