# -*- coding: utf-8 -*-

dic = {
    "lodDist": 100.0,
    "SmallCull": 0.04,
    "DistCull": 500.0,
    "trilinear": 40,
    "farclip": 477
}

"""
����һ:ʹ���ַ�����str.ljust(),str.rjust(),str.center()�ֱ�������ҡ��ж���
"""
for k in dic.keys():
    print k.ljust(10), ":", dic[k]


"""
������:ʹ��format����
"""

# ���ֵռ�õ�����ֽ���
w = max(map(len, dic.keys()))

for k in dic:
    print k.ljust(w), ":", dic[k]