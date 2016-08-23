# -*- coding: utf-8 -*-

# 并行情况，内置函数zip()
from random import randint
chinese = [randint(60, 100) for _ in xrange(20)]
math = [randint(60, 100) for _ in xrange(20)]
english = [randint(60, 100) for _ in xrange(20)]

total = []
for a,b,c in zip(chinese, math, english):
    total.append(a + b + c)

print total

# 串行情况,itertools.chain将多个可迭代对象连接
from itertools import chain
from random import randint

e1 = [randint(60, 100) for _ in xrange(20)]
e2 = [randint(60, 100) for _ in xrange(20)]
e3 = [randint(60, 100) for _ in xrange(20)]
e4 = [randint(60, 100) for _ in xrange(20)]

count = 0

for s in chain(e1, e2, e3, e4):
    if s >90:
        count += 1

print count