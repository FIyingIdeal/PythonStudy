# 实例属性和类属性

class Student(object):
    name = 'Student'

s = Student()
print('Student.name = ', Student.name)  # Student
print('s.name = ', s.name)  # Student

s.name = 'name'     # 这里只是修改了实例属性的值，但没有修改类属性的值
print('Student.name = ', Student.name)  # Student
print('s.name = ', s.name)  # name

del s.name   # del 可以用来删除实例的属性
print('s.name = ', s.name)  # Student
# 建议不要对实例属性和类属性起同样的名字


######################################
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
