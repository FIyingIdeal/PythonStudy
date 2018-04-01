# -*- coding: utf-8 -*-
import os
# 操作系统类型，如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
print(os.name)
# 获取环境变量
print(os.environ)
print(os.environ.get('path'))

# 查看当前目录的绝对路径:
print('os.path.abspath ', os.path.abspath('../'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数
# 这样可以正确处理不同操作系统的路径分隔符
print(os.path.join(os.path.abspath('.'), 'testDir'))
# 然后创建一个目录:
# os.mkdir('E:/Coding/python/pythonStudy/learning/IO/testDir')
# 删掉一个目录:
# os.rmdir('E:/Coding/python/pythonStudy/learning/IO/testDir')

# 要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数
# 这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
print(os.path.split('E:\Coding\python\pythonStudy\learning\IO\\testDir'))
print(os.path.split('E:\Coding\python\pythonStudy\learning\IO\\testDir\\test.txt'))
# os.path.splitext()可以直接让你得到文件扩展名
print(os.path.splitext('E:\Coding\python\pythonStudy\learning\IO\\testDir\\test.txt'))

# 文件重命名
# print('rename: ', os.rename('test.py', 'test.txt'))
# 删除文件
# print('remove:', os.remove('test.py'))

# 列出当前文件夹下的所有文件
print(os.listdir('.'))

print([x for x in os.listdir('E:\\Coding\\python\\pythonStudy\\learning') if os.path.isdir(os.path.join('E:\\Coding\\python\\pythonStudy\\learning', x))])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

###############在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径
print('tttttttttttttttttttttt')
print([x for x in os.walk('../')])


def find(str, path = '.'):
    # TODO 使用os.walk会输出两次...
    for root, dirs, files in os.walk(path):
        for file in files:
            if str in file:
                print(os.path.join(root, file))
        for dir in dirs:
            find(str, os.path.join(root, dir))


def new_find(str, path = '.'):
    files = [x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))]
    dirs = [x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]
    for file in files:
        if str in file:
            print(os.path.join(path, file))
    for dir in dirs:
        new_find(str, os.path.join(path, dir))


new_find('Test', '../')