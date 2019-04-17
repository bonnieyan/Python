class Person():
    pass

#
# print(Person)
#
# p = Person
# print(p)
# p.name = "张三"
# print(p.name)


# def func(p):
#     print(p.name)
#
#
# func(Person)

# type 动态创建类
# print(type(p))
# print(type("2"))
# print(type(1))

def get_class(name):
    if name == "dog":
        class Dog():
            def run(self):
                print("dog run")
        return Dog
    else:
        class Cat():
            def run(self):
                print("cat run")
        return Cat


# c = get_class("dog")
# print(c)
# c.run(c)
# c = get_class(c)
# print(c)
# c.run(c)

Person2 = type('Person2', (), {})
# print(Person2)

p2 = Person2()
# print(p2)


class Person3():
    name = "张三"


# print(Person3.name)
Person3 = type('Person3', (), {'name': '李四'})
# print(Person3.name)
# 继承
Person4 = type('Person4', (Person3,), {})
print(Person4.name)


def person4_run(self):
    print("person4 run")


@staticmethod
def person4_run2():
    print("person4 run2")


Person4 = type('Person4', (Person3,), {'person4_run':person4_run,'person4_run2':person4_run2})
p = Person4()
p.person4_run()
p.person4_run2()

# 元类，可生成类，类可生成实例

class MyMetaClass(type):
    def __new__(cls, name, bases, attrs):
        print("元类new方法运行")
        print(name)
        print(bases)
        attrs['add'] = lambda self, value: value+value
        print(attrs)
        return type.__new__(cls, name, bases, attrs)


class MyClass(Person4,metaclass=MyMetaClass):
    pass

# 用metaclass　实例化 myclass
my_class = MyClass()
r = my_class.add(2)
print(r)