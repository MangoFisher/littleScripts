# coding=utf-8

# 定义类IntTuple继承内置tuple，并实现__new__，修改实例行为


class IntTuple(tuple):
    def __new__(cls, iterable):
        g = (x for x in iterable if isinstance(x, int) and x > 0)
        return super(IntTuple, cls).__new__(cls, g)

    def __init__(self, iterable):
        super(IntTuple, self).__init__(iterable)


t = IntTuple([1, -1, "abc", 6, ["x", "y"], 3])
print t
