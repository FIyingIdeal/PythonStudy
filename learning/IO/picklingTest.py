import pickle

d = dict(name='Bob', age=20, score=88)
# pickle.dumps()方法可以把任意对象序列化成一个bytes
print('pickling: ', pickle.dumps(d))

# 将对象序列化以后写入到文件中
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

# 读取保存对象序列化以后的文件，将其还原成对象
f = open('dump.txt', 'rb')
d1 = pickle.load(f)
f.close()
print('unpickling: ', d1)



