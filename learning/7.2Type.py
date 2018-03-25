import types

def fn():
    pass

print(type(fn) == types.FunctionType)       # True
print(type(abs) == types.BuiltinFunctionType)       # True
print(type(lambda x: x) == types.LambdaType)       # True
print(type((x for x in range(10))) == types.GeneratorType)       # True


# isInstance()
print(isinstance('abc', str))
print(isinstance(b'a', bytes))

# dir()用于获取一个对象的所有属性和方法
print('dir(): ', dir('abc'))
# len()与__len__()，len()函数内部其实是调用了对象的__len__()方法
# 所以只要自定义的类中定义了__len__()方法，也可以使用len()来获取对象的长度
str1 = 'abc'
print(str1.__len__() == len(str1))

class Test(object):
    def __len__(self):
        return 10

test = Test()
print('自定义类中的__len__()测试：', len(test))


# 使用getattr()、setattr()、hasattr()直接操作一个对象的状态
class MyObject(object):
    def power(self):
        return self.x * self.x

    def __init__(self):
        self.x = 9

obj = MyObject()
print('hasattr(obj, "x") : ', hasattr(obj, 'x'))    # True
print('hasattr(obj, "y") : ', hasattr(obj, 'y'))    # False
setattr(obj, 'y', 10)
print('hasattr(obj, "y") : ', hasattr(obj, 'y'))    # True
print('getattr(obj, "y") : ', getattr(obj, 'y'))
print('getattr(obj, "z") : ', getattr(obj, 'z', 100))   # 100  获取默认值

print('hasattr(obj, "power") : ', hasattr(obj, 'power'))    # True
fn1 = getattr(obj, 'power')
print('getattr(obj, "power")', fn1)
print('getattr(obj, "power")()', fn1())     # 81

