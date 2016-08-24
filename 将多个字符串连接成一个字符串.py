# -*- coding: utf-8 -*-

# 遍历列表并进行 "+"操作，空间开销大
# l = ["abc", "123", "def", "456", "789"]
# s = ""
# for p in l:
#     s += p
# print s
#

# 使用str.join()方法，避免过大的控件开销
l = ["abc", "123", "def", "456", "789"]
s = "".join(l)
print s


# 列表中有字符串和非字符串
l = ["abc", 123, "def", "456", 789]

# 1.列表解析，对原列表所有项进行字符串转换，生成了新的列表还是有额外控件浪费
s = "".join([str(x) for x in l ])
print s

 2.生成器表达式,(str(x) for x in l)是生成器对象
s = "".join(str(x) for x in l)
print s