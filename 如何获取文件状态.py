# coding=utf-8

# 方法一:使用标准库os中的三个系统调用stat、fstat、lstat
import os
import stat
import time
s = os.stat("test.txt")

# 判断是否为目录
print stat.S_ISDIR(s.st_mode)
# 判断是否为普通文件
print stat.S_ISREG(s.st_mode)

# 判断文件的权限
print s.st_mode & stat.S_IRUSR

# 查询文件时间
print time.localtime(s.st_atime)

# 查询普通文件的大小
print s.st_size


# 方法二:使用标准库中os.path下一些函数，更加简洁
import os

# 获得文件类型
print os.path.isdir("test.txt")

# 判断是否是普通文件
print os.path.isfile("test.txt")

# 获取文件时间
print os.path.getatime("test.txt")

# 获取普通文件大小
print os.path.getsize("test.txt")