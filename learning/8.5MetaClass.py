class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


# MyList的父类是list，这里相当于
class MyList(list, metaclass=ListMetaclass):
    pass


L = MyList()
L.add(1)
L.add(2)
print(isinstance(L, list))
for index, value in enumerate(L):
    print(index, value)
