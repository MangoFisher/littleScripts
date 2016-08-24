# -*- coding: utf-8 -*-

dic = {
    "lodDist": 100.0,
    "SmallCull": 0.04,
    "DistCull": 500.0,
    "trilinear": 40,
    "farclip": 477
}

"""
方法一:使用字符串的str.ljust(),str.rjust(),str.center()分别进行左、右、中对齐
"""
for k in dic.keys():
    print k.ljust(10), ":", dic[k]


"""
方法二:使用format函数
"""

# 求键值占用的最大字节数
w = max(map(len, dic.keys()))

for k in dic:
    print k.ljust(w), ":", dic[k]