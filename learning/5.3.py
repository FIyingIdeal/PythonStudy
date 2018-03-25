# 高级特性 -- 列表生成式

import os
# 生成 1-9 的List
l1 = list(range(1, 10))
print('生成 1-9 的List', l1)

# 生成 1-9 平方的List
l2 = [x * x for x in range(1, 10)]
print('生成 1-9 平方的List', l2)

# 生成 1-9 中偶数平方的List
l3 = [x * x for x in range(1, 10) if x % 2 == 0]
print('生成 1-9 中偶数平方的List', l3)

# 使用两层循环
l4 = [m + n for m in 'Hello' for n in 'World']
print('使用两层循环', l4)

# 列出指定目录下的所有文件和目录名
files = [d for d in os.listdir('../..')]    # os.listdir可以列出文件和目录
print(files)

# 使用两个变量生成list
d = {'a': 'A', 'b': 'B', 'c': 'C'}
l5 = [k + '=' + v for k, v in d.items()]
print(l5)

# 将list中的所有字符串都变成小写的
l6 = ['Hello', 'World', 'Python']
l7 = [s.lower() for s in l6]
print(l6, l7)

# 练习，当list中既存在字符串有存在数字等其他类型变量的时候，在程序不出错的情况下将所有的字符串变为小写
l8 = ['Hello', 'World', 18, 'Apple', None]
l9 = [s.lower() for s in l8 if isinstance(s, str)]
print(l9)
if l9 == ['hello', 'world', 'apple']:
    print('测试通过')
else:
    print('测试失败')