class Person():
    def __init__(self):
        print("构造方法运行")

    # 这个new方法是在Person实例化的时候首先运行，这个方法的返回值决定到时实例化哪个类
    def __new__(cls, *args, **kwargs):
        print("new方法运行")
        return object.__new__(Person)
        # return Dog()

    # 这个方法可以让类像函数一样被调用
    def __call__(self, *args, **kwargs):
        print("call方法运行")

    def __del__(self):
        print("析构方法运行")


class Dog():
    def __init__(self):
        print("dog __init__方法")

    def run(self):
        print("dog run")


p = Person()
# p.run()
p(1)
