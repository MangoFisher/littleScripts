# coding=utf-8
import mmap
f = open("test.txt", "r+b")

# 获取文件描述符
d = f.fileno()

m = mmap.mmap(d, 0, access=mmap.ACCESS_WRITE)
print type(m)
print m[0]
print m[10:20]
m[0] = "\x41"
print m[0]