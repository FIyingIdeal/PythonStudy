# python Iterable 与 Iterator 的区别
# Iterable -- 可迭代对象，可直接作用于for循环的对象都是Iterable类型，如list，tuple，generator，set，dict，str；
# Iterator -- 迭代器，可以被next()函数调用并不断返回下一个值的对象称为迭代器，generator就是一个迭代器对象
# generator是Iterator对象，也是一个Iterable对象，但list，tuple，set，dict，str是Iterable对象，但不是Iterator对象
# python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

from collections import Iterable, Iterator

print(isinstance('abc', Iterable))     # True
print(isinstance('abc', Iterator))     # False

print(isinstance([x for x in range(5)], Iterable))     # True
print(isinstance([x for x in range(5)], Iterator))     # False

print(isinstance((x for x in range(5)), Iterable))     # True
print(isinstance((x for x in range(5)), Iterator))     # True

print(isinstance([], Iterable))     # True
print(isinstance([], Iterator))     # False


