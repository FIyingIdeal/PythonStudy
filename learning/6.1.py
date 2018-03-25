# filter() filter()函数返回的是一个Iterator，也就是一个惰性序列
# 使用埃氏筛法求素数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


# for n in primes():
#     if n < 100:
#         print(n)
#     else:
#         break

# 找回数（从左读与从右读一样的数字）
def is_palindrome(n):
    str_num = str(n)
    half_length = len(str_num)
    for i in range(0, half_length):
        if str_num[i] == str_num[-i - 1]:
            continue
        else:
            return False
    return True


def is_palindrome_new(n):
    str_num = str(n)
    # S[::-1]是将S倒叙
    if str_num == str_num[::-1]:
        return True


# 测试:
output = filter(is_palindrome, range(1, 2000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
                                                  111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

# sorted
l1 = ['bob', 'about', 'Zoo', 'Credit']
# 对l1进行排序（根据ASCII码进行排序）
print(sorted(l1))
# 对l1进行忽略大小写排序，通过key指定一个函数来对各个元素进行中间转换后对原数据排序
print(sorted(l1, key=str.lower))
# 对l1进行忽略大小写倒叙排序 通过reverse=True来指定倒叙排序
print(sorted(l1, key=str.lower, reverse=True))


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# L按照名字排序
def by_name(t):
    return t[0]


L2 = sorted(L, key=by_name)
print('按照姓名排序：', L2)


def by_score(t):
    return -t[1]


L2 = sorted(L, key=by_score)
print('按照成绩高到低排序：', L2)
# return t[1]
# L2 = sorted(L, key=by_score, reverse=True)
