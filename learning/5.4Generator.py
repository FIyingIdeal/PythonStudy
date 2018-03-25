# python 生成器 generator
# 生成器的作用是：在循环的过程中按照某种算法不断推算出后续的元素，而不必创建完整的list，从而节省大量的空间

# 创建generator方式一：将列表生成式的[]改成()
g1 = (x * x for x in range(11))
print(g1)  # <generator object <genexpr> at 0x00000000007FE4C0>

# 通过next(g)来遍历generator中的元素，但每一次只能遍历出一个
print(next(g1))  # 0
# 另一种遍历generator的方式是通过for循环
for i in g1:
    print(i)  # 打印从1开始，因为第0个元素被next(g1)获取过了

print('-------------------')


# 通过函数生成一个斐波那契数列
def fib(max_num):
    n, a, b = 0, 0, 1
    while n < max_num:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


f1 = fib(6)
print(f1)
print('-------------------')


# 创建generator方式二：通过yield
# 通过generator生成一个斐波那契数列
def fib1(max_num):
    n, a, b = 0, 0, 1
    while n < max_num:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


f2 = fib1(10)
print(f2)   # <generator object fib1 at 0x000000000111F570>

# 从上述输出来看f2是一个generator，fib1其实也是一个generator，而要遍历其中的元素，可以使用next()或for循环
print('next(fib1(8))', next(fib1(8)))

for i in fib1(8):
    print('for 输出generator生成的斐波那契数列', i)
# for 输出generator生成的斐波那契数列 1
# for 输出generator生成的斐波那契数列 1
# for 输出generator生成的斐波那契数列 2
# for 输出generator生成的斐波那契数列 3
# for 输出generator生成的斐波那契数列 5
# for 输出generator生成的斐波那契数列 8
# for 输出generator生成的斐波那契数列 13
# for 输出generator生成的斐波那契数列 21

# 通过上边输出可以看到，通过for循环遍历generator时，无法获取到return语句的返回值，如果想要拿到，需要捕获StopIteration错误，返回值包含在StopIteration的value中
f3 = fib1(6)
while True:
    try:
        i = next(f3)
        print('g:', i)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break   # 必须要有break，否则的话就是死循环


# 通过generator生成杨辉三角，每一行看成是一个list
def triangles():
    line, first_or_last = 1, 1
    lists = []
    while True:
        length = len(lists)
        if line < 3:
            next_inner_list = []
            while len(next_inner_list) < line:
                next_inner_list.append(first_or_last)
            lists.append(next_inner_list)
        else:
            i = 0
            last_inner_list = lists[length - 1]
            last_inner_list_length = len(last_inner_list)
            next_inner_list = []
            while i <= last_inner_list_length:
                if i == 0 or i == last_inner_list_length:
                    next_inner_list.append(first_or_last)
                else:
                    next_inner_list.append(last_inner_list[i - 1] + last_inner_list[i])
                i = i + 1
            lists.append(next_inner_list)
        yield lists[line - 1]
        line = line + 1


# 结合使用列表生成式更加简单，list的“+”操作可以合并两个list到一个list当中
def triangles1():
    l1 = [1]
    while True:
        yield l1
        l1 = [1] + [(l1[n] + l1[n + 1]) for n in (range(len(l1) - 1))] + [1]

n = 0
results = []
for t in triangles1():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')