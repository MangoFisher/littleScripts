# -*- coding: utf-8 -*-

"""
方法一:字符串strip(),lstrip(),rstrip()方法去掉字符串两端字符
"""
s = "   abc   123   "
print s.strip()
print s.lstrip()
print s.rstrip()


"""
方法二:删除单个固定位置的字符，可以使用切片+拼接的方式
"""
s = "abc:123"
print s[:3] + s[4:]


"""
方法三:字符串的replace()方法或正则表达式re.sub()删除任意位置字符
"""
s1 = "\tabc\t123\txyz"
print s1.replace("\t", "")

import re

s2 = "\tabc\t123\txyz\ropq\r"
s3 = re.sub("[\t\r]", "", s2)
print s3


"""
方法四:字符串translate()方法，可以同时删除多种不同字符
"""
import string
s4 = "\tabc\t123\txyz\ropq\r"

print s4.translate(string.maketrans("abc", "xyz"), "\t\r")
