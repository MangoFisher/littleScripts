# -*- coding: utf-8 -*-

class FloatRange:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step

# for x in FloatRange(1.0, 10.0, 0.5):
#     print x


for y in reversed(FloatRange(1.0, 10.0, 0.1)):
    print y