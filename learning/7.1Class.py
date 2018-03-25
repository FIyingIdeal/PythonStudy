# 定义类


class Student(object):

    # __init__方法的第一个参数永远是self，表示创建的实例本身
    # 有了__init__方法后，在创建实例的时候，就不能传入空的参数了
    # 必须传入与__init__方法匹配的参数，但self不需要传，python解释器会把实例变量传进去
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # 与普通的函数相比，类中定义的函数只有一点不同，那就是第一个参数永远是实例变量self，且调用时不用传递该参数
    def print_score(self):
        print('%s: %s' % (self.name, self.score))


lisa = Student('lisa', 20)
lisa.print_score()
print('lisa\'s name: ', lisa.name)
# 可以自由的给一个实例变量绑定属性
lisa.sex = 'f'
print('lisa\'s sex: ', lisa.sex)
bob = Student('bob', 22)
# print('bob\'s sex', bob.sex) # 该对象没有设置sex属性，不能访问


class Student0(object):

    def __init__(self, name, age):
        # 实例变量如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
        # 但需要注意的是变量名类似__name__(以双下划线开头，双下划线结尾的)是特殊变量，可以直接访问，不是private变量
        # 还有需要注意的是以单下划线开头的，如_name，该变量虽然可以在外部访问，但按约定应该把它视为私有变量，不要随意访问
        self.__name = name
        self.__age = age

    def print_score(self):
        print('%s: %s' % (self.__name, self.__age))


joe = Student0('joe', '22')
# 不能直接访问私有变量，但不是绝对的。
# joe.__name
# python解释器把__name变量改成了_Student_name，所以通过_Student__name可以来访问__name变量
# 但强烈建议不要这么干，因为不同版本的python解释器可能会把__name改成不同的变量名
print('不建议的private变量访问方式：', joe._Student0__name)
joe.print_score()


class Student1(object):

    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender


# 测试:
bart = Student1('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')