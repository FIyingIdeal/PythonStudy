# -*- coding: utf-8 -*-

try:
    # 调用open方法打开文件，如果文件不存在则会抛出FileNotFoundError异常
    f = open('./test.txt', 'r')
    # 将文件中的所有内容一次性读取到一个str对象
    # 其还有一个重载的方法read(size)表示每次最多读取size个字节的内容
    s = f.read()
    print(s)
finally:
    if f:
        f.close()

# 使用with简化io关闭流的操作，无需自己关闭io流，这与java7中的try-with-resource类似
with open('./test.txt', 'r') as f:
    print(f.read())

# readLines()读取一行
with open('./test.txt', 'r') as f:
    i = 0
    for line in f.readlines():
        print(i, line.strip()) # strip()用于将行尾的\n删除
        i += 1

# 读取二进制文件的话需要使用'rb'
# f = open('./test.jpg', 'rb')

# 指定编码
# f = open('./test.txt', 'r', encoding='GBK')


# StringIO与BytesIO 在内存中读写
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
# getvalue()方法用于获得写入后的str
print(f.getvalue())
