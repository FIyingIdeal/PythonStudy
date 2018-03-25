# 返回函数

def lazy_sun(*args):
    def sum_function():
        count = 0
        for i in args:
            count += i
        return count
    return sum_function


sum_function = lazy_sun(1, 2, 3)
print(sum_function)
print(sum_function())

# 闭包 当一个函数返回了一个函数后，其内部的局部变量还被新函数引用
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i * i
        fs.append(f)
    return fs


# 返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
f1, f2, f3 = count()
print(f1())  # 9
print(f2())  # 9
print(f3())  # 9


# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变
def count():
    def f(i):
        def g():
            return i * i
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs


f1, f2, f3 = count()
print(f1())  # 1
print(f2())  # 4
print(f3())  # 9

# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
# 1.内部函数一般无法修改外部函数的参数
# 2.想要修改需要声明 nonlocal
# 3.内部函数可以修改外部list中的元素
def createCounter():
    s = [0]
    def counter():
        s[0] += 1
        return s[0]
    return counter


def createCounter_nonlocal():
    m = 0
    def counter():
        nonlocal m  # nonlocal是python3才开始支持的
        m += 1
        return m
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
