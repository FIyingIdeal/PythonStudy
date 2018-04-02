import json

d = dict(name='Bob', age=20, score=88)
# dumps()方法用于将一个对象转换成json字符串
json_str = json.dumps(d)
print('to json: ', json_str)
# loads()方法用于将一个json字符串反序列化为对象
obj = json.loads(json_str)
print('loads to object: ', obj)

f = open('json.txt', 'w')
# dump()方法用于将json写入一个file-like-Object
json.dump(d, f)
f.close()

f = open('json.txt', 'r')
# load()方法从file-like-Object中读取字符串并反序列化为对象
obj1 = json.load(f)
f.close()
print('load to object: ', obj1)


class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student: name = %s, age=%d, socre=%d' % (self.name, self.age, self.score)


s = Student('Alix', 22, 90)
class2Json = json.dumps(s, default=lambda o: o.__dict__)
print('class object to json: ', class2Json)


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


json2class = json.loads(class2Json, object_hook=dict2student)
print('json to class object: ', json2class)


obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)
