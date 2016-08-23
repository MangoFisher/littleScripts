# -*- coding: utf-8 -*-
from itertools import islice
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

t = iter(l)

for x in islice(t, 3, 5):
    print x

for x in islice(t, 1, 3):
    print x
