# -*- coding: utf-8 -*-

"""
����һ:�ַ���strip(),lstrip(),rstrip()����ȥ���ַ��������ַ�
"""
s = "   abc   123   "
print s.strip()
print s.lstrip()
print s.rstrip()


"""
������:ɾ�������̶�λ�õ��ַ�������ʹ����Ƭ+ƴ�ӵķ�ʽ
"""
s = "abc:123"
print s[:3] + s[4:]


"""
������:�ַ�����replace()������������ʽre.sub()ɾ������λ���ַ�
"""
s1 = "\tabc\t123\txyz"
print s1.replace("\t", "")

import re

s2 = "\tabc\t123\txyz\ropq\r"
s3 = re.sub("[\t\r]", "", s2)
print s3


"""
������:�ַ���translate()����������ͬʱɾ�����ֲ�ͬ�ַ�
"""
import string
s4 = "\tabc\t123\txyz\ropq\r"

print s4.translate(string.maketrans("abc", "xyz"), "\t\r")
